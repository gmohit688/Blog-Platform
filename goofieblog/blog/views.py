from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import posts

# Create your views here.
# class based views for posts
class postslist(generic.ListView):
    queryset = posts.objects.filter(status=1).order_by('-created_on')
    template_name = 'home.html'
    paginate_by = 4

# class based views for each post
class postdetail(generic.DetailView):
    model = posts
    template_name = 'post.html'

def post_detail(request, slug):
    post = get_object_or_404(posts, slug=slug)
    return render(request, 'post_detail.html', {'post': post})
    
def post_detail_amp(request, slug):
    post = get_object_or_404(posts, slug=slug)
    return render(request, 'post_detail_amp.html', {'post': post})