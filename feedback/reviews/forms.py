from .models import Review
from django import forms

# class ReviewForm(forms.Form):
#   user_name = forms.CharField(label="Name", max_length=10, error_messages={
#     "required": "Enhhh!! try again!!",
#     "max_length": "You name is really that long!! Think Again!!"
#   })
#   review_text = forms.CharField(label="Your Feedback", widget=forms.Textarea, max_length=300)
#   rating = forms.IntegerField(label="Your Rating", min_value=1, max_value=5)

class ReviewForm(forms.ModelForm):
  class Meta:
    model = Review
    # fields = '__all__'
    exclude = ["owner_comment"]
    labels = {
      "user_name": "Your Name",
      "review_text": "Yout Review",
      "rating": "Your Rating",
    }
    error_messages = {
      "user_name": {
        "required": "Enhhh!! try again!!",
        "max_length": "You name is really that long!! Think Again!!"
      },
    }
