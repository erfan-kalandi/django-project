from django.shortcuts import get_object_or_404,render,redirect
from django.template import loader
from .models import *
from django.http import HttpResponse

from  .forms import *

from django.template.context_processors import csrf

def post(request):
    return render(request, 'poem/post.html', {})


def poemlist(request, id):

    poemi = poem.objects.filter(poet_id=id)
    return render(request, 'poem/poemlist.html', {"poem": poemi})



def poetlist(request):
    poeti = poet.objects.all()
    poetdic = {
        'poet': poeti
    }
    return render(request, 'poem/poetlist.html', poetdic)


def create(request):
    if request.POST:
        form = poemform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request,'poem/finishadding.html')
    else:
        form = poemform()
        args = {}
        args.update(csrf(request))
        args['poet'] = poet.objects.all()
        args['form'] = form
        return render(request, 'poem/create.html',args)



def searchword(request):
    if request.method == "GET":
        return render(request, 'poem/search.html', {})

    elif request.method == "POST":
        data = request.POST['search2']
        if data != "":
            x = poem.objects.filter(text__contains=data)
            if len(x) == 0:
                return render(request, 'poem/noresualt.html')
            else:
                res = {"resualt": x}
                return render(request, 'poem/searchresualt.html', res)
        else:
            return render(request, 'poem/noresualt.html')

def searchstartword(request):
    if request.method == "GET":
        return render(request, 'poem/search.html', {})
        
    elif request.method == "POST":
        data = request.POST['search1']
        if data != "":
            x = poem.objects.filter(text__startswith=data)
            if len(x) == 0:
                return render(request, 'poem/noresualt.html')
                
            else:
                res = {"resualt": x}
                return render(request, 'poem/searchresualt.html', res)
        else:
            return render(request, 'poem/noresualt.html')

def showtext(request):
    if request.method == "POST":
        data = request.POST.get('poem')
  
        if data == None:

            return render(request,'poem/noresualt.html' )

        text = poem.objects.get(title=data)
        return render(request, 'poem/searchpoem.html', {"text":text})
        



        
    

    
