import mimetypes
import random
import string
import os
import datetime

from django.shortcuts import render, HttpResponse, redirect
from django.views.generic import CreateView, View
from django.contrib.auth.hashers import check_password
from django.core.files.storage import FileSystemStorage

from urlapp.forms import UploadForm
from urlapp.models import UrlData
from urlapp.encrypt_util import encrypt, decrypt


class ShortendUrl(CreateView):
    form_class = UploadForm
    template_name = 'index.html'

    def post(self, request, *args, **kwargs):
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            slug = ''.join(random.choice(string.ascii_letters)
                           for x in range(10))

            file = form.cleaned_data.get("file")
            url = form.cleaned_data.get('url')
            password = form.cleaned_data['password']

            if file:
                fname, ext = os.path.splitext(file.name)
                filename = fname + str(datetime.datetime.now()) + ext
                fs = FileSystemStorage(location='media/uploads/')  # defaults to   MEDIA_ROOT
                fs.save(filename, file)
                encrypted_file = encrypt(password, filename)
                file_obj = UrlData(file=encrypted_file, slug=slug, password=password)
                file_obj.save()
                return HttpResponse(f'Shortened URL: <a href="{slug}">{slug}</a>')

            else:
                encrypted_url = encrypt(password, url)
                file_obj = UrlData(url=encrypted_url, slug=slug, password=password)
                file_obj.save()
                return HttpResponse(f'Shortened URL: <a href="{slug}">{slug}</a>')


class ResponseData(View):
    template_name = 'form.html'

    def get(self, request, slug):
        try:
            file_data = UrlData.objects.get(slug=slug)
            if file_data:
                return render(request, self.template_name)
        except Exception:
            return HttpResponse("Please enter correct url")

    def post(self, request, slug):
        password = request.POST.get('password')
        try:
            url_obj = UrlData.objects.get(slug=slug)
            if url_obj and check_password(password, url_obj.password):

                if url_obj.url:
                    url = bytes(url_obj.url, 'utf-8')
                    decrypt_url = decrypt(password, url)
                    return redirect(decrypt_url)

                elif url_obj.file:
                    filename = url_obj.file
                    decrypt_file = decrypt(password, filename)
                    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
                    filepath = BASE_DIR + '/media/uploads/' + decrypt_file
                    path = open(filepath, 'r')
                    mime_type, _ = mimetypes.guess_type(filepath)
                    response = HttpResponse(path, content_type=mime_type)
                    response['Content-Disposition'] = "attachment; filename=%s" % decrypt_file
                    return response

                else:
                    return HttpResponse("Invalid")
            else:
                return HttpResponse("Password or data can be wrong. Please enter it again")
        except Exception:
            return HttpResponse("Invalid data. Please enter right data")
