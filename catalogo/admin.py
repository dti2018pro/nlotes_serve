from django.contrib import admin
from catalogo.models.diagnostico import Diagnostico
from catalogo.models_raiz import Categoria
# Register your models here.
admin.site.register(Diagnostico)

admin.site.register(Categoria)

