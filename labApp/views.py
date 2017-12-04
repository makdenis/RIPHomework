from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import View
from django.views.generic import ListView
from .models import *
from django import forms
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def home(request):
    par = {
        'header': '"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."'
    }
    return render(request, 'home.html', context=par)


class CustomerView(ListView):
    model = Customer
    template_name = 'customer_list.html'


# class ProdactsView(ListView):
#     model = zakaz
#     template_name = 'zakazs.html'
#     context_object_name = 'zakaz_list'
#
#
# class OrderView(ListView):
#     model = Usluga
#     template_name = 'order_list.html'


# представления для веб-форм


def registration_form(request):
    errors = {}
    request.encoding = 'utf-8'
    if request.method == 'POST':
        username = request.POST.get('username')
        if not username:
            errors['uname']='Введите логин'
        elif len(username) < 5:
            errors['uname']='Длина логина должна быть более 5 символов'

        if User.objects.filter(username=username).exists():
            errors['uname']='Такой логин уже занят'

        password = request.POST.get('password')
        if not username:
            errors['psw']='Введите пароль'
        elif len(password) < 6:
            errors['psw']='Длина пароля должна быть более 6 символов'
        password2 = request.POST.get('password2')

        if password != password2:
            errors['psw2']='Пароли не совпадают'

        email = request.POST.get('email')
        if not email:
            errors['email'] = 'Введите email'

        last_name = request.POST.get('last_name')
        if not last_name:
            errors['lname'] = 'Введите фамилию'

        first_name = request.POST.get('first_name')
        if not first_name:
            errors['fname'] = 'Введите имя'

        print(username, password,"1")


        if not errors:

            user = User.objects.create_user(username, email, password)
            print(user)
            cust = Customer()
            cust.user = user
            #cust.customer_name = username
            cust.email = email
            cust.last_name = last_name
            cust.first_name = first_name

            cust.save()
            return HttpResponseRedirect('/authorization')
        else:
            context = {'errors': errors, 'username': username, 'email': email, 'last_name': last_name,
                   'first_name': first_name}
            return render(request, 'registration_form.html', context)

    return render(request, 'registration_form.html', {'errors': errors })


# форма регистрации
class RegistrationForm(forms.Form):
    username = forms.CharField(min_length=5,label='Логин')
    password = forms.CharField(min_length=8,widget=forms.PasswordInput, label='Пароль')
    password2 = forms.CharField(min_length=8, widget=forms.PasswordInput, label='Повторите ввод')
    email = forms.EmailField(label='Email')
    last_name = forms.CharField(label='Фамилия')
    first_name = forms.CharField(label='Имя')


class AuthorizationForm(forms.Form):
    username = forms.CharField(label='Логин')
    password = forms.CharField(widget=forms.PasswordInput, label='Пароль')


# регистрация
def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        is_val = form.is_valid()
        data = form.cleaned_data
        if data['password']!=data['password2']:
            is_val = False
            form.add_error('password2', ['Пароли должны совпадать'])
        if User.objects.filter(username=data['username']).exists():
            form.add_error('username', ['Такой логин уже занят'])
            is_val = False

        if is_val:
            data = form.cleaned_data
            user = User.objects.create_user(data['username'], data['email'], data['password'])
            print(user)
            cust = Customer()
            cust.user = user
            cust.first_name = data['first_name']
            cust.last_name = data['last_name']

            cust.save()
            return HttpResponseRedirect('/authorization')
    else:
        form = RegistrationForm()

    return render(request, 'registration.html', {'form': form})


# авторизация вручную
def authorization_form(request):
    errors = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        if not username:
            errors['uname']='Введите логин'
        elif len(username) < 5:
            errors['uname']='Длина логина должна быть не меньше 5 символов'

        password = request.POST.get('password')
        if not password:
            errors['psw']='Введите пароль'
        elif len(password) < 8:
            errors['psw']='Длина пароля должна быть не меньше 8 символов'

        user = authenticate(request, username=username, password=password)
        #user = authenticate(request, username='petrov',password='12345678')
        print(user)
        if user is None and 'uname' not in errors.keys() and 'psw' not in errors.keys():
            errors['login'] = 'Логин или пароль введены неверно'

        if not errors:
            login(request, user)
            return HttpResponseRedirect('/success_authorization_form')
            #return HttpResponseRedirect('/success_authorization')
        else:
            context = {'errors': errors}
            return render(request, 'authorization_form.html', context)

    return render(request, 'authorization_form.html', {'errors':errors})


# авторизация django
def authorization(request):
    if request.method == 'POST':
        form = AuthorizationForm(request.POST)
        print(form)
        data = form.cleaned_data

        if form.is_valid():
            user = authenticate(request, username=data['username'], password=data['password'])
            # user = authenticate(request, username='petrov',password='12345678')
            print(len(data['username']),len(data['password']))
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/success_authorization')
            else:
                form.add_error('username', ['Неверный логин или пароль'])
            #raise forms.ValidationError('Имя пользователя и пароль не подходят')

    else:
        form = AuthorizationForm()

    return render(request, 'authorization.html', {'form': form})


# успешная авторизация вручную
def success_authorization_form(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/authorization')


# успешная авторизация django
@login_required(login_url='/authorization')
def success_authorization(request):
    return HttpResponseRedirect('/')
class OrdersView(View):
    def get(self, request):
        empty_orders = []
        computers_in_order = BelongTO.objects.all()  # код заказа - компы
        prices = {}  # цены
        data = Order.objects.filter(
            customer_id=request.user.id).all()  # заказы пользователя
        for o in data:
            computers = BelongTO.objects.filter(
                order_id=o.code).all()  # компьютеры заказа
            if len(computers) == 0:
                empty_orders.append(o.code)
            total = 0
            for c in computers:
                cur_comp = Computer.objects.get(name=c.item_id)
                if c.item_id not in prices.keys():
                    prices[c.item_id] = cur_comp.price
                total = total + cur_comp.price*c.quantity
            o.total = total
            o.save()

        return render(request, 'orders.html',
                      context={"data": data,
                               "computers": computers_in_order,
                               "prices": prices,
                               'empty_orders': empty_orders})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')



# class ZakazView(ListView):
#     model = zakaz
#     template_name = 'zakazs.html'
#     context_object_name = 'zakaz_list'