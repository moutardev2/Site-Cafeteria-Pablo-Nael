from django.db import models

# Create your models here.

class Student(models.Model):
    # Django crée un ID tout seul ici (c'est la Clé Primaire, ça bouge jamais)
    
    # Nom de l'élève
    name = models.CharField(max_length=100)
    
    # Son mail unique
    email = models.EmailField(unique=True)
    
    # Combien il lui reste d'argent
    credit = models.FloatField(default=0.0)

    # Pour que ça affiche le nom dans l'admin
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    stock = models.IntegerField(default=0)
    available = models.BooleanField(default=True)
    image = models.ImageField(upload_to='products/', blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.price}€)"

class Transaction(models.Model):
    # C'est la Clé Étrangère : le lien qui pointe vers l'ID de l'élève
    student = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True) # Date du jour automatique
    amount = models.FloatField()

    def __str__(self):
        return f"Transaction de {self.amount}€ le {self.date}"

