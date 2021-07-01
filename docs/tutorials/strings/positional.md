Getting stated with strings is a simple as calling clime() on an attrs class:

```Python 
{!../docs_src/strings/tutorial_001.py!}
```
Check it:

<div class="termy">

```console
$ python main.py

usage: tutorial_001.py [-h] name

positional arguments:
  name

optional arguments:
  -h, --help  show this help message and exit

```
</div>

Cool!
- Dude is a normal attrs decorated class.
- Name is a an argument type annotated with `str`.
- CliMe takes the class and turns it into a CLI with the builtin ArgumentParser.
Try it!

```console
$ python main.py joe
hi! my name is joe
```
It works!

Want to know what will not work? No arguments:
```console
$ python main.py
usage: tutorial_001.py [-h] name
tutorial_001.py: error: the following arguments are required: name
```

Or using --name as on optional argument..
```console
$ python main.py
usage: tutorial_001.py [-h] name
tutorial_001.py: error: unrecognized arguments: --name
```
Note that this is an unfortunate difference between argument parser and the underlying class init.
The class can take kwargs as positional. Argument parser cannot. 

Anyways... that's it.
All you need to take positional strings is an attrs decorated class with a 'str' annotated class variable.


