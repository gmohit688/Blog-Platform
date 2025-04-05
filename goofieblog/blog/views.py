from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .models import posts
from .forms import PostForm, CommentForm
from django.contrib.auth.decorators import login_required

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        context['comments'] = post.comments.filter(active=True)  # Fetch active comments
        context['comment_form'] = CommentForm()  # Add the comment form to the context
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        post = self.object
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post  # Associate the comment with the current post
            new_comment.save()
        return self.get(request, *args, **kwargs)

def post_detail_amp(request, slug):
    post = get_object_or_404(posts, slug=slug)
    return render(request, 'post_detail_amp.html', {'post': post})

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user  # Set the current logged-in user as the author
            post.save()
            return redirect('home')  # Redirect to the homepage or posts list
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form})