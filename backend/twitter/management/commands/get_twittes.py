from django.core.management.base import BaseCommand
import json
import oauth2 as oauth
import time

class Command(BaseCommand):
    help = 'Get twittes'

    def get_twittes(self):
        from twitter.models import Twitte, TwitteSearchSetting, TwitterSettings
        consumer_settings = TwitterSettings.objects.latest('pk')
        consumer = oauth.Consumer(
            key=consumer_settings.consumer_key, secret=consumer_settings.consumer_secret)
        access_token = oauth.Token(key=consumer_settings.access_token, secret=consumer_settings.access_token_secret)
        client = oauth.Client(consumer, access_token)
        for search_settings in TwitteSearchSetting.objects.all():
            endpoint = "https://api.twitter.com/1.1/search/tweets.json?q={0}".format(search_settings.key_to_search)
            response, data = client.request(endpoint)
            tweets = json.loads(data.decode('utf-8'))
            for twitte in tweets.get('statuses'):
                if twitte.get('text')[0:2] != 'RT' and not Twitte.objects.filter(id_twitte=twitte.get('id_str')).exists():
                    new_twitte = Twitte()
                    new_twitte.twitte_json = twitte
                    new_twitte.id_twitte = twitte.get('id_str')
                    new_twitte.text = twitte.get('text')
                    new_twitte.screen_name = twitte.get('user').get('screen_name')
                    new_twitte.retweeted = twitte.get('retweeted')
                    new_twitte.created_at = time.strftime('%Y-%m-%d %H:%M:%S',
                                                          time.strptime(twitte['created_at'], '%a %b %d %H:%M:%S +0000 %Y'))
                    new_twitte.save()

    def handle(self, *args, **options):
        self.get_twittes()
