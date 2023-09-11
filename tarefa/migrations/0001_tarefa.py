# Generated by Django 3.2.20 on 2023-08-18 22:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TarefaModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.CharField(max_length=254)),
                ('feita', models.BooleanField(default=False)),
                ('creat_at', models.DateTimeField(auto_now_add=True)),
                ('delete', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tarefa', to=settings.AUTH_USER_MODEL)),
            ], # o field é para se comunicar com o banco de dados
        ),
    ]
#cria o codigo que traduz o que escrevemos no python para o sql no qual estamos utilizando