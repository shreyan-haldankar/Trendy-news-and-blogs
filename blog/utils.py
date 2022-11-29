from django.db.models import Q
from .models import Post
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage



def paginateBlogs(request,blogs, results):
    page = request.GET.get('page')
    paginator = Paginator(blogs,results)
    try:
        blogs = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        blogs = paginator.page(page)

    except EmptyPage:
        page = paginator.num_pages
        blogs = paginator.page(page)


    # Pages on left side
    leftIndex = (int(page) - 4)
    if leftIndex < 1:
        leftIndex = 1
    
    rightIndex = (int(page) + 5)
    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1

    custom_range = range(leftIndex, rightIndex)
    return custom_range, blogs




def searchBlogs(request):
    search_query = ""

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')


    blogs = Post.objects.distinct().filter(
        Q(title__icontains=search_query) |
        Q(content__icontains=search_query) |
        Q(author__name__icontains=search_query)
    )

    return blogs, search_query