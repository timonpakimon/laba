from django.contrib import admin
from .models import Artiles, Category, Tag, Author

admin.site.register(Artiles),
admin.site.register(Category),
admin.site.register(Tag),
admin.site.register(Author)
