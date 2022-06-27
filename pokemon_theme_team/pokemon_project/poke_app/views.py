from urllib import response
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import requests as HTTP_Client
import pprint
import os
import random

# pokeIndex = Math.trunc(Math.random() * 898) + 1;



# Create your views here.
def index(request, id_number):
    
    poke_list = []

    poke_index = random.randrange(1, 151) 

    endpoint = f"https://pokeapi.co/api/v2/pokemon/{id_number}"
    API_response = HTTP_Client.get(endpoint)
    responseJSON = API_response.json()

    first_type = responseJSON['types'][0]['type']['name']
    starter_pokemon = responseJSON['forms'][0]['name']

    pokemon_gif = f"https://projectpokemon.org/images/normal-sprite/{starter_pokemon}.gif"
    
    poke_list.append(pokemon_gif)



    while len(poke_list) < 6:
        random_index = random.randrange(1, 300) 
        endpoint_2 = f"https://pokeapi.co/api/v2/pokemon/{random_index}"
        API_response_2 = HTTP_Client.get(endpoint_2)
        responseJSON_2 = API_response_2.json()

        poke_type = responseJSON_2['types'][0]['type']['name']
        
        pokemons = responseJSON_2['forms'][0]['name']

        pokemon_gif_2 = f"https://projectpokemon.org/images/normal-sprite/{pokemons}.gif"
        
        if poke_type == first_type:
            if pokemon_gif_2 not in poke_list:
                poke_list.append(pokemon_gif_2)

        # API_response_type = HTTP_Client.get(poke_type)
        # responseJSON_2 = API_response_type.json()
        # type_list = responseJSON_2['pokemon']

    # for i in range(1, 5):
        
        

    return render(request, 'pages/index.html', {"poke_list": poke_list})