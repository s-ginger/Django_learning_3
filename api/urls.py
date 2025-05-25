from django.urls import path
from .views import NoteList

urlpatterns = [
    path('books/', NoteList.as_view(), name='book-list'),
]
