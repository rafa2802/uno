from django.db import models
from app.core.models import UUIDUser

class Carta(models.Model):
	COR = (
	(0, 'Vermelho'),
	(1, 'Amarelo'),
	(2, 'Verde'),
	(3, 'Azul')
	)

	PODER = (
	(0, 'Sim'),
	(1, 'Não')
	)
	titulo = models.CharField(max_length = 70, verbose_name = 'título')
	carta = models.ImageField(upload_to = 'cartas/', verbose_name = 'imagem da carta')
	numero = models.IntegerField(verbose_name = 'número da carta', blank = True, null = True)
	cor = models.IntegerField(choices = COR, verbose_name = 'cor da carta', blank = True, null = True)
	inverso = models.IntegerField(choices = PODER, verbose_name = 'inverter jogo')
	comprar2 = models.IntegerField(choices = PODER, verbose_name = 'comprar +2')
	comprar4 = models.IntegerField(choices = PODER, verbose_name = 'comprar +4')
	bloqueio = models.IntegerField(choices = PODER, verbose_name = 'bloqueio')

	def __str__(self):
		if self.cor == 0:
			return 'Carta: %s | Cor: Vermelha' % (self.titulo)
		elif self.cor == 1:
			return 'Carta: %s | Cor: Amarelo' % (self.titulo)
		elif self.cor == 2:
			return 'Carta: %s | Cor: Verde' % (self.titulo)
		elif self.cor == 3:
			return 'Carta: %s | Cor: Azul' % (self.titulo)
		else:
			return 'Carta: %s | Carta Coringa' % (self.titulo)

	class Meta:
		verbose_name = 'carta'
		verbose_name_plural = 'cartas'

class Partida(models.Model):
	STATUS = (
	(0, 'Aguardando Jogadores'),
	(1, 'Em Andamento'),
	(2, 'Finalizada')
	)
	usuario = models.ForeignKey(UUIDUser, on_delete = models.CASCADE, related_name = 'usuario', verbose_name = 'usuário')
	qt_jogadores = models.IntegerField(verbose_name = 'quantidade de jogadores')
	jogadores = models.ManyToManyField(UUIDUser, related_name = 'jogadores', verbose_name = 'jogadores', blank = True)
	turno = models.ForeignKey(UUIDUser, on_delete = models.CASCADE, related_name = 'turnos', blank = True, verbose_name = 'jogador atual', null = True)
	status = models.IntegerField(choices = STATUS, verbose_name = 'Status')
	last_card = models.ForeignKey('CartaDeck', on_delete = models.CASCADE, related_name = 'last_cards', blank = True, null = True, verbose_name = 'última carta jogada')

	def __str__(self):
		return 'Partida do Jogador: %s' % self.usuario.username

	class Meta:
		verbose_name = 'partida'
		verbose_name_plural = 'partidas'

class CartaDeck(models.Model):
	STATUS = (
	(0, 'Não Usada'),
	(1, 'Usada')
	)
	carta = models.ForeignKey(Carta, on_delete = models.CASCADE, verbose_name = 'carta', related_name = 'cartas')
	status = models.IntegerField(choices = STATUS, verbose_name = 'status')

	def __str__(self):
		return self.carta.titulo

	class Meta:
		verbose_name = 'carta do deck'
		verbose_name_plural = 'cartas dos decks'

class Deck(models.Model):
	usuario = models.ForeignKey(UUIDUser, on_delete = models.CASCADE, verbose_name = 'usuário', related_name = 'user')
	partida = models.ForeignKey(Partida, on_delete = models.CASCADE, related_name = 'partida', verbose_name = 'partida')
	cartas = models.ManyToManyField(CartaDeck, related_name = 'cards', verbose_name = 'cartas', blank = True)

	def __str__(self):
		return 'Deck do usuário: %s' % self.usuario.username

	class Meta:
		verbose_name = 'deck'
		verbose_name_plural = 'decks'
