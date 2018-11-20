import json

from django.test import TestCase, Client
from django.urls import reverse

from rest_framework import status

from apps.home.models import Checkmarks
from apps.home.serializers import CheckmarksSerializer


# initialize the APIClient app
client = Client()


class CheckmarksTest(TestCase):
    """ Test module for Checkmarks model """

    def setUp(self):
        Checkmarks.objects.create(name='one', value=True)        

    def test_checkmark_str(self):
        checkmark_one = Checkmarks.objects.get(name='one')
        self.assertEqual(
            str(checkmark_one), "one")


class GetAllCheckmarksTest(TestCase):
    """ Test module for GET all checkmarks API """

    def setUp(self):
        Checkmarks.objects.create(name='one', value=True)
        Checkmarks.objects.create(name='two', value=False)

    def test_get_all_checkmarks(self):
        # get API response
        response = client.get(reverse('checkmarks-list'))
        # get data from db
        checkmarks = Checkmarks.objects.all()
        serializer = CheckmarksSerializer(checkmarks, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class CreateNewCheckmarksTest(TestCase):
    """ Test module for inserting a new checkmark """

    def setUp(self):
        self.valid_payload = {
            'name': 'one',
            'value': True
        }
        self.invalid_payload = {
            'name': 'one',
            'value': 'invalid value'
        }

    def test_create_valid_checkmark(self):
        response = client.post(
            reverse('checkmarks-list'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_checkmark(self):
        response = client.post(
            reverse('checkmarks-list'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class GetSingleCheckmarksTest(TestCase):
    """ Test module for GET single checkmark API """

    def setUp(self):
        self.one = Checkmarks.objects.create(name='one', value=True)
        self.two = Checkmarks.objects.create(name='two', value=False)

    def test_get_valid_single_checkmark(self):
        response = client.get(
            reverse('checkmarks-detail', kwargs={'pk': self.one.pk}))
        checkmark = Checkmarks.objects.get(pk=self.one.pk)
        
        serializer = CheckmarksSerializer(checkmark)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_get_invalid_single_checkmark(self):
        response = client.get(
            reverse('checkmarks-detail', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class UpdateSingleCheckmarksTest(TestCase):
    """ Test module for updating an existing checkmark record """

    def setUp(self):
        self.one = Checkmarks.objects.create(name='one', value=True)
        self.two = Checkmarks.objects.create(name='two', value=False)
        self.valid_payload = {
            'name': 'one',
            'value': True
        }
        self.invalid_payload = {
            'name': 'one',
            'value': 'invalid value'
        }

    def test_valid_update_checkmark(self):
        response = client.put(
            reverse('checkmarks-detail', kwargs={'pk': self.one.pk}),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_update_checkmark(self):
        response = client.put(
            reverse('checkmarks-detail', kwargs={'pk': self.two.pk}),
            data=json.dumps(self.invalid_payload),
            content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
        
class DeleteSingleCheckmarksTest(TestCase):
    """ Test module for deleting an existing checkmark record """

    def setUp(self):
        self.one = Checkmarks.objects.create(name='one', value=True)
        self.two = Checkmarks.objects.create(name='two', value=False)

    def test_valid_delete_checkmark(self):
        response = client.delete(
            reverse('checkmarks-detail', kwargs={'pk': self.one.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_checkmark(self):
        response = client.delete(
            reverse('checkmarks-detail', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
