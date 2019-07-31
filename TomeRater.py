# Elad Dolev / TomeRater Project
# ------------------------------
#
# A good practice and that is what I do now when I start using the know;edge from this Course that I apply to my work as QA, writing Scripts to
# maintain my VM and Environments, would be use each Class in a seperate File but for some reason I kept getting Errors and I decide does not worth the trouble
# of Debugging as I use this Practice already in daily Life .

class Book(object):
    def __init__(self, title, isbn, price = 0.0):
        self.title = title
        self.isbn = isbn
        self.ratings = []
        self.price = price #My addition

    def __hash__(self):
        return hash((self.title, self.isbn))

    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def set_isbn(self, new_ISBN):
        self.isbn = new_ISBN
        print("The ISBN of the book {} has been updated to {}".format(self.title, self.isbn))

    def get_price(self):
        return self.price

    def add_rating(self, rating):
        if rating:
            if rating > 0 and rating < 4:
                self.ratings.append(rating)
            else:
                print("Invalid Rating")

    def __eq__(self, other_book):
        if self.title == other_book.title and self.isbn == other_book.isbn:
            return True
        else:
            return False

    def __repr__(self):
        return self.title

    def get_average_rating(self):
        rtg_summ = 0
        for rtg in self.ratings:
            rtg_summ += rtg
        if len(self.ratings) > 0:
            avg_rtg = rtg_summ / len(self.ratings)
        else:
            avg_rtg = 0
        return avg_rtg

class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

    # Return email of this user
    def get_email(self):
        return self.email

    # Change email of this user
    def change_email(self, address):
        self.email = address
        print("The user {} email has been updated to {}".format(self.name, self.email))

    # Representation of the user
    def __repr__(self):
        return ("The user: {}, with email: {}, has {} books read".format(self.name, self.email, len(self.books)))

    # Test if equal is same as another email user
    def __eq__(self, other_user):
        if self.name == other_user.name and self.email == other_user.email:
            return True
        else:
            return False

    # Method to call when user has read a book, Rating is Optional
    def read_book(self, book, rating=None):
        self.books[book] = rating

    # Method to get Average Rating of Books read and rated by User
    def get_average_rating(self):
        books_count = 0
        rtg_summ = 0
        for rtg in self.books.values():
            if rtg:
                books_count += 1
                rtg_summ += rtg
                avgrtg = rtg_summ / books_count
        return avgrtg

class Fiction(Book):

    def __init__(self, title, author, isbn, price):
        super().__init__(title, isbn)
        self.author = author

    def get_author(self):
        return self.author

    def __repr__(self):
        return ("{} by {}".format(self.title, self.author))

class NonFiction(Book):

    def __init__(self, title, subject, level, isbn, price):
        super().__init__(title, isbn, price)
        self.subject = subject
        self.level = level

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level

    def __repr__(self):
        return ("{}, a {} manual on {} for ${price}".format(self.title, self.level, self.subject, price=self.price))

class TomeRater(object):

    def validate_email(self, email):
        if "@" in email and email[-4:] in [".com", ".edu", ".org", ".de"]:
            return True
        else:
            return False

    def __init__(self):
        self.users = {}
        self.books = {}

    def __repr__(self):
        return "TomeRater {} and {}".format(self.users, self.books)

    def __str__(self):
        return "in TomeRater users are {} and books are {}".format(self.users, self.books)

    def __eq__(self, other_rater):
        if self.users == other_raters.users and self.books == other_rater.books:
            return True
        else:
            return False

    def create_book(self, title, isbn, price):
        new_book = Book(title, isbn)
        return new_book

    def create_novel(self, title, author, isbn, price):
        new_novel = Fiction(title, author, isbn, price)
        return new_novel

    def create_non_fiction(self, title, subject, level, isbn, price):
        new_nf = NonFiction(title, subject, level, isbn, price)
        return new_nf

    def add_book_to_user(self, book, email, rating=None):
        user = self.users.get(email, None)
        if user:
            user.read_book(book, rating)
            if book not in self.books:
                self.books[book] = 0
            self.books[book] += 1
            book.add_rating(rating)
        else:
            print("No user with email " + email)

    def add_user(self, name, email, user_books=None):
        new_user = User(name, email)
        #Workaround if all checks and  pass, then proceed is set to True and User can be added
        proceed = False
        #I found many ways to go with Validation, after several tries I go with this Method of split"."
        #Which I compare to the Valid Extension I defined before.
        valid_email_extensions = ["com", "edu", "org"]
        try:
            ext = (email.split(".")[-1])
            valid_ext = False
            for item in valid_email_extensions:
                if ext == item:
                    valid_ext = True
        except:
            print("Something is wrong with Email Format.")

        if self.users.get(email):
            print ("The User with email address {} already exists.\n".format(email))
        elif "@" not in email:
            print("Missing @: Email address {} is not valid. Try again. \n".format(email))
        elif valid_ext == False:
            print("User typed: {} - Email must end in .com, .edu or .org.\n".format(email))
        else:
            proceed = True
        if proceed == True:
            self.users.update({email: new_user})
            print("User {} with email {} added successfully!\n".format(name, email))
            if user_books is not None:
                for book in user_books:
                    self.add_book_to_user(book, email, rating=None)

    def get_Investment_of_user(self, user_email):
        # Total Value spent by User on Books
        worth = 0
        user = self.users[user_email]
        for book in user.books:
            worth += book.price
        return "Total Value owned by user: {0}: ${1:.2f}".format(user_email, worth)

    def print_catalog(self):
        for item in self.books:
            print(item)

    def print_users(self):
        for user in self.users.values():
            print(user)

    def most_read_book(self):
        mostread = None
        highest_read_count = 0
        for book in self.books:
            value = self.books.get(book)
            if value > highest_read_count:
                mostread = book
                highest_read_count = value
        print("The most read book is:  {} with {} reads!".format(mostread, highest_read_count))
        return mostread #I need still to understand how to avoid here the 2nd Return of the Book Name

    def highest_rated_book(self):
        high_rtg = 0
        high_rtd_book = None
        for book in self.books:
            bookavgrtg = book.get_average_rating()
            if bookavgrtg > high_rtg:
                high_rtg = bookavgrtg
                high_rtd_book = book
            return high_rtd_book

    def most_positive_user(self):
        high_rtg = 0
        posit_user = None
        for user in self.users.values():
            useravgrtg = user.get_average_rating()
            if useravgrtg > high_rtg:
                high_rtg = useravgrtg
                posit_user = user
        return posit_user

    def spacing(self): # Just simple Line spacing to be used in populate.py
        print("")
        print("")


