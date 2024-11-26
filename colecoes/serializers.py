from rest_framework import serializers
from .models import Colecao, Livro

class LivroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livro
        fields = ['id', 'titulo', 'autor']

class ColecaoSerializer(serializers.ModelSerializer):
    livros = LivroSerializer(many=True)  # Inclui os livros na resposta

    class Meta:
        model = Colecao
        fields = ['id', 'nome', 'descricao', 'livros', 'colecionador']
