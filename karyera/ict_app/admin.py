from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register([Blog,Category,
				Carousel,Course,Comment,
				Most_popular_books,Book,ContactPart,About_part])

admin.site.register(User, UserAdmin)