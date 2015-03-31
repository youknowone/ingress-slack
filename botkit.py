
import config
import json
import requests
from config import *
from _secret import *

HOOK_URL = INCOMING_HOOK_URL

class Bot(object):
    """An abstract bot API wrapper for slack.
    """
    def __init__(self, chan=DEFAULT_CHANNEL, username=DEFAULT_USERNAME, emoji=DEFAULT_EMOJI):
        self.payload = {'channel': chan, 'username': username, 'emoji': emoji}

    def send(self, *texts):
        """Sends a message via incoming hook in `print` semantic of python."""
        self.payload['text'] = ' '.join(map(unicode, texts))
        return requests.post(HOOK_URL, data={'payload': json.dumps(self.payload)})


