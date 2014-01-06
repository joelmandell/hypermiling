from django.test import TestCase
from forum.models import Subject
from django.contrib.auth.models import User
from django.utils import timezone

class ForumTest(TestCase):
  def setUp(self):
    Subject.objects.create(dateModified=timezone.now(),subjectTitle="This is a test subject",subjectDescription="This is a description")
    
  def testCreationOfSubject(self):
    subject = Subject.objects.get(id=1)
    #Should return 1 = created subject success!
    self.assertEqual(subject.id,1)
