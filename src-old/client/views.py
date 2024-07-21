from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Client
from django.contrib import messages
import uuid
from django.http import JsonResponse
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import requests
from django.conf import settings





# Create your views here.
def client(request):
    """view for track project"""
    client_id = request.session.get('client_id')

    if client_id is None:
        # Si aucun ID client n'est trouvé dans la session, rediriger vers la page de connexion
        return redirect('requestnumber')
    try:
        # aller chercher le cliet sur trello
        search_id = client_id
        board_id = settings.BOARD_ID
        key = settings.KEY_TRELLO
        token = settings.TOKEN_TRELLO
        list_id = find_card_by_id(board_id, key, token, search_id)

        match list_id:
            case settings.ID_LIST_1 :
                advancement = 1
            case settings.ID_LIST_2 :
                advancement = 2
            case settings.ID_LIST_3 :
                advancement = 3
            case settings.ID_LIST_4 :
                advancement = 4
            case settings.ID_LIST_5 :
                advancement = 5
            case settings.ID_LIST_6 :
                advancement = 6
        
        steps = range(1, 7)
        
    except :
        # Gérer l'erreur si l'ID de session ne correspond à aucun client
        return redirect('requestnumber')
    # Passer le client au template
    return render(request, 'client/client.html', context={"advancement": advancement, 'steps': steps})

def request_number(request):
    """juste check if the client exist and put id in session"""
    if request.method == 'POST':
        identification_number = request.POST.get('identification_number')
        print("okokoko10", identification_number)
        try:
            search_id = identification_number
            board_id = settings.BOARD_ID
            key = settings.KEY_TRELLO
            token = settings.TOKEN_TRELLO
            # aller chercher le client sur trello (juste verifier si il existe)
            check = check_card_by_id(board_id, key, token, search_id)

            if check :
                print("okokok2")
                # Par exemple, stocker l'ID client dans la session
                request.session['client_id'] = str(identification_number)
                return redirect('client')  # Redirige vers l'interface du client
            else :
                messages.error(request, 'Numéro d\'identification invalide.')
        except Client.DoesNotExist:
            messages.error(request, 'Numéro d\'identification invalide.')
    return render(request, 'client/request-number.html')



def finish_session(request):
    """Supprime l'ID client de la session et redirige vers l'entrée de nouveau numéro."""
    if 'client_id' in request.session:
        del request.session['client_id']
    return redirect('requestnumber')  # Assurez-vous que le nom d'URL est correct



# function 


def trello_func_base(board_id, key, token):
        # URL de l'API pour obtenir toutes les cartes du tableau
    url = f"https://api.trello.com/1/boards/{board_id}/cards?key={key}&token={token}"
    
    # Faire la requête GET à l'API de Trello
    response = requests.get(url)
    if response.status_code != 200:
        return None, "Failed to retrieve cards"

    # Charger les données JSON des cartes
    cards = response.json()
    return cards


def find_card_by_id(board_id, key, token, search_id):
    cards = trello_func_base(board_id, key, token)
    
    # Rechercher la carte avec l'ID spécifié dans la description
    for card in cards:
        if search_id in card['name']:
            # Extraire l'ID de la liste et la description
            list_id = card['idList']
            return list_id

    return None, "Card not found"



def check_card_by_id(board_id, key, token, search_id):
    cards = trello_func_base(board_id, key, token)

    
    # Rechercher la carte avec l'ID spécifié dans la description
    for card in cards:
        if search_id in card['name']:

            return True
    print("false")
    return False







