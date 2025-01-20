from django.shortcuts import render
from .models import *
# Create your views here.
def homepage(request):
        aboutUs = About_us.objects.all()[0]
        contex = {
                'about':aboutUs
        }
        return render(request,'anim_blog/index.html',contex)