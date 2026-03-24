from django import forms

from .models import Product, Student, Transaction


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["name", "email", "credit"]


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "stock", "available"]


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ["student", "product", "amount"]
