#! /usr/bin/env python
from pathlib import Path

import deepl

authkey_filename = Path(Path.home(), '.deepl', 'auth_key')

authkey = ''
with open(authkey_filename) as authkey_file:
    authkey = authkey_file.read().rstrip()

translator = deepl.Translator(authkey)

usage = translator.get_usage().character
print("Usage so far: "+str(usage.count)+" characters used out of "+str(usage.limit))
