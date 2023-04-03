from django.shortcuts import render
from .models import Mymessage


# Create your views here.
def home(request):
    contaxt={'home':'active'}
    return render(request, 'core/home.html', contaxt)

def contact(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        youmsg=request.POST['youmsg']
        obj=Mymessage(name=name, email=email, youmsg=youmsg)
        obj.save()
  
    return render(request, 'core/contact.html')


def services(request):
    contaxt1={'services':'active'}
    return render(request, 'core/services.html', contaxt1)



# Create your views here.
def education(request):
    contaxt={'education':'active'}
    return render(request, 'core/skill.html',contaxt)



