import mysql.connector


class Connection:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="krinal",
            password="Test@1234",
            database="manage_books",
        )
        self.cursor = self.conn.cursor()
        print("\nOpened database successfully")


class Book(Connection):
    def __init__(self):
        super().__init__()
        self.result = None
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS books (book_id int PRIMARY KEY, book_name VARCHAR(255), price INT,"
            "quantity INT, book_type VARCHAR(255) ,author_name VARCHAR(250))"
        )

    def insert(self, counts):
        for count in range(0, counts):
            id = input("Enter id ")
            name = input("Enter Book_name ")
            price = int(input("Enter Price "))
            qty = int(input("Enter Quantity "))
            book_type = input("Enter book type ")
            author = input("Author Name ")
            insert_query = "INSERT INTO books (book_id,book_name,price,quantity,book_type,author_name) VALUES (%s, %s," \
                           "%s,%s,%s,%s)"
            values = (id, name, price, qty, book_type, author)
            self.cursor.execute(insert_query, values)
            self.conn.commit()

    def update(self, field_name, new_value, field_name1, current_value):
        update_query = (
            "UPDATE books SET {field_name} = %s WHERE {field_name1} = %s".format(
                field_name=field_name, field_name1=field_name1
            )
        )

        data = (new_value, current_value)
        self.cursor.execute(update_query, data)
        self.conn.commit()
        print("Record Updated successfully")

    def delete(self, field_name, value):
        delete_query = f"Delete from books where {field_name}=%s".format(
            field_name=field_name
        )
        data = (value,)
        self.cursor.execute(delete_query, data)
        self.conn.commit()
        print(self.cursor.rowcount, "record(s) deleted")

    def search_book(self, field_name, current_value):
        select_query = "SELECT * FROM books WHERE {field_name}=%s".format(
            field_name=field_name
        )
        value = (current_value,)
        self.cursor.execute(select_query, value)
        self.result = self.cursor.fetchall()
        return self.result

    def get_all_books(self):
        sql = "SELECT * FROM books"
        self.cursor.execute(sql)
        self.result = self.cursor.fetchall()
        return self.result

    def display(self):
        for book_data in self.result:
            print(book_data)

    def create_file(self):
        with open("books_data.txt", "w") as f:
            for book_data in self.result:
                f.write(str(book_data) + "\n")


class Bill:
    def __init__(self):
        self.total_amount = 0

    def calculate_amount(self, price, quantity):
        self.total_amount = self.total_amount + price * quantity

    def display(self):
        print("Total amount is = {amount}".format(amount=self.total_amount))


if __name__ == "__main__":
    book = Book()
    bill = Bill()
    print("Enter 1 to insert values")
    print("Enter 2 to update values")
    print("Enter 3 to make bill")
    print("Enter 4 to search data")
    print("Enter 5  to display whole data")
    print("Enter 6 to write data to a file")
    print("Enter 7 to delete data")
    choice = int(input("\nEnter your choice "))
    while choice != 0:
        if choice == 1:
            num = int(input("\nHow many insertions you want to do "))

            book.insert(num)
            book.get_all_books()
            book.display()

        elif choice == 2:
            field_to_be_changed = input("Enter the field name to be set ")
            new_value = input("Enter the new value ")
            field_name1 = input("Enter the field name where to put condition ")
            current_value = input("Enter the current value \n")

            book.update(
                field_to_be_changed, new_value, field_name1, current_value
            )
            book.get_all_books()
            book.display()

        elif choice == 3:
            counts = int(input("\nhow many different books to buy "))
            for count in range(0, counts):
                field_name = "book_name"
                book_name = input("\nEnter the book name ")
                result = book.search_book(field_name, book_name)
                if result:
                    price = result[0][2]
                    quantity = int(input("quantity"))
                    bill.calculate_amount(price, quantity)
                    bill.display()
                    original_quantity = result[0][3]
                    updated_quantity = original_quantity - quantity
                    book.update(
                        "quantity", updated_quantity, field_name, book_name
                    )
                    book.get_all_books()
                    book.display()
                else:
                    print("\nRecord not found")

        elif choice == 4:
            field_name = input("\nEnter the field name ")
            value = input("\nEnter the value ")
            book.search_book(field_name, value)
            book.display()

        elif choice == 5:
            book.get_all_books()
            book.display()

        elif choice == 6:
            book.get_all_books()
            book.create_file()

        elif choice == 7:
            field_name = input("\nEnter the field name ")
            value = input("\nEnter the value ")
            book.delete(field_name, value)
            book.get_all_books()
            book.display()

        else:
            print("Not a valid choice")

        choice = int(input("\nEnter your choice "))

    book.conn.close()
    print("\nConnection closed")
