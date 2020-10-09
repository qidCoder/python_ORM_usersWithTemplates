from django.db import models

# Create your models here.
# Create a model called User following the ERD above
class User(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email_address = models.CharField(max_length = 255)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    # def __repr__(self):
    #     return "Title: {}".format(self.title)

    def __str__(self):
        return f"<User object: {self.first_name} (id: {self.id})>"


