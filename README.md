# Chib production analysis note

[Latest (pdf)](http://amazurov.web.cern.ch/amazurov/chib_note.pdf)

## How to build

I'm using texlive full distribution on Ubuntu and latexmk to build latex project.

``latexmk`` is a perl script. If you don't have it in your OS you can run it
from my public lxplus directory: replace the ``latexmk`` command in
``~/scripts/bootstrap`` to ``$> ~amazurov/public/latexmk/latexmk.pl``.


```sh
$> git clone https://github.com/mazurov/note.git
$> cd note
$> ./scripts/bootstrap
$> evince ./build/chib_note.pdf
```

## How to send  changes to me

```sh
$> git diff > changes.diff

... and mail me changes.diff file.
```

