
import json
import requests
from settings import *
from _secret import *

HOOK_URL = INCOMING_HOOK_URL

class Bot(object):
    """An abstract bot API wrapper for slack.
    """
    def __init__(self, channel=DEFAULT_CHANNEL, username=DEFAULT_USERNAME, emoji=':ai:'):
        self.payload = {'channel': channel, 'username': username, 'emoji': emoji}

    def send(self, *texts, **kwargs):
        """Sends a message via incoming hook in `print` semantic of python."""
        payload = self.payload.copy()
        if 'channel' in kwargs:
            payload['channel'] = kwargs['channel']
        if 'username' in kwargs:
            payload['username'] = kwargs['username']
        payload['text'] = ' '.join(map(unicode, texts))
        return requests.post(HOOK_URL, data={'payload': json.dumps(payload)})

