from django.shortcuts import render
from .models import Categorys,Videos

# Create your views here.
def gallery(request):
    categorys=Categorys.objects.all()
    videos= Videos.objects.all()

    context={'categorys':categorys,'videos':videos}
    return render( request, "videos/gallery.html",context)

def viewVideo(request,pk):
    videos= Videos.objects.get(id=pk)
    return render( request, "videos/video.html" , {'videos':videos })    


def addVideos(request):
    categorys=Categorys.objects.all()
    if request.method == 'POST':
        data=request.POST
        video= request.FILES.get('video')
        if data['category']!='none':
            category=Categorys.objects.get(id=data['category'])
        elif data['category_new']!='':
            category, created=Categorys.objects.get_or_create(name=data['category_new'])
        else:
            category= None
        video=Videos.objects.create(
            Category=category,
            description=data['description'],
            video=video,
        )     

    context={'categorys':categorys }
    return render( request, "videos/add.html",context)        