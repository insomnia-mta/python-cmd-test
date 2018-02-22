# python-cmd-test

Simple command line tool demonstration for python.

## Global installation

The package will be installed to the global python install location. Elevated write access may be required.

### Install 

```
[sudo] python setup.py install
```
### Uninstall

```
[sudo] pip uninstall imre
```


## Global development installation

It installs the package in development mode. Sources willbe symlinked, so changes in them will take effect immediately. Elevated write access may be required.

### Install 

```
[sudo] python setup.py develop
```

### Uninstall

```
[sudo] pip uninstall imre
```


## Local development installation

To install the package to the current user only in development mode, make sure you have `~/.local/bin` directory in your `PATH`.

### Install 

```
python setup.py develop --user
```
### Uninstall

```
pip uninstall imre
```

# Troubleshooting

If you tried to install the package both locally and globally, there might be a chance that your shell cached the command location, and the newly installed package fails to run, as the command points to the old location. You can clear the cached paths with the following command:

```
hash -r
```
