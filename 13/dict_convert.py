from collections import namedtuple
from datetime import datetime
import json


blog = dict(name='PyBites',
            founders=('Julian', 'Bob'),
            started=datetime(year=2016, month=12, day=19),
            tags=['Python', 'Code Challenges', 'Learn by Doing'],
            location='Spain/Australia',
            site='https://pybit.es')

# define namedtuple here
nt = namedtuple('Blog', ['name', 'founders', 'started', 'tags', 'location', 'site'])

def dict2nt(dict_):
    return nt(name=dict_['name'], founders=dict_['founders'], started=dict_['started'],tags=dict_['tags'],location=dict_['location'],site=dict_['site'])

def conv(x):
    if isinstance(x, datetime):
        return x.__str__()

def nt2json(nt):
    return json.dumps(nt._asdict(), default=conv)
