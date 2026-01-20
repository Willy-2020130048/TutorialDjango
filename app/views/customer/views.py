from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect

from app.models.customer import Customer
from app.views.customer.form import CustomerForm
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_POST


def home(request):
    customers = Customer.objects.all()

    form = CustomerForm()

    context = {
        'customers': customers,
        'form': form
    }

    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()

    return render(request, "customer/home.html", context)

def add(request):
    form = CustomerForm()

    context = {
        'form': form
    }

    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        return render(request, "customer/form.html", context)

    return redirect("customer_home")

def detail(request, customer_id):
    customer = Customer.objects.get(customer_id=customer_id)
    form = CustomerForm(instance=customer)
    if request.method == "POST":
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect("customer_home")

    context = {
        'customer': customer,
        'form': form
    }
    return render(request, "customer/form.html", context)

@require_POST
def delete(request, customer_id):
    customer = get_object_or_404(Customer, customer_id=customer_id)
    customer.delete()
    return JsonResponse({"success": True, "id": customer_id})