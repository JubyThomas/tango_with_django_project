import  requests
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    # Refer to the TwD book for more information on how this updated view works.
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    # Spoiler: you don't need to pass a context dictionary here.
    return render(request, 'rango/about.html')



    
def show_movies(request):

        result = requests.get('https://api.disneyapi.dev/characters')
        json = result.json()
        return render(request, 
                  "rango/movie_list.html", 
                  context={'obj': json}) 