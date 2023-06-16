from django.shortcuts import render,redirect
from redditApp.models import categorydb,productdb
from webapp.models import signupdb,contactdb,cartdb,checkoutdb
from django.contrib import messages


# Create your views here.
def homefn(request):
    data = categorydb.objects.all()
    return render(request,"home.html", {'data':data})
def aboutusfn(request):
    return render(request,"aboutus.html")
def shopfn(request):
    return render(request,"shop.html")
def productfn(request,cat_name):
    data = categorydb.objects.all()
    pro =productdb.objects.filter(Category=cat_name)
    return render(request,"product.html",{'data':data,'pro':pro})
def singleprodetail(request,dataid):
    pro = productdb.objects.get(id=dataid)
    return render(request,"singleprodd.html",{'pro':pro})
def usersinup(request):
    return render(request,"userlogin.html")
def user_signupfn(request):
    if request.method=="POST":
        una = request.POST.get('usrname')
        email = request.POST.get('email')
        phnum = request.POST.get('number')
        pword = request.POST.get('password')
        image = request.FILES['image']
        obj=signupdb(User_Name=una,Email=email,Phone_number=phnum,Password=pword,User_Image=image)
        obj.save()
        messages.success(request, "Registration  Successfull")
        return redirect(usersinup)
def userloginfn(request):
    if request.method=="POST":
        uname=request.POST.get('usrname')
        pwd=request.POST.get('password')
        if signupdb.objects.filter(User_Name=uname,Password=pwd).exists():
            request.session['User_Name']=uname
            request.session['Password']=pwd
            messages.success(request, "Login Successfull")
            return redirect(homefn)
        else:
            messages.error(request, "Password or username does not match")
            return redirect(usersinup)
    else:
        messages.error(request, "Password or username does not match")
        return redirect(usersinup)
def userlogoutfn(request):
    del request.session['User_Name']
    del request.session['Password']
    return redirect(usersinup)
def conaactdisplay(requst):
    return render(requst,"contact.html")
def contactfn(request):
    if request.method=="POST":
        una = request.POST.get('name')
        num = request.POST.get('number')
        email = request.POST.get('email')
        sub = request.POST.get('subject')
        mess = request.POST.get('message')
        obj=contactdb(Name=una,Number=num,Email=email,Subject=sub,Message=mess)
        obj.save()
        return redirect(conaactdisplay)
def cartfn(request):
    data=cartdb.objects.filter(User_name=request.session['User_Name'])
    return render(request,"cart.html",{'data':data})
def cart_save(request):
    if request.method=="POST":
        una = request.POST.get('username')
        proname = request.POST.get('proname')
        price = request.POST.get('price')
        decs = request.POST.get('description')
        qty = request.POST.get('quty')
        obj = cartdb(User_name=una,Product_name=proname,Price=price,Description=decs,Quantity=qty)
        obj.save()
        messages.success(request, "Added to cart")
        return redirect(cartfn)
def deletecart(request,dataid):
    data=contactdb.objects.filter(id=dataid)
    data.delete()
    return redirect(cartfn)
def checkoutfn(request):
    return render(request,"checkoutpg.html")
def checkoutsave(request):
    if request.method=="POST":
        fna = request.POST.get('firstname')
        lna = request.POST.get('lastname')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        ad1 = request.POST.get('addressone')
        ad2 = request.POST.get('addresstwo')
        ctry = request.POST.get('country')
        cty = request.POST.get('city')
        st = request.POST.get('state')
        zip = request.POST.get('zipcode')
        obj = checkoutdb(Fist_Name=fna,Last_Name=lna,Email=email,Mobile=mobile,AdressoOne=ad1,AddressTwo=ad2,Country=ctry,City=cty,State=st,Zipcode=zip)
        obj.save()
        messages.success(request, "Order placed successfully")
        return redirect(homefn)
