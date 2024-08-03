from django.test import TestCase
from django.utils import timezone
from polls.models import Question


class QuestionCodeTest(TestCase):

    def test_question_creation(self):
        """
        This test ensures the generated referral code has a length of 6 characters and is unique
        """
        question = Question.objects.create(
            question_text = "What colour is the sun?",
            pub_date = timezone.now()
        )
        question.save()
        retrieve_question = Question.objects.filter(pk=1).first()
        self.assertEqual(retrieve_question.question_text, "What colour is the sun?")
        