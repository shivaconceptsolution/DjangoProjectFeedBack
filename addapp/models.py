from django.db import models

class Register(models.Model):
  emailid= models.CharField(max_length=200)
  password= models.CharField(max_length=200)
  mobile= models.CharField(max_length=200)
  fullname= models.CharField(max_length=200)
  def __str__(self):
  	return "emailid is "+self.emailid +" password is "+self.password +" mobile is "+self.mobile+" fullname is "+self.fullname
class Feedback(models.Model):
  feedby= models.CharField(max_length=200)
  feedto= models.CharField(max_length=200)
  feeddesc= models.CharField(max_length=200)
  feedbackrate= models.IntegerField()
  def __str__(self):
  	return "feedby  "+self.feedby+" feed to "+self.feedto +" desc "+self.feeddesc+" Rating is "+str(self.feedbackrate)
class Faculty(models.Model):
  emailid= models.CharField(max_length=200)
  password= models.CharField(max_length=200)
  mobile= models.CharField(max_length=200)
  fullname= models.CharField(max_length=200)
  deptname= models.CharField(max_length=200)
  def __str__(self):
    return "emailid is "+self.emailid +" password is "+self.password +" mobile is "+self.mobile+" fullname is "+self.fullname + "deptname is "+self.deptname