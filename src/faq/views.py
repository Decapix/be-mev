from django.shortcuts import render
from .models import Ask
# Create your views here.


def faq(request):
    """view for track project"""
    ask = Ask.objects.filter(show=True)
    return render(request, 'faq/ask.html', context={"ask": ask})

