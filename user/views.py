from django.shortcuts import render, HttpResponseRedirect, reverse, redirect
from django.urls import reverse_lazy
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required
# Create your views here.
from user.forms import LoginForm


def login_executed(redirect_to):
    """This Decorator kicks authenticated user out of a view"""

    def _method_wrapper(view_method):
        def _arguments_wrapper(request, *args, **kwargs):
            if request.user.is_authenticated:
                return redirect(redirect_to)
            return view_method(request, *args, **kwargs)

        return _arguments_wrapper

    return _method_wrapper

@login_required
def logoutView(request):
    logout(request)
    return HttpResponseRedirect(reverse_lazy('ecommerce:index'))


@login_executed('ecommerce:index')
def loginView(request):
    form = LoginForm()
    next_page = request.GET.get('next')
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        username, password = request.POST.get('username'), request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                if next_page:
                    return redirect(next_page)
                if user.user_type == 'seller':
                    return HttpResponseRedirect(reverse('product:inventory'))
                return HttpResponseRedirect(reverse('ecommerce:index'))

    context = {
        'form': form,
    }

    return render(request, 'login.html', context)

