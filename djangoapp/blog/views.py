from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from blog.models import Page, Post, Category, Tag
from django.contrib.auth.models import User
from django.db.models import Q
from django.views.generic import ListView


PER_PAGE = 6

class BaseListView(ListView):
    template_name = 'blog/pages/index.html'
    context_object_name = 'posts'
    paginate_by = PER_PAGE
    extra_context = {
        'is_welcome': True,
        'page_title': 'Home'
    }

    def get_queryset(self):
        return Post.objects.get_published_and_order_by()


def post(request, slug):
    post_obj = Post.objects.get_published_and_order_by().filter(slug=slug).first()

    if not post_obj:
        raise Http404("Post does not exist")

    return render(request, 'blog/pages/post.html', {'post': post_obj})


def custom_page(request, slug):
    page = get_object_or_404(Page, slug=slug, is_published=True)

    return render(request, 'blog/pages/custom_page.html', {'page': page})


class PostsByAuthorListView(BaseListView):
    def get_queryset(self):
        author_id = self.kwargs.get("author_id")
        self.author = get_object_or_404(User, pk=author_id)

        queryset = (
            super()
            .get_queryset()
            .filter(created_by__pk=author_id)
        )

        if not queryset.exists():
            raise Http404("No posts or author found.")

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        author = self.author
        full_name = author.get_full_name()
        page_title = f"Posts by {full_name}" if full_name else f"Posts by {author.username}"

        context.update({
            'is_welcome': False,
            'author': author,
            'page_title': page_title,
        })
        return context


class PostsByCategoryListView(BaseListView):
    def get_queryset(self):
        slug = self.kwargs.get("slug")
        self.category = get_object_or_404(Category, slug=slug)

        queryset = (
            super()
            .get_queryset()
            .filter(category__slug=slug)
        )

        if not queryset.exists():
            raise Http404("No posts found in this category.")

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context.update({
            'is_welcome': False,
            'category': self.category,
            'page_title': f'Category: {self.category.name}',
        })

        return context


class PostsByTagListView(BaseListView):
    def get_queryset(self):
        slug = self.kwargs.get("slug")
        self.tag = get_object_or_404(Tag, slug=slug)

        queryset = (
            super()
            .get_queryset()
            .filter(tags__slug=slug)
        )

        if not queryset.exists():
            raise Http404("No posts found in this tag.")

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context.update({
            'is_welcome': False,
            'tag': self.tag,
            'page_title': f'Tag: {self.tag.name}',
        })

        return context


class PostSearchListView(BaseListView):
    def dispatch(self, request, *args, **kwargs):
        self.q = request.GET.get("q", "").strip()

        if not self.q:
            return redirect('blog:index')

        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        queryset = (
            super()
            .get_queryset()
            .filter(
                Q(title__icontains=self.q) |
                Q(excerpt__icontains=self.q) |
                Q(content__icontains=self.q)
            )
        )
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'is_welcome': False,
            'search_term': self.q,
            'page_title': f'Search results for: {self.q}',
        })
        return context


# ================== Previous function-based views for reference =============

#def index(request):
#    posts = Post.objects.get_published_and_order_by()
#
#    paginator = Paginator(posts, PER_PAGE)
#    page_number = request.GET.get("page")
#    page_obj = paginator.get_page(page_number)
#
#    return render(
#        request,
#        'blog/pages/index.html',
#        {
#            'page_obj': page_obj, 'is_welcome': True, 'page_title': 'Home'
#        }
#)
#
#
#def posts_by_author(request, author_id):
#    author = get_object_or_404(User, pk=author_id)
#    posts = Post.objects.get_published_and_order_by().filter(created_by__pk=author_id)
#
#    if not posts.exists():
#        raise Http404("No posts or author found.")
#
#    paginator = Paginator(posts, PER_PAGE)
#    page_number = request.GET.get("page")
#    page_obj = paginator.get_page(page_number)
#
#    return render(
#        request,
#        'blog/pages/index.html',
#        {
#            'page_obj': page_obj, 'is_welcome': False, 'author': author, 'page_title': 'Posts by ' + author.get_full_name() or author.username,
#        }
#    )
#
#
#def posts_by_category(request, slug):
#    category = get_object_or_404(Category, slug=slug)
#    posts = Post.objects.get_published_and_order_by().filter(category__slug=slug)
#    
#    if not posts.exists():
#        raise Http404("No posts found in this category.")
#
#    paginator = Paginator(posts, PER_PAGE)
#    page_number = request.GET.get("page")
#    page_obj = paginator.get_page(page_number)
#
#    return render(
#        request,
#        'blog/pages/index.html',
#        {
#            'page_obj': page_obj, 'is_welcome': False, 'category': category, 'page_title': f'Category: {category.name}' 
#        }
#    )
#
#def posts_by_tag(request, slug):
#    tag = get_object_or_404(Tag, slug=slug)
#    posts = Post.objects.get_published_and_order_by().filter(tags__slug=slug)
#
#    if not posts.exists():
#        raise Http404("No posts found in this tag.")
#
#    paginator = Paginator(posts, PER_PAGE)
#    page_number = request.GET.get("page")
#    page_obj = paginator.get_page(page_number)
#
#    return render(
#        request,
#        'blog/pages/index.html',
#        {
#            'page_obj': page_obj, 'is_welcome': False, 'tag': tag, 'page_title': f'Tag: {tag.name}'
#        }
#    )
#
#
#def search(request):
#    q = request.GET.get("q", "").strip()
#
#    if not q:
#        return redirect('blog:index')
#
#    posts = Post.objects.get_published_and_order_by().filter(
#        Q(title__icontains=q) |
#        Q(excerpt__icontains=q) |
#        Q(content__icontains=q)
#    )
#
#    paginator = Paginator(posts, PER_PAGE)
#    page_number = request.GET.get("page")
#    page_obj = paginator.get_page(page_number)
#
#    return render(request, 'blog/pages/index.html', {'page_obj': page_obj, 'is_welcome': False, 'search_term': q, 'page_title': f'Search results for: {q}'})
#
