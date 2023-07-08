from django.shortcuts import render, redirect, HttpResponse
from home.models import Category, Product, Contact_us, Order, Brand, userProfile, profession, Details
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth.decorators import login_required
from cart.cart import Cart

# Create your views here.
def index(request):
    category = Category.objects.all()
    brand = Brand.objects.all()
    product_tshirts = Product.objects.filter(sub_category__name = "T-Shirts")
    product_shirts = Product.objects.filter(sub_category__name = "Shirts")
    product_trousers = Product.objects.filter(sub_category__name = "Trousers", price__lt=3300)
    product_kids = Product.objects.filter(sub_category__name = "PartyWear")
    recommended = Product.objects.filter(price__lte=1500)


    categoryID = request.GET.get('category')
    brandID = request.GET.get('brand')
    if categoryID:
        product = Product.objects.filter(sub_category = categoryID).order_by('-id')
    elif brandID:
        product = Product.objects.filter(brand = brandID).order_by('-id')
    else:
        product = Product.objects.all()

    
    
    context = {
        'category':category,
        'product':product,
        'brand':brand,
        'product_tshirts':product_tshirts,
        'product_shirts':product_shirts,
        'product_trousers':product_trousers,
        'product_kids':product_kids,
        'recommended':recommended
    }

    return render(request,'index.html',context)



def signup(request):
    if request.method == 'POST':
        uname = request.POST.get("username")
        email = request.POST.get("email")
        pass1 = request.POST.get("password1")
        pass2 = request.POST.get("password2")

        if pass1 != pass2:
            return HttpResponse("Password and confirm Passwords are not same")
        
        else:
            my_user = User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('loginPage')
        
        # image = 
        # profile = userProfile(user=my_user, image = )

    return render(request,'signup.html')

def loginPage(request):
    if request.method == 'POST':
        uname = request.POST.get("username")
        pass1 = request.POST.get("pass")

        user = authenticate(request,username=uname,password=pass1)
        if user is not None:
            # loging in the user
            login(request,user)
            return redirect('homepage')
        else:
            return HttpResponse("Either Username or Password is Invalid:")

    return render(request,'login.html')


def LogoutPage(request):
    logout(request)
    return redirect('index')

# @login_required(login_url='index')

def home(request):
    category = Category.objects.all()
    brand = Brand.objects.all()
    product_tshirts = Product.objects.filter(sub_category__name = "T-Shirts")
    product_shirts = Product.objects.filter(sub_category__name = "Shirts")
    product_trousers = Product.objects.filter(sub_category__name = "Trousers", price__lt=3300)
    product_kids = Product.objects.filter(sub_category__name = "PartyWear")
    recommended = Product.objects.filter(price__lte=1500)


    categoryID = request.GET.get('category')
    brandID = request.GET.get('brand')
    if categoryID:
        product = Product.objects.filter(sub_category = categoryID).order_by('-id')
    elif brandID:
        product = Product.objects.filter(brand = brandID).order_by('-id')
    else:
        product = Product.objects.all()

    
    
    context = {
        'category':category,
        'product':product,
        'brand':brand,
        'product_tshirts':product_tshirts,
        'product_shirts':product_shirts,
        'product_trousers':product_trousers,
        'product_kids':product_kids,
        'recommended':recommended
    }

    return render(request,'home.html',context)



def PasswordReset(request):
    return render(request,'Password_Reset_Form.html')


# For the Cart based Details:
@login_required(login_url="/accounts/login/")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("homepage")


@login_required(login_url="/accounts/login/")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required(login_url="/accounts/login/")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url="/accounts/login/")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required(login_url="/accounts/login/")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required(login_url="/accounts/login/")
def cart_detail(request):
    return render(request, 'cart/cart_detail.html')


def contactPage(request):
    if request.method == "POST":
        contact = Contact_us(
            name = request.POST.get('name'),
            email = request.POST.get('email'),
            subject = request.POST.get('subject'),
            message = request.POST.get('message')
        )
        contact.save()

    return render(request,'contact.html')

def CheckoutPage(request):
    if request.method == "POST":
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        pincode = request.POST.get('pincode')
        cart = request.session.get('cart')
        uid = request.session.get('_auth_user_id')
        user = User.objects.get(pk = uid)

        for i in cart:
            a = int(cart[i]['price'])
            b = cart[i]['quantity']
            total = a*b
            order = Order(
                user = user,
                product = cart[i]['name'],
                price = cart[i]['price'],
                quantity = cart[i]['quantity'],
                image = cart[i]['image'],
                address = address,
                pincode = pincode,
                phone = phone,
                total = total
            )

            order.save()
        return redirect('homepage')

    return HttpResponse("This is our checkout Page see this:")

def Your_Order(request):
    uid = request.session.get('_auth_user_id')
    user = User.objects.get(pk = uid)

    order = Order.objects.filter(user = user)

    context = {
        "order": order
    }
    return render(request, 'order.html', context)

def productpage(request):
    category = Category.objects.all()
    brand = Brand.objects.all()

    categoryID = request.GET.get('category')
    brandID = request.GET.get('brand')
    if categoryID:
        product = Product.objects.filter(sub_category = categoryID).order_by('-id')

    elif brandID:
        product = Product.objects.filter(brand = brandID).order_by('-id')

    else:
        product = Product.objects.all()
    
    context = {
        'category':category,
        'product':product,
        'brand':brand
    }

    return render(request, 'product.html', context)

def productDetail(request, id):
    category = Category.objects.all()
    brand = Brand.objects.all()
    product = Product.objects.filter(id = id).first()
    product_tshirts = Product.objects.filter(sub_category__name = "T-Shirts")
    product_shirts = Product.objects.filter(sub_category__name = "Shirts")
    product_trousers = Product.objects.filter(sub_category__name = "Trousers", price__lt=3300)
    product_kids = Product.objects.filter(sub_category__name = "PartyWear")
    recommended = Product.objects.filter(price__lte=1500)
    
    context = {
        'category':category,
        'product':product,
        'brand':brand,
        'product_tshirts':product_tshirts,
        'product_shirts':product_shirts,
        'product_trousers':product_trousers,
        'product_kids':product_kids,
        'recommended':recommended
    }
    return render(request, 'product_detail.html',context)

def accountDetail(request):
    # Passing the user information to the Page:
    uid = request.session.get('_auth_user_id')
    user = User.objects.get(pk = uid)

    profile = Details.objects.filter(user = user)

    context ={
        'user':user,
        'profile':profile
    }
    
    return render(request, 'Account.html', context)


def searchproduct(request):
    query = request.GET['query']
    product = Product.objects.filter(name__icontains = query)

    context = {
        'product':product
    }
    return render(request, 'search.html', context)

def stripePayment(request):
    return render(request, 'payment.html')


# def get_context_data(sel, **kwargs):
#     context = super().get_context_data(**kwargs)
#     context['key'] = settings.STRIPE_PUBLISHABLE_KEY
#     return context