from .Categories import Categories;
from .Customers import Customers;
from .Policies import Policies;

from .settings import *;

class ShareTempus:
    def __init__(self, key):

        # set user auth key
        setKey(key);

        self.categories = Categories();
        self.customers = Customers();
        self.policies = Policies();
