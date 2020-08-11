import json
from rest_framework import status
from django.test import TestCase,Client
from django.urls import reverse
from ..models import Pass
from ..serializers import PassSerializer
client= Client()


class GetAllPassesTest(TestCase):
    """ Test module for GET all passes API """

    def setUp(self):
        self.umamahesh = Pass.objects.create(
            name='umamahesh', age=36, id_number=982434123411, address='Nellore',status='pending')
        self.kartheek = Pass.objects.create(
            name='kartheek', age=2, id_number=982434123413, address='Nellore',status='pending')
        self.geetha = Pass.objects.create(
            name='geetha', age=31, id_number=982434123412, address='Nellore', status='pending')
        self.valid_payload = {
            'name': 'Rakesh',
            'age': 24,
            'id_number': 123412345678,
            'address': 'Tirupati',
            'status': 'pending'
        }
        self.invalid_payload = {
            'name': '',
            'age': 24,
            'id_number': 123412345678,
            'address': 'Tirupati',
            'status': 'pending'
        }
        self.valid_update_payload = {
            'name': 'umamahesh',
            'age': 35,
            'id_number': 982434123411,
            'address': 'Tirupati',
            'status': 'issued'
        }
        self.invalid_update_payload = {
            'name': '',
            'age': 35,
            'id_number': 982434123411,
            'address': 'Tirupati',
            'status': 'issued'
        }

    def test_get_pending_passes(self):
        # get API response
        response = client.get(reverse('get_pending_pass'))
        # get data from db
        passes = Pass.objects.filter(status='pending')
        serializer = PassSerializer(passes, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_issued_passes(self):
        # get API response
        response = client.get(reverse('get_issued_pass'))
        # get data from db
        passes = Pass.objects.filter(status='issued')
        serializer = PassSerializer(passes, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_valid_single_pass(self):
        response=client.get(reverse('get_update_pass',kwargs={'pk':self.geetha.pk}))
        pas=Pass.objects.get(pk=self.geetha.pk)
        serializer = PassSerializer(pas)
        self.assertEqual(response.data,serializer.data)
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    def test_get_invalid_single_pass(self):
        response=client.get(reverse('get_update_pass',kwargs={'pk':30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_create_valid_pass(self):
        response = client.post(
            reverse('insert_pass_data'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_pass(self):
        response = client.post(
            reverse('insert_pass_data'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_valid_update_pass(self):
        response = client.put(
            reverse('get_update_pass', kwargs={'pk': self.umamahesh.pk}),
            data=json.dumps(self.valid_update_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_update_pass(self):
        response = client.put(
            reverse('get_update_pass', kwargs={'pk': self.umamahesh.pk}),
            data=json.dumps(self.invalid_payload),
            content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)