from django.urls import path
from book.views import book_create, book_list, book_detail, book_update, book_delete


urlpatterns = [
    path('new/', book_create, name='book_create'),
    path('list/', book_list, name='list'),
    path('<int:pk>/', book_detail, name='book_detail'),
    path('<int:pk>/edit/', book_update, name='book_update'),
    path('<int:pk>/delete/', book_delete, name='book_delete'),
]

