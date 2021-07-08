Lets say you want all want to validate your input.
Just use [attrs validators](https://www.attrs.org/en/stable/examples.html#validators)... 


```Python
{!../docs_src/supercharge_with_attrib/tutorial_002.py!}
```
Try it!

```console
$ python docs_src\supercharge_with_attrib\tutorial_002.py  10
My favorite number less than 100 is 10

```
What if you enter and invalid input?

```console
$ python docs_src\supercharge_with_attrib\tutorial_002.py  101
Traceback (most recent call last):
  File "C:\Users\ilanb\PycharmProjects\attrsargparser\docs_src\supercharge_with_attrib\tutorial_002.py", line 24, in <module>
    main()
  File "C:\Users\ilanb\PycharmProjects\attrsargparser\docs_src\supercharge_with_attrib\tutorial_002.py", line 20, in main
    clime(Dude).print_favorite_number_less_than_100()
  File "C:\Users\ilanb\PycharmProjects\attrsargparser\clime\clime.py", line 100, in clime
    return attrs_decorated_class(**args.__dict__)
  File "<attrs generated init __main__.Dude>", line 4, in __init__
  File "C:\Users\ilanb\PycharmProjects\attrsargparser\venv\lib\site-packages\attr\_make.py", line 2975, in __call__
    v(inst, attr, value)
  File "C:\Users\ilanb\PycharmProjects\attrsargparser\docs_src\supercharge_with_attrib\tutorial_002.py", line 9, in x_smaller_than_100
    raise ValueError(f"{attribute.name} has to be smaller than 100!")
ValueError: favorite_number_less_than_100 has to be smaller than 100!

```
You won't do that again!


