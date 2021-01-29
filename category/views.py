from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from django.http import HttpResponse

def loadCategory(request):
    return render(request, 'category.html')

def addCategory(request):
    if request.method == 'POST':
        name = request.POST['name']
        print(name)
        if Category(name=name):
            return HttpResponse("Category Added")
        else:
            return HttpResponse("Category Not Added")


def showCategory(request):
    category = Category.objects.all
    return render(request, 'showcate.html',{'category':category})

def subCategory(request):
    category = Category.objects.all
    if request.method == 'POST':
        name = request.POST['name']
        cate_id = request.POST['cate_id']

        if SubCategory.objects.filter(name=name).exists():
            messages.error(request, "SubCategory already exist")

        else:
            query = SubCategory(name=name)
            query.cat_id_id = cate_id
            query.save()
            #return HttpResponse("SubCategory Added")
            return redirect('subcategory')
    return render(request,'subcate.html',{'category':category})

def showSub(request):
    subcate = SubCategory.objects.all
    return render(request, 'showsub.html',{'subcate':subcate})

def editSubcategory(request,id):
    category = Category.objects.all
    subcate = SubCategory.objects.get(id=id)
    return render(request, 'subedit.html',{'subcate': subcate,'category':category})

def updateSubcategory(request,id):
    if request.method == 'POST':
        name = request.POST['name']
        cate_id = request.POST['cate_id']

        if SubCategory.objects.filter(name=name).exists():
            messages.error(request, "SubCategory already exist")
            return redirect('showsub')

        else:
            SubCategory.objects.filter(id=id).update(name=name,cat_id=cate_id)
            #return HttpResponse("SubCategory Added")
            return redirect('showsub')

def deleteSubcategory(request,id):
    subcate = SubCategory.objects.get(id=id)
    subcate.delete()
    return redirect('showsub')

def product(request):
    cat = Category.objects.all
    sub = SubCategory.objects.all
    if request.method == 'POST':
        name = request.POST['name']
        price = request.POST['price']
        date = request.POST['date']
        stock = request.POST['stock']
        size = request.POST.getlist('size[]')
        size_split = ",".join(size)
        cate_id = request.POST['cate_id']
        sub_id = request.POST['sub_id']

        if Product.objects.filter(name=name).exists():
            messages.error(request, "Product already exist")

        else:
            query = Product(name=name,price=price,date=date,stock=stock,size=size_split)
            query.cat_id_id = cate_id
            query.sub_id_id = sub_id
            query.save()
            return HttpResponse("Product Added")
            #return redirect('subcategory')


    return render(request,'product.html',{'cat':cat,'sub':sub})

def showProduct(request):
    product = Product.objects.all
    return render(request, 'showproduct.html',{'product':product})

def editProduct(request,id):
    product = Product.objects.get(id=id)
    size = product.size
    size_list = size.split(",")
    print(size_list)
    cat = Category.objects.all
    sub = SubCategory.objects.all
    return render(request, 'editproduct.html', {'product': product,'cat':cat,'sub':sub,'size_list':size_list})

def updateProduct(request,id):
    if request.method == 'POST':
        name = request.POST['name']
        price = request.POST['price']
        date = request.POST['date']
        stock = request.POST['stock']
        size = request.POST.getlist('size[]')
        size_split = ",".join(size)
        cate_id = request.POST['cate_id']
        sub_id = request.POST['sub_id']

        if Product.objects.filter(name=name).exists():
            messages.error(request, "Product already exist")

        else:
            Product.objects.filter(id=id).update(name=name,price=price,date=date,stock=stock,size=size_split,cat_id=cate_id,sub_id=sub_id)
            # return HttpResponse("SubCategory Added")
            return redirect('showProduct')
