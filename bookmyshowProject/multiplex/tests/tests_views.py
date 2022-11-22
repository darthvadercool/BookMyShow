
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
import json


from ..models import State
from ..serializers import StateSerializer


client = Client()


class GetAllStatesTest(TestCase):
    """ Test module for GET all states API """

    def setUp(self):
        State.objects.create(name='UP')
        State.objects.create(name='Karnataka')
        State.objects.create(name='Delhi')
        State.objects.create(name='kashmir')

    def test_get_all_states(self):

        response = client.get(reverse('get_all_states'))
        states = State.objects.all()
        serializer = StateSerializer(states, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetSingleStateTest(TestCase):
    """ Test module for GET single state API """

    def setUp(self):
        self.state1 = State.objects.create(name='Delhi')
        self.state2 = State.objects.create(name='UP')
        self.state3 = State.objects.create(name='Karnataka')
        self.state4 = State.objects.create(name='kashmir')

    def test_get_valid_single_state(self):

        response = client.get(
            reverse('get_delete_update_state', kwargs={'pk': self.state1.id}))
        state = State.objects.get(pk=self.state1.id)
        serializer = StateSerializer(state)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_state(self):
        response = client.get(
            reverse('get_delete_update_state', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class CreateNewStateTest(TestCase):
    """ Test module for inserting a new state """

    def setUp(self):
        self.valid_payload = {
            'name': 'Tamil Nadu',

        }

        self.invalid_payload = {
            'name': '',

        }

    def test_create_valid_state(self):
        response = client.post(
            reverse('get_all_states'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_state(self):
        response = client.post(
            reverse('get_all_states'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class UpdateSingleStateTest(TestCase):
    """ Test module for updating an existing state record """

    def setUp(self):
        self.state1 = State.objects.create(name='Delhi')
        self.state2 = State.objects.create(name='UP')
        self.valid_payload = {
            'name': 'Delhi updated',

        }

        self.invalid_payload = {
            'name': '',

        }

    def test_valid_update_state(self):
        response = client.put(
            reverse('get_delete_update_state', kwargs={'pk': self.state1.id}),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_update_statetate(self):
        response = client.put(
            reverse('get_delete_update_state', kwargs={'pk': self.state2.id}),
            data=json.dumps(self.invalid_payload),
            content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class DeleteSingleSatteTest(TestCase):
    """ Test module for deleting an existing state record """

    def setUp(self):
        self.state1 = State.objects.create(name='Delhi')
        self.state2 = State.objects.create(name='UP')

    def test_valid_delete_puppy(self):
        response = client.delete(
            reverse('get_delete_update_state', kwargs={'pk': self.state1.id}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_puppy(self):
        response = client.delete(
            reverse('get_delete_update_state', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
