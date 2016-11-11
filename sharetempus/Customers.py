from .ShareTempusMethod import ShareTempusMethod

class Customers(ShareTempusMethod):
    def __init__(self):
        ShareTempusMethod.__init__(self, {
            "create": {
                "method"  : 'POST',
                "path"    : '/customers/create'
            },

            "update": {
                "method"  : 'POST',
                "path"    : '/customers/update'
            },

            "retrieve": {
                "method"  : "GET",
                "path"    : "/customers/{customer}",
                "params"  : ["customer"]
            }
        });

    def __setitem__(self, key, value):
        self.__dict__[key] = value

    def __getitem__(self, key):
        return getattr(self, key);
