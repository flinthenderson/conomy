from django.db import models

# Create your models here.

class Wallet(models.Model):
	user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	name = models.CharField(max_length=30)
	description = models.CharField(max_length=100)

	def __str__(self):
		return self.name

class Transaction(models.Model):
	wallet = models.ForeignKey('account.Wallet', related_name='transactions', on_delete=models.CASCADE)
	volume = models.IntegerField()
	description = models.CharField(null=False, max_length=40)
	date = models.DateTimeField()


	def __str__(self):
		return self.description + ' ' + str(self.volume)

