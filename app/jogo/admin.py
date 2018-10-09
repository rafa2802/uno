from django.contrib import admin
from .models import *
# Register your models here.
class PartidaAdmin(admin.ModelAdmin):
  filter_horizontal = ('jogadores',)

class DeckAdmin(admin.ModelAdmin):
  filter_horizontal = ('cartas',)

admin.site.register(Carta)
admin.site.register(Partida, PartidaAdmin)
admin.site.register(Deck, DeckAdmin)
admin.site.register(CartaDeck)