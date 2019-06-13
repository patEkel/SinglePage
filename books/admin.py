from django.contrib import admin

from .models import Review, Book, Author

from markdownx.admin import MarkdownxModelAdmin


class ReviewAdmin(admin.ModelAdmin):
    model = Review
    # add forms? or rely on admin?
admin.site.register(Review, MarkdownxModelAdmin)

class BookAdmin(admin.ModelAdmin):
    model = Book
admin.site.register(Book, BookAdmin)

class AuthorAdmin(admin.ModelAdmin):
    model = Author
admin.site.register(Author, AuthorAdmin)

