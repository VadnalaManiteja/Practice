from django.shortcuts import render , redirect
from .models import Contact
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from django.db import transaction

# Create your views here.
def operations(request):
    if request.method == 'POST':
        # Retrieve data from the POST request
        username = request.POST.get('username')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        city = request.POST.get('city')
        pancard = request.POST.get('pancard')
        state = request.POST.get('state')
        profile_picture = request.FILES.get('profilepicture')
        # Create and save the Contact object
        Contact.objects.create(
            username=username,
            mobile=mobile,
            email=email,
            city=city,
            pancard=pancard,
            state=state,
            profile_picture=profile_picture
        )

        if request.POST.get('submit') == 'save':
            messages.success(request, 'Contact data has been saved. You can add more Contacts.')
            return render(request, 'operations.html')  # Stay on the same form page

        # If "Submit" button was clicked
        if request.POST.get('submit') == 'submit':
            messages.success(request, 'Contact data has been successfully submitted.')
            return redirect('operations_list')  # Redirect to the contact list page

    # Handle GET requests and render the form
    return render(request, 'operations.html')

def operations_list(request):
    contacts = Contact.objects.all()  # Query to get all contacts records
    return render(request, 'operations-list.html', {'contacts': contacts})

def delete_operations(request, id):
    contact = get_object_or_404(Contact, id=id)
    contact.delete()
    messages.success(request, 'Contact deleted successfully.')

    with transaction.atomic():
        contacts = Contact.objects.all().order_by('id')
        for index, contact in enumerate(contacts, start=1):
            contact.serial_number = index
            contact.save(update_fields=['serial_number'])

    return redirect('operations_list')

def update_contact(request, id):
    contact = get_object_or_404(Contact, id=id)
    if request.method == 'POST':
        contact.username = request.POST.get('username')
        contact.mobile = request.POST.get('mobile')
        contact.email = request.POST.get('email')
        contact.city = request.POST.get('city')
        contact.pancard = request.POST.get('pancard')
        contact.state = request.POST.get('state')
        if 'profilepicture' in request.FILES:
            contact.profile_picture = request.FILES['profilepicture']
        contact.save()
        messages.success(request, 'Contact updated successfully.')
        return redirect('operations_list')
    return render(request, 'update-operations.html', {'contact': contact})

def view_operation(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    return render(request, 'view-operations.html', {'contact': contact})