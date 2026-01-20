from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404

from app.models.item import Item
from app.views.item.form import ItemForm


def home(request):
    form = ItemForm()
    context = {
        'form': form
    }

    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            new_item = form.save()
            return JsonResponse({
                'item_id': new_item.item_id,
                'item_no': new_item.item_no,
                'item_name': new_item.item_name,
                'stock': new_item.stock,
            })
        else:
            return JsonResponse({'error': 'Data tidak valid'}, status=400)
    else:
        return render(request, "item/home_vue.html", context)

def fetch_items(request):
    items = Item.objects.all()  # Ambil semua item dari database
    items_data = list(items.values('item_id', 'item_no', 'item_name', 'stock'))
    return JsonResponse(items_data, safe=False)

def detail(request, item_id):
    item = Item.objects.get(item_id=item_id)
    form = ItemForm(instance=item)
    if request.method == "POST":
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect("item_home")

    context = {
        'item': item,
        'form': form
    }
    return render(request, "item/form.html", context)

def delete(request, item_id):
    item = get_object_or_404(Item, item_id=item_id)
    item.delete()
    return JsonResponse({"success": True, "id": item_id})
