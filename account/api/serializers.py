from rest_framework import serializers
from account.models import Wallet, Transaction

class WalletSerializer(serializers.ModelSerializer):
	class Meta:
		model = Wallet
		fields = ['id', 'name', 'description', 'balance']

class TransactionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Transaction
		fields = ['id', 'wallet', 'volume', 'description']