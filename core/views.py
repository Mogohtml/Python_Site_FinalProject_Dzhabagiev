from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404

from .forms import PostForm, ClothesForm, RentalRequestForm, TransactionForm, RegistrationForm
from .models import Post, Clothes, RentalRequest, Transaction

def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(request, email=email, password=raw_password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Registration successful.')
                return redirect('home')
            else:
                messages.error(request, 'Authentication failed.')
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {"form": form})

def user_login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful.')
            return redirect('home')
        else:
            messages.error(request, 'Invalid login credentials.')
    return render(request, 'registration/login.html')

def user_logout(request):
    logout(request)
    return redirect('home')


# Views for Clothes model
def clothes_list(request):
    clothes = Clothes.objects.all()
    return render(request, 'clothes/clothes_list.html', {'clothes': clothes})

def clothes_detail(request, pk):
    clothes = get_object_or_404(Clothes, pk=pk)
    return render(request, 'clothes/clothes_detail.html', {'clothes': clothes})

def create_clothes(request):
    if request.method == 'POST':
        form = ClothesForm(request.POST)
        if form.is_valid():
            clothes = form.save()
            return redirect('clothes/clothes_detail', pk=clothes.pk)
    else:
        form = ClothesForm()
    return render(request, 'clothes/create_clothes.html', {'form': form})


# Views for Post model
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'posts/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'posts/post_detail.html', {'post': post})

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect('posts/post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'posts/create_post.html', {'form': form})

def approve_post(request):
    posts = Post.objects.filter(is_approved=True)
    if request.method == 'POST':
        for post in posts:
            if str(post.pk) not in request.POST:
                post.is_approved = True
                post.save()
        return redirect('home')
    return render(request, 'posts/approve_post.html', {'posts': posts})



# Views for RentalRequest model
def rental_list(request):
    rentals = RentalRequest.objects.all()
    return render(request, 'rentals/rental_list.html', {'rentals': rentals})

def rental_detail(request, pk):
    rental = get_object_or_404(RentalRequest, pk=pk)
    return render(request, 'rentals/rental_detail.html', {'rental': rental})

def create_rental(request):
    if request.method == 'POST':
        form = RentalRequestForm(request.POST)
        if form.is_valid():
            rental = form.save()
            return redirect('rentals/rental_detail', pk=rental.pk)
    else:
        form = RentalRequestForm()
    return render(request, 'rentals/create_rental.html', {'form': form})


# Views for Transaction model
def transaction_list(request):
    transactions = Transaction.objects.all()
    return render(request, 'transactions/transaction_list.html', {'transactions': transactions})

def transaction_detail(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk)
    return render(request, 'transactions/transaction_detail.html', {'transaction': transaction})

def create_transaction(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save()
            return redirect('transactions/transaction_detail', pk=transaction.pk)
    else:
        form = TransactionForm()
    return render(request, 'transactions/create_transaction.html', {'form': form})