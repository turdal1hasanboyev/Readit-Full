from django.urls import path

from .api.contact.ContactLC.views import ContactLCView
from .api.contact.ContactRUD.views import ContactRUDView


app_name = 'contact'

urlpatterns = [
    path('contactlc/', ContactLCView.as_view(), name='contact_lc'),
    path('contactrud/<str:name>/', ContactRUDView.as_view(), name='contact_rud'),
]
