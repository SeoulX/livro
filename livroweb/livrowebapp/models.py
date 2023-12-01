from django.db import models

class Member(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=16)
    type_user = models.CharField(max_length=10)
    #active = models.BooleanField(default=True) 
    #member can have multiple libraries
    libraries = models.ManyToManyField('Library')
    
    def __str__(self):
        return self.username
    
# on_delete=models.CASCADE means that if a value is deleted, all its related data will be deleted as well (ata i think)
    
class Library(models.Model):
    library_name = models.CharField(max_length=200)
    book_count = models.IntegerField()
    # Assuming we want to establish a one-to-many relationship between Library and Book
    # A Library can have multiple books, but each book belongs to only one library
    book = models.ForeignKey('Book', on_delete=models.CASCADE)
    #library can have multiple books
    books = models.ManyToManyField('Book')

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    genre = models.CharField(max_length=100)
    description = models.TextField()
    book_cover = models.ImageField(upload_to='book_covers/')
    #book can have multiple feedbacks
    feedbacks = models.ManyToManyField('Feedback')

class Feedback(models.Model):
    user = models.ForeignKey(Member, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    likes = models.PositiveIntegerField()
    dislikes = models.PositiveIntegerField()
    comments = models.TextField()
    
    
