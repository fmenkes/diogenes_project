#coding: utf-8

from django.test import TestCase
from models import Book
from registration.models import UserModel

class BookMethodTests(TestCase):
    def test_ensure_encoding_works(self):
        alice = UserModel().objects.create_user('alice', 'alice@example.com', 'secret')
        book = Book(title="Ñ%$#", first_name="Jesús", last_name="Öberg", user=alice)
        book.save()