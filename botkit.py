
import config
import json
import requests
import _secret

HOOK_URL = 'https://irk.slack.com/services/hooks/incoming-webhook?token=' + _secret.INCOMING_HOOK_TOKEN

class Bot(object):
    """An abstract bot API wrapper for slack.
    """
    def __init__(self, chan=config.DEFAULT_CHANNEL, username=config.DEFAULT_USERNAME, emoji=config.DEFAULT_EMOJI):
        self.payload = {'channel': chan, 'username': username, 'emoji': emoji}

    def send(self, *texts):
        """Sends a message via incoming hook in `print` semantic of python."""
        self.payload['text'] = ' '.join(map(str, texts))
        return requests.post(HOOK_URL, data={'payload': json.dumps(self.payload)})


