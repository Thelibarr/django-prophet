from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from .forms import PostForm
from .models import StockTicker


# Create your views here.
def index(request):
    list_of_numbers=list(range(30))

    return render(request, 'correlation/predict.html')


def post_form_upload(request):
    #return HttpResponse('<h1>Form Upload</h1>')

    if request.method == 'GET':
        form = PostForm()
    else:
        form = PostForm(request.POST)

        if form.is_valid():
            instance = StockTicker()
            instance.ticker = request.POST.get('ticker')
            instance.save()

            return post_result(request)

    context = {'form': form}

    return render(request, 'correlation/form_upload.html', context)


def post_result(request):

    ticker= request.POST.get('ticker')
    print(ticker)
    context = {
        'ticker': ticker
    }

    return render(request, 'correlation/post_result.html', context)
