from django.urls import path
from webapp import views
urlpatterns=[
    path('homefn/',views.homefn,name="homefn"),
    path('aboutusfn/',views.aboutusfn,name="aboutusfn"),
    path('shopfn/',views.shopfn,name="shopfn"),
    path('usersinup/',views.usersinup,name="usersinup"),
    path('user_signupfn/',views.user_signupfn,name="user_signupfn"),
    path('productfn/<cat_name>',views.productfn,name="productfn"),
    path('singleprodetail/<int:dataid>/',views.singleprodetail,name="singleprodetail"),
    path('userloginfn/',views.userloginfn,name="userloginfn"),
    path('userlogoutfn/',views.userlogoutfn,name="userlogoutfn"),
    path('conaactdisplay/',views.conaactdisplay,name="conaactdisplay"),
    path('contactfn/',views.contactfn,name="contactfn"),
    path('cartfn/',views.cartfn,name="cartfn"),
    path('cart_save/',views.cart_save,name="cart_save"),
    path('deletecart/<dataid>/',views.deletecart,name="deletecart"),
    path('checkoutfn/',views.checkoutfn,name="checkoutfn"),
    path('checkoutsave/',views.checkoutsave,name="checkoutsave"),
]