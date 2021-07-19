Boolean attributes must be given a default value.
When set defaulted to `False`, CliMe will use ArguementParsers's `action="store_false"`.
Using the flag will set it to True

```Python 
{!../docs_src/booleans/tutorial_001.py!}
```
Check it:
<div class="termy">

```console
$ python tutorial_001.py --help

usage: tutorial_001.py [-h] [--likes-ice-cream]

optional arguments:
  -h, --help         show this help message and exit
  --likes-ice-cream  (default: False)

```
</div>

Super!

*note: CliMe converts underscores from variable names to dashes in the CLI*

*In the this case 'likes_ice_cream' became 'likes-ice-cream'*

Running without arguments will keep that attribute `False`.

Try it!

```console
$ python tutorial_001.py
hi! i do not like ice cream
```
Running with the  --likes-ice-cream flag  will set the attribute `True`.

```console
$ python tutorial_001.py  --likes-ice-cream
hi! i like ice cream
```
It works with flags!

That's it.
For boolean arguments just set a default value!


