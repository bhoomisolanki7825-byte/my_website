from django.shortcuts import render
def home_page(request):
    return render(request,'index.html')
def about_page(request):
    return render(request,'about.html')
def products(request):
    return render(request,'products.html')
def contact(request):
    return render(request,'contacts.html')