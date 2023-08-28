
from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import ReviewForm # For using our forms class we have to import those from this

from .models import Review

from django.views import View  # It is for writing class based views if iuse this and create class based views then also have to make change into the our url also.

from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView

from .models import Review

from django.views.generic.edit import FormView , CreateView





# Create your views here.



# class ReviewView(View):  # Here i have created class based view
#     def get(self, request):  # django will automatically class this methods based of type of request
#         form = ReviewForm()

#         return render(request, "reviews/review.html",{
#             "form": form
#         })

#     def post(self, request):
#         form = ReviewForm(request.POST)

#         if form.is_valid():
#           form.save()
#           return HttpResponseRedirect("/thank-you")

#         return render(request, "reviews/review.html",{
#             "form": form
#         })


# class ReviewView(FormView):  # This form class will automatically taken care of which kind of request is coming get or post and behave according that and also does the validation. 
#     form_class = ReviewForm  # by using this form_class attribute i have t point out to form name.
#     template_name = "reviews/review.html"  # Which templates we want ot render
#     success_url = "/thank-you"  # Where to redirect if validation is succesful.


#     def form_valid(self, form):  # This will render Template But won't save to database for saving data we have to create this method and have to tell it that if validation is complete then this will do the saving data.
#         form.save()
#         return super().form_valid(form)


class ReviewView(CreateView):  # This form class CreateViews will do work of FormView class as well as in addition automatically save data to the database also  
     model = Review # Pointing out to the model database table
     form_class = ReviewForm  # by using this form_class attribute i have t point out to form name.
     template_name = "reviews/review.html"  # Which templates we want ot render
     success_url = "/thank-you"







 
# def review(request):   # I have replaced this with the class based views 
#     if  request.method == "POST": 
#         form = ReviewForm(request.POST)

#         if form.is_valid():
#         #   print(form.cleaned_data["user_name"])
#         #   review  =Review(user_name=form.cleaned_data["user_name"],    # If we are using modelforms then we dont't have to initiate our model here we just have to save it.
#         # review_text=form.cleaned_data["review_text"],                      
#         # rating = form.cleaned_data["rating"])      
#         # review.save()    
#            form.save()                                  
#            return HttpResponseRedirect("/thank-you")

#     else:
#         form = ReviewForm()

#     return render(request, "reviews/review.html", {
#         "form": form
#     })



class ThankYouView(TemplateView):
    template_name = "reviews/thank_you.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = "This Works!"
        return context
    



# def thank_you(request):
#     return render(request,"reviews/thank_you.html")

# class ReviewListView(TemplateView):  # It is okay to use this method  and render data to Template but if we want to show list of our data to the template then there is a better and sort method shown as below ListView.
#     template_name = "reviews/review_list.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         reviews = Review.objects.all()
#         context["reviews"] = reviews
#         return context


class ReviewListView(ListView):
    template_name = "reviews/review_list.html"
    model = Review
    context_object_name = "reviews"

    # def get_queryset(self):  # There is lots of get methods we can play with this is for queirying data.
    #     base_query = super().get_queryset()
    #     data = base_query.filter(rating__gt=4)
    #     return data


# class SingleReviewView(TemplateView): 
#     template_name = "reviews/single_review.html"

#     def get_context_data(self, **kwargs):         # We were using this for showing details about single review but instead of writing this much of code we can use view class CALLED ###  DetailView  ### as below   
#         context = super().get_context_data(**kwargs)
#         review_id = kwargs["id"]
#         selected_review = Review.objects.get(pk=review_id)
#         context["review"] = selected_review
#         return context


class SingleReviewView(DetailView):  # By using DetailView we can get easily get single piece of data from database using pk or id also have to change url  int slug to pk fro proper working , also in tempate we can directly use model name and use for loop n all using DetailView class view
    template_name = "reviews/single_review.html"
    model = Review

    def get_context_data(self, **kwargs):
     context = super().get_context_data(**kwargs)
     loaded_review = self.object
     request = self.request 
     favorite_id  = request.session.get("favorite_review")  # Here i can directly by writing in [favorite_review] i can get session data but if we use this method then tere migth be we some time get error if this key not seted yet , so  accesing it with .get method is always a safe way. 
     context ["is_favorite"] = favorite_id == str(loaded_review.id)
     return context





class AddFavoriteView(View):
    def post(self, request):
        review_id =request.POST["review_id"]
        request.session["favorite_review"] = review_id # Here which data is being stored is stored as a string as character it is number but as a string # When we store data to json it'll store data in format of json.  javascript object notation. So it can't conatin objects. we can store string or dictionaries to it.
        return HttpResponseRedirect("/reviews/" + review_id)
        