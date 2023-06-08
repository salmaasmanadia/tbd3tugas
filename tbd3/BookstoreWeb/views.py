from django.shortcuts import render, redirect
from .models import Staff, Author, Payment, Orders, Address, Customer, Store, Book
from .forms import StaffForm, AuthorForm, PaymentForm, OrderForm, AddressForm,CustomerForm, StoreForm, BookForm
from django.contrib import messages

def join(request):
    return render(request, 'join.html', {})

def staff(request):
    all_staff = Staff.objects.all()
    return render(request, 'staff.html', {'staff_data': all_staff})

def author(request):
    all_author = Author.objects.all()
    return render(request, 'author.html', {'author_data': all_author})

def payment(request):
    all_payment = Payment.objects.all()
    return render(request, 'payment.html', {'payment_data': all_payment})

def order(request):
    all_order = Orders.objects.all()
    return render(request, 'order.html', {'order_data': all_order})

def address(request):
    all_address = Address.objects.all()
    return render(request, 'address.html', {'address_data': all_address})

def customer(request):
    all_customer = Customer.objects.all()
    return render(request, 'customer.html', {'customer_data': all_customer})

def store(request):
    all_store = Store.objects.all()
    return render(request, 'store.html', {'store_data': all_store})

def book(request):
    all_book = Book.objects.all()
    return render(request, 'book.html', {'book_data': all_book})

def newCustomer(request):
    if request.method == "POST":
        form = CustomerForm(request.POST or None)
        if form.is_valid():
            form.save()
        else:
        	customer_id = request.POST['customer_id']
        	first_name = request.POST['first_name']
        	last_name = request.POST['last_name']
        	email = request.POST['email']
        	address_name = request.POST['address_name']
        	last_update = request.POST['last_update']

        	messages.success(request, "There was an error in your form! Please try again...")
        	return render(request, 'newCustomer.html', {
        		'customer_id': customer_id,
        		'first_name': first_name,
        		'last_name': last_name,
        		'email': email,
        		'address_name': address_name,
        		'last_update': last_update
        		})
        messages.success(request,('Your form has ben submitted successfully!'))
        return redirect('customer')
    else:
        return render(request, 'newCustomer.html', {})

def newPayment(request):
    if request.method == "POST":
        form = PaymentForm(request.POST or None)
        if form.is_valid():
            form.save()
        else:
        	payment_id = request.POST['payment_id']
        	order_id = request.POST['order_id']
        	payment_date = request.POST['payment_date']
        	amount = request.POST['amount']
        	last_update = request.POST['last_update']

        	messages.success(request, "There was an error in your form! Please try again...")
        	return render(request, 'newPayment.html', {
        		'payment_id': payment_id,
        		'order_id': order_id,
        		'payment_date': payment_date,
        		'amount': amount,
        		'last_update': last_update
        		})
        messages.success(request,('Your form has ben submitted successfully'))
        return redirect('payment')
    else:
        return render(request, 'newPayment.html', {})

def newOrder(request):
    if request.method == "POST":
        form = OrderForm(request.POST or None)
        if form.is_valid():
            form.save()
        else:
        	order_id = request.POST['order_id']
        	first_name = request.POST['first_name']
        	last_name = request.POST['last_name']
        	staff_name = request.POST['staff_name']
        	order_date = request.POST['order_date']
        	total_amount = request.POST['total_amount']
        	last_update = request.POST['last_update']
	
        	messages.success(request, "There was an error in your form! Please try again...")
        	return render(request, 'newOrder.html', {
        		'order_id': order_id,
        		'first_name': first_name,
        		'last_name': last_name,
        		'staff_name': staff_name,
        		'order_date': order_date,
        		'total_amount': total_amount,
        		'last_update': last_update
        		})
        messages.success(request,('Your form has ben submitted successfully'))
        return redirect('order')
    else:
        return render(request, 'newOrder.html', {})

def newAddress(request):
    if request.method == "POST":
        form = AddressForm(request.POST or None)
        if form.is_valid():
            form.save()
        else:
        	address_id = request.POST['address_id']
        	address_name = request.POST['address_name']
        	district = request.POST['district']
        	city = request.POST['city']
        	country = request.POST['country']
        	postal_code = request.POST['postal_code']
        	last_update = request.POST['last_update']

        	messages.success(request, "There was an error in your form! Please try again...")
        	return render(request, 'newAddress.html', {
        		'address_name': address_name,
        		'address_id': address_id,
        		'district': district,
        		'city': city,
        		'country': country,
        		'postal_code': postal_code,
        		'last_update': last_update
        		})
        messages.success(request,('Your form has ben submitted successfully'))
        return redirect('address')
    else:
        return render(request, 'newAddress.html', {})

def newBook(request):
    if request.method == "POST":
        form = BookForm(request.POST or None)
        if form.is_valid():
            form.save()
        else:
        	book_id = request.POST['book_id']
        	title = request.POST['title']
        	author_name = request.POST['author_name']
        	genre = request.POST['genre']
        	category = request.POST['category']
        	publication_date = request.POST['publication_date']
        	rating = request.POST['rating']
        	price = request.POST['price']
        	last_update = request.POST['last_update']

        	messages.success(request, "There was an error in your form! Please try again...")
        	return render(request, 'newBook.html', {
        		'book_id': book_id,
        		'title': title,
        		'author_name': author_name,
        		'genre': genre,
        		'category': category,
        		'publication_date': publication_date,
        		'rating': rating,
        		'price': price,
        		'last_update': last_update
        		})
        messages.success(request,('Your form has ben submitted successfully'))
        return redirect('book')
    else:
        return render(request, 'newBook.html', {})

def newAuthor(request):
    if request.method == "POST":
        form = AuthorForm(request.POST or None)
        if form.is_valid():
            form.save()
        else:
        	author_id = request.POST['author_id']
        	author_name = request.POST['author_name']
        	gender = request.POST['gender']
        	birthdate = request.POST['birthdate']
        	address_name = request.POST['address_name']
        	last_update = request.POST['last_update']

        	messages.success(request, "There was an error in your form! Please try again...")
        	return render(request, 'newAuthor.html', {
        		'author_id': author_id,
        		'author_name': author_name,
        		'gender': gender,
        		'birthdate': birthdate,
        		'address_name': address_name,
        		'last_update': last_update
        		})
        messages.success(request,('Your form has ben submitted successfully'))
        return redirect('author')
    else:
        return render(request, 'newAuthor.html', {})

def newStaff(request):
    if request.method == "POST":
        form = StaffForm(request.POST or None)
        if form.is_valid():
            form.save()
        else:
        	first_name = request.POST['first_name']
        	last_name = request.POST['last_name']
        	email = request.POST['email']
        	address_name = request.POST['address_name']
        	store_name = request.POST['store_name']
        	last_update = request.POST['last_update']

        	messages.success(request, "There was an error in your form! Please try again...")
        	return render(request, 'newStaff.html', {
        		'first_name': first_name, 
        		'last_name': last_name, 
        		'email':email, 
        		'address_name': address_name,
        		'store_name': store_name,
        		'last_update': last_update
        		})
        messages.success(request,('Your form has ben submitted successfully'))
        return redirect('staff')
    else:
        return render(request, 'newStaff.html', {})

def newStore(request):
    if request.method == "POST":
        form = StoreForm(request.POST or None)
        if form.is_valid():
            form.save()
        else:
        	store_id = request.POST['store_id']
        	store_name = request.POST['store_name']
        	address_name = request.POST['address_name']
        	last_update = request.POST['last_update']

        	messages.success(request, "There was an error in your form! Please try again...")
        	return render(request, 'newStore.html', {
        		'store_id': store_id, 
        		'name':name, 
        		'address_name':address_name, 
        		'last_update': last_update
        		})
        messages.success(request,('Your form has ben submitted successfully'))
        return redirect('store')
    else:
        return render(request, 'newStore.html', {})
