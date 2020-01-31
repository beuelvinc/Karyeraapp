
from django.urls import path
from . import views
from django.views.generic.base import TemplateView




urlpatterns = [
    path('', views.home, name='ict-home'),
    path('about/', views.about, name='ict-about'),
    path('contact/', views.contact, name='ict-contact'),
    path('blogs/', views.blogs, name='ict-blogs'),
    path('create/', views.create, name='ict-create'),
    path('login/', views.Login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.Logout, name='logout'),
    path('blogs/<int:id>/', views.Detailview,name='blog_details'),
    path('category/<str:name>/', views.category,name='blog_category'),
    path("search/",views.search,name='search'),
    path('voting/<int:id>', views.voting, name='voting'),
    path('books/<int:id>/', views.BookDetail,name='book_details'),
    path('books/', views.books_list, name='ict-books_list'),
    path('courses/', views.courses, name='ict-courses'),
    path('courses/<int:id>', views.courses_detail, name='ict-courses_detail'),
    path('course_voting/<int:id>', views.course_voting, name='course_voting'),

]



