from django.shortcuts import render
from .models import Post
from .forms import CommentForm
from django.core.paginator import Paginator

def post_list(request):
    posts = Post.objects.all().order_by('-published_date')
    paginator = Paginator(posts_list, 3)
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)
    return render(request,'blog/post_list.html', {'posts': posts})
def post_detail(request, pk):
    post = Post.objects.get(id=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            
            from django.shortcuts import redirect
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/post_detail.html', {'post': post, 'form': form})
