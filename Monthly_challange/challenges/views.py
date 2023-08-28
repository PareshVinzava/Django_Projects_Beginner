from django.shortcuts import render
from django.http import Http404 ,HttpResponse, HttpResponseNotFound, HttpResponseRedirect
# Never Foreget to import  this all While Working With Requestes and Responses
from django.urls import reverse
#Now for using Templates import following thing but we also have shortcut instead of using render_to string we can simply use render which we have imported from django.shortcuts
# from django.template.loader import render_to_string  


monthly_challenges = {

               "january": "This works very well" ,
               "february": "It's feb bruh start preparing for exam",
               "march": "It's March Exams are started now", 
               "april": "Exams are over now enjoy your Vacations ",
               "may": "it's may start lokking for good colleges ",
               "june": "it's june finalize colleage " , 
               "july": " Tripathi birthay Party  ",
               "augest": "Take new incitavies",
               "september":"improve your non - verbal skills",
               "october": " start preparing for mid examinatons ", 
               "november": None,
               "december": " participant into Cultural fest."
}

# Create your views here.



def index(request): 
    list_items = ""
    months = list(monthly_challenges.keys())

    return render(request,"challenges/index.html",{"months":months})

    # for month in months:
    #     capitalized_month = month.capitalize()
    #     month_path = reverse("month-challenges", args=[month])
    #     list_items += f"<li><a href= \"{month_path}\">{capitalized_month}</a></li>"


    # response_data = f"<ul>{list_items}</ul>"
    # return HttpResponse(response_data)




# def index(request):
#     return HttpResponse("This works very well")

# def february(request):
#     return HttpResponse("Walk for at least 20 minutes every day! ")

# def monthly_challange_by_number(request, month):
    
#     return HttpResponse(month)

# def monthly_challange(request, month): # here this will take two parameters bcz 1st is default req. and sec is for month so we don't have to write it again and again
#     # This Second Parameter month will be taken from urls.py which will be given by user and fetch into <month> into urls.py file of app.
#     challange_text = None
#     # Instead of writing this whole long elif statememnt better way is to use dictionaray for this type of senarios  
#     if month == "february":
#         challange_text = "It's feb bruh start preparing for exam"
#     elif month == "march":
#         challange_text = "It's March Exams are started now"
#     elif month == "april":
#         challange_text = "Exams are over now enjoy your Vacations "
#     else:
#         return HttpResponse(" This month is not supported")

#     return HttpResponse(challange_text)




# Now Our Next Task Is To To Redirect user intizers requestes to months

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("<h1>Invalid Month</h1>")
    
    redirect_month = months[month-1]
    redirect_path = reverse("month-challenges", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


   # return HttpResponseRedirect("/challenges/" + redirected_month) # so here i am redirecting the name of month 

    # as example june so it'll be given as 8000/challenges/june so this way numbers will be redirectrd into months
    # But we can make it more dynamical by using reverse function and named url

# it is Good and Optimized way  by using Dictionary 
def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]  # It is always a good practice to wrote app name / before the html file bcz if i have so many apps and same named html files then django will merge them and we don't want to happen this.
        #this is short cut we can use this instead of render_to_string 
        # don't foget it'll take two arguments first is always request and second one is appname/html file name.            

        return render(request,"challenges/challenge.html",{"text":challenge_text, "month_name":month}) # this is okay for static hard written html response but for making it dynamic see below
        #return HttpResponse(challenge_text)

 
        # response_data = f"<h1>{challenge_text}</h1>" # note here is we have to write challenges / html bcz only html won't going to work ||| #f"<h1>{challenge_text}</h1>"    # This is how we can return HTML
        # return HttpResponse(response_data) # this try section of code will not work until and unless i do the settings for the Templates
        # when setting for Templates Done then try section will work and except will not 
    except:
        raise Http404 # This is how we can return HTML
    


