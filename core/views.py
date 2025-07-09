from django.shortcuts import render, redirect, get_object_or_404

from .forms import PostForm, ClothesForm, RentalRequestForm, TransactionForm
from .models import Post, Clothes, RentalRequest, Transaction


# Views for Post model
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'posts/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'posts/post_detail.html', {'post': post})

def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect('posts/post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'posts/create_post.html', {'form': form})


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