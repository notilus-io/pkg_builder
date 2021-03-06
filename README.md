# WAGON tools - Python package buiilder

This package is a meta-package that provide python libs for projects
and mainly `wagon-make-package` script.

`wagon-make-package` create a Python package template.

## Install `pkg_builder`
```bash
pip install pkg_builder
```

## Create a `new_pkg_name` package

Use `wagon-make-package` to create a new python package:
```bash
  $ build-package -n new_pkg_name -d "New project package"
    => New python package new_pkg_name created
  $ cd new_pkg_name/
  $ git init; git add *; git commit -am 'initial commit'
  $ git tag -a 0.42 -m 0.42
  $ make clean
```

Check that `__version__` is set:
```bash
  $ cd /tmp
  $ python -c 'import new_pkg_name; print (new_pkg_name.__version__)'
  0.42
  $
```

Check that `new_pkg_name` script work:

```bash
  $ (venv)user@machine:/tmp$ new_pkg_name-run
  new_pkg_name/data/data.csv.gz Loaded
  ==> out.csv MADE
      shape is (999, 142)
  (venv)user@machine:/tmp$ wc -l out.csv
  1000 out.csv
  (venv)user@machine:/tmp$
```


