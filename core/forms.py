from django.contrib.auth.forms import UserCreationForm

from django.forms import ModelForm
from django import forms
from core.models import Post, Clothes, RentalRequest, Transaction
from users.models import User


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('email',
                  'password1',
                  'password2'
                  )
    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']

        if commit:
            user.save()
        return user

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description', 'image', 'price', 'address', 'start_date', 'end_date', 'user', 'clothes']

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
        fields = ['cost', 'rental_period_start', 'rental_period_end', 'user', 'post']