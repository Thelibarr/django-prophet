
from django.shortcuts import render, get_object_or_404, redirect
from .forms import PostForm
from .models import StockTicker
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .forms import UserForm

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


class UserFormView(View):
    form_class = UserForm
    template_name = 'correlation/registration_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    #proccess form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            #clean normalized data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            # return User objects if credentials are correct

            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    print('user is logged in')
                    return redirect('correlation:index')

        return render(request, self.template_name, {'form': form})
