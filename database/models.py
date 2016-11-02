from django.db import models
from django.utils import timezone

# Create your models here.

class Mol(models.Model):
#	author = models.ForeignKey('auth.User')
	id_mol = models.CharField(max_length=200)
	parentid_mol = models.CharField(max_length=200)
	smi_mol = models.TextField()
#	submitted_date = models.DateTimeField(
#			default = timezone.now)


	def __str__(self):
		return self.id_mol

