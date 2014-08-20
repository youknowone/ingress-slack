
import json
import requests
import _secret

HOOK_URL = 'https://irk.slack.com/services/hooks/incoming-webhook?token=' + _secret.INCOMING_HOOK_TOKEN

class Bot(object):
    def __init__(self, chan='#general', username='irk-bot', emoji=':ghost:'):
        self.payload = {'channel': chan, 'username': username, 'emoji': emoji}

    def send(self, *texts):
        self.payload['text'] = ' '.join(texts)
        return requests.post(HOOK_URL, data={'payload': json.dumps(self.payload)})


