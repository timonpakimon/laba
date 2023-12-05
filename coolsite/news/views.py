from django.shortcuts import render, redirect
from .models import Artiles, Category, Author, Tag
from .forms import ArtilesForm
from django.views.generic import DetailView, UpdateView, DeleteView


# Create your views here

def tegs(request):
    tags = Tag.objects.all()
    return render(request, 'news/tegs.html', {'tags': tags})


def authors(request):
    authors_list = Author.objects.all()
    return render(request, 'news/author.html', {'authors': authors_list})


def categories(request):
    category = Category.objects.all()
    return render(request, 'news/category.html', {'categories': category})


def news_home(request):
    news = Artiles.objects.order_by('-data')
    return render(request, 'news/new_home.html', {'news': news})


class NewsDetailView(DetailView):
    model = Artiles
    template_name = 'news/details_view.html'
    context_object_name = 'artiles'


class NewsUpdateView(UpdateView):
    model = Artiles
    template_name = 'news/create.html'
    form_class = ArtilesForm


class NewsDeleteView(DeleteView):
    model = Artiles
    success_url = '/news/'
    template_name = 'news/delete.html'


def create(request):
    error = ''
    if request.method == 'POST':
        form = ArtilesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error: 'Форма не вірна'

    form = ArtilesForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'news/create.html', data)
