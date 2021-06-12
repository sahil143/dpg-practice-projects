from profiles.models import UserProfile
# from django.shortcuts import render
# from django.views import View
# from django.http import HttpResponseRedirect
# Create your views here.
from django.views.generic.edit import CreateView
from django.views.generic import ListView
# from .forms import ProfileForm


def store_file(file):
  with open("temp/image.jpg", "wb+") as dest:
    for chunk in file.chunks():
      dest.write(chunk)

# class CreateProfileView(View):
#     def get(self, request):
#         form = ProfileForm ()
#         return render(request, "profiles/create_profile.html", {
#           "form": form
#         })

#     def post(self, request):
#         submitted_form = ProfileForm(request.POST, request.FILES)

#         if submitted_form.is_valid():
#           profile = UserProfile(user_image=request.FILES["user_image"])
#           profile.save()
#           return HttpResponseRedirect("/profiles")
        
#         return render(request, "profiles/create_profile.html", {
#           "form": submitted_form
#         })

class CreateProfileView(CreateView):
    model = UserProfile
    template_name = "profiles/create_profile.html"
    fields = '__all__'
    success_url = '/profiles'

class ProfilesView(ListView):
  model = UserProfile
  template_name = "profiles/user_profiles.html"
  context_object_name = "profiles"


