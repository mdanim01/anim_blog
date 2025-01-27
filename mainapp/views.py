from django.shortcuts import render
from .models import *
# Create your views here.
def homepage(request):
        aboutUs = About_us.objects.all()[0]
        banner = Banner.objects.all()[0]
        service_heading = Service_heading.objects.all()[0]
        post = S_post.objects.all()
        contex = {
                'about':aboutUs,
                'banner':banner,
                'serviceHeading':service_heading,
                'post':post 
        }
        return render(request,'anim_blog/index.html',contex)

def services(request):
       return render(request,'anim_blog/services-single.html')