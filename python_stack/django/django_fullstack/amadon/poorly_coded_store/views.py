from django.shortcuts import redirect, render
from .models import Order, Product
from django.contrib import messages

def index(request):
    context = {
        "all_products": Product.objects.all()
    }
    return render(request, "store/index.html", context)

def seed(request):
    Product.objects.create(description="Shirt", price=15.99)
    Product.objects.create(description="Pants", price=25.99)
    Product.objects.create(description="Hat", price=12.99)

    messages.success(request, "Products seeded successfully!")

    return redirect("/")    

def checkout(request):
    quantity_from_form = int(request.POST["quantity"])
    product = Product.objects.get(id=request.POST["product_id"])
    price_from_form = product.price
    total_charge = quantity_from_form * price_from_form
    print("Charging credit card...")
    Order.objects.create(quantity_ordered=quantity_from_form, total_price=total_charge)

    messages.success(request, f"Successfully purchased {quantity_from_form} {product.description}(s) for ${total_charge:.2f}!")

    context = {
        "total_price": total_charge,
        "quantity_from_form": quantity_from_form,
    }

    return redirect('/thank_you')

def thank_you(request):
    return render(request, "store/thank_you.html")