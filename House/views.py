from django.shortcuts import render

# Create your views here.
def Show_IndexPage(request):
    context = {}
    return render(request,"index.html",context)