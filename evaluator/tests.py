from django.test import TestCase, Client
from .models import Company, User
from django.urls import reverse
# Create your tests here.

class CompanyModelTests(TestCase):

    def test_recommend_companies(self):
        # run server: python manage.py runserver
        # run tests: python manage.py test evaluator
        # line coverage: 
        #           1- coverage run --source='.' manage.py test evaluator
        #           2- coverage report
        data = {
            "FOI": "CS",
            "Score": "90",
        }
        response = self.client.post('/evaluator/recommend/', data, content_type='application/json')
        print(response)
        self.assertEqual(response.status_code, 200)

    
    def test_recommend_users(self):
        data = {
            "Open_field": "CS",
            "min_score": "80",
        }
        response = self.client.post('/evaluator/recommendUsers/', data, content_type='application/json')
        print(response)
        self.assertEqual(response.status_code, 200)