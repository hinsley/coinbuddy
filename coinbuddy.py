#!/usr/bin/env python3
import datetime

from coinbase.wallet.client import Client
from coinbase.wallet.model import APIObject

# TODO: Move to OAuth instead of using API keys.
api_key = ''
api_secret = ''
account_id = ''

client = Client(api_key, api_secret)

def get_account(client=client, account_id=account_id):
    '''Get description of wallet account.'''
    return client.get_account(account_id)

def get_price(client=client, currency_pair='ETH-USD'):
    '''Get price of Ethereum or other currency.
    Returns an APIObject with two fields: `amount`, `currency`.'''
    response = client._get('v2', 'prices', currency_pair, 'spot')
    return client._make_api_object(response, APIObject)

def get_price_string(client=client, currency_pair='ETH-USD'):
    '''Get a string detailing current time in UTC, currency pair requested,
    price, and currency value.'''
    price = get_price(client=client, currency_pair=currency_pair)
    return '[%s] %s: %s %s' % (
        str(datetime.datetime.utcnow()).split('.')[0],
        currency_pair,
        price.amount,
        price.currency
    )

