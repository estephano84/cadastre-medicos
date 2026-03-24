from django.contrib import admin
from .models import Medico

admin.site.register(Medico)
#CUSTOMIZAÇÃO DO ADMIN
admin.site.site_header = "Sistemas de Médicos"
admin.site.site_title = "Administração"
admin.site.index_title = "Painel de Controle"