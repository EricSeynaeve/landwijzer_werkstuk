# Treatise for the Landwijzer training

Welcome to the source code of my treatise for the Landwijzer training.

## Conceptual version

There are two PDF files of this document:

* [to print (double sided)](https://github.com/EricSeynaeve/landwijzer_werkstuk/raw/master/text/manuscript-en_print.pdf)
* [to read on a screen (single sided)](https://github.com/EricSeynaeve/landwijzer_werkstuk/raw/master/text/manuscript-en_screen.pdf)

## Technical version

This translation is still a work in progress.

## What after this treatise?

As emntioned in the treatise, the drive to start the system of Ferme du Bec Hellouin in Flanders became bigger. If you want to learn more about the progress on this road, got to the [website of 'Ferme Cultuur'](https:///www.fermecultuur.be).

## For those who want to make changes

If you wish to change the source code itself, you will need [LyX](https://www.lyx.org). Check installation instructions on that website.
Aftewards, you will still need to install following LaTeX packages:

* Dutch spelling & hyphenation rules
* French spelling
* wrapfig
* multirow
* mhchem
* tocbibind
* qrcode
* adjustbox
* titling

On Fedore Linux, this is all done with following command:
```
yum install lyx texlive-babel-dutch texlive-babel-french texlive-hyphen-dutch texlive-wrapfig texlive-multirow texlive-mhchem texlive-tocbibind texlive-qrcode texlive-adjustbox texlive-titling
```

The document also uses following LyX module:

* [longtablepage](https://wiki.lyx.org/Layouts/Modules#toc4)

(if I missed something because it was installed by default, file a github issue.)
