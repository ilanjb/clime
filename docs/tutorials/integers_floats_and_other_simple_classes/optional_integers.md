Type conversion works with Optional annotations, too
```Python 
{!../docs_src/integers_floats_and_other_simple_classes/tutorial_002.py!}
```
Check it:

<div class="termy">

```console
$ python docs_src/integers_floats_and_other_simple_classes/tutorial_002.py

usage: tutorial_002.py [-h] [--age-in-years AGE_IN_YEARS]

optional arguments:
  -h, --help            show this help message and exit
  --age-in-years AGE_IN_YEARS
                        type: <int> (default: None)


optional arguments:
  -h, --help    show this help message and exit

```
</div>
Cool! 

- age_in_years is annotated with `Optional[int]`
- CliMe takes converts it an optional argument

Try it!

No arguments:
<div class="termy">

```console
$ python docs_src/integers_floats_and_other_simple_classes/tutorial_002.py --age-in-years 12
I am 12 years old.

```
</div>


With arguments:
<div class="termy">

```console
$ python docs_src/integers_floats_and_other_simple_classes/tutorial_002.py 
A script never reveals its age

```
</div>

That's it.
