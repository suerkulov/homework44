from django.urls import path

from webapp.views import check_view, game_history

urlpatterns = [
    path('', check_view),
    path('history/', game_history)
]