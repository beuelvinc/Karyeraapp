from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from .forms import *
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout,login,authenticate
from django.views.generic import DetailView, TemplateView
from django.http import Http404
from django.core.files.storage import FileSystemStorage
from django.db.models import Count,F
from django.contrib.auth.decorators import login_required

def home(request):
    carousel=Carousel.objects.all()
    blogs=Blog.objects.order_by('-created_date')[:4]
    mpbs=Most_popular_books.objects.all()
    ctgry=Category.objects.all()
    pop_blogs=Blog.objects.annotate(number_of_comments=Count('comments')).order_by('-number_of_comments')[:3]
    return render(request,"home.html",{"blogs":blogs,"carousel":carousel,"mpbs":mpbs,"ctgries":ctgry,"pop_blogs":pop_blogs})
    

def about(request):
    data=About_part.objects.first()
    return render(request, 'about.html',{"data":data})

def contact(request):
    if request.method=="POST":
        send_mail(
            request.POST.get("firstname"),
            request.POST.get("subject"),
            request.POST.get("e-mail"),
            ['elvinc402@gmail.com'],
            fail_silently=False,
        )
        return redirect("/")
    contact=ContactPart.objects.first()
    return render(request, 'contact.html',{"contact":contact})

def teachers(request):
    return HttpResponse('<h1> Teachers Page </h1>')

def courses(request):
    return HttpResponse('<h1> Courses Page </h1>')



def ebooks(request):
    return HttpResponse('<h1> Ebooks Page </h1>')

def search(request):
    query = request.GET.get('q')
    if query:
        data=Blog.objects.filter(title__icontains=query)
    else:
        data=[]
    posts_all=Blog.objects.all()[:4]
    return render(request,"blogs.html",{"data":data,"blogs":posts_all,"posts":data})
 


def blogs(request):
    posts_all=Blog.objects.all()
    blogs=Blog.objects.all()[:4]
    return render(request,"blogs.html",{"blogs":blogs,"posts":posts_all})


@login_required
def create(request):
    form=BLogForm()
    if request.method=='POST':
        data=request.POST
        uploaded_file=request.FILES['file']
        fs=FileSystemStorage()
        fs.save(uploaded_file.name,uploaded_file)
        if data:
            form=BLogForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect("/")
    return render(request,"create.html",{"form":form})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(request, email=user.email, password=raw_password)
            if user is not None:
                login(request, user)
            else:
                print("user is not authenticated")
            return redirect('/')

    else:
        form = SignUpForm()
    return render (request,'signup.html',{'form':form})


def Login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(email=username, password=password)
            if user is not None:
                    login(request, user)
                    return redirect("/")
        
    else:
        form = AuthenticationForm()

    return render(request,'login.html',{'form':form})

@login_required
def Logout(request):
    logout(request)
    return redirect('/') 



# def description(request, id):
#     blog = blogs.objects.get(id=id)
#     print(blog.title)
#     nom=Nominatim()
   
    # comments = Comment.objects.filter(post=id)
    # if request.method == "POST":
    #     post = get_object_or_404(Blog, id=id)
    #     form = CommentForm(request.POST)
    #     if form.is_valid():
    #         comment = form.save(commit=False)
    #         comment.author = request.user
    #         comment.post = post
    #         comment.save()
    #         return redirect('blog_detail', id=post.id)
    # else:
    #     form = CommentForm()
#     blogs = Blog.objects.filter(blog=id)
#     print(blogs)


def Detailview(request,id):
    data=Blog.objects.filter(id=id).first()
    comments = Comment.objects.filter(post=id)
    form=CommentForm()
    if request.method == "POST":
        if request.user.is_authenticated:
            post = get_object_or_404(Blog, id=id)
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.author = request.user
                comment.post = post
                comment.save()
                return redirect('blog_details', id=post.id)
        else:
            return redirect("/login")
    else:
        form = CommentForm()
   
    if data:
        return render(request,'single.html',{"blg":data,"form":form,"comments":comments})
    else :
        raise  Http404("<h1>Page not found</h1>")



def category(request,name):
    blogs=Blog.objects.all()[:4]

    posts=Blog.objects.filter(tag__name=name)
    print(posts)
    return render(request,'category.html',{"blogs":blogs,"posts":posts,"tag":name})




    