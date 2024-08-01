from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from cart.forms import AddProductForm
from main.form import AddCar, RegistrationForm, LoginForm, NewLoginForm, NewPasswordForm
from main.models import Car, Brand,Manufacture
from orders.models import Order, OrderItem


# Create your views here.



def get_page_1(request):
    cars = Car.objects.select_related('brand').all()
    # brand = Brand.objects.all()
    # manufacturer = Manufacture.objects.all()
    context = {
        'cars':cars,
        # 'brand':brand,
        # 'manufacturer':manufacturer,
    }

    return render(request,'page_1.html',context)



def get_brand(request):
    brand_car = Car.objects.filter(brand=request.GET.get('brand'))
    # brand = Brand.objects.all()
    # manufacturer = Manufacture.objects.all()
    manuf_car = Car.objects.filter( manufacturer__in = request.GET.getlist('manufacturer'))
    context = {
            'cars': brand_car if brand_car else manuf_car,
            # 'brand': brand,
            # 'manufacturer': manufacturer,
        }
    # if request.GET.get('manufacturer'):
    #     context = {
    #         'cars':brand_car,
    #         'brand': brand,
    #         'manufacturer':manufacturer,
    #     }
    # if request.GET.get('manufacturer'):
    #     context = {
    #         'cars': manuf_car,
    #         'brand': brand,
    #         'manufacturer': manufacturer,
    #     }
    # print(request.GET)
    return render(request,'brand.html', context)


def page_add_car(request):
    forms = AddCar()
    car_all = Car.objects.all()

    if request.method == 'POST':
        forms = AddCar(request.POST,request.FILES)
        if forms.is_valid():
            # new_car = Car(brand=forms.cleaned_data['brand'], model=forms.cleaned_data['model'],
            #               price=forms.cleaned_data['price'], description=forms.cleaned_data['description'],
            #               image=forms.cleaned_data['image'])
            # new_car.save()
            # new_car.manufacturer.set(forms.cleaned_data['manufacturer'])
            # print(forms.cleaned_data)
            forms.save()
            return redirect('home')
    context ={
        'forms':forms,
        'car_all':car_all,
    }
    return render(request,'add_car.html',context)

def detail_info(request,id):
    car = Car.objects.get(id=id)
    form = AddProductForm()
    context={
            'car':car,
            'form':form,
    }
    return render(request,'detail.html',context)

def get_search(request):
    results = Car.objects.filter(brand__title__icontains=request.GET.get('search')) | Car.objects.filter(description__icontains=request.GET.get('search'))
    context={
        'cars':results,
    }
    return render(request,'search.html',context)


def get_registration(request):
    form = RegistrationForm()

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # if request.POST.get('password') == request.POST.get('password2'):
            #     form.save()
            #     # print('Bob')
            #     # print(form.cleaned_data)
            #     # return redirect('home')
            # else:
            #     context['error'] = 'Пароли не совподают'
            # form.save()

            # 1 sposob
            # User.objects.create_user(username=form.cleaned_data.get('username'),
            #                          password=form.cleaned_data.get('password'))

            # 2 sposob
            user = form.save(commit=False)
            user.set_password(form.cleaned_data.get('password'))
            user.save()
            return redirect('home')
    context = {
        'form': form,
    }
    return render(request, 'registration.html', context)


def autoriz(request):
    form = LoginForm()
    context = {
        'form': form,
    }
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(request,**form.cleaned_data)
            if user:
                login(request, user)
                return redirect('home')
            else:
                error_massage = 'Пользователь не найден'
                context = {
                    'form': form,
                    'error_massage':error_massage,
                }
    return render(request, 'autoriz.html', context)

def logaut_user(request):
    logout(request)
    return redirect('home')


@login_required
def kabinet(request):
    new_log = NewLoginForm(initial=  {'username': request.user.username})

    pass_form = NewPasswordForm()
    context={
        'log_form':new_log,
        'pass_form':pass_form,
        }
    if request.method == 'POST':
        new_log = NewLoginForm(request.POST)
        pass_form = NewPasswordForm(request.POST)
        if request.POST.get('username'):
            if new_log.is_valid():
                user_log = request.user
                user_log.username = new_log.cleaned_data.get('username')
                user_log.save()
                context = {
                    'log_form': new_log,
                    'pass_form': pass_form,
                    'new_username':user_log,
                }
        if request.POST.get('password'):
            if pass_form.is_valid():
                user_pass = request.user
                user_pass.set_password(pass_form.cleaned_data.get('password'))
                user_pass.save()
                context = {
                    'log_form': new_log,
                    'pass_form': pass_form,
                    'new_pass':user_pass,
                }

    return render(request,'kabinet.html',context)


def my_orders(request):
    orders = Order.objects.filter(user_id=request.user.id)

    context = {
        'orders': orders,
    }
    return render(request,'kabinet.html',context)