from django.shortcuts import get_object_or_404,render

from .models import BOOK  # here i have imported my model class

from django.http import Http404

from django.db.models import Avg, Max,Min

# Create your views here.


def index(request):

    books = BOOK.objects.all().order_by("-rating")  # i saved my query into books variable
    num_books = books.count()
    avg_rating = books.aggregate(Avg("rating"))  #  rating__avg, rating__min we have to write this into the templates for using it's values.
    return render(request, "book_outlet/index.html", {
        "books":books,
        "total_number_of_books": num_books,
        "average_rating": avg_rating
    })


def book_details(request,slug):
    # try:
        # book = BOOK.objects.get(pk=id)
    # except:
        # raise Http404()

    book = get_object_or_404(BOOK, slug=slug) # Whenever i use this get_object_or_404 function i dont have to write except and raise 404.html it'll automatically do this for us but from shortcut we have to import this function.
    return render(request, "book_outlet/book_detail.html", {
        "title":book.title,
        "author":book.author,
        "rating":book.rating,
        "is_bestselling": book.is_bestselling
    })







