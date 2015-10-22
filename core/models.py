from django.db import models

title_options = (
(0, ''),
(1, 'Mr'),
(2, 'Ms'),
(3, 'Mrs'),
(4, 'Dr'),
(5, 'Seniora'),
(6, 'Senior'),
)

# Create your models here.
class Question(models.Model):
  title = models.IntegerField(choices=title_options, default=0)
  name = models.CharField(max_length=300)
  email = models.EmailField(max_length=254, blank=False, null= True, unique= False)
  message = models.TextField(null=True, blank=True)
  created_at = models.DateTimeField(auto_now_add=True)

  def __unicode__(self):
      return self.name
