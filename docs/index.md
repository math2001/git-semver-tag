# Git Semver Tag

Git Semver Tag is a simple python script that allows you to create [semver][] git tags without
worrying about the last tag. It's relative. You say:

> Create a new tag: it's a patch

for example. It'll manage the number for you. Of course, it's not that verbose, but you get the idea
:simple_smile:

```sh
gst --patch
```

This is how you'd do. Sounds good? Keep reading then!

## Installation

You need [python][] installed on your system. I'm using it with python 3.4, but it should work with
python 2 too.

So, let's get going!

```bash
$ cd <somewhere>
$ git clone https://github.com/math2001/git-semver-tag/
```

And then, just alias the `git-semver-tag.py` to whatever you want (in the example above, I did it
for `gst`).

### On Windows

If you don't know how to create aliases on Windows, here's how:

Write this into a file, say in `C:/Users/you_username/aliases.cmd`.

```bash
doskey gst=python "<somewhere>\git-semver-tag\git-semver-tag.py" $*
```

Quickly, `doskey` is the command to alias. Then `gst` is the name of the alias. After the `=`, it's
the command that is going to be called. The `$*` allows to give args to the actual command through
the alias.

Then, create a shortcut for `cmd`, on the desktop for example. Right click on it, select
`Properties`, in the `Shortcut` tab, click in the `Target` tab and type:

```bash
cmd /k C:/Users/you_username/aliases.cmd
```

Of course, replace `C:/Users/you_username/aliases.cmd` with the actual path to the alias file.

Click `OK`, and double click on this shortcut. You have now access to the alias `gst`.

### On other platforms

I only have a pc using Windows, so, Google's your best friend if you don't know how to create an
alias.

## Usage

```bash
$ git last-tag # see git aliases at the bottom of this page
v1.0.0

$ gst --patch
$ git last-tag
v1.0.1

$ gst --minor
$ git last-tag
v1.1.0

$ gst --major
$ git last-tag
v2.0.0
```

!!! bug
    Make sure you don't create 2 tags that points to the same commits. Otherwise, the tag you'll try
    to create will be already existing.

### Recommendation

I recommend you to add the option `--sure` to your alias, because otherwise, it'll ask you each time
if you're sure you want to create the tag.

```bash
gst=python "<somewhere>\git-semver-tag\git-semver-tag.py" --sure $*
```

### Git aliases

A few little git aliases:

```bash
$ git config --global alias.last=log -1
$ git last # shows the last commit

$ git config --global alias.last-tag=describe --abbrev=0 --tags
$ git last-tag # shows the last tag

$ git config --global alias.hub="!f() { [ -f .githubrepo ] && REPO=$(head -n 1 .githubrepo) || REPO=${PWD##*/}; URL=\"https://github.com/math2001/$REPO\"; if [ \"$1\" == i ]; then start \"$URL/issues\"; elif [ \"$1\" == p ]; then start \"$URL/pulls\"; elif [ \"$1\" == w ]; then start $URL/wiki; else start $URL/$1; fi; }; f"
$ git hub # opens the github repo.
```

More infos about the [last one](https://gist.github.com/math2001/58e241ec9ea004a11be908a13cf8485d)

[semver]: http://semver.org
[python]: http://python.org
