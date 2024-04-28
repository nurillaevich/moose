from django.shortcuts import render, get_object_or_404, redirect
from .models import Article, Author, About, Tage, Comment, Contact
from .form import CommentForm


# Create your views here.

def home_page(request):
    post = Article.objects.all()
    context = {
        'posts': post,
    }
    return render(request, 'index.html', context)


def about_page(request):
    about = About.objects.all()
    contex = {
        'abouts': about
    }
    return render(request, 'about.html', contex)


def blog_page(request):
    blog = Article.objects.all()
    context = {
        'blogs': blog
    }
    return render(request, 'blog.html', context)


def article_detail(request, pk, *args, **kwargs):
    form = CommentForm()
    post = get_object_or_404(Article, pk=pk)
    comment = Comment.objects.filter(post__id=pk).order_by('-created')
    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect(f'detail/{post.id}')
    context = {'form': form,
               'posts': post,
               'comments': comment}
    return render(request, 'blog-single.html', context)
