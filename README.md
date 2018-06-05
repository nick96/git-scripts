# Git scripts
Scripts for helping out my git flow a bit.

## Install

Use the bash snippet below to install one of the scripts, or any other script
you wish git to use. It doesn't have to be `~/.local/bin/`, it just has to be
on your path. By using the `git-` prefix you will be able to call the scripts
using `git <alias>`, which is pretty neat!

```bash
chmod +x <file>
ln -s $PWD/file ~/.local/bin/git-<alias>
```

## Git SSH clone

This is a super basic script which you can use instead as a convenience wrapper
of `git clone`. It converts the HTTP URL to the URI you can use for clonging
via SSH. I prefer to work with my git repos via SSH but it is way more
convenient to copy the URL for github or where ever the code is hosted.
