from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView, UpdateView, DeleteView

from django.core.paginator import Paginator


def news_home(request):
    news = Articles.objects.order_by("-date")
    return render(request, 'news/news_home.html', {'news': news})


class NewsDetailView(DetailView):
    model = Articles
    template_name = 'news/details_view.html'
    context_object_name = 'article'



class NewsUpdate(UpdateView):
    model = Articles
    template_name = 'news/create.html'
    form_class = ArticlesForm


class NewsDelete(DeleteView):
    model = Articles
    success_url = '/news/'
    template_name = 'news/news-delete.html'


def news_home(request):
    news = Articles.objects.order_by("-date")

    paginator = Paginator(news, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'news/news_home.html', {'page_obj': page_obj})


def create(request):
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("news_home")
    form = ArticlesForm()
    data = {
        'form': form,
    }
    return render(request, 'news/create.html', data)
