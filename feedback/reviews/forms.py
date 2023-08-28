from django import forms

from .models import Review
    

# class ReviewForm(forms.Form):  # It was an good approach but instead of making it like this and then configuring it with the model instead we can create directly modelforms as below second calss and in sub class we can pointout to the perticular class.
#     user_name = forms.CharField(label="Your Name",max_length=100, error_messages={
#         "required":"Your name must not be empty!",
#         "max_length":"Please enter a shorter name!"
#     })
#     review_text = forms.CharField(label="Your Feedback", widget=forms.Textarea, max_length=200)
#     rating = forms.IntegerField(label="Your Rating", min_value=1, max_value=5)


class ReviewForm(forms.ModelForm): # When we use modelforms it'll auto set lables of form as coloumns we used into models. but we can change it.
    class Meta:  # Here in meta subclass i have pointout to a model which to use,
        model= Review # pointing out to model
        fields = '__all__'  # It means thta i am considering all the models
        # exculde = ['owner_comment']
        labels = {
            "user_name": "Your Name",
            "review_text": "Your Feedback",
            "rating": "Your Rating"
        }

        error_messages = {
            "user_name": {
                "required": "Your name must not be empty",
                "max_length": "Please enter a shorter mname!"
            }
        }