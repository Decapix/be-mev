"""
URL configuration for mevsite project.

The `urlpatterns` list routes URLs to  For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('prestation/', prestation, name="prestation"),
    path('contact/', contact, name="contact"),
    path('entreprise/', entreprise, name="entreprise"),

    path('prestation/dgt/', presta_dgt, name='presta_dgt'),
    path('prestation/amo/', presta_amo, name='presta_amo'),
    path('prestation/dpe/', presta_dpe, name='presta_dpe'),
    path('prestation/audit/', presta_audit, name='presta_audit'),
    path('prestation/renove/', presta_renove, name='presta_renove'),
    path('prestation/audit_regle/', presta_audit_regle, name='presta_audit_regle'),
    path('prestation/bilan/', presta_bilan, name='presta_bilan'),
    
]
