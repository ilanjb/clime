To use defaul values, just add a default value to the attribute

```Python 
{!../docs_src/strings/tutorial_002.py!}
```
Check it:
<div class="termy">

```console
$ python tutorial_002.py

usage: tutorial_002.py [-h] [--name NAME]

optional arguments:
  -h, --help   show this help message and exit
  --name NAME  (default: joe)
```
</div>

Super!

Name is now a positional argument with a defaul value.
The default value is added to the --help. 

Try it!

```console
$ python tutorial_002.py
hi! my name is joe
```
It works with defaults!

```console
$ python tutorial_002.py --name mike
hi! my name is mike
```
It works with optional arguments!

Want to know what will not work? Positional arguments:

```console
$ python tutorial_002.py mike
usage: tutorial_002.py [-h] [--name NAME]
tutorial_002.py: error: unrecognized arguments: mike
```
Note that this is an unfortunate difference between argument parser and the underlying class init.
The class can attributes with default argument as positional. Argument parser cannot. 

Anyways... that's it.
All you need to take use default values is give the attribute a default value!


