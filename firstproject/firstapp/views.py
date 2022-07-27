from django.shortcuts import render
from django.http import HttpResponse
from firstapp.models import Topic,Webpage,AccessRecord,users
from firstapp.forms import NewUser

# Create your views here.

def index(request):
    wbpage = AccessRecord.objects.order_by('date')
    my_dict = {'access_records':wbpage}
    return render(request, 'firstapp/index.html', context=my_dict)

def help(request):
    helpdict = {'help_me':'Help me  page'}
    return render(request, 'firstapp/help.html', context=helpdict)

def display_users(request):
    form = NewUser()

    if request.method =="POST":
        form = NewUser(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("Error Form invalid")

    return render(request,'firstapp/users.html',{'form':form})
