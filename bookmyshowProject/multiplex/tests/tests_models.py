from django.test import TestCase
from multiplex.models import State


class StateTest(TestCase):
    """ Test module for State model """

    def setUp(self):
        State.objects.create(name='Casper')
        State.objects.create(name='Muffin')

    def test_state_name(self):
        state_casper = State.objects.get(name='Casper')
        state_muffin = State.objects.get(name='Muffin')
        self.assertEqual(state_casper.__str__(), "Casper")
        self.assertEqual(state_muffin.__str__(), "Muffin")
