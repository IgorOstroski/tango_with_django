from django.test import TestCase
from .models.category import Category

class teste_Category(TestCase):

    def teste_comment_nulo(self):
       Category.objects.get_or_create(name = "Teste")
       self.assertEquals(Category.objects.find(name = "Teste"),True)
