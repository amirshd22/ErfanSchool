from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator , EmptyPage , PageNotAnInteger, InvalidPage
from .models import Blog

# Create your views here.

def homePage(request):
    templates = 'home.html'
    context = {}
    return render(request , templates , context )



def BlogPage(request):
    BLogsQs = Blog.objects.all().order_by('-date')
    paginator = Paginator(BLogsQs, 12)
    try:
        page = int(request.GET.get('page', '1'))
    except :
        page= 1

    try:
        items=paginator.get_page(page)
    except(EmptyPage, InvalidPage):
        items= paginator.page(paginator.num_pages)
    templates = 'Blog.html'
    context = {
        'key': BLogsQs,
        "items" : items
    }
    return render(request, templates , context)



def blogDetails(request, blog_id):
    blogQs = get_object_or_404(Blog,pk=blog_id)
    templates = 'details.html'
    context ={
        'key':blogQs
    }
    return render(request, templates, context)