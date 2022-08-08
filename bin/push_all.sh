#! /bin/bash

set -o xtrace
set -o errexit

cowsay "Creating pdf's"
cd "$(git rev-parse --show-toplevel)/text"

function generate_files {
	short_filename=$1
	type_text=$2
	language=$3
	base_filename="$short_filename-${language,,}"

	lyx_filename="$base_filename.lyx"
	pdf_base_filename="$base_filename"

	cowsay -f small "$type_text, ${language^^}, Double sided"
	cp -f "$lyx_filename" tmp.lyx
	sed -i 's#^\\papersides .*#\\papersides 2#' tmp.lyx
	sed -i 's#^\\usepackage{pdflscape}.*#\\usepackage{lscape}#' tmp.lyx
	if [[ $type_text == "Conceptual" ]]
	then
		sed -i 's#^\\paperfontsize .*#\\paperfontsize default#' tmp.lyx
		sed -i '/^\\topmargin /d' tmp.lyx
		sed -i '/^\\bottommargin /d' tmp.lyx
	fi
	sed -i -e '/\\branch screen/,+1s/\\selected.*/\\selected 0/' -e '/\\branch print/,+1s/\\selected.*/\\selected 1/' tmp.lyx
	diff -u "$lyx_filename" tmp.lyx || true
	time /usr/bin/lyx -E pdf2 "${pdf_base_filename}_print.pdf" tmp.lyx && git add "${pdf_base_filename}_print.pdf"

	cowsay -f small "$type_text, ${language^^},Single sided"
	cp -f "$lyx_filename" tmp.lyx
	sed -i 's#^\\papersides .*#\\papersides 1#' tmp.lyx
	sed -i 's#^\\usepackage{lscape}.*#\\usepackage{pdflscape}#' tmp.lyx
	if [[ $type_text == "Conceptual" ]]
	then
		sed -i 's#^\\paperfontsize .*#\\paperfontsize 12#' tmp.lyx
		if ! grep '^\\bottommargin ' tmp.lyx >/dev/null 2>&1
		then
			sed -i 's#^\\end_index#&\n\\bottommargin 0#' tmp.lyx
		fi
		if ! grep '^\\topmargin ' tmp.lyx >/dev/null 2>&1
		then
			sed -i 's#^\\end_index#&\n\\topmargin 0#' tmp.lyx
		fi
		sed -i 's#^\\topmargin .*#\\topmargin 2cm#' tmp.lyx
		sed -i 's#^\\bottommargin .*#\\bottommargin 2cm#' tmp.lyx
	fi
	sed -i -e '/\\branch screen/,+1s/\\selected.*/\\selected 1/' -e '/\\branch print/,+1s/\\selected.*/\\selected 0/' tmp.lyx
	diff -u "$lyx_filename" tmp.lyx || true
	time /usr/bin/lyx -E pdf2 "${pdf_base_filename}_screen.pdf" tmp.lyx && git add "${pdf_base_filename}_screen.pdf"

	rm tmp.lyx
}

generate_files manuscript Conceptual nl
generate_files manuscript-tech Technical nl

cowsay "Commit & push"
git commit
GIT_SSH_COMMAND="/usr/bin/ssh -i $HOME/.ssh/id_rsa_landwijzer" git push
