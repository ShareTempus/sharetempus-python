from .ShareTempusMethod import ShareTempusMethod

class Policies(ShareTempusMethod):
    def __init__(self):
        ShareTempusMethod.__init__(self, {
            "quote": {
                "method"  : "POST",
                "path"    : "/policies/quote"
            },

            "create": {
                "method"  : 'POST',
                "path"    : '/policies/create'
            },

            "update": {
                "method"  : "POST",
                "path"    : "/policies/update"
            },

            "etrieve": {
                "method"  : "GET",
                "path"    : "/policies/{policy}",
                "params"  : ["policy"]
            }
        });

    def __setitem__(self, key, value):
        self.__dict__[key] = value

    def __getitem__(self, key):
        return getattr(self, key);
