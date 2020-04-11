from django.db import models
from django.utils import timezone
# Create your models here.

class Wallet(models.Model):
	#Не обязателен, т.к. требование: Кошельков может быть больше чем 1, но сам пользователь один
	# (это его персональный веб сервис).
	#Если требуется аутентификация, можно раскоментировать и расширить функционал
	#user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	name = models.CharField(max_length=30)
	description = models.CharField(max_length=100)
	def __str__(self):
		return self.name

class Transaction(models.Model):
	wallet = models.ForeignKey('account.Wallet', related_name='transactions', on_delete=models.CASCADE)
	volume = models.IntegerField()
	description = models.CharField(null=False, max_length=40)
	date = models.DateTimeField(default=timezone.now())

	def __str__(self):
		return self.description + ' ' + str(self.volume)

