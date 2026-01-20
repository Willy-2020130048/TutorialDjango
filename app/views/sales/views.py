from django.forms import model_to_dict
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

from app.models.sales import Sales
from app.views.sales.form import SalesForm


def home(request):
    sales = Sales.objects.all()
    form = SalesForm()
    context = {
        'sales': sales,
        'form': form,
    }

    if request.method == "POST":
        form = SalesForm(request.POST)
        if form.is_valid():
            new_item = form.save()

            item_dict = model_to_dict(new_item.item)

            return JsonResponse({
                'sales_id': new_item.sales_id,
                'sales_no': new_item.sales_no,
                'item': item_dict,
                'quantity': new_item.quantity,
            })
        else:
            return JsonResponse({'error': 'Data tidak valid'}, status=400)
    else:
        return render(request, "sales/home.html", context)

def fetch_data(request):
    sales = Sales.objects.all()
    sales_data = []

    for s in sales:
        sales_data.append({
            'sales_id': s.sales_id,
            'sales_no': s.sales_no,
            'quantity': s.quantity,
            'item': {
                'item_id': s.item.item_id,
                'item_name': s.item.item_name,
                'item_no': s.item.item_no
            }
        })
    return JsonResponse(sales_data, safe=False)


def delete(request, sales_id):
    sales = get_object_or_404(Sales, sales_id=sales_id)
    sales.delete()
    return JsonResponse({"success": True, "id": sales_id})
