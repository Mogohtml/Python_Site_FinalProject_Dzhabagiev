from django.forms import ModelForm

from core.models import Post, Clothes, RentalRequest, Transaction


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description', 'price', 'address', 'start_date', 'end_date', 'contact', 'clothes']

class ClothesForm(ModelForm):
    class Meta:
        model = Clothes
        fields = ['title', 'description', 'material', 'size', 'color', 'category']

class RentalRequestForm(ModelForm):
    class Meta:
        model = RentalRequest
        fields = ['start_date', 'end_date', 'quantity', 'comment', 'user', 'post']

class TransactionForm(ModelForm):
    class Meta:
        model = Transaction
        fields = ['date', 'cost', 'rental_period_start', 'rental_period_end', 'user', 'post']