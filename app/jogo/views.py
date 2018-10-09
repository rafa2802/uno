from django.shortcuts import render, redirect, HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.views import View
from random import randint
from .models import *

class Home(TemplateView):
	template_name = 'jogo/index.html'

class Regras(TemplateView):
	template_name = 'jogo/regras.html'

class Sobre(TemplateView):
	template_name = 'jogo/sobre.html'

class DeletarPartida(View):
	def get(self, request, pk):
		partida = Partida.objects.filter(id = pk).first()
		partida.delete()
		return render(request, 'jogo/perfil/sucesso.html', {'mensagem': 'Partida excluída com sucesso!'})

class PartidasDisponiveis(View):
	def get(self, request, pk):
		partidas = Partida.objects.filter(status = 0).exclude(usuario = self.request.user)
		partida2 = []
		for partida in partidas:
			if self.request.user not in partida.jogadores.all():
				partida2.append(partida)
		return render(request, 'jogo/perfil/partidas-disponiveis.html', {'partidas': partida2})

class MinhasPartidas(View):
	def get(self, request, pk):
		partidas = Partida.objects.all()
		partidas2 = []
		for partida in partidas:
			if self.request.user in partida.jogadores.all():
				partidas2.append(partida)
		return render(request, 'jogo/perfil/minhas-partidas.html', {'partidas': partidas2})

class CriarPartida(View):
	def post(self, request):
		partida = Partida(usuario = self.request.user, qt_jogadores = int(request.POST['jogadores']), status = 0)
		partida.save()
		partida.jogadores.add(self.request.user)
		partida.save()
		deck = Deck(usuario = self.request.user, partida = partida)
		deck.save()
		cartas = Carta.objects.all()
		for x in range(1, 8):
			carta = randint(1, len(cartas))
			carta_deck = CartaDeck(carta = cartas[carta - 1], status = 0)
			carta_deck.save()
			deck.cartas.add(carta_deck)
			deck.save()
		return render(request, 'jogo/perfil/sucesso.html', {'mensagem': 'Você criou uma nova partida com sucesso! Aguarde os jogadores para iniciar a partida!'})

class EntrarPartida(View):
	def get(self, request, pk):
		partida = Partida.objects.filter(id = pk).first()
		partida.jogadores.add(self.request.user)
		partida.save()
		deck = Deck(usuario = self.request.user, partida = partida)
		deck.save()
		cartas = Carta.objects.all()
		for x in range(1, 8):
			carta = randint(1, len(cartas))
			carta_deck = CartaDeck(carta = cartas[carta - 1], status = 0)
			carta_deck.save()
			deck.cartas.add(carta_deck)
			deck.save()
		if partida.qt_jogadores == len(partida.jogadores.all()):
			partida.status = 1
			partida.save()
		return redirect('jogo:minhas-partidas', pk = self.request.user.pk)

class JogarPartida(View):
	def get(self, request, pk):
		partida = Partida.objects.filter(id = pk).first()
		if partida.qt_jogadores == len(partida.jogadores.all()):
			deck = Deck.objects.filter(usuario = self.request.user, partida = partida).first()
			return render(request, 'jogo/perfil/jogo.html', {'deck': deck})
		return render(request, 'jogo/perfil/erro.html', {'mensagem': 'Ainda não há jogadores suficientes para essa partida!'})

