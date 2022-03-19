#! /bin/bash

set -o xtrace
set -o errexit

cd "$HOME/Nextcloud/Landwijzer/True cost of food/text/ondersteunende_documenten"
for f in *.mm;
do
	svg_f="${f%.mm}.svg"
	$HOME/bin/freeplane/freeplane.sh -S -XSaveToSvg_on_selected_node "$f"
	cutoff=$(grep -n '<rect.*url(#clipPath1)' "$svg_f" | cut -d: -f1)
	cutoff_begin=$(( $cutoff - 2 ))
	cutoff_end=$(( $cutoff + 2 ))
	head -n $cutoff_begin "$svg_f" > "figuren/$svg_f"
	tail -n +$cutoff_end  "$svg_f" >> "figuren/$svg_f"
	rm "$svg_f"
done
