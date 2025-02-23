from django.db import models


class Contact(models.Model):
    TYPE_CHOICES = [
        ('particulier', 'Particulier'),
        ('collectivite', 'Collectivité'),
        ('visiteur', 'Visiteur'),
    ]

    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField()
    type_contact = models.CharField(max_length=20, choices=TYPE_CHOICES)
    message = models.TextField()
    date_envoi = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.prenom} {self.nom} - {self.date_envoi}"
# Create your models here.
