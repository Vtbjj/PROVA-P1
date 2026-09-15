
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clientes', '0001_initial'),
        ('produtos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField(default=1)),
                ('data_pedido', models.DateField(auto_now_add=True)),
                ('status', models.CharField(default='pendente', max_length=50)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pedidos', to='clientes.cliente')),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pedidos', to='produtos.produto')),
            ],
        ),
    ]
