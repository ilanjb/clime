Defaults can be set to None, too.

```Python 
{!../docs_src/strings/tutorial_003.py!}
```
Check it:
<div class="termy">

```console
$ python tutorial_003.py --help

usage: tutorial_003.py [-h] [--name NAME]

optional arguments:
  -h, --help   show this help message and exit
  --name NAME  (default: None)

```
</div>

Super!

Name is now a positional argument with a defaul value.
The default value is added to the --help. 

Try it!

```console
$ python tutorial_003.py
hi! my name is a secret
```
It works with defaults!

```console
$ python tutorial_003.py --name mike
hi! my name is mike
```
It works with optional arguments!

That's it. Go ahead. Default to `None`!
