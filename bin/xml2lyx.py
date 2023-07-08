#! /usr/bin/env python

import re
import sys

import xml.etree.ElementTree as ET
import xml.parsers.expat as expat

doc = sys.argv[1]
lang = sys.argv[2]
input_filename = '/extra_disk/landwijzer_werkstuk/text/'+doc+'-'+lang+'.xml'
output_filename = '/extra_disk/landwijzer_werkstuk/text/'+doc+'-'+lang+'-back.lyx'

sentence_end_re=re.compile('([!?]|[^.][.]|[\n])')
header = False
text = ''
def write_sentence(s):
    max_len = 78
    while len(s) > max_len:
        split = s.rfind(' ', 0, max_len)
        if split >= 0:
            output_file.write(s[:split]+'\n')
            s = s[split:]
        else:
            break
    output_file.write(s.rstrip('\n')+'\n')
def write_text():
    global text
    if len(text) > 0:
        # split on end of sentences
        splitted = sentence_end_re.split(text.rstrip('\n'))
        while len(splitted) > 1:
            sentence = splitted[0]+splitted[1]
            write_sentence(sentence)
            splitted = splitted[2:]
        if len(splitted) == 1:
            if splitted[0] != '':
                write_sentence(splitted[0])
    text = ''
def comment(data):
    write_text()

    output_file.write('#'+data+'\n')
def start_element(name, attrs):
    global header
    write_text()

    # special tags
    if name == 'lyx2xml':
        return
    if name == 'empty_line':
        output_file.write('\n')
        return
    if name == '__param':
        start_tab = attrs.pop('start_tab')
        if start_tab == "True":
            output_file.write('\t')
        value_present = attrs.pop('value_present')
        if value_present == "True":
            param = ' '.join([k+' '+v for (k, v) in attrs.items()])
        else:
            param = ' '.join([k for k in attrs.keys()])
        output_file.write(param+'\n')
        return

    # xml-like structure
    if name.startswith('__'):
        if len(attrs) > 0:
            param = ' '.join([k+'="'+v+'"' for (k, v) in attrs.items()])
            output_file.write('<'+name[2:]+' '+param+'>\n')
        else:
            output_file.write('<'+name[2:]+'>\n')
        return

    # lyx blocks
    if name.startswith('_'):
        if name == '_ert_inset':
            name = '_inset'
        if name == '_header':
            header = True
        output_file.write('\\begin'+name)
    else:
        output_file.write('\\'+name)
    if len(attrs) > 0:
        output_file.write(' '+' '.join(attrs.values())+'\n')
    else:
        output_file.write('\n')
def end_element(name):
    global header
    write_text()

    # special tags
    if name == '__param':
        return

    # xml-like structure
    if name.startswith('__'):
        if name[2:] not in ('features', 'column'):
            output_file.write('</'+name[2:]+'>\n')
        return

    # lyx blocks
    if name.startswith('_'):
        if name == '_ert_inset':
            name = '_inset'
        if name == '_header':
            header = False
        output_file.write('\\end'+name+'\n')
def char_data(data):
    global text
    global header
    if header is True:
        output_file.write(data.replace('<empty_line/>',''))
        return

    if len(text) == 0:
        if data == '\n':
            return
    text += data.replace('<empty_line/>','')

with open(output_filename, 'w') as output_file:
    p = expat.ParserCreate()

    p.CommentHandler = comment
    p.StartElementHandler = start_element
    p.EndElementHandler = end_element
    p.CharacterDataHandler = char_data
    
    with open(input_filename, 'rb') as input_file:
        p.ParseFile(input_file)
