from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Person
from faker import Faker
import random
def insert_rows(request):
    fake = Faker()
    for _ in range(5):
        Person.objects.create(
            name=fake.name(),
            age=random.randint(18,50),
            email=fake.email()
        )
    persons=Person.objects.all()
    return HttpResponse("5 records inserted successfully.")

def person_list(request):
    # Get sorting field and order from GET parameters
    sort_by = request.GET.get('sort', 'name')  # Default to 'name' if not provided
    order = request.GET.get('order', '')

    # Check if the field to sort by is valid
    valid_fields = ['name', 'age', 'email', 'id']  # List of valid fields in the Person model
    if sort_by not in valid_fields:
        sort_by = 'name'  # Default field if invalid

    # Apply descending order if 'order' is 'desc'
    if order == "desc":
        sort_by = f"-{sort_by}"

    # Query the persons and order by the selected field
    persons = Person.objects.all().order_by(sort_by)

    return render(request, 'personlist.html', {
        'persons': persons, 
        'sort_by': sort_by, 
        'order': order
    })
def delete_all(request):
    # Delete all records from the Person model
    Person.objects.all().delete()


# Create your views here.
