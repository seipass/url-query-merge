from __future__ import annotations
def run(url,params):
 from urllib.parse import urlsplit,urlunsplit,parse_qsl,urlencode
 p=parse_qsl(urlsplit(url).query,keep_blank_values=True); p.extend(params.items())
 s=urlsplit(url); return urlunsplit((s.scheme,s.netloc,s.path,urlencode(p),s.fragment))
