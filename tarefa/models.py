from django.db import models
from uuid import uuid4 
from user.models import UserModel #importei models de user para ca 

class TarefaModel(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid4,editable=False)
    user=models.ForeignKey(UserModel,on_delete=models.CASCADE,related_name="tarefa") #criado para que quando se deletar um usuario (ForeignKey pega esse id do usuario que sera apagado) as suas tarefas sejam apagadas(on_delete) em cascata
    nome=models.CharField(max_length=100)
    descricao=models.CharField(max_length=254)
    feita=models.BooleanField(default=False)
    creat_at=models.DateTimeField(auto_now_add=True)
    delete=models.BooleanField(default=False) 