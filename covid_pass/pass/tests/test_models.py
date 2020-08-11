from django.test import TestCase
from ..models import Pass


class PassTest(TestCase):
    """ Test module for Pass model """

    def setUp(self):
        Pass.objects.create(
            name='Mahesh', age=36, id_number=918212342344, address='Nellore', status='pending')
        Pass.objects.create(
            name='Geetha', age=31, id_number=918212342346, address='Nellore', status='pending')

    def test_pass_status(self):
        pass_mahesh = Pass.objects.get(name='Mahesh')
        pass_geetha = Pass.objects.get(name='Geetha')
        self.assertEqual(
            pass_mahesh.get_pass(), "Mahesh")
        self.assertEqual(
            pass_geetha.get_pass(), "Geetha")