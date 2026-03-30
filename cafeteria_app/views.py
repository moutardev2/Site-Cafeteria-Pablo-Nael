from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required

from .forms import ProductForm, StudentForm, TransactionForm
from .models import Product, Student, Transaction


def home(request):
    if request.user.is_authenticated:
        return redirect("product_list")
    return redirect("cas_ng_login")

@login_required
def product_list(request):
    # On filtre pour n'avoir que les produits disponibles (available=True)
    products = Product.objects.filter(available=True)
    return render(request, 'product_list.html', {'products': products})


@login_required
def product_manage_list(request):
    products = Product.objects.all().order_by("name")
    return render(request, "product_manage_list.html", {"products": products})


@login_required
def product_add(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("product_manage_list")
    else:
        form = ProductForm()

    return render(request, "product_form.html", {"form": form, "title": "Ajouter un produit"})


@login_required
def product_edit(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect("product_manage_list")
    else:
        form = ProductForm(instance=product)

    return render(request, "product_form.html", {"form": form, "title": "Modifier un produit"})


@login_required
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == "POST":
        product.delete()
        return redirect("product_manage_list")

    return render(request, "product_confirm_delete.html", {"product": product})


@login_required
def student_list(request):
    students = Student.objects.all().order_by("name")
    return render(request, "student_list.html", {"students": students})


@login_required
def student_add(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("student_list")
    else:
        form = StudentForm()

    return render(request, "student_form.html", {"form": form, "title": "Ajouter un étudiant"})


@login_required
def student_edit(request, pk):
    student = get_object_or_404(Student, pk=pk)

    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect("student_list")
    else:
        form = StudentForm(instance=student)

    return render(request, "student_form.html", {"form": form, "title": "Modifier un étudiant"})


@login_required
def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)

    if request.method == "POST":
        student.delete()
        return redirect("student_list")

    return render(request, "student_confirm_delete.html", {"student": student})


@login_required
def transaction_list(request):
    transactions = Transaction.objects.select_related("student", "product").order_by("-date")
    return render(request, "transaction_list.html", {"transactions": transactions})


@login_required
def transaction_add(request):
    if request.method == "POST":
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("transaction_list")
    else:
        form = TransactionForm()

    return render(request, "transaction_form.html", {"form": form, "title": "Ajouter une transaction"})


@login_required
def transaction_edit(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk)

    if request.method == "POST":
        form = TransactionForm(request.POST, instance=transaction)
        if form.is_valid():
            form.save()
            return redirect("transaction_list")
    else:
        form = TransactionForm(instance=transaction)

    return render(request, "transaction_form.html", {"form": form, "title": "Modifier une transaction"})


@login_required
def transaction_delete(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk)

    if request.method == "POST":
        transaction.delete()
        return redirect("transaction_list")

    return render(request, "transaction_confirm_delete.html", {"transaction": transaction})