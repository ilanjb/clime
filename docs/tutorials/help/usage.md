
The docstrings of the class are passed to ArgumentParser for the usage kwarg.

```Python 
{!../docs_src/usage/tutorial_001.py!}
```
Check it:

<div class="termy">

```console
python tutorial_001.py --help
usage:
    Amaze your friends by printing you name to the console

positional arguments:
  name        type: <str>

optional arguments:
  -h, --help  show this help message and exit

```
</div>

Cool!

That's it... To add a usage message just add docstrings to your class