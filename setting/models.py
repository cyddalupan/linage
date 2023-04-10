from django.db import models
from django.forms import DateField, DateInput, ModelForm
from django import forms

class Setting(models.Model):
  user_id = models.IntegerField()
  firstname = models.CharField(max_length=255)
  middlename = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  birthday = models.DateField(null=True, blank=True)
  parent_id = models.IntegerField()

  def __str__(self):
    return self.firstname + " " + self.middlename + " " + self.lastname


class SettingForm(ModelForm):
    class Meta:
        model = Setting
        fields = ["firstname", "middlename", "lastname", "birthday"]
        widgets = {
            'birthday': DateInput(attrs={'type': 'date'})
        }