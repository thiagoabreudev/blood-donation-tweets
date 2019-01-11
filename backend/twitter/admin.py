from django.contrib import admin
from .models import Twitte, TwitteSearchSetting, TwitterSettings
from django.utils.safestring import mark_safe

# Register your models here.


@admin.register(TwitterSettings)
class TwitterSettingsAdmin(admin.ModelAdmin):
	pass

@admin.register(TwitteSearchSetting)
class TwitteSearchSettingAdmin(admin.ModelAdmin):
	pass

@admin.register(Twitte)
class TwitteAdmin(admin.ModelAdmin):
    list_display = ['created_at', 'screen_name', 'text', 'ask_donation', 
    'donated_blood', 'intention_to_blood_donation', 'invalid', 'checked', 'show_link_twitte_url']
    search_fields = ['text', 'screen_name']
    list_editable = ['ask_donation', 'donated_blood', 'intention_to_blood_donation', 'invalid']

    def show_link_twitte_url(self, obj):
        return mark_safe('<a href="%s" target="_blank">%s</a>' % (obj.link_twitte, obj.link_twitte))

    show_link_twitte_url.allow_tags = True
