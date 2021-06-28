Using the power of attr.ib can supercharge your CliMe.
Lets say you want all name to be capitalized, but you're happy to be flexible on input
Ie Joe, joe, JOE and even jOe should all be understood as Joe
Just use attr.ib(converter=str.capitalize) like this:

```Python
{!../docs_src/strings/tutorial_002.py!}
```

Try it!

```console
$ python main.py joe
hi! my name is Joe
```
It works!