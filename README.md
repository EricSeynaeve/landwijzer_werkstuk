# Verdiepend werkstuk voor de Landwijzer opleiding

Welkom op de broncode van mijn verdiepend werkstuk voor de Landwijzer opleiding.

## Conceptuele versie

Er zijn twee **voorlopige** PDF files van dit document:

* [om af te drukken (dubbelzijdig)](https://github.com/EricSeynaeve/landwijzer_werkstuk/raw/master/text/manuscript-nl_print.pdf)
* [om op het scherm te lezen (enkelzijdig)](https://github.com/EricSeynaeve/landwijzer_werkstuk/raw/master/text/manuscript-nl_screen.pdf)

## Technische versie

Er zijn twee PDF files met meer cijfers en grafieken:

* [om af te drukken (dubbelzijdig)](https://github.com/EricSeynaeve/landwijzer_werkstuk/raw/master/text/manuscript-tech-nl_print.pdf)
* [om op het scherm te lezen (enkelzijdig)](https://github.com/EricSeynaeve/landwijzer_werkstuk/raw/master/text/manuscript-tech-nl_screen.pdf)

## Voor de diegenen die aanpassingen willen doen

Wil je de broncode zelf aanpassen, heb je [LyX](https://www.lyx.org) nodig. Zie daar voor de instructies om het te installeren.
Daarna moet je nog volgende LaTeX pakketten installeren:

* Nederlandse spelling & afbreekregels
* Franse spelling
* wrapfig
* multirow
* mhchem
* tocbibind
* qrcode
* adjustbox
* titling

Op Fedora Linux is allemaal te installeren via volgend commando:
```
yum install lyx texlive-babel-dutch texlive-babel-french texlive-hyphen-dutch texlive-wrapfig texlive-multirow texlive-mhchem texlive-tocbibind texlive-qrcode texlive-adjustbox texlive-titling
```

Ook gebruikt het document volgende LyX module:

* [longtablepage](https://wiki.lyx.org/Layouts/Modules#toc4)

(als ik er een aantal gemist heb omdat die bij mij standaard geïnstalleerd zijn, laat het maar weten in de issues op github.)
