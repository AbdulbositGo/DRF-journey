import random
from django.test import TestCase
from django.urls import reverse

from .models import User, Order


class UserorderTestCase(TestCase):
    def setUp(self):
        user1 = User.objects.create_user(username="user1", password="test")
        user2 = User.objects.create_user(username="user2", password="test")
        
        for _ in range(10):
            Order.objects.create(user=random.choice([user1, user2]))

    # Test user order endpoint retrieves only authenticated user orders
    def test_user_order(self):
        user1 = User.objects.get(username="user1")
        self.client.force_login(user1)
        response = self.client.get(reverse('api:user-orders'))
        
        assert response.status_code == 200
        orders = response.json()
        
        self.assertTrue(all([order['user'] == user1.username for order in orders]))
        
        
    def test_user_order_unauthenticated(self):
        response = self.client.get(reverse('api:user-orders'))
        self.assertEqual(response.status_code, 403)