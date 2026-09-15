
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('descricao', models.TextField(blank=True)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=10)),
                ('estoque', models.IntegerField(default=0)),
                ('ativo', models.BooleanField(default=True)),
                ('data_cadastro', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
