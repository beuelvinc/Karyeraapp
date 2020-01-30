from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register([Blog,Category,
				Documents,
				Carousel,Comment,
				Most_popular_books,ContactPart,About_part])

admin.site.register(User, UserAdmin)