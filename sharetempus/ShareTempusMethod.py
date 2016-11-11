import requests;
import json;
from functools import partial;
import argparse as ap;
from .settings import *;

DEFAULT_HOST = "http://api.sharetempus.com/v1";

class ShareTempusMethod:
    def __init__(self, methods):
        for method in methods:
            self[method] = partial(self.method, methods[method]);

    def method(self, *args):

        spec = ap.Namespace(**args[0]);
        try:
            body = args[1];
        except IndexError:
            body = {};

        if hasattr(spec, 'params'):
            for param in spec.params:
                if body and hasattr(ap.Namespace(**body), param):
                    spec.path = spec.path.replace("{" + param + "}", body[param]);

        req = requests.request(
            spec.method,
            DEFAULT_HOST + spec.path,
            auth=(getKey(), ''),
            data=json.dumps(body),
            headers={'content-type': 'application/json'});

        return json.loads(req.text);
