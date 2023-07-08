#! /usr/bin/env python
import sys
from pathlib import Path

import deepl

source_filename = sys.argv[1]
target_filename = sys.argv[2]
target_lang = 'EN-US'
if len(sys.argv) > 3:
    target_lang = sys.argv[3]
source_lang = None
if len(sys.argv) > 4:
    source_lang = sys.argv[4]

authkey_filename = Path(Path.home(), '.deepl', 'auth_key')

authkey = ''
with open(authkey_filename) as authkey_file:
    authkey = authkey_file.read().rstrip()

translator = deepl.Translator(authkey)

usage = translator.get_usage().character
print("Usage so far: "+str(usage.count)+" characters used out of "+str(usage.limit))

print("Translating "+source_filename+" in "+target_filename+", target language: "+target_lang)
try:
    result = translator.translate_document_from_filepath(source_filename, target_filename, source_lang=source_lang, target_lang=target_lang)
except deepl.DeepLException as error:
    # Errors during upload raise a DeepLException
    print(error)

usage = translator.get_usage().character
print("Usage so far: "+str(usage.count)+" characters used out of "+str(usage.limit))
