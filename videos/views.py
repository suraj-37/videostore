from django.shortcuts import render
from .models import Categorys,Videos

# Create your views here.
def gallery(request):
    categorys=Categorys.objects.all()
    videos= Videos.objects.all()

    context={'categorys':categorys,'videos':videos}
    return render( request, "videos/gallery.html",context)

def addVideos(request):
    return render( request, "videos/add.html")

def viewVideo(request,pk):
    videos= Videos.objects.get(id=pk)
    return render( request, "videos/video.html" , {'videos':videos })        