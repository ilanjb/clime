Attributes annotated with `int` are converted to type: int in argparser

```Python 
{!../docs_src/integers_floats_and_other_simple_classes/tutorial_001.py!}
```
Check it:

<div class="termy">

```console
$ python docs_src/integers_floats_and_other_simple_classes/tutorial_001.py

usage: tutorial_001.py [-h] age_in_years

positional arguments:
  age_in_years  type: <int>

optional arguments:
  -h, --help    show this help message and exit

```
</div>
Cool! 

- age_in_years is annotated with`int`
- CliMe takes converts it into an integer
Try it!

<div class="termy">

```console
$ python docs_src/integers_floats_and_other_simple_classes/tutorial_001.py 12
I am 12 years old.

```
</div>

Non-integers will be caught by ArgumentParser
<div class="termy">

```console
$ python docs_src/integers_floats_and_other_simple_classes/tutorial_001.py hi
usage: tutorial_001.py [-h] age_in_years
tutorial_001.py: error: argument age_in_years: invalid int value: 'hi'
```
</div>

<div class="termy">

```console
$ python docs_src/integers_floats_and_other_simple_classes/tutorial_001.py 12.1
usage: tutorial_001.py [-h] age_in_years
tutorial_001.py: error: argument age_in_years: invalid int value: '12.1'

```
</div>

That's it\.
