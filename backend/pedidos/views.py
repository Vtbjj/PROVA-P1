from django.http import JsonResponse

from .models import Pedido


def lista_pedidos(request):
	pedidos = list(Pedido.objects.values(
		'id',
		'cliente_id',
		'produto_id',
		'quantidade',
		'data_pedido',
		'status',
	))
	return JsonResponse(pedidos, safe=False)
