from django.test import TestCase
from .models import Profile,Post,Comment,Following

class FollowingTestClass(TestCase):
    def setUp(self):
        self.esther=Following(username='esther',followed='john')
                            
    def test_instance(self):
        self.assertTrue(isinstance(self.esther,Following))

class CommentTestClass(TestCase):
    def setUp(self):
        self.first=Comment(post=1,
                            username='esther',
                            comment='Epic performance',
                            date='May 24, 2019, 12:41 a.m.',
                            count=0)

    def test_instance(self):
        self.assertTrue(isinstance(self.first,Comment))