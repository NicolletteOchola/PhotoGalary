from django.db import models

# Create your models here.
class Location(self):

  location = models.CharField(max_length=255, blank =True)

  def save_location(self):
    self.save()

  def delete_location(self):
    self.delete()

  @classmethod
  def get_location(cls):
    locations = cls.objects.all()
    return locations

  def __str__(self):
    return self.location

  class Meta:
    verbose_name = 'Location'
    verbose_name_plural = 'Locations'

