from .ShareTempusMethod import ShareTempusMethod

class Events(ShareTempusMethod):
    def __init__(self):
        ShareTempusMethod.__init__(self, {
            "retrieve": {
                "method"  : "GET",
                "path"    : "/events/{event}",
                "params"  : ["event"]
            }
        });

    def __setitem__(self, key, value):
        self.__dict__[key] = value

    def __getitem__(self, key):
        return getattr(self, key);
