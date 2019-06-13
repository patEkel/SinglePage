from django.db import models
from django.template.defaultfilters import slugify

from markdownx.models import MarkdownxField
from markdownx.utils import markdownify

 
class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    website_link = MarkdownxField(max_length=250, null=True, blank=True)
    email = models.EmailField(null=True,  blank=True) # blank sets required to false for form

    def __str__(self):
        return self.first_name + " " + self.last_name

    @property
    def show_website_link(self):
        return markdownify(self.website_link)        


class Book(models.Model):
    title = models.CharField(max_length=100)
    book_image = models.ImageField(upload_to='books/img/', verbose_name='image', null=True, blank=True)
    purchase_link = MarkdownxField(max_length=250, null=True, blank=True)
    authors = models.ManyToManyField(Author)
    publication_date = models.DateField()

    def __str__(self):
        return self.title

    @property
    def show_purchase_link(self):
        return markdownify(self.purchase_link)


class Review(models.Model):
    name = models.SlugField(max_length=255)
    review_text = MarkdownxField(max_length=10000, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.book)

    @property
    def show_markdown(self):
        return markdownify(self.review_text)


    """
    from django import template
    from markdownx.utils import markdownify
    register = template.Library()
    @register.filter
    def show_markdown(text):
        return markdownify(text)
    """
