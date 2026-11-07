import math
import copy

def _seq(x):
    if not isinstance(x,(list,tuple)) or len(x)>1000: raise ValueError("Use a list or tuple of at most 1000 items")
    return list(x)

def _text(x):
    if not isinstance(x,str) or len(x)>10000: raise ValueError("Use a string of at most 10000 characters")
    try: x.encode('utf-8')
    except UnicodeError: raise ValueError("Use valid Unicode scalar characters")
    return x

def _key(x):
    x=_text(x)
    if not x or len(x)>100: raise ValueError("Use a nonempty string key of at most 100 characters")
    return x

def _strings(x):
    return [_text(v) for v in _seq(x)]

def _ids(x):
    return [_key(v) for v in _seq(x)]

def _int(x,lo=-1000000000,hi=1000000000):
    if type(x) is not int or not lo<=x<=hi: raise ValueError("Integer outside documented bounds")
    return x

def _num(x):
    if type(x) not in (int,float) or not math.isfinite(x) or abs(x)>1e9: raise ValueError("Use finite real numbers of magnitude at most 1e9")
    return x

def _data(x,depth=0):
    if depth>6: raise ValueError("Nesting is limited to six levels")
    if x is None or type(x) is bool: return x
    if type(x) in (int,float): return _num(x)
    if isinstance(x,str): return _text(x)
    if isinstance(x,(list,tuple)): return [_data(v,depth+1) for v in _seq(x)]
    if isinstance(x,dict) and len(x)<=1000: return {_key(k):_data(v,depth+1) for k,v in x.items()}
    raise ValueError("Use bounded plain Python data")

def _record(x):
    if not isinstance(x,dict): raise ValueError("Use a dictionary record")
    _data(x)
    return x

def _rows(x):
    return [_record(v) for v in _seq(x)]

def _field(row,key):
    if key not in row: raise ValueError("Missing required field")
    return row[key]

def _unique_ids(x):
    values=_ids(x)
    if len(set(values))!=len(values): raise ValueError("Identifiers must be unique")
    return values

import re
import urllib.parse
def parse_query_values(query):
    query=_text(query)
    if query.startswith('?'): raise ValueError('Omit leading question mark')
    out={}
    def decode(s):
        if re.search(r'%(?![0-9A-Fa-f]{2})',s): raise ValueError('Malformed percent escape')
        try: return urllib.parse.unquote_plus(s,encoding='utf-8',errors='strict')
        except UnicodeError as exc: raise ValueError('Invalid UTF-8') from exc
    for part in query.split('&'):
        if not part: continue
        raw=part.split('=',1); key=_key(decode(raw[0])); value=_text(decode(raw[1] if len(raw)==2 else ''))
        out.setdefault(key,[]).append(value)
    return out
