from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator
from blog.models import Post, Category
from django.contrib.auth.models import User


def index(request):
    posts = Post.objects.get_published_and_order_by()

    paginator = Paginator(posts, 6)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        'blog/pages/index.html',
        {
            'page_obj': page_obj, 'is_welcome': True,
        }
    )


def post(request, slug):
    post = Post.objects.get_published_and_order_by().filter(slug=slug).first()
    return render(request, 'blog/pages/post.html', {'post': post})


def custom_page(request, slug):
    return render(request, 'blog/pages/custom_page.html')


def posts_by_author(request, author_id):
    author = get_object_or_404(User, pk=author_id)
    posts = Post.objects.get_published_and_order_by().filter(created_by__pk=author_id)
    paginator = Paginator(posts, 6)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        'blog/pages/index.html',
        {
            'page_obj': page_obj, 'is_welcome': False, 'author': author,
        }
    )


def posts_by_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = Post.objects.get_published_and_order_by().filter(category__slug=slug)
    paginator = Paginator(posts, 6)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        'blog/pages/index.html',
        {
            'page_obj': page_obj, 'is_welcome': False, 'category': category,
        }
    )
