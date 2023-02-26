from django.db import models

class Prov_Questions(models.Model):
    question = models.CharField(max_length=300)    
    Q_Image = models.ImageField(upload_to='images/')
    answer = models.CharField(max_length=100)
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.question

class Answers(models.Model):
    toQuestion = models.ForeignKey(Prov_Questions, on_delete = models.CASCADE)  
    choice_one = models.CharField(max_length=100)  
    choice_two = models.CharField(max_length=100)
    choice_three = models.CharField(max_length=100)
    
