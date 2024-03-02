from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Client
from django.contrib import messages
import uuid
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import gspread
from oauth2client.service_account import ServiceAccountCredentials


@csrf_exempt
def google_sheets_webhook(request):
    if request.method == 'POST':
        data = request.POST
        # Supposons que le payload contient 'name' et 'description'
        Item.objects.create(
            name=data.get('name'),
            description=data.get('description')
        )
        return JsonResponse({"status": "success"}, status=200)
    return JsonResponse({"error": "Méthode non autorisée"}, status=405)


# Create your views here.
def client(request):
    """view for track project"""
    client_id = request.session.get('client_id')
    if client_id is None:
        # Si aucun ID client n'est trouvé dans la session, rediriger vers la page de connexion
        return redirect('requestnumber')
    try:
        client_id = uuid.UUID(client_id)  # Convertir la chaîne en UUID
        clien = Client.objects.get(id=client_id)
    except Client.DoesNotExist:
        # Gérer l'erreur si l'ID de session ne correspond à aucun client
        return redirect('requestnumber')

    # Passer le client au template
    return render(request, 'client/client.html', context={"client": clien})

def request_number(request):
    if request.method == 'POST':
        identification_number = request.POST.get('identification_number')
        try:
            client = Client.objects.get(identification_number=identification_number)
            # Ici, vous pouvez gérer la session de connexion selon vos besoins
            # Par exemple, stocker l'ID client dans la session
            request.session['client_id'] = str(client.id)
            return redirect('client')  # Redirige vers l'interface du client
        except Client.DoesNotExist:
            messages.error(request, 'Numéro d\'identification invalide.')
    return render(request, 'client/request-number.html')




