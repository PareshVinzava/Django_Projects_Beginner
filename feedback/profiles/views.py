from django.shortcuts import render
from django.views import  View
from django.http import  HttpResponseRedirect

# from .forms import  ProfileForm

from .models import UserProfile

from django.views.generic.edit import CreateView

from django.views.generic import  ListView

# Create your views here.


# def store_file(file):  # I have created this function for saving the uploaded image to temp named folder in root directory. when i get image from user i will pass that into this function.
#     with open("temp/image.png", "wb+") as dest:
#         for chunk in file.chunks():
#             dest.write(chunk) # I have commented this bcz noe i amusing models to save file so don't need this now.



class CreateProfileView(CreateView):
    template_name = "profiles/create_profile.html"
    model = UserProfile
    fields = "__all__"    # If i use this view class then i won't have to write below long class and dont even need to use forms.py file at all.
    success_url = "/profiles"



class ProfilesView(ListView):
    model = UserProfile
    template_name = "profiles/user_profiles.html"
    context_object_name = "profiles"





# class CreateProfileView(View):
#     def get(self, request):
#         form = ProfileForm()
#         return render(request, "profiles/create_profile.html", {
#             "form": form  # We create this think because when we render our template with that template we can senf our inbuilt created form class to it using variable name to html file.
#         }) # and also it is inbuilt form so will auto handel errors and error messages written into the form class. it is normal form class not a model form bcz we haven't created any models yet.


#     def post(self, request):
#         submitted_form = ProfileForm(request.POST, request.FILES)
        
#         if submitted_form.is_valid():
#             profile = UserProfile(image=request.FILES["user_image"])
#             profile.save()
#             # store_file(request.FILES["image"])       # For handling non file type of data which get through form through the user at that time we use request.POST but in file type of data we have to use request.FILES
#             return HttpResponseRedirect("/profiles")

#         return render(request, "profiles/create_profile.html", {
#             "form": submitted_form 
#         })