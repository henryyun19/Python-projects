Object oriented programming

class Book:
    def __init__(self,author,title,status):
        self.author = author
        self.title = title
        #checks for error is status is any other than below
        if status != 'yes' and status != 'no' and status != 'unknown' \
        and status != 'overdue':
            raise BookError("unrecognized loan status '"+status+"'")
        else:
            self.status = status
        
    def __str__(self):
        s = str(self.title) + ', ' + str(self.author) + ': ' + str(self.status)
        return s
        
    def __eq__(self,other):
        if self.title == other.title and self.author == other.author and\
        self.status == other.status:
            return True
        else:
            return False
            
    def is_on_loan(self):
        if self.status == 'no' or self.status == 'unknown':
            return False
        else:
            return True
    
    
class Library:
    def __init__(self,books = []):
        books = []
        self.books = books
        
    def __str__(self):
        if len(self.books) == 0:
            return 'Library:\n'
        #special case for when books == 0 and for below always first book to
        #start the list then in a loop continues till there are no more books 
        if len(self.books) == 1:
            s = 'Library:\n\t'+str(self.books[0].title)+', '+\
            str(self.books[0].author)+': '+str(self.books[0].status)+'\n'
            return s
        else:
            s = 'Library:\n\t'+str(self.books[0].title)+', '+\
            str(self.books[0].author)+': '+str(self.books[0].status)+'\n'
            for i in range(1,len(self.books)):
                s = s +'\t'+str(self.books[i].title)+', '+\
                str(self.books[i].author)+': '+str(self.books[i].status)+'\n'
            return s
    
    def __eq__(self,other):
        #checks to see if the book list equal each other 
        if len(self.books) == len(other.books):
            return True
        else:
            return False
        
    def add_book(self, book):
        if book in self.books:
            #checks to see if book is already in list if so error is raised
            raise BookError("duplicate book titled '"+book.title+"'")
        else:
            self.books.append(book)
        
    def books_by_author(self, author):
        g = []
        for i in self.books:
        #gets a list of all the authors and returns them if there is none 
        #an error is raised
            if i.author == author:
                g.append(i)
        if len(g) == 0:
            raise BookError("no books written by '"+author+"'")
        else:
            return g
        
    def book_by_title(self, title):
        for i in self.books:
            if i.title == title:
                return i
        #if no book by the title is found the error is raised
        raise BookError("no book found titled '"+title+"'")

    def total_on_loan(self): 
        count = 0
        for i in self.books:
            #checks if any loan is there then raised counts and returns
            if i.status == 'yes' or i.status == 'overdue':
                count += 1
        return count


class BookError(Exception):
    def __init__(self,msg):
        self.msg = msg
        
    def __str__(self):
        return self.msg
