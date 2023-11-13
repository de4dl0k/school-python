from django.contrib import messages, auth
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate


def index(request):
    return render(request, 'index.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'invalid credentials')
            return redirect('login')
    return render(request, "login.html")


# def login(request):
#     if request.method == 'POST':
#         # Handle login form submission
#         username = request.POST['usernames']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             # Redirect to a different page after successful login
#             return redirect()  # 'dashboard' is the name of the URL pattern for the dashboard page
#         else:
#             messages.error(request, 'Invalid username or password.')
#
#     # Render the login page template
#     return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')


def form_page(request):
    return render(request, 'form.html')


def submit_form(request):
    if request.method == 'POST':

        name = request.POST.get('name')
        dob = request.POST.get('dob')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        address = request.POST.get('address')
        department = request.POST.get('department')
        course = request.POST.get('course')
        purpose = request.POST.get('purpose')
        materials = request.POST.getlist('materials')
        return render(request, 'success.html')

    return render(request, 'form.html')


def submit_form(request):
    if request.method == 'POST':
        message = "Order Confirmed"
        return render(request, 'confirmation.html', {'message': message})

    return HttpResponse("Invalid request method. Use POST.")
