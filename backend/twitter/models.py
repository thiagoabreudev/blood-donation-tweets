from django.db import models
from django.contrib.postgres.fields import JSONField
from enum import Enum


class CategoryTwitte(Enum):
  ASK_DONATION = 'Pedindo doação'
  DONATED_BLOOD = 'Doou sangue'
  INTENTION_TO_BLOOD_DONATION = 'Tem intenção de doar'
  INVALID = "Inválido"


  def __str__(self):
    return self.name

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
  category = models.CharField(verbose_name='Category', null=True, blank=True, max_length=255, choices=((x.name, x.value) for x in CategoryTwitte))

  @property
  def link_twitte(self):
      return "https://twitter.com/{screen_name}/status/{id_twitte}".format(screen_name=self.screen_name,
                                                                        id_twitte=self.id_twitte)

  class Meta:
      ordering = ['-created_at']
