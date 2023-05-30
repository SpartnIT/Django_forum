from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from .forms import PostForm

# Create your views here.
def index(request):
    # If the method is POST 
    if request.method == 'POST':
       form = PostForm(request.POST)
       # If the method is valid
       if form.is_valid():
           # Yes, save
           form.save()

           # Redirect to homepage
           return HttpResponseRedirect('/')
       
       else:   
           #No, Show error
           return HttpResponseRedirect({form.errors.as_json})




    #get all posts, limit 20
    posts = Post.objects.all().order_by('-created_at')[:20]
    #show
    return render(request, 'posts.html',{'posts':posts})

def delete(request, post_id):
    # Find post
    posts = Post.objects.get(id = post_id)
    posts.delete()
    return HttpResponseRedirect('/')


#model for image and like button in models.py
#add two function for edit and like button in views.py
#add cloudinary configration in settings.py
#add the urls for edit and like button in urls.py in app
#in template you need to add edit.html
#download images for the application
#style.css

