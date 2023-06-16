from django.urls import path
from redditApp import views

urlpatterns=[

path('indexfn/',views.indexfn,name="indexfn"),
path('addCategoryfn/',views.addCategoryfn,name="addCategoryfn"),
path('loginpage/',views.loginpage,name="loginpage"),
path('categorysavefunction/',views.categorysavefunction,name="categorysavefunction"),
path('displaycatfn/',views.displaycatfn,name="displaycatfn"),
path('displayprod/',views.displayprod,name="displayprod"),
path('catdeletefn/<int:dataid>/',views.catdeletefn,name="catdeletefn"),
path('prodeletefn/<int:dataid>/',views.prodeletefn,name="prodeletefn"),
path('update_category/<int:dataid>/',views.update_category,name="update_category"),
path('updateprod/<int:dataid>/',views.updateprod,name="updateprod"),
path('editpage/<int:dataid>/',views.editpage,name="editpage"),
path('editpro/<int:dataid>/',views.editpro,name="editpro"),
path('addprodfn/',views.addprodfn,name="addprodfn"),
path('productsavefunction/',views.productsavefunction,name="productsavefunction"),
path('loginfn/',views.loginfn,name="loginfn"),
path('admin_logout/',views.admin_logout,name="admin_logout"),
path('displaycontact/',views.displaycontact,name="displaycontact"),
path('deletecontact/<int:dataid>/',views.deletecontact,name="deletecontact"),




]