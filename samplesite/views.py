from django.http import HttpResponse

import random

def hello_world(request):
    return HttpResponse("Hello world")

def root_page(request):
    return HttpResponse("Root page")

def random_number(request,min_rand=0,max_rand=100):
    random_num=random.randrange(int(min_rand),int(max_rand))

    msg="random number is %d between:%s - %s " %(random_num,min_rand,max_rand) 
    return HttpResponse(msg)    