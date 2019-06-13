from django.db import models
from django.template.defaultfilters import slugify

from markdownx.models import MarkdownxField
from markdownx.utils import markdownify

 
class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    person_image = models.ImageField(upload_to='people/img/', verbose_name='image', null=True, blank=True)
    website_link = MarkdownxField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.first_name + " " + self.last_name

    @property
    def show_website_link(self):
        return markdownify(self.website_link)        

class Summary(models.Model):
    name = models.SlugField(max_length=255)
    summary_text = MarkdownxField(max_length=10000, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.person)

    @property
    def show_markdown(self):
        return markdownify(self.summary_text)
