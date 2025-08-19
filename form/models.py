from django.db import models

# Create your models here.

class FormSubmission(models.Model): 
    submission_id = models.AutoField(primary_key=True)
    time = models.DateTimeField()
    mood = models.CharField(max_length=20)
    productivity = models.TextField()
    accomplishment = models.TextField()
    stress = models.TextField()

    def __str__(self): 
        return (str(self.submission_id) + ": " + str(self.time) + ", " + self.mood + ", " + self.productivity + ", " + self.accomplishment + ", " + self.stress)

class User(models.Model): 
    username = models.CharField(max_length=30)
    form_submissions = models.ManyToManyField(FormSubmission, blank=True)

    def __str__(self): 
        return (str(self.username))