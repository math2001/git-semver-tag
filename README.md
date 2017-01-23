# Git Semver Tag

Help manager [semver](http://semver.org) tagging with git written in Python. It allows you to prefix
your tags with a `v`.

## Usage

You just need to bind the `git-semver-tag.py` to an alias:

```
gst=python "path\to\git-semver-tag.py" $*
```

### Windows

If you don't know how to create aliases on Windows, here's how:

Write this into a file, say in `C:/Users/you_username/aliases.cmd`.

```bash
doskey gst=python "path\to\git-semver-tag.py" $*
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

### Other platform

I only have a pc using Windows, so, Google's your best friend if you don't know how to create an
alias.
