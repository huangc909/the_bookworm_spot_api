from django.db import models

from .user import User

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    note = models.CharField(max_length=300)
    onWishlist = models.BooleanField()
    onRead = models.BooleanField()
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
          'onWishlist': self.onWishlist,
          'onRead': self.onRead
        }
