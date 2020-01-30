
from django.urls import path
from . import views
from django.views.generic.base import TemplateView




urlpatterns = [
    path('', views.home, name='ict-home'),
    path('about/', views.about, name='ict-about'),
    path('contact/', views.contact, name='ict-contact'),
    path('teachers/', views.teachers, name='ict-teachers'),
    path('blogs/', views.blogs, name='ict-blogs'),
    path('courses/', views.courses, name='ict-courses'),
    path('ebooks/', views.ebooks, name='ict-ebooks'),
    path('create/', views.create, name='ict-create'),
    path('login/', views.Login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.Logout, name='logout'),
    path('blogs/<int:id>/', views.Detailview,name='blog_details'),
    path('category/<str:name>/', views.category,name='blog_category'),
    path("search/",views.search,name='search')
]



