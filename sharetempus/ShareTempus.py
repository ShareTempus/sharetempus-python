from .Categories import Categories;
from .Claims import Claims;
from .Customers import Customers;
from .Events import Events;
from .Policies import Policies;

from .settings import *;

class ShareTempus:
    def __init__(self, key):

        # set user auth key
        setKey(key);

        self.categories = Categories();
        self.claims = Claims();
        self.customers = Customers();
        self.events = Events();
        self.policies = Policies();
