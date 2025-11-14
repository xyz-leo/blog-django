from django.shortcuts import render
from django.core.paginator import Paginator


# Hardcoded to test the paginator
posts = list(range(500))

def index(request):
    paginator = Paginator(posts, 9)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        'blog/pages/index.html',
        {
            'page_obj': page_obj
        }
    )


def post(request):
    return render(request, 'blog/pages/post.html')


# to implement later
#def index(request):
#    posts_list = Post.objects.all().order_by('-created_at')
#
#    paginator = Paginator(posts_list, 6)  # 6 posts per page
#    page_number = request.GET.get('page')
#    page_obj = paginator.get_page(page_number)  # safe
#
#    return render(request, 'blog/pages/index.html', {
#        'page_obj': page_obj,
#    })
