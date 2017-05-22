#!/usr/bin/env python3
import pricelogger
import apikeys

from coinbase.wallet.client import Client
from coinbase.wallet.model import APIObject

# TODO: Move to OAuth instead of using API keys.

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

def get_price_string(client=client, currency_pair='ETH-USD', price_type='spot', log=True):

    '''Get a string detailing price type, currency pair requested, price, and
    currency value.
    `price_type` may be 'spot', 'buy', or 'sell'.
    If `log` == `True`, logs price data retrieved.
    Returns a string.'''

    price = get_price(
        client=client,
        currency_pair=currency_pair,
        price_type='spot'
    )

    result = '%s %s: %s %s' % (
        currency_pair,
        price_type,
        price.amount,
        price.currency
    )
    
    if log:
        pricelogger.log(result)

    return result

