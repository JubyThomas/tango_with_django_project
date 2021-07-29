import  requests
from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category


def index(request):
    category_list = Category.objects.order_by('-likes')[:5]
    context_dict = {}
    context_dict['boldmessage'] = 'Crunchy, creamy, cookie, candy, cupcake!'
    context_dict['categories'] = category_list
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    return render(request, 'rango/about.html')



    
def show_movies(request):

        result = requests.get('https://api.disneyapi.dev/characters')
        json = result.json()
        return render(request, 
                  "rango/movie_list.html", 
                  context={'obj': json}) 