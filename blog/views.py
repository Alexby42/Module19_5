from django.db.models.sql.datastructures import Empty
from django.shortcuts import render
from django.template.defaultfilters import title
from .models import Posts
from django.core.paginator import Paginator


# Create your views here.
def index(request):
    SELECT_CHOICE = ['3', '5', '10']
    title_ = 'Главная'
    posts = Posts.objects.all()

    if request.GET.get('page_') is None:
        page_ = 3
    else:
        page_ = request.GET.get('page_')

    if request.method == 'POST':
        select = request.POST.get('select')
        if select is None:
            page_ = 3
        else:
            page_ = select


    paginator = Paginator(posts, page_)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'title': title_,
        'page_obj': page_obj,
        'select_choice': SELECT_CHOICE,
        'page_': page_,
    }
    return render(request, 'index.html', context=context)
