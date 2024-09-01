from django.urls import path

from .api.user.UserLC.views import UserLCView
from .api.user.UserRUD.views import UserRUDView

from .api.client.ClientLC.views import ClientLCView
from .api.client.ClientRUD.views import ClientRUDView


app_name = 'user'

urlpatterns = [
    path('userlc/', UserLCView.as_view(), name='userlc'),
    path('userrud/<int:pk>/', UserRUDView.as_view(), name='userrud'),
    
    path('clientlc/', ClientLCView.as_view(), name='clientlc'),
    path('clientrud/<int:pk>/', ClientRUDView.as_view(), name='clientrud'),
]
