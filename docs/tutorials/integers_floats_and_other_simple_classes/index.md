CliMe will convert any annotation into a type arguments for ArgumentParser.
This will work well for any class that can be instantiated with a string.

The following classes are converted automatically:

- int
- float
- ord
- str
- Path
    
Other classes (including you own custom classes) will be converted after checking that they can be instantiated with a string.

Thee following demo works with `int` as an example.