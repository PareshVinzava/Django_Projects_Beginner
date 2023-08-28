from pickle import FALSE
from tabnanny import verbose
from django.db import models
from matplotlib.pyplot import title
from django.core.validators import MinValueValidator,MaxValueValidator # It is for using validaters after import we have to write which validater we want to use 
from django.urls import reverse
from django.utils.text import slugify 

# Create your models here.


class Country(models.Model):
    name = models.CharField(max_length=80)
    code = models.CharField(max_length=2)


    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Countries"


    
    

class Address(models.Model):
    street = models.CharField(max_length=80)
    postal_code = models.CharField(max_length=5)
    city = models.CharField(max_length=50)
    # Here in Address clas and Author class we have one to one relation

    def __str__(self):
        return f"{self.street}, {self.postal_code}, {self.city}"


    class Meta: # Here i  have created a subclass named Meta which is advanced special feature of django using this we can change what we want ot show in place of our table name on admin panel.
        verbose_name_plural = "Address Entries"
      #verbose_name = ""

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.OneToOneField(Address, on_delete=models.CASCADE, null=True)

    def full_name(self):
        return f"{self.first_name}  {self.last_name}"


    def __str__(self):
        return self.full_name()


class BOOK(models.Model):  # here i am telling django that i want to creates BOOK named table and inherited model class

    title = models.CharField(max_length=50) # coloumn title 
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]) # coloumns rating ## suppose I want that rating should be limited like only from 1 to 5 so for doing this i can use validaters
    author = models.ForeignKey("Author",on_delete=models.CASCADE,null=True, related_name="books")  # one to many realtion # Here by using models.foreinkey i am making relationship with author model and this models class named author and also relation regarding deletion.
    is_bestselling = models.BooleanField(default=False)
    slug = models.SlugField(default="", blank=True ,null=FALSE , db_index=True)   # if Harry Potter 1--> harry-potter-1
         # Here between BOOK and Author we have one to many relation
    published_countries = models.ManyToManyField(Country)  # Here i have established many to many relation with model country
      
    def get_absolute_url(self):  # it is function by using which we can create model urls and use that urls into the tempaltes have write this name into url tage 
        return reverse("book-detail", args=[self.slug])


    
    # def save(self, *args, **kwargs):  # i commented this bcz i don't want to slugify every url name by default and want to give acces to admin panel there admin can change this as per relavance.so i have commented this overweitten save() method here
    #     self.slug = slugify(self.title)
    #     super().save(*args, **kwargs)
      

    # def __str__(self):
    #     return f"{self.title} ({self.rating})"   # here i have overwritten the dundler method so whenever i will use all() function into python interactive terminal it'll only show me this two things of saved data.
         
 # But How To Insert Data using django 
 # For that we have to open interactive terminal by command ##### python3 manage.py shell ####
 # In that terminal first import from projectname.models import classname 
 # Then Create object and save that then django will automatically write sql quiry for inserting data.
 # for seeing data inter python interactive terminal write BOOK.objects.all()  this will show how many data we have but if we want to see content of data we ahve to create new method.
 # There's concept called validaters they are used for changing functionality of model.
 # For using validaters we have to import  from django.corevalidaters import models