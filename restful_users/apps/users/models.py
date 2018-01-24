from __future__ import unicode_literals
from django.db import models
import re

EMAIL_REGEX = re.compile('^[_a-z0-9-]+(.[_a-z0-9-]+)@[a-z0-9-]+(.[a-z0-9-]+)(.[a-z]{2,4})$')

class BlogManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 5:
            errors['first_name'] = 'First Name should be more than five characters.'
        if len(postData['last_name']) < 5:
            errors['last_name'] = 'Last Name should be more than five characters.'
        # if not EMAIL_REGEX.match(postData['email']):
        #     errors['email'] = 'Email is not valid.'
        if not re.match(EMAIL_REGEX, postData['email']):
            errors['email'] = 'Email is not valid.'
            
        return errors

class User(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    objects = BlogManager()
