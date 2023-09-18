import random

def generate_OHLC(refValue:float=random.randrange(1, 9999), deviation: float=20):
    '''
    Generate OHLC

    Returns:
        open, close, high, low
    '''
    open = refValue
    delta_change = random.randrange(1,deviation) / 100 * refValue
    pos_neg = random.randrange(0,2)
    close = refValue + delta_change if pos_neg == 1 else refValue - delta_change
    low = min([open, close]) - delta_change * (1 - (random.randrange(1, deviation) / 100))
    high = max([open, close]) + delta_change * (1 + (random.randrange(1, deviation) / 100))
    return open, close, high, low

def generate_price(refValue, deviation: float=20):
    delta = random.randrange(1,deviation) / 100 * refValue
    return refValue + delta if random.randrange(0,2) == 1 else refValue - delta
