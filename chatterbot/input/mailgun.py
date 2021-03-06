from __future__ import unicode_literals
from chatterbot.input import InputAdapter
from chatterbot.conversation import Statement
import requests
import datetime


class Mailgun(InputAdapter):

    def __init__(self, **kwargs):
        super(Mailgun, self).__init__(**kwargs)

        # Use the bot's name for the name of the sender
        self.name = kwargs.get('name')
        self.from_address = kwargs.get('mailgun_from_address')
        self.api_key = kwargs.get('mailgun_api_key')
        self.endpoint = kwargs.get('mailgun_api_endpoint')

    def get_email_stored_events(self):
        yesterday = datetime.datetime.now() - datetime.timedelta(1)
        return requests.get(
            '{}/events'.format(self.endpoint),
            auth=('api', self.api_key),
            params={
                'begin': yesterday.isoformat(),
                'ascending': 'yes',
                'limit': 1
            }
        )

    def get_stored_email_urls(self):
        response = self.get_email_stored_events()
        data = response.json()

        for item in data.get('items', []):
            if 'storage' in item:
                if 'url' in item['storage']:
                    yield item['storage']['url']

    def get_message(self, url):
        return requests.get(
            url,
            auth=('api', self.api_key)
        )

    def process_input(self, statement):
        urls = m.get_stored_email_urls()
        url = first(urls)

        response = self.get_message(url)
        message = response.json()

        text = message.get('stripped-text')

        return Statement(text)
