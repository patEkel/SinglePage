from django.contrib import admin
from .models import Summary, Person
from markdownx.admin import MarkdownxModelAdmin


class SummaryAdmin(admin.ModelAdmin):
    model = Summary

class PersonAdmin(admin.ModelAdmin):
    model = Person

admin.site.register(Summary, MarkdownxModelAdmin)
admin.site.register(Person, PersonAdmin)
