# library management system
# ye program librarian ke liye hai jo books ka record rakhta hai
# aur ye bhi dekhta hai k kon si book kis student ko issue hui


# ---------- book class ----------
# har book ek object hogi, is class mein book ki sari detail hai
class Book:
    def __init__(self, book_id, title, author, quantity):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.quantity = quantity      # total copies jitni library ke pass hain
        self.available = quantity     # shuru mein sari copies available hoti hain

    # book ki detail print karne wala function
    def show(self):
        print("Book ID   :", self.book_id)
        print("Title     :", self.title)
        print("Author    :", self.author)
        print("Total Qty :", self.quantity)
        print("Available :", self.available)


# ---------- library class ----------
# ye class sare kaam sambhalti hai (add, issue, return waghera)
class Library:
    def __init__(self):
        self.books = {}    # dictionary: key = book id, value = Book object
        self.issued = []   # list of dictionaries: {"book_id": ..., "student": ...}

    # book dhoondne ka chota sa helper, id se
    def find_by_id(self, book_id):
        return self.books.get(book_id)   # agr nahi mili to None return hoga

    # 1. nai book add karna
    def add_book(self, book_id, title, author, quantity):
        # unique id check, same id dobara allow nahi
        if book_id in self.books:
            print("Error: is ID ki book pehle se mojood hai!")
            return
        self.books[book_id] = Book(book_id, title, author, quantity)
        print("Book added successfully!")

    # 2. sari books dikhana
    def view_all(self):
        if len(self.books) == 0:
            print("Library mein abhi koi book nahi hai.")
            return
        print("\n----- ALL BOOKS -----")
        for book in self.books.values():
            book.show()
            print("-" * 25)

    # 3. book search karna (id ya title se)
    def search(self, keyword):
        keyword = keyword.lower()
        found = False
        for book in self.books.values():
            # id exact match ya title mein keyword aye to book mil gai
            if book.book_id.lower() == keyword or keyword in book.title.lower():
                print("-" * 25)
                book.show()
                found = True
        if not found:
            print("Book nahi mili!")

    # 4. book issue karna
    def issue_book(self, book_id, student):
        book = self.find_by_id(book_id)
        if book is None:
            print("Error: book nahi mili!")
            return
        # agr available quantity zero hai to issue nahi ho sakti
        if book.available == 0:
            print("Sorry, is book ki koi copy available nahi hai.")
            return
        book.available -= 1
        self.issued.append({"book_id": book_id, "student": student})
        print("Book issued successfully!")
        print("Available Quantity:", book.available)

    # 5. book wapis lena
    def return_book(self, book_id, student):
        book = self.find_by_id(book_id)
        if book is None:
            print("Error: book nahi mili!")
            return
        # issued list mein dekhna hai k ye student ne ye book li bhi thi ya nahi
        for record in self.issued:
            if record["book_id"] == book_id and record["student"].lower() == student.lower():
                self.issued.remove(record)
                book.available += 1
                print("Book returned successfully!")
                print("Available Quantity:", book.available)
                return
        print("Error: is student k naam par ye book issue nahi hai!")

    # 6. book delete karna
    def delete_book(self, book_id):
        book = self.find_by_id(book_id)
        if book is None:
            print("Error: book nahi mili!")
            return
        # agr koi copy issue hai to delete nahi kar sakte
        for record in self.issued:
            if record["book_id"] == book_id:
                print("Error: is book ki copy issue hai, delete nahi ho sakti!")
                return
        del self.books[book_id]
        print("Book deleted successfully!")

    # 7. issued books dikhana
    def view_issued(self):
        if len(self.issued) == 0:
            print("Abhi koi book issue nahi hai.")
            return
        print("\n----- ISSUED BOOKS -----")
        for record in self.issued:
            book = self.books[record["book_id"]]
            print("Book ID:", book.book_id, "| Title:", book.title, "| Student:", record["student"])


# ---------- helper functions ----------

# quantity lene ka function, jab tak sahi (positive whole number) na ho bar bar poochta hai
def get_quantity():
    while True:
        value = input("Enter Quantity: ").strip()
        # isdigit() se pata chalta hai k sirf digits hain ya nahi
        if value.isdigit() and int(value) > 0:
            return int(value)
        print("Invalid! quantity positive whole number honi chahiye.")


# khali input ko reject karne ka function
def get_text(message):
    while True:
        value = input(message).strip()
        if value != "":
            return value
        print("Ye khali nahi ho sakta, dobara likhein.")


def show_menu():
    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Add Book")
    print("2. View All Books")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Delete Book")
    print("7. View Issued Books")
    print("8. Exit")


# ---------- main program ----------
def main():
    library = Library()   # library ka object bana liya

    # while loop jab tak user exit na kare program chalta rahe ga
    while True:
        show_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            print("\nADD NEW BOOK")
            book_id = get_text("Enter Book ID: ")
            title = get_text("Enter Book Title: ")
            author = get_text("Enter Author Name: ")
            quantity = get_quantity()
            library.add_book(book_id, title, author, quantity)

        elif choice == "2":
            library.view_all()

        elif choice == "3":
            print("\nSEARCH BOOK")
            keyword = get_text("Enter Book ID or Title: ")
            library.search(keyword)

        elif choice == "4":
            print("\nISSUE BOOK")
            book_id = get_text("Enter Book ID: ")
            student = get_text("Enter Student Name: ")
            library.issue_book(book_id, student)

        elif choice == "5":
            print("\nRETURN BOOK")
            book_id = get_text("Enter Book ID: ")
            student = get_text("Enter Student Name: ")
            library.return_book(book_id, student)

        elif choice == "6":
            print("\nDELETE BOOK")
            book_id = get_text("Enter Book ID: ")
            library.delete_book(book_id)

        elif choice == "7":
            library.view_issued()

        elif choice == "8":
            print("Thank you! Program band ho raha hai.")
            break   # loop khatam, program exit

        else:
            # menu mein se koi aur cheez likhi to ye chale ga
            print("Invalid choice! 1 se 8 tak number likhein.")


# program yahan se start hota hai
if __name__ == "__main__":
    main()
