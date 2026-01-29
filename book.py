class Book():
    def __init__(self,title,author,publication_year,is_borrowed,borrowed_by):
        self.title = title
        self.author = author
        self.pubication_year = publication_year
        self.is_borrowed = is_borrowed
        self.borrowed_by = borrowed_by

    def show_info(self):
        print("Title", self.title)
        return
         

    def borrow(user):
        pass

    def return_book():
        pass

    def to_dict():
        pass


class Novel(Book):
    def __init__(self,title,author,publication_year,is_borrowed,borrowed_by,genre):
        Book.__init__(self,title,author,publication_year,is_borrowed,borrowed_by) 
        self.genre = genre  

class Magazine(Novel):
    def __init__(self,title,author,publication_year,is_borrowed,borrowed_by, issue)
        Book.__init__(self,title,author,publication_year,is_borrowed,borrowed_by)
        self.issue = issue