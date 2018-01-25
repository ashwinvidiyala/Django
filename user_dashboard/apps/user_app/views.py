from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
import bcrypt
from models import *

def index(request):
    return render(request, 'user_app/index.html')

def login_page(request):
    return render(request, 'user_app/login.html')

def register_page(request):
    return render(request, 'user_app/register.html')

# def dashboard(request):
#     return render(request, 'user_app/dashboard.html')

def users_new(request):
    return render(request, 'user_app/users_new.html')

def users_homepage(request, id):
    user = User.objects.filter(id = id)
    for user in user:
        context = {
            'first_name': user.first_name,
            'last_name': user.last_name,
            'id': user.id,
            'email': user.email,
            'description': user.description,
            'user_level': user.user_level,
            'created_at': user.created_at,
        }

    return render(request, 'user_app/users_homepage.html', context)

def register(request):
    if request.POST['submit'] == 'Register':
        errors = User.objects.basic_validator(request.POST)
        if len(errors):
            for tag, error in errors.iteritems():
                messages.error(request, error, extra_tags = tag)
            return redirect('/register')

        password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        user = User.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], email = request.POST['email'], password = password)
        return redirect('/users/show/'+str(user.id))

def login(request):
    if request.POST['submit'] == 'Login':
        user = User.objects.filter(email = request.POST['email'])
        if not user:
            messages.add_message(request, messages.INFO, 'User does not exist')
            return redirect('/login')
        else:
            for user in user:
                user_password = user.password
            if bcrypt.checkpw(request.POST['password'].encode(), user_password.encode()):
                context = {
                    'name': user.first_name,
                    'status': 'logged in',
                    'email_error': 'User does not exist'
                }
                if 'login_status' not in request.session:
                    request.session['login_status'] = 1
                else:
                    request.session['login_status'] = 1
                return redirect('/users/show/'+str(user.id))
            else:
                messages.add_message(request, messages.INFO, 'Password is incorrect')
                return redirect('/login')

def logout(request):
    request.session['login_status'] = 0
