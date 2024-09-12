from django.shortcuts import render, HttpResponse
from .models import Contact
from django.shortcuts import redirect
from django.http import HttpResponse


# Create your views here.
def home(request):
    return render(request,'home.html')

def products(request):
    courses = [
        {'id': 1, 'name': 'Python for Beginners', 'description': 'Learn Python from scratch.', 'price': 50.00},
        {'id': 2, 'name': 'Web Development Bootcamp', 'description': 'Master front-end and back-end development.', 'price': 75.00},
        {'id': 3, 'name': 'Data Science Essentials', 'description': 'Learn data science and machine learning.', 'price': 100.00},
        # Add more products here
    ]
    
    context = {
        'courses': courses
    }

    return render(request, 'products.html', context)

def view_cart(request):
    # Retrieve the cart from the session, or create an empty one if it doesn't exist
    cart = request.session.get('cart', {})
    
    cart_items = []
    total_price = 0
    
    # Loop through the cart and fetch product details based on product ID
    for product_id, quantity in cart.items():
        product = products.get(int(product_id))
        if product:
            total_cost = product['price'] * quantity
            cart_items.append({
                'id': product_id,
                'name': product['name'],
                'price': product['price'],
                'quantity': quantity,
                'total_cost': total_cost,
            })
            total_price += total_cost
    
    # Pass cart items and total price to the template
    return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price})

def add_to_cart(request, product_id):
    # Retrieve the cart from the session or create a new empty cart
    cart = request.session.get('cart', {})
    
    # Update the quantity of the product in the cart
    if str(product_id) in cart:
        cart[str(product_id)] += 1
    else:
        cart[str(product_id)] = 1
    
    # Save the updated cart back to the session
    request.session['cart'] = cart
    
    return redirect('view_cart')

def remove_from_cart(request, product_id):
    # Retrieve the cart from the session
    cart = request.session.get('cart', {})
    
    # Remove the item from the cart if it exists
    if str(product_id) in cart:
        del cart[str(product_id)]
    
    # Save the updated cart back to the session
    request.session['cart'] = cart
    
    return redirect('view_cart')

def contact_us(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        Contact.objects.create(name=name, email=email, message=message)
        return redirect('home')
    return render(request, 'contact_us.html')