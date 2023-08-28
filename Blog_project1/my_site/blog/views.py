from django.shortcuts import get_object_or_404, render
from django.http import Http404,HttpResponse,HttpResponseNotFound

from .models import post 

# Create your views here.

from datetime import date


# all_posts = [
   
# ]



def get_date(post):
    return post["date"]


def starting_page(request):
    latest_posts = post.objects.all().order_by("-date")[:3]
    # sorted_posts = sorted(all_posts, key=get_date)
    # latest_posts = sorted_posts[-3:]  # I had used this for dummy data but now no longer i need this bcz now we are taking data from the database and not from this dummy data.
    return render(request, "blog/index.html",  {
        "posts": latest_posts             # When i use this view for latest views so for the all posts i will start getting error so for all postes also i have to make changes into views of posts.
    })


def posts(request):
    all_posts = post.objects.all().order_by("-date")
    return render(request, "blog/all-posts.html", {
        "all_posts":all_posts
    })

def post_details(request,slug):  #here it'll take slug parameter 
    identified_post = get_object_or_404(post, slug=slug)
    # all_posts = post.objects.all()
    # identified_post = next(post for post in all_posts if post.slug == slug )  # We could have used this both commented line of code and it's totally fine way to do so. but here we'll use different way of doing this.
    return render(request, "blog/post-details.html" , {
        "post":identified_post,
        "post_tags": identified_post.tags.all()
    })