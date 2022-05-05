#! /bin/bash

set -o xtrace
set -o errexit

cowsay "Creating pdf's"
cd "$HOME/Nextcloud/Landwijzer/True cost of food/text"

cowsay -f small "Double sided (default)"
time /usr/bin/lyx --export pdf2 manuscript.lyx && git add manuscript.pdf

cowsay -f small "Single sided"
cp -f manuscript.lyx manuscript_single.lyx
sed -i 's#^\\papersides .*#\\papersides 1#' manuscript_single.lyx
sed -i 's#^\\usepackage{lscape}.*#\\usepackage{pdflscape}#' manuscript_single.lyx
awk -v RS="\0" -v ORS=""  '{gsub(/manusc\nript\.pdf/,"manusc\nript_single.pdf"); print}' manuscript_single.lyx > manuscript_single.$$ && mv manuscript_single.$$ manuscript_single.lyx
awk -v RS="\0" -v ORS=""  '{gsub(/manuscrip\nt\.pdf/,"manuscrip\nt_single.pdf"); print}' manuscript_single.lyx > manuscript_single.$$ && mv manuscript_single.$$ manuscript_single.lyx
diff -u manuscript.lyx manuscript_single.lyx || true
time /usr/bin/lyx --export pdf2 manuscript_single.lyx && git add manuscript_single.pdf
rm manuscript_single.lyx

cowsay "Creating FULL pdf's"
cd "$HOME/Nextcloud/Landwijzer/True cost of food/text"

cowsay -f small "Double sided (default)"
time /usr/bin/lyx --export pdf2 manuscript-full.lyx && git add manuscript-full.pdf

cowsay -f small "Single sided"
cp -f manuscript-full.lyx manuscript-full_single.lyx
sed -i 's#^\\papersides .*#\\papersides 1#' manuscript-full_single.lyx
sed -i 's#^\\usepackage{lscape}.*#\\usepackage{pdflscape}#' manuscript-full_single.lyx
awk -v RS="\0" -v ORS=""  '{gsub(/manusc\nript\.pdf/,"manusc\nript_single.pdf"); print}' manuscript-full_single.lyx > manuscript-full_single.$$ && mv manuscript-full_single.$$ manuscript-full_single.lyx
awk -v RS="\0" -v ORS=""  '{gsub(/manuscrip\nt\.pdf/,"manuscrip\nt_single.pdf"); print}' manuscript-full_single.lyx > manuscript-full_single.$$ && mv manuscript-full_single.$$ manuscript-full_single.lyx
diff -u manuscript-full.lyx manuscript-full_single.lyx || true
time /usr/bin/lyx --export pdf2 manuscript-full_single.lyx && git add manuscript-full_single.pdf
rm manuscript-full_single.lyx

cowsay "Commit & push"
git commit
GIT_SSH_COMMAND="/usr/bin/ssh -i $HOME/.ssh/id_rsa_landwijzer" git push