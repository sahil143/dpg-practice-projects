
from django.http.response import HttpResponseRedirect
from blog.forms import CommentForm
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.views import View
from .models import Post

# Create your views here.


def get_date(post):
    return post['date']


# def starting_page(request):
#     latest_posts = Post.objects.all().order_by("-date")[:3]
#     return render(request, 'blog/index.html', {"posts": latest_posts})

class StartingPageView(ListView):
    template_name = 'blog/index.html'
    model = Post
    ordering = ["-date"]
    context_object_name = "posts"

    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset[:3]
        return data


# def posts(request):
#     all_posts = Post.objects.all()
#     return render(request, 'blog/all-posts.html', {"all_posts": all_posts})

class PostsView(ListView):
    model = Post
    template_name = 'blog/all-posts.html'
    context_object_name = "all_posts"


# def post_detail(request, slug):
#     post = get_object_or_404(Post, slug=slug)
#     return render(request, 'blog/post-detail.html', {
#         "post": post,
#         "tags": post.tags.all()
#         })

class PostDetailView(View):

    def is_stored_post(self, request, post_id):
        stored_posts = request.session.get("stored_posts")
        if stored_posts is not None:
            is_saved_for_later = post_id in stored_posts
        else:
            is_saved_for_later = False
        return is_saved_for_later

    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        return render(request, 'blog/post-detail.html', {
            "post": post,
            "post_tags": post.tags.all(),
            "comment_form": CommentForm(),
            "comments": post.comments.all().order_by("-id"),
            "saved_for_later": self.is_stored_post(request, post.id)
            
        })

    def post(self, request, slug):
        comment_form = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)
        if(comment_form.is_valid()):
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            return HttpResponseRedirect(reverse("post-detail-page", args=[slug]))
        
        return render(request, 'blog/post-detail.html', {
            "post": post,
            "post_tags": post.tags.all(),
            "comment_form": comment_form,
            "comments": post.comments.all().order_by("-id"),
            "saved_for_later": self.is_stored_post(request, post.id)
        })

class ReadLaterView(View):

    def get(self, request):
        stored_posts = request.session.get("stored_posts")
        context = {}
        if stored_posts is None or len(stored_posts) == 0:
            context["posts"] = []
            context["has_posts"] = False 
        else:
            context["posts"] = Post.objects.filter(id__in=stored_posts)
            context["has_posts"] = True

        return render(request, 'blog/stored-posts.html', context)

        
    
    def post(self, request):
        stored_posts = request.session.get("stored_posts")

        if stored_posts is None:
            stored_posts = []
        
        post_id = int(request.POST["post_id"])
        if post_id not in stored_posts:
            stored_posts.append(int(request.POST["post_id"]))
        else:
            stored_posts.remove(post_id)
        request.session["stored_posts"] = stored_posts

        return HttpResponseRedirect("/")

