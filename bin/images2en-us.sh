#! /bin/bash

root_path=$(realpath "$0")
root_path="${root_path%/*}/../text/ondersteunende_documenten/"

if [[ -n "$1" ]]
then
	file_pattern="$1"
else
	file_pattern=$(ls -1 "$root_path"/figuren/*.svg "$root_path"/grafieken/\*.svg)
fi

translation_sed=$(mktemp)
# skip some lines in files which might contain one or more patterns
echo "/inkscape:label=/{p;d;}" > $translation_sed
# make it a sed expression and add word boundaries
sed -e 's/\([a-zA-Z]\)|/\1\\b|/' -e 's/^/s|\\b/' -e 's/$/|/' "$root_path/images2en-us.txt" >> $translation_sed
echo "$file_pattern" | while read svg
do
	svg_en="${svg%.*}_en-us.svg"
	if [[ "$svg" == *"_en-us.svg" ]]
	then
		continue
	fi
	if [[ -e "$svg_en" ]]
	then
		echo "'$svg' is already translated. Skipping."
		continue
	fi
	echo "Translating '$svg' to '$svg_en'"
	tmp_file=$(mktemp)
	cp "$svg" $tmp_file
	sed -i -f $translation_sed $tmp_file
	if ! diff -q "$svg" $tmp_file >/dev/null
	then
		cp $tmp_file "$svg_en"
	else
		echo "No difference found. Are the translation terms added to '$root_path/images2en-us.txt'?"
	fi
	rm $tmp_file
done
rm $translation_sed
