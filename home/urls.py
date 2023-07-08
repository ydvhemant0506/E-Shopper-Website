from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from home import views


urlpatterns = [
    path('', views.index ,name='index'),
    path('signup', views.signup ,name='signup'),
    path('login', views.loginPage ,name='loginPage'),
    path('LogoutPage', views.LogoutPage ,name='LogutPage'),
    path('homepage', views.home ,name='homepage'),
    path('reset_password', views.PasswordReset ,name='PasswordReset'),
    path('contactpage',views.contactPage, name = 'contact'),
    path('account',views.accountDetail, name='account'),
    path('search/',views.searchproduct, name='search'),
    path('payment/',views.stripePayment, name='payment'),

    # For the password Reset functionality:
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="accounts/password_reset.html"),name='reset_password'),

    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="accounts/password_reset_sent.html"), name='password_reset_done'),

    path('reset/<uid64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset_form.html"), name='password_reset_confirm'),

    path('reset_password_complete/', auth_views.PasswordResetView.as_view(template_name="accounts/password_reset_done.html"), name='password_reset_complete'),

    # From the django-Shopping-Cart feture:
    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart-detail/',views.cart_detail,name='cart_detail'),

    #Checkout Page:
    path('checkout/',views.CheckoutPage, name='checkout'),
    path('order/',views.Your_Order, name='order'),
    path('product/',views.productpage, name='product'),
    path('product/<str:id>',views.productDetail, name='productDetail'),
    

]   