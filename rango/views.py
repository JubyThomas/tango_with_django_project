  
import  requests
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    return render(request, 'rango/about.html')

def show_movies(request):

        result = requests.get('https://api.disneyapi.dev/characters')
        json = result.json()


    
        return render(request, 
                  "rango/movie_list.html", 
                  context={'obj': json}) 