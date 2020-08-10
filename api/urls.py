from django.urls import path
from .views.mango_views import Mangos, MangoDetail
from .views.user_views import SignUp, SignIn, SignOut, ChangePassword
from .views.book_views import AllBooks, AllBooksDetail, Books, BookDetail

urlpatterns = [
	# Restful routing
    path('mangos/', Mangos.as_view(), name='mangos'),
    path('mangos/<int:pk>/', MangoDetail.as_view(), name='mango_detail'),
    path('sign-up/', SignUp.as_view(), name='sign-up'),
    path('sign-in/', SignIn.as_view(), name='sign-in'),
    path('sign-out/', SignOut.as_view(), name='sign-out'),
    path('change-pw/', ChangePassword.as_view(), name='change-pw'),
    path('all-books/', AllBooks.as_view(), name='all-books'),
    path('all-books-detail/', AllBooksDetail.as_view(), name='all-books-detail'),
    path('books/', Books.as_view(), name='books'),
    path('books/<int:pk>/', BookDetail.as_view(), name='book-detail')
]
