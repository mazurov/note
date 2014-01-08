# Chib production analysis note


## How to build

I'm using texlive full dictribuiton on Ubuntu and latexmk to build latex project.

```sh
$> git clone https://github.com/mazurov/note.git
$> ./scripts/bootstrap
$> evince ./build/chib_note.pdf
```

## How to send  changes to me

```sh
$> git diff > changes.diff

... and mail me changes.diff file.
```

