# ShareTempus API for Python

## Installation

`pip install --upgrade sharetempus`

## Documentation

Documentation is available at http://docs.sharetempus.com

## API Overview

Every element is accessed via your `sharetempus` instance:

```python
from sharetempus.ShareTempus import ShareTempus;
sharetempus = ShareTempus('your sharetempus API key');
// sharetempus.{ ELEMENT_NAME }.{ METHOD_NAME }
```

Example:

```python
customer = sharetempus.customers.create({
    "email": "email@test.com",
    "legalEntity": {
        "type": "individual",
        "firstName": "Trenton",
        "lastName": "Large",
        "birthdate": 637124400000,
        "ssnLast4": "1234",
        "address": {
            "city": "New York City",
            "country": "US",
            "line1": "East 169th Street",
            "line2": "Apt. 2A Bronx",
            "postalCode": "10456",
            "state": "New York"
        }
    }
});

print(customer);
```
