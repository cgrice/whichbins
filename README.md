[![Build Status](https://travis-ci.org/cgrice/whichbins.svg?branch=master)](https://travis-ci.org/cgrice/whichbins)

# whichbins

A simple service to send reminders for bin collections. 
 
This service is pretty heavily tailored towards me. If you'd like to run something similar, you'll need to gather the data 
in [bins.json](./bins.json) that corresponds to your local authority and collection zone. Hopefully they have an API!

The service is designed to run in AWS lambda, under python 3.7.

## Installing

Requires [pipenv](https://pipenv.readthedocs.io/en/latest/install/#installing-pipenv).

```
make install
```

## Building

To create a zip file ready to upload to AWS Lambda:

```
make clean package
```

## Testing

```
pipenv install --dev
pipenv run nosetests
```