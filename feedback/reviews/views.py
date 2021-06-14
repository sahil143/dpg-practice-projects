from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, FormView
from .forms import ReviewForm
from .models import Review

from django.views import View
# Create your views here.


def review(request):
    if request.method == 'POST':
        # existing_data = Review.objects.get(pk=1)
        form = ReviewForm(request.POST)  # instance=existing_data

        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/thank-you")
    else:
        form = ReviewForm()

    return render(request, 'reviews/review.html', {
        "form": form
    })

# class ThankYouView(View):
#   def get(self, request):
#     return render(request, 'reviews/thank_you.html')

def thank_you(request):
    return render(request, 'reviews/thank_you.html')


# class ReviewView(View):
#     def get(self, request):
#         form = ReviewForm()
#         return render(request, 'reviews/review.html', {
#             "form": form
#         })

#     def post(self, request):
#         form = ReviewForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect("/thank-you")
#         return render(request, 'reviews/review.html', {
#             "form": form
#         })

# class ReviewView(FormView):
#   form_class = ReviewForm
#   template_name = 'reviews/review.html'
#   success_url = "/thank-you"

#   def form_valid(self, form):
#       form.save()
#       return super().form_valid(form)

class ReviewView(CreateView):
  model = Review
  form_class = ReviewForm
  form_class = ReviewForm
  template_name = 'reviews/review.html'
  success_url = "/thank-you"

class ThankYouView(TemplateView):
  template_name = "reviews/thank_you.html"

  def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context["message"] = "This Works!!"
      return context  

class ReviewListView(ListView):
  template_name = "reviews/review_list.html"
  model = Review
  context_object_name = "reviews"

  # def get_queryset(self):
  #     base_query = super().get_queryset()
  #     data = base_query.filter(rating__gt=4)
  #     return base_query.all()
  

# class SingleReviewView(TemplateView):
#   template_name = "reviews/single_review.html"

#   def get_context_data(self, **kwargs):
#       context = super().get_context_data(**kwargs)
#       review_id = kwargs["id"]
#       context["review"] = Review.objects.get(pk=review_id)
#       return context
  
class SingleReviewView(DetailView):
  template_name = "reviews/single_review.html"
  model = Review

  def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      loaded_review = self.object
      favorite_id = self.request.session["favorite_review"]
      context["is_favorite"] = favorite_id == str(loaded_review.id)
      return context
  

class AddFavoriteView(View):
  def post(self, request):
    review_id = request.POST["review_id"]
    request.session["favorite_review"] = review_id
    return HttpResponseRedirect('/reviews/' + review_id)


  
  
  
