from django.db import models

class Form(models.Model):
    """
    Job Application Form Model
    Stores applicant information
    """
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    email = models.EmailField()
    date = models.DateField()
    occupation = models.CharField(max_length=80)
    
    def __str__(self):
        """
        String representation of the model
        Displays in admin panel
        """
        return f"{self.first_name} {self.last_name}"