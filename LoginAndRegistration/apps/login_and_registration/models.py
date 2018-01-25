from __future__ import unicode_literals
from django.db import models
import re

EMAIL_REGEX = re.compile('^[_a-z0-9-]+(.[_a-z0-9-]+)@[a-z0-9-]+(.[a-z0-9-]+)(.[a-z]{2,4})$')
# EMAIL_REGEX = re.compile('\b[\w\.-]+@[\w\.-]+\.\w{2,4}\b')

class BlogManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['first_name']) == 0:
            errors['empty_first_name'] = 'First Name cannot be empty'
        if len(postData['last_name']) == 0:
            errors['empty_last_name'] = 'Last Name cannot be empty'
        if len(postData['email']) == 0:
            errors['empty_email'] = 'Email cannot be empty'
        if len(postData['password']) == 0:
            errors['empty_password'] = 'Password cannot be empty'
        if len(postData['password_confirmation']) == 0:
            errors['empty_password_confirmation'] = 'Password confirmation cannot be empty'
        if not re.match(r'^\w{2,}', postData['first_name']):
            errors['first_name'] = 'First Name should be more than two characters and only letters.'
        if not re.match(r'^\w{2,}', postData['last_name']):
            errors['last_name'] = 'Last Name should be more than two characters and only letters.'
        if not re.match(EMAIL_REGEX, postData['email']):
            errors['email'] = 'Email is not valid.'
        for user in User.objects.filter(email = postData['email']):
            if user:
                errors['repeated_email'] = 'The email already exists. Please use a different one.'
        if len(postData['password']) < 8:
            errors['password'] = 'Password needs to be at least 8 characters long.'
        if postData['password'] != postData['password_confirmation']:
            errors['password_confirmation'] = 'Passwords have to match.'

        return errors

class User(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    password = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = BlogManager()