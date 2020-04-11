from django.shortcuts import render, get_object_or_404
from account.models import Wallet, Transaction

# Create your views here.
def index(request):
	list_of_wallets = Wallet.objects.all()

	context = {'list_of_wallets': list_of_wallets}
	return render(request, 'account/index.html', context)