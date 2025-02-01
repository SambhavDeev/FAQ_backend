from django.db import models
from googletrans import Translator

class FAQ(models.Model):
    # Fields for storing questions and answers in multiple languages
    question = models.TextField()
    answer = models.TextField()  # Will use CKEditor for rich text
    question_hi = models.TextField(blank=True, null=True)  # Hindi translation
    question_bn = models.TextField(blank=True, null=True)  # Bengali translation
    answer_hi = models.TextField(blank=True, null=True)
    answer_bn = models.TextField(blank=True, null=True)

    def get_translated_question(self, lang='en'):
        """
        Retrieve the translated question based on the language.
        Fallback to English if translation is unavailable.
        """
        if lang == 'hi':
            return self.question_hi or self.question
        elif lang == 'bn':
            return self.question_bn or self.question
        return self.question

    def get_translated_answer(self, lang='en'):
        """
        Retrieve the translated answer based on the language.
        Fallback to English if translation is unavailable.
        """
        if lang == 'hi':
            return self.answer_hi or self.answer
        elif lang == 'bn':
            return self.answer_bn or self.answer
        return self.answer

    def save(self, *args, **kwargs):
        """
        Override the save method to automatically translate fields
        if translations are not already provided.
        """
        translator = Translator()

        # Translate question if translations are missing
        if not self.question_hi:
            self.question_hi = translator.translate(self.question, dest='hi').text
        if not self.question_bn:
            self.question_bn = translator.translate(self.question, dest='bn').text

        # Translate answer if translations are missing
        if not self.answer_hi:
            self.answer_hi = translator.translate(self.answer, dest='hi').text
        if not self.answer_bn:
            self.answer_bn = translator.translate(self.answer, dest='bn').text

        # Call the superclass save method to save the object
        super().save(*args, **kwargs)