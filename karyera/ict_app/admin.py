from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register([Blog,
				Carousel,Course,Comment,
				Most_popular_books,Book,About_part])

admin.site.register(User, UserAdmin)