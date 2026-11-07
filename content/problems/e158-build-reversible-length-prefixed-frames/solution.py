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

def text_frames(value,mode):
    if mode=='encode':
        messages=_strings(value)
        chunks=[]; size=0
        for message in messages:
            payload=message.encode('utf-8'); header=str(len(payload)).encode('ascii')+b':'
            size+=len(header)+len(payload)
            if size>10000000: raise ValueError('Framed stream exceeds byte limit')
            chunks.extend((header,payload))
        return b''.join(chunks)
    if mode!='decode' or not isinstance(value,bytes) or len(value)>10000000: raise ValueError('Invalid mode or byte stream')
    out=[]; pos=0
    while pos<len(value):
        colon=value.find(b':',pos)
        if colon<0: raise ValueError('Missing length separator')
        header=value[pos:colon]
        if not 1<=len(header)<=8 or any(c<48 or c>57 for c in header) or len(header)>1 and header[0]==48: raise ValueError('Invalid length header')
        length=int(header); start=colon+1; end=start+length
        if end>len(value): raise ValueError('Truncated payload')
        try: text=value[start:end].decode('utf-8')
        except UnicodeError as exc: raise ValueError('Invalid payload UTF-8') from exc
        out.append(_text(text)); pos=end
        if len(out)>1000: raise ValueError('Too many frames')
    return out
