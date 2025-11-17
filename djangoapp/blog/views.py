from django.shortcuts import render
from django.core.paginator import Paginator
from blog.models import Post


def index(request):
    posts = Post.objects.all().order_by('created_at').filter(is_published=True)

    paginator = Paginator(posts, 6)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        'blog/pages/index.html',
        {
            'page_obj': page_obj
        }
    )


def post(request, slug):
    return render(request, 'blog/pages/post.html')



def custom_page(request):
    return render(request, 'blog/pages/custom_page.html')
