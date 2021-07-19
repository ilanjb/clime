Lets say you want all names to be capitalized, but you're happy to be flexible on input.
Ie Joe, joe, JOE and even jOe should all be understood as Joe
Just use [attrs converters](https://www.attrs.org/en/stable/examples.html#conversion)... 

```Python
{!../docs_src/supercharge_with_attrib/tutorial_001.py!}
```
Try it!

```console
$ python main.py joe
hi! my name is Joe
```
It works!

When using an explicit converter, Clime will not try to convert the input into the annotated type.
That means you can do whatever you want with as long as it starts with a string.
Here, we input a date:


```Python
{!../docs_src/supercharge_with_attrib/tutorial_003.py!}
```

Try it!

```console
$ python \docs_src\supercharge_with_attrib\tutorial_003.py 2000-11-22
My birthday is 2000-11-22

```
It works!

But what if the date is invalid?

Lets check...
```console
$ python \docs_src\supercharge_with_attrib\tutorial_003.py 2000-13-22
Traceback (most recent call last):
  File "\docs_src\supercharge_with_attrib\tutorial_003.py", line 29, in <module>
    main()
  File "\docs_src\supercharge_with_attrib\tutorial_003.py", line 25, in main
    clime(Dude).print_my_birthday()
  File "\clime\clime.py", line 100, in clime
    return attrs_decorated_class(**args.__dict__)
  File "<attrs generated init __main__.Dude>", line 2, in __init__
  File "\docs_src\supercharge_with_attrib\tutorial_003.py", line 14, in year_month_day_to_date
    return datetime.datetime.strptime(year_month_day, '%Y-%m-%d').date()
  File "C:\Program Files\Python38\lib\_strptime.py", line 568, in _strptime_datetime
    tt, fraction, gmtoff_fraction = _strptime(data_string, format)
  File "C:\Program Files\Python38\lib\_strptime.py", line 349, in _strptime
    raise ValueError("time data %r does not match format %r" %
ValueError: time data '2000-13-22' does not match format '%Y-%m-%d'
```
2000-13-22 is not a valid date so the conversion fails.

In other words, the conversion acts as an implicit [validator](../validators/).  
Amazing!


