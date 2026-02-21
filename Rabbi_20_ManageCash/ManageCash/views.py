from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from ManageCash.models import *


def register_function(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        username_exists = CustomUserModel.objects.filter(username=username).exists()
        email_exists = CustomUserModel.objects.filter(email=email).exists()

        if username_exists:
            messages.error(request, "Username already exists!")
            return redirect("register")
        
        if email_exists:
            messages.error(request, "Email already exists!")
            return redirect("register")

        if password == confirm_password:
            user = CustomUserModel.objects.create_user(
                username=username,
                email=email,
                password=password,
            )
            messages.success(request, "Registration successful! Please login.")
            return redirect("login")
        else:
            messages.error(request, "Passwords do not match!")
            return redirect("register")

    return render(request, "register.html")


def login_function(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        # Try to authenticate with username first
        user = authenticate(username=username, password=password)
        
        # If username doesn't work, try email
        if not user:
            try:
                user_obj = CustomUserModel.objects.get(email=username)
                user = authenticate(username=user_obj.username, password=password)
            except CustomUserModel.DoesNotExist:
                user = None

        if user:
            login(request, user)
            return redirect("dashboard")
        else:
            messages.error(request, "Invalid username/email or password!")

    return render(request, "login.html")


def logout_function(request):
    logout(request)
    return redirect("login")


def dashboard_function(request):
    if not request.user.is_authenticated:
        return redirect("login")
    
    user = request.user
    cash_entries = AddCashModel.objects.filter(user=user).order_by('-datetime')
    expenses = ExpenseModel.objects.filter(user=user).order_by('-datetime')
    
    total_cash = sum(entry.amount for entry in cash_entries)
    total_expenses = sum(expense.amount for expense in expenses)
    balance = total_cash - total_expenses
    
    context = {
        'user': user,
        'cash_entries': cash_entries,
        'expenses': expenses,
        'total_cash': total_cash,
        'total_expenses': total_expenses,
        'balance': balance,
    }
    return render(request, "dashboard.html", context)


def add_cash_function(request):
    if not request.user.is_authenticated:
        return redirect("login")
    
    if request.method == "POST":
        source = request.POST.get("source")
        amount = request.POST.get("amount")
        description = request.POST.get("description")
        
        if source and amount:
            AddCashModel.objects.create(
                user=request.user,
                source=source,
                amount=amount,
                description=description
            )
            messages.success(request, "Cash added successfully!")
            return redirect("dashboard")
        else:
            messages.error(request, "Please fill in all required fields!")
    
    return render(request, "add_cash.html")


def add_expense_function(request):
    if not request.user.is_authenticated:
        return redirect("login")
    
    if request.method == "POST":
        description = request.POST.get("description")
        amount = request.POST.get("amount")
        
        if description and amount:
            ExpenseModel.objects.create(
                user=request.user,
                description=description,
                amount=amount
            )
            messages.success(request, "Expense added successfully!")
            return redirect("dashboard")
        else:
            messages.error(request, "Please fill in all required fields!")
    
    return render(request, "add_expense.html")


def profile_function(request):
    if not request.user.is_authenticated:
        return redirect("login")
    
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        
        user = request.user
        user.username = username
        user.email = email
        user.first_name = first_name
        user.last_name = last_name
        user.save()
        
        messages.success(request, "Profile updated successfully!")
        return redirect("profile")
    
    return render(request, "profile.html", {'user': request.user})


# Keep home_function for backward compatibility
def home_function(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
    return redirect("login")
