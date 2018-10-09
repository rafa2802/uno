from django.urls import include, path
from django.conf.urls import include, url
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

from . import views as jogo

app_name = 'jogo'

urlpatterns = [
	path('', jogo.Home.as_view(), name='home'),
	path('regras/', jogo.Regras.as_view(), name='regras'),
	path('perfil/partidas/<pk>', jogo.MinhasPartidas.as_view(), name='minhas-partidas'),
	path('perfil/partidas/<pk>/disponiveis', jogo.PartidasDisponiveis.as_view(), name='partidas-disponiveis'),
	path('sobre/', jogo.Sobre.as_view(), name='sobre'),
	path('partida/nova/', jogo.CriarPartida.as_view(), name='criar-partida'),
	path('partida/excluir/<pk>', jogo.DeletarPartida.as_view(), name='excluir'),
	path('partida/<pk>/entrar', jogo.EntrarPartida.as_view(), name='entrar'),
	path('partida/<pk>/jogar', jogo.JogarPartida.as_view(), name='jogar'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)