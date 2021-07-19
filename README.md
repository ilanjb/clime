Auto-generated, [Argparse](https://docs.python.org/3/library/argparse.html) based, 
CLIs from [attrs](https://www.attrs.org/en/stable/) classes.
Full docs here: [https://ilanjb.github.io/clime/](https://ilanjb.github.io/clime/)


hello world:
```Python 
{!../docs_src/sample_usage/tutorial_000.py!}
```

Check the help:
<div class="termy">

```console 
$ python tutorial_000.py --help
usage:
    Everything about the Dude!


positional arguments:
  name        type: <str>

optional arguments:
  -h, --help  show this help message and exit

```
</div>

Run it 
<div class="termy">

```console 
$ python tutorial_000.py joe
Dude(name='joe')
```
</div>

 