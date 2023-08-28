from django.db import models
from django.forms import CharField
from matplotlib.pyplot import title
from django.core.validators import MinLengthValidator

# Create your models here.


class Tag(models.Model):
    caption = models.CharField(max_length=20)


    def __str__(self):
        return self.caption



class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_address = models.EmailField()


    def full_name(self):
        return f"{self.first_name} {self.last_name}"


    def __str__(self):
        return self.full_name()




class post(models.Model):
    title = models.CharField(max_length=150)
    excert = models.CharField(max_length=200)
    image_name = models.CharField(max_length=100)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True, db_index=True)
    content = models.TextField(validators=[MinLengthValidator])
    author = models.ForeignKey(
        Author, on_delete=models.SET_NULL,null=True, related_name = "posts"
    )  # Here i have set the relation one to many and  on_delete seted null means on detetion of author it won't going to affect the post, and for reverse quiery into interactive shell i have given related_name="posts"
       # i told django that on deletion of author set this field null but i also have to allow this by giving null=True
    tags = models.ManyToManyField(Tag) # Here i have seted many to many rrlation with the Tag model and POst model
