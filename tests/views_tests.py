import unittest
from django.test import TestCase
from users.models import User
from django.utils import timezone
from core.models import Post, Clothes, Category, Size, RentalRequest, Transaction
from core.forms import PostForm, ClothesForm, RentalRequestForm, TransactionForm
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
import logging

# Настройка логгера
logging.basicConfig(filename='tests.log', level=logging.DEBUG)


class BaseTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email='test@example.com',
            password='testpass123'
        )
        self.category = Category.objects.create(
            title='Test Category',
            description='Test Description'
        )
        self.size = Size.objects.create(size='M')
        self.clothes = Clothes.objects.create(
            title='Test Clothes',
            description='Test Description',
            material='Test Material',
            size=self.size,
            color='Red'
        )
        self.clothes.category.add(self.category)

        self.post = Post.objects.create(
            title='Test Post',
            description='Test Description',
            price=100.00,
            address='Test Address',
            start_date=timezone.now(),
            end_date=timezone.now() + timezone.timedelta(days=7),
            contact=self.user
        )
        self.post.clothes.add(self.clothes)


class TestAddPostToDatabase(BaseTestCase):
    def test_add_post(self):
        post_data = {
            'title': 'New Post',
            'description': 'New Description',
            'price': 50.00,
            'address': 'New Address',
            'start_date': timezone.now(),
            'end_date': timezone.now() + timezone.timedelta(days=5),
            'contact': self.user.pk,
            'clothes': [self.clothes.pk]
        }

        response = self.client.post(reverse('create_post'), post_data)
        self.assertEqual(response.status_code, 302)  # Проверяем редирект после успешного создания
        self.assertTrue(Post.objects.filter(title='New Post').exists())
        logging.info("Post creation test passed")


class TestClothesViews(BaseTestCase):
    def test_clothes_list_view(self):
        response = self.client.get(reverse('clothes_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Clothes')

    def test_clothes_detail_view(self):
        response = self.client.get(reverse('clothes_detail', args=[self.clothes.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.clothes.title)


class TestPostViews(BaseTestCase):
    def test_post_list_view(self):
        response = self.client.get(reverse('post_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.post.title)

    def test_post_detail_view(self):
        response = self.client.get(reverse('post_detail', args=[self.post.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.post.description)


class TestRentalRequestViews(BaseTestCase):
    def test_create_rental_request(self):
        rental_data = {
            'start_date': timezone.now(),
            'end_date': timezone.now() + timezone.timedelta(days=3),
            'quantity': 1,
            'comment': 'Test comment',
            'user': self.user.pk,
            'post': self.post.pk
        }

        form = RentalRequestForm(data=rental_data)
        self.assertTrue(form.is_valid())

        response = self.client.post(reverse('create_rental'), rental_data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(RentalRequest.objects.filter(post=self.post).exists())


class TestTransactionViews(BaseTestCase):
    def test_create_transaction(self):
        transaction_data = {
            'cost': 100.00,
            'rental_period_start': timezone.now(),
            'rental_period_end': timezone.now() + timezone.timedelta(days=7),
            'user': self.user.pk,
            'post': self.post.pk
        }

        form = TransactionForm(data=transaction_data)
        self.assertTrue(form.is_valid())

        response = self.client.post(reverse('create_transaction'), transaction_data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Transaction.objects.filter(post=self.post).exists())


class TestFormValidation(TestCase):
    def test_invalid_post_form(self):
        form_data = {'title': ''}  # Неполные данные
        form = PostForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_invalid_clothes_form(self):
        form_data = {'title': '', 'price': -10}  # Неполные и неверные данные
        form = ClothesForm(data=form_data)
        self.assertFalse(form.is_valid())


class TestAuthenticationViews(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email='authuser@example.com',
            password='testpass123'
        )

    def test_login_view(self):
        response = self.client.post(reverse('login'), {
            'email': 'authuser@example.com',
            'password': 'testpass123'
        })
        self.assertEqual(response.status_code, 302)  # Проверяем редирект после успешного входа

    def test_register_view(self):
        response = self.client.post(reverse('register'), {
            'email': 'newuser@example.com',
            'password1': 'complexpass123',
            'password2': 'complexpass123'
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(email='newuser@example.com').exists())


if __name__ == '__main__':
    unittest.main()
