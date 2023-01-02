from django.db import models

# Create your models here.

class contactform(models.Model):
    name = models.CharField(max_length=100, blank=False)
    email = models.CharField(max_length=100, blank=False)
    subject = models.CharField(max_length=400, blank=False)
    message = models.TextField(max_length=800, blank=False)
    
    def __str__(self):
        return self.subject
    
class QuesModel(models.Model):
    question = models.CharField(max_length=200,null=True)
    op1 = models.CharField(max_length=200,null=True)
    op2 = models.CharField(max_length=200,null=True)
    op3 = models.CharField(max_length=200,null=True)
    op4 = models.CharField(max_length=200,null=True)
    ans = models.CharField(max_length=200,null=True)
    
    class Meta:
        db_table = "Quiz_One_Questions"
    
    
    def __str__(self):
        return self.question
    


class QuesModelTwo(models.Model):
    question = models.CharField(max_length=200, blank=False)
    op1 = models.CharField(max_length=200, blank=False)
    op2 = models.CharField(max_length=200, blank=False)
    op3 = models.CharField(max_length=200, blank=False)
    op4 = models.CharField(max_length=200, blank=False)
    ans = models.CharField(max_length=200, blank=False)
    
    class Meta:
        db_table = "Quiz_Two_Questions"

    def __str__(self):
        return self.question
    



