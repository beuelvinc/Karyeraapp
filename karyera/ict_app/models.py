from django.db import models
from ckeditor.fields import RichTextField

from django.contrib.auth.models import AbstractUser
from django.conf import settings

from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=120)
    def __str__(self):
        return self.name


class Book_category(models.Model):
    name = models.CharField(max_length=120)
    def __str__(self):
        return self.name


class Course_category(models.Model):
    name = models.CharField(max_length=120)
    def __str__(self):
        return self.name


class Carousel(models.Model):
    description=models.CharField(max_length=200, blank=True, null=True)
    image=models.ImageField(upload_to='carousel',blank=True)


class Blog(models.Model):
    image=models.ImageField(upload_to="blog_pics",blank=True, null=True)
    author=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    tag = models.ForeignKey(Category, on_delete=models.CASCADE,default='Design')
    content = RichTextField(config_name='awesome_ckeditor')
    created_date = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    approved_blog = models.BooleanField(default=False)
    rank=models.IntegerField(default=0)
    def approve(self):
        self.approved_blog = False
        self.save()
    def __str__(self):
        return self.title
 

class Book(models.Model):
    title = models.CharField(max_length=210)
    image=models.ImageField(upload_to="book_pics",blank=True, null=True)
    shared_date = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    content=models.TextField(blank=True, null=True)
    file=models.FileField(upload_to="books_file")
    tag = models.ForeignKey(Book_category, on_delete=models.CASCADE,blank=True, null=True)

    def __str__(self):
        return self.title
 

class Comment(models.Model):
    author=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,default="")
    post = models.ForeignKey(
        'Blog', on_delete=models.CASCADE, related_name='comments')
    comment = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
 

    def __str__(self):
        return self.author.email


class Course(models.Model):
    title=models.CharField(max_length=50,default='add')
    content=models.TextField(default='Nothing')
    course_link=models.TextField(default='Nothing')
    image=models.ImageField( upload_to="course_images",blank=True, null=True)
    rank=models.IntegerField(default=0)
    created_date = models.DateTimeField(auto_now_add=True)
    tag = models.ForeignKey(Course_category, on_delete=models.CASCADE,blank=True, null=True)

    def __str__(self):
        return self.title


class Most_popular_books(models.Model):
    image=models.ImageField(blank=True, null=True)
    title=models.CharField(max_length=50)

    def __str__(self):
        return self.title





class ContactPart(models.Model):
    content=models.TextField()
    number=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    def __str__(self):
        return "Yalniz 1 eded olmalidir"




class About_part(models.Model):
    title=models.CharField(max_length=50)
    description=models.TextField()
    main_image=models.ImageField()
    second_image=models.ImageField()
    awards=models.PositiveSmallIntegerField()
    articles=models.PositiveSmallIntegerField()
    projects=models.PositiveSmallIntegerField()

    card_title_1=models.CharField(max_length=250)
    card_description_1=models.TextField()

    card_title_2=models.CharField(max_length=250)
    card_description_2=models.TextField() 
    
    card_title_3=models.CharField(max_length=250)
    card_description_3=models.TextField()

    def __str__(self):
        return "Yalniz 1 eded olmalidir"










from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

class UserManager(BaseUserManager):
    def create_user(self, email,  password=None, is_admin=False, is_staff=False, is_active=True):
        if not email:
            raise ValueError("User must have an email")
        if not password:
            raise ValueError("User must have a password")

        user = self.model(
            email=self.normalize_email(email)
        )
        user.set_password(password)  # change password to hash
        # user.profile_picture = profile_picture
        user.admin = is_admin
        user.staff = is_staff
        user.active = is_active
        user.save(using=self._db)
        return user

    def create_staffuser(self, email,  password=None):
        user = self.create_user(
            email,
            password=password,
            is_staff=True,
        )
        return user

    def create_superuser(self, email,  password=None):
        user = self.create_user(
            email,
            password=password,
            is_staff=True,
            is_admin=True,
        )
        return user


from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class UserManager(BaseUserManager):

  def _create_user(self, email, password, is_staff, is_superuser, **extra_fields):
    if not email:
        raise ValueError('Users must have an email address')
    now = timezone.now()
    email = self.normalize_email(email)
    user = self.model(
        email=email,
        is_staff=is_staff, 
        is_active=True,
        is_superuser=is_superuser, 
        last_login=now,
        date_joined=now, 
        **extra_fields
    )
    user.set_password(password)
    user.save(using=self._db)
    return user

  def create_user(self, email, password, **extra_fields):
    return self._create_user(email, password, False, False, **extra_fields)

  def create_superuser(self, email, password, **extra_fields):
    user=self._create_user(email, password, True, True, **extra_fields)
    return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=254, unique=True)
    name = models.CharField(max_length=254, null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def get_absolute_url(self):
        return "/users/%i/" % (self.pk)



from django.contrib.auth.admin import UserAdmin as BaseUserAdmin



class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password', 'name', 'last_login')}),
        ('Permissions', {'fields': (
            'is_active', 
            'is_staff', 
            'is_superuser',
            'groups', 
            'user_permissions',
        )}),
    )
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': ('email', 'password1', 'password2')
            }
        ),
    )

    list_display = ('email', 'name', 'is_staff', 'last_login')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ('groups', 'user_permissions',)


