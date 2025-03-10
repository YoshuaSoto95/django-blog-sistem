from django.shortcuts import get_object_or_404, render
from dashboard.models import Post

# Create your views here.
def home(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'home.html', context)

def view_post(request, id):
    posts = get_object_or_404(Post, id=id)
    context = {'post': posts}
    return render(request, 'view_post.html', context)