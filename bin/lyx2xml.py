#! /usr/bin/env python

import sys

from xml.sax.saxutils import escape,quoteattr

doc = sys.argv[1]
lang = sys.argv[2]
input_filename = '/extra_disk/landwijzer_werkstuk/text/'+doc+'-'+lang+'.lyx'
output_filename = '/extra_disk/landwijzer_werkstuk/text/'+doc+'-'+lang+'.xml'

def tag_with_attr(text):
    els = text.split()
    xml = els[0]
    count = 1
    for el in els[1:]:
        xml += ' tag'+str(count)+'='+quoteattr(el)
        count += 1
    return xml

with open(output_filename, 'w') as output_file:
    output_file.write('<lyx2xml>\n')
    header=False
    inset_stack=list()
    inset_parameters=False
    text=''
    with open(input_filename) as input_file:
        for line in input_file:
            line = line.rstrip('\n')
            # handle the header
            if line.startswith('\\begin_header'):
                header = True
                output_file.write('<_header><![CDATA[\n')
                continue
            if line.startswith('\\end_header'):
                header = False
                output_file.write(']]></_header>\n')
                continue
            if header == True:
                if line == '':
                    output_file.write('<empty_line/>\n')
                else:
                    output_file.write(line+'\n')
                continue

            # handle xml-like structure
            if line.startswith('</'):
                output_file.write('</__'+line[2:]+'\n')
                continue
            if line.startswith('<'):
                if line[1:5] in ('feat', 'colu'):
                    output_file.write('<__'+line[1:-1]+'/>\n')
                else:
                    output_file.write('<__'+line[1:]+'\n')
                continue

            # handle instuctions
            if line.startswith('\\begin_'):
                output_file.write(text)
                text=''
                inset_parameters = False
                els = line[6:].split()
                xml = els[0]
                if xml == '_inset':
                    inset_type = els[1].lower()
                    inset_stack.append(inset_type)
                    if inset_type == 'ert':
                        xml = '_ert_inset'
                    inset_parameters = True
                count = 1
                for el in els[1:]:
                    xml += ' tag'+str(count)+'='+quoteattr(el)
                    count += 1
                output_file.write('<'+xml+'>\n')
                continue
            if line.startswith('\\end_'):
                output_file.write(text)
                text=''
                inset_parameters = False
                xml = line[4:]
                if xml == '_inset':
                    inset_type = inset_stack.pop()
                    if inset_type == 'ert':
                        xml = '_ert_inset'
                output_file.write('</'+xml+'>\n')
                continue
            if line.startswith('\\'):
                output_file.write(text)
                text=''
                inset_parameters = False
                output_file.write('<'+tag_with_attr(line[1:])+'/>\n')
                continue

            # handle special lines
            if line.startswith('#'):
                inset_parameters = False
                output_file.write('<!--'+escape(line[1:])+'-->\n')
                continue
            if line == '':
                inset_parameters = False
                output_file.write('<empty_line/>\n')
                continue

            # handle any other lines
            if inset_parameters is True:
                start_tab = False
                value_present = True
                if line[0] in ('\t'):
                    line = line.lstrip()
                    start_tab = True
                sep = line.find(' ')
                name = line[:sep]
                value = line[sep+1:]
                if sep == -1:
                    value_present = False
                    name = line
                output_file.write('<__param start_tab="'+str(start_tab)+'" value_present="'+str(value_present)+'" '+name)
                if len(value) > 0:
                    if value_present is True:
                        output_file.write('='+quoteattr(value))
                    else:
                        output_file.write('="True"')
                output_file.write("/>\n")
            else:
                text += escape(line)
    output_file.write('</lyx2xml>\n')
