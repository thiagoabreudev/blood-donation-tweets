from django.db import models
from django.contrib.postgres.fields import JSONField
# Create your models here.

class TwitterSettings(models.Model):
  consumer_key = models.CharField(max_length=255, verbose_name='Consumer Key')
  consumer_secret = models.CharField(max_length=255, verbose_name='Consumer secret')
  access_token = models.CharField(max_length=255, verbose_name='Access Token')
  access_token_secret = models.CharField(max_length=255, verbose_name='Access Token Secret')

  def __str__(self):
    return self.consumer_key

class TwitteSearchSetting(models.Model):
  key_to_search = models.CharField(verbose_name="Key to search", max_length=255)

  def __str__(self):
      return self.key_to_search


class Twitte(models.Model):
  created_at = models.DateTimeField(verbose_name="Create date", null=True, blank=True)
  id_twitte = models.CharField(verbose_name='ID twitte', max_length=255)
  text = models.TextField(verbose_name="Text")        
  screen_name = models.CharField(verbose_name="Usuário", max_length=255)        
  twitte_json = JSONField(null=True, blank=False, verbose_name='Twitte Json')
  ask_donation = models.BooleanField(verbose_name='Ask Donation', default=False)
  donated_blood = models.BooleanField(verbose_name='Donated blood', default=False)
  intention_to_blood_donation = models.BooleanField(verbose_name='Intentio to blood donation', default=False)
  invalid = models.BooleanField(verbose_name='Invalid', default=False)
  checked = models.BooleanField(verbose_name='Checked', default=False)

  @property
  def link_twitte(self):
      return "https://twitter.com/{screen_name}/status/{id_twitte}".format(screen_name=self.screen_name,
                                                                        id_twitte=self.id_twitte)

  def save(self, *args, **kwargs):    
    checks = [
      self.ask_donation, self.donated_blood, self.intention_to_blood_donation, 
      self.invalid
    ]
    if any(checks):
      self.checked = True
    else: 
      self.checked = False
    super().save(*args, **kwargs)

  class Meta:
      ordering = ['-created_at']
