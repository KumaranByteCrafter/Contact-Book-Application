from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect,get_object_or_404
from .forms import RegistrationForm, ContactForm, CategoryForm
from .models import Contact, Category
import csv
from django.http import HttpResponse
from django.contrib.auth.views import LoginView
from django.contrib import messages

# registration
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(request.POST['password'])
            user.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'contacts/register.html', {'form': form})


# dashboard
@login_required
def dashboard(request):
    contacts = Contact.objects.filter(user=request.user)
    categories = Category.objects.filter(user=request.user)
    return render(request, 'contacts/dashboard.html', {'contacts': contacts, 'categories': categories})


# add Contact

@login_required
def add_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST, user=request.user)  # giving form  user here
        if form.is_valid():
            contact = form.save(commit=False)
            contact.user = request.user
            contact.save()
            return redirect('dashboard')
    else:
        form = ContactForm(user=request.user)  # for GET request from form
    return render(request, 'contacts/add_contact.html', {'form': form})

@login_required
def delete_contact(request, pk):  # <-- Must accept `pk`
    contact = get_object_or_404(Contact, pk=pk)
    contact.delete()
    return redirect('dashboard')

@login_required
def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category/categories.html', {'categories': categories})
# add Category
@login_required
def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.user = request.user
            category.save()
            return redirect('dashboard')
    else:
        form = CategoryForm()
    return render(request, 'category/add_category.html', {'form': form})

@login_required
def delete_category(request, category_id):
    if request.method == 'POST':
        category = get_object_or_404(Category, id=category_id)
        category.delete()
        messages.success(request, f"Category '{category.name}' deleted successfully.")
    return redirect('dashboard')
# export to as  csv file with fields
@login_required
def export_contacts(request):
    contacts = Contact.objects.filter(user=request.user)
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=contacts.csv'
    writer = csv.writer(response)
    writer.writerow(['Name','Phone','Email','Address','Category'])
    for contact in contacts:
        writer.writerow([contact.name, contact.phone, contact.email, contact.address, contact.category.name if contact.category else ''])
    return response


# import from CSV
def import_contacts(request):
    if request.method == "POST":
        csv_file = request.FILES['csv_file']
        decoded_file = csv_file.read().decode('utf-8').splitlines()
        reader = csv.DictReader(decoded_file)
       
        for row in reader:
            category_name = row.get('Category')#this is for when we import non-existing 
            category_obj, created = Category.objects.get_or_create(name=category_name)
            Contact.objects.create(
                name=row.get('Name'),
                phone=row.get('Phone'),
                email=row.get('Email'),
                address = row.get('Address'),
                category = category_obj,
                user=request.user,
            )

        return redirect('dashboard')
    return render(request, 'contacts/import_contacts.html')

