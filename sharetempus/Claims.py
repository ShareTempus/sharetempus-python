from .ShareTempusMethod import ShareTempusMethod

class Claims(ShareTempusMethod):
    def __init__(self):
        ShareTempusMethod.__init__(self, {
            "create": {
                "method"  : 'POST',
                "path"    : '/claims/create'
            },

            "retrieve": {
                "method"  : "GET",
                "path"    : "/claims/{claim}",
                "params"  : ["claim"]
            }
        });

    def __setitem__(self, key, value):
        self.__dict__[key] = value

    def __getitem__(self, key):
        return getattr(self, key);
