from django.shortcuts import render

# Create your views here.

def index(request):
    link = request.GET.get('link', None)
    is_slugcustom = request.GET.get('is_slugcustom', None)
    custom_slug = request.GET.get('customslug', None)
    if link is not None:
        #making page with random slug
        if is_slugcustom == 'on' and custom_slug is not None:
            pass
            #making page with custom slug
    return render(request,'index.html',)