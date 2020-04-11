from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from account.models import Wallet, Transaction
from account.api.serializers import WalletSerializer, TransactionSerializer
import json

#############################################################################################
#CRUD FOR WALLETS
#############################################################################################

@api_view(["GET"])
def list_wallets(request):
	try:
		wallets = Wallet.objects.all()
		for wallet in wallets:
			wallet.update_balance()

		serializer = WalletSerializer(wallets, many=True)
		return JsonResponse({'wallets': serializer.data}, safe=False, status=status.HTTP_200_OK)
	except Exception:
		return JsonResponse({'error': 'Something went wrong'}, safe=False,
							status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["GET"])
def get_wallet_by_id(request, id):
	try:
		wallet = Wallet.objects.filter(pk=id)[0]
		wallet.update_balance()
		transactions = Transaction.objects.filter(wallet=id)

		serializer = WalletSerializer(wallet, many=False)
		serializer_transactions = TransactionSerializer(transactions, many=True)
		return JsonResponse({'wallet': serializer.data, 'transactions':serializer_transactions.data}, safe=False,
							status=status.HTTP_200_OK)
	except Exception:
		return JsonResponse({'error': 'Something went wrong'}, safe=False,
							status=status.HTTP_500_INTERNAL_SERVER_ERROR)



@api_view(["POST"])
def add_wallet(request):
	#THIS IS IT
	payload = json.loads(str(request.POST.dict()).replace("\'", "\""))

	try:
		wallet = Wallet.objects.create(
			name=payload["name"],
			description=payload["description"],
		)
		serializer = WalletSerializer(wallet)
		return JsonResponse({'wallets': serializer.data}, safe=False, status=status.HTTP_201_CREATED)
	except Exception:
		return JsonResponse({'error': 'Something went wrong'}, safe=False,
							status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["PUT"])
def update_wallet(request, id):
	payload = json.loads(str(request.POST.dict()).replace("\'", "\""))
	try:
		wallet = Wallet.objects.filter(pk=id)
		wallet.update(**payload)
		wallet = Wallet.objects.get(pk=id)
		serializer = WalletSerializer(wallet)
		return JsonResponse({'wallet': serializer.data}, safe=False, status=status.HTTP_200_OK)
	except Exception:
		return JsonResponse({'error': 'Something went wrong'}, safe=False,
							status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["DELETE"])
def delete_wallet(request, id):
	try:
		wallet = Wallet.objects.get(pk=id)
		wallet.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)
	except Exception:
		return JsonResponse({'error': 'Something went wrong'}, safe=False,
							status=status.HTTP_500_INTERNAL_SERVER_ERROR)

#############################################################################################
#CRUD FOR TRANSACTIONS
#############################################################################################

@api_view(["GET"])
def list_all_transactions(request):
	transactions = Transaction.objects.all()
	serializer = TransactionSerializer(transactions, many=True)
	return JsonResponse({'transactions': serializer.data}, safe=False, status=status.HTTP_200_OK)

#ADD TRANSACTION TO A WALLET
@api_view(["POST"])
#id is id of wallet for transaction
#possible to pass id a part of slug instead
#def add_transaction(request, id):
def add_transaction(request):
	#THIS IS IT
	payload = json.loads(str(request.POST.dict()).replace("\'", "\""))
	id = payload["id"]

	try:
		transaction = Transaction.objects.create(
			volume=payload["volume"],
			description=payload["description"],
			wallet=Wallet.objects.get(pk=id)
		)
		serializer = TransactionSerializer(transaction)
		return JsonResponse({'transaction': serializer.data}, safe=False, status=status.HTTP_201_CREATED)
	except ObjectDoesNotExist as e:
		return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
	except Exception:
		return JsonResponse({'error': 'Something terrible went wrong'}, safe=False,
							status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["DELETE"])
def delete_transaction(request):
	try:
		payload = json.loads(str(request.POST.dict()).replace("\'", "\""))
		id = payload['id']
		transaction = Transaction.objects.get(pk=id)

		transaction.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)
	except ObjectDoesNotExist as e:
		return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
	except Exception:
		return JsonResponse({'error': 'Something went wrong'}, safe=False,
							status=status.HTTP_500_INTERNAL_SERVER_ERROR)