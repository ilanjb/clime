Any custom enum class can be used to annotate an attibute and converted into an argument.

```Python 
{!../docs_src/enums/tutorial_001.py!}
```
Check it:
<div class="termy">

```console
$ python tutorial_001.py --help

usage: tutorial_001.py [-h] {Colors.red,Colors.blue}

positional arguments:
  {Colors.red,Colors.blue}
                        type: <Colors>

optional arguments:
  -h, --help            show this help message and exit

```
</div>

*Note that the choices given are a bit misleading*
Colors.red should be entered as red. If you have a better solution than [one of Raymond Hettinger suggestions](https://bugs.python.org/issue25061) please let me know. 

Super!

Try it:
<div class="termy">

```console
$ python tutorial_001.py blue
my favorite color is blue

```
</div>
Nice!

If you give it a bad option, ArgumentParser will give you a nice message:

<div class="termy">

```console
$ python tutorial_001.py chocolate
usage: tutorial_001.py [-h] {Colors.red,Colors.blue}
tutorial_001.py: error: argument favorite_color: invalid Colors value: 'chocolate'

```
</div>

That's it. To use choices, just annotate with an Enum class.
