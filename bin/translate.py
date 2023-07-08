#! /usr/bin/env python
import sys
from pathlib import Path

import deepl

file_name = sys.argv[1]
target_lang = 'en-us'
if len(sys.argv) > 2:
    target_lang = sys.argv[2]
source_lang = 'nl'
if len(sys.argv) > 3:
    source_lang = sys.argv[3]

authkey_filename = Path(Path.home(), '.deepl', 'auth_key')
source_filename = Path('/extra_disk', 'landwijzer_werkstuk','text', file_name+'-'+source_lang+'.xml')
target_filename = Path('/extra_disk', 'landwijzer_werkstuk','text', file_name+'-'+target_lang+'.xml')

authkey = ''
with open(authkey_filename) as authkey_file:
    authkey = authkey_file.read().rstrip()

translator = deepl.Translator(authkey)

usage = translator.get_usage().character
print("Usage so far: "+str(usage.count)+" characters used out of "+str(usage.limit))

with open(target_filename, 'w') as target_file:
    with open(source_filename) as source_file:
        source_text = source_file.read()

        try:
            result = translator.translate_text(source_text, source_lang=source_lang, target_lang=target_lang,
                    tag_handling='xml', ignore_tags=['_header', '_ert_inset'])
        except deepl.DeepLException as error:
            # Errors during upload raise a DeepLException
            print(error)

    target_file.write(result.text)

usage = translator.get_usage().character
print("Usage so far: "+str(usage.count)+" characters used out of "+str(usage.limit))
