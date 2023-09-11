from django.db import models
from uuid import uuid4 
from django.contrib.auth.models import AbstractUser

# Create your models here.

class UserModel(AbstractUser): #  pega a herança de abstractuser que é usado apenas para o usuario
    TIPO_CHOICES=[ #para o tipo de clients que teremos , so teremos dois o root e client e este é uma tupla(ou seja imutavel)
        ("root","Root"),
        ("client","Client"),

        ]
    id=models.UUIDField (primary_key=True,default=uuid4,editable=False) # uuid é usado no campo id para definí-lo como primary_key (UNICO DE 128 BITS) deste model. Este tipo de campo aloca um valor único global para cada instância 
    tipo=models.CharField(max_length=10, choices=TIPO_CHOICES,default="client") # de inicio ao se cadastrar esse usuario sera client
    suspenso=models.BooleanField(default=False) #tipo booleano porque so pode ser vdd ou falso e esse defaut é o padrao
    email=models.EmailField(unique=True) #para email e verificar que ele unico

    
