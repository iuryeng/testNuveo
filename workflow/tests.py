import mock
from django.db import models
from django.test import TestCase
from workflow.models import Workflow



class TestWorkflow(TestCase):

    def test_field_uuid(self):
        field = Workflow._meta.get_field('UUID')
        self.assertTrue(isinstance(field, models.UUIDField))
        self.assertTrue(field.primary_key)

    def test_uuid_is_unique(self):
        unique = Workflow._meta.get_field('UUID').unique
        self.assertEquals(unique, True)


    def test_field_updated_at(self):
        field = Workflow._meta.get_field('data')
        self.assertTrue(isinstance(field, models.JSONField))




