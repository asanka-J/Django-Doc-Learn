from django.http import HttpResponse

def index(request):
    return HttpResponse("you are arrived to polls page")