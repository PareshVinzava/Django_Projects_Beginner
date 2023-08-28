from django.urls import path

from . import views


urlpatterns = [
    # path("january", views.index), # here simply i am writing the parameters ,response and second parameter is which view logic we want to use for that resquest , simply pointing out 
    # but if we know the numbers of requests like here i have months as a requestes then it is
    # defined and i know the how many requestes will be ther
    # so instead of writting all months here in urls config we can use dynamic path segment $ captured values
    # for that we have inbuilt function <here we have to  write > in between the both the signs 

    #Now if not full path is written then what to show for that we can do something as below 
    path("",views.index, name="index") ,

    path("<int:month>", views.monthly_challenge_by_number), # here i used in dynamic segment is "<int:month>" so if it int then it'll points that to views of by numbers 
    # IMPORTED Note HERE ----> here order of the path matters if i want that first it is checked for intizer then i have to write it first 
    # Otherwise first it'll check for string and will return httpsresponse and for intizer it'll won't be checked 
    # So remember this  ;)


    path("<str:month>", views.monthly_challenge, name="month-challenges") # okay so "<>" is dynamic segment identifier and value with in this is used for view logic
    # But what if i want to check whether what comeing inside it is string or int or what so also we can do that is below
    
]