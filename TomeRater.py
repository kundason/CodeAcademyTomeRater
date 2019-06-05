class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = []

    def get_email(self):
        return self.email

    def change_email(self, address):
        self.email = address
        return "User has updated its email address. New email is: " + self.email

    def __repr__(self):
        user_details = "User" + self.name + ", email: " + self.email + ", books read: " + len(str(books.read))
        return user_details

    def __eq__(self, other_user):
        if self.name == other_user and self.email == other_user.email:
            return True
        else
            return False




class Book(object):
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        # maybe add later validation for isbn if an integer

    def get_title(self):
        reruen self.title

    def get_isbn(self):
        return self.isbn

    def set_isbn(self, new_isbn):
        try:
            old_isbn = self.isbn
            self.isbn = int(new_isbn)
            print (""" Trying to change thr ISBN for {}...
            Old ISBN was:
            New ISBN is:

    def add_rating(self, rating):
        self.rating = rating
        try:
            if int(rating >=0 and <=4):
                self.rating.append(self.rating)
            else:
                print("Invalid Rating")
        except:
            print("User Error, value entered must between 0 and 4)


    def __eq__ (self, another_book):


class Non_Fiction(Book):

    def __init__(self, title, subjuct, level, isbn):



