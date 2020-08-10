from django.db import models
# from django_fields import DefaultStaticImageField

from .user import User

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    note = models.CharField(max_length=500)
    # rating = models.CharField(max_length=100)
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    onWishlist = models.BooleanField()
    onRead = models.BooleanField()
    photo = models.ImageField(upload_to='books', default='books/default_Image.jpg')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    # Returns a sensical string representation of the data
    def __str__(self):
        return self.title

    # Before serializers we want dictionary representations of the data
    def as_dict(self):
        return {
          'id': self.id,
          'title': self.title,
          'author': self.author,
          'note': self.note,
          'rating': self.rating,
          'onWishlist': self.onWishlist,
          'onRead': self.onRead,
          'photo': self.photo
        }
