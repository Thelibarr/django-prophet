from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from .forms import PostForm

# Create your views here.
def index(request):
    list_of_numbers=list(range(30))

    return render(request, 'correlation/predict.html')


def post_form_upload(request):
    #return HttpResponse('<h1>Form Upload</h1>')

    if request.method == 'GET':
        form = PostForm()
    else:
        #It must be a POST request

        form = PostForm(request.POST)

        if form.is_valid():
            content = form.cleaned_data['content']
            name= form.cleaned_data['name']
            created_at = form.cleaned_data['created_at']
            post = m.Post.objects.create(content=content,
                                         created_at=created_at)
            return HttpResponseRedirect(reverse('post_detail',
                                                kwargs={'post_id': post.id}))
    return render(request, 'correlation/form_upload.html', {
                  'form': form,
    })

