from django.contrib import admin
from cursos.models import Aulas, Cursos, Comentarios, NotasAulas

# Register your models here.

@admin.register(Cursos)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'descricao')

@admin.register(Aulas)
class AulaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'descricao')

@admin.register(Comentarios)
class ComentarioAdmin(admin.ModelAdmin):
    list_display  = ('aula', 'usuario', 'data')

@admin.register(NotasAulas)
class NotasAulas(admin.ModelAdmin):
    list_display = ('aula','nota','usuario')