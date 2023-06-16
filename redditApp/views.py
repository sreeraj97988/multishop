from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render,redirect
from django.utils.datastructures import MultiValueDictKeyError
from webapp.models import contactdb
from django.contrib import messages
from redditApp.models import categorydb,productdb

# Create your views here.
def indexfn(request):
    return render(request,"index.html")
def addCategoryfn(request):
    return render(request,"addCategory.html")
def categorysavefunction(request):
    if request.method=="POST":
        cna=request.POST.get('catname')
        image = request.FILES['image']
        description=request.POST.get('descriptionn')
        obj=categorydb(category=cna,descriptions=description,category_img=image)
        obj.save()
        messages.success(request,"saved succesful")
        return redirect(addCategoryfn)

def displaycatfn(request):
    data = categorydb.objects.all()
    return render(request,"displaycaat.html",{'data':data})
def editpage(req,dataid):
     data = categorydb.objects.get(id=dataid)
     return render(req,"editcat.html",{'data':data})
def update_category(request,dataid):
    if request.method == "POST":
        cna = request.POST.get('catname')
        description = request.POST.get('descriptionn')
        try:
            image1 = request.FILES['image']
            fs=FileSystemStorage()
            file=fs.save(image1.name, image1)
        except MultiValueDictKeyError:
            file=categorydb.objects.get(id=dataid).category_img
        categorydb.objects.filter(id=dataid).update(category=cna,descriptions=description,category_img=file)
        return redirect(displaycatfn)
def catdeletefn(request,dataid):
    data = categorydb.objects.filter(id=dataid)
    data.delete()
    return redirect(displaycatfn)
def addprodfn(request):
    data=categorydb.objects.all()
    return render(request,"addproduct.html",{'data':data})

def productsavefunction(request):
    if request.method=="POST":
        cna = request.POST.get('catname')
        pname = request.POST.get('prodname')
        price = request.POST.get('price')
        prodesc = request.POST.get('prodescriptionn')
        brand = request.POST.get('Brand')
        image = request.FILES['image']
        obj=productdb(Category=cna,Product_name=pname,Price=price,Description=prodesc,Brand=brand,product_img=image)
        obj.save()
        return redirect(addprodfn)
def displayprod(request):
    data = productdb.objects.all()
    return render(request,"displayprod.html",{'data':data})
def updateprod(request,dataid):
    if request.method == "POST":
        cna = request.POST.get('catname')
        pname = request.POST.get('prodname')
        price = request.POST.get('price')
        prodesc = request.POST.get('prodescriptionn')
        brand = request.POST.get('Brand')
        try:
            image1 = request.FILES['image']
            fs=FileSystemStorage()
            file=fs.save(image1.name, image1)
        except MultiValueDictKeyError:
            file=productdb.objects.get(id=dataid).product_img
        productdb.objects.filter(id=dataid).update(Category=cna,Product_name=pname,Price=price,Description=prodesc,Brand=brand,product_img=file)
        return redirect(displayprod)

def prodeletefn(request,dataid):
    data = productdb.objects.filter(id=dataid)
    data.delete()
    return redirect(displayprod)

def editpro(request,dataid):
    data = productdb.objects.get(id=dataid)
    cat = categorydb.objects.all()
    return render(request,"editproduct.html",{'data':data, 'cat':cat})
def loginpage(request):
    return render(request,"logn.html")

def loginfn(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        if User.objects.filter(username__contains=username).exists():
            user=authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                messages.success(request,"Login Successfull")
                return redirect(indexfn)
            else:
                messages.error(request, "Password or username does not match")
                return redirect(loginpage)
        else:
            messages.error(request,"Password or username does not match")
            return redirect(loginpage)
def admin_logout(request):
    return redirect(loginpage)

def displaycontact(request):
    data = contactdb.objects.all()
    return render(request,"displayContact.html",{'data':data})

def deletecontact(request,dataid):
    data=contactdb.objects.filter(id=dataid)
    data.delete()
    return redirect(displaycontact)