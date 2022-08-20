#! /bin/bash

root_path=$(realpath "$0")
root_path="${root_path%/*}/../text/ondersteunende_documenten/"

translation_sed=$(mktemp)
# skip some lines in files which might contain one or more patterns
echo "/inkscape:label=/{p;d;}" > $translation_sed
# make it a sed expression and add word boundaries
sed -e 's/|/\\b|/' -e 's/^/s|\\b/' -e 's/$/|/g' "$root_path/images2en-us.txt" >> $translation_sed
for svg in "$root_path"/figuren/*.svg "$root_path"/grafieken/*.svg
do
	svg_en="${svg%.*}_en-us.svg"
	if [[ "$svg" == *"_en-us.svg" || -e "$svg_en" ]]
	then
		continue
	fi
	tmp_file=$(mktemp)
	cp "$svg" $tmp_file
	sed -i -f $translation_sed $tmp_file
	if ! diff -q "$svg" $tmp_file >/dev/null
	then
		cp $tmp_file "${svg%.*}_en-us.svg"
	fi
	rm $tmp_file
done
# rm $translation_sed
