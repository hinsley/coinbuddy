#!/usr/bin/env python3
import datetime

# TODO: Move to OAuth instead of using API keys.
import apikeys

from coinbase.wallet.client import Client
from coinbase.wallet.model import APIObject

client = Client(apikeys.api_key, apikeys.api_secret)

def get_account(client=client, account_id=apikeys.account_id):
    '''Get description of wallet account.'''

    return client.get_account(account_id)

def get_price(client=client, currency_pair='ETH-USD', price_type='spot'):
    '''Get price of Ethereum or other currency.
    `price_type` may be 'spot', 'buy', or 'sell'.
    Returns an APIObject with two fields: `amount`, `currency`.'''

    response = client._get('v2', 'prices', currency_pair, price_type)

    return client._make_api_object(response, APIObject)

def get_price_string(client=client, currency_pair='ETH-USD', price_type='spot'):

    '''Get a string detailing current time in UTC, currency pair requested,
    price, and currency value.
    `price_type` may be 'spot', 'buy', or 'sell'.
    Returns a string.'''
    price = get_price(
        client=client,
        currency_pair=currency_pair,
        price_type='spot'
    )

    return '[%s] %s: %s %s' % (
        str(datetime.datetime.utcnow()).split('.')[0],
        currency_pair,
        price.amount,
        price.currency
    )

