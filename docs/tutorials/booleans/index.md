CliMe uses argparse's "store_true" and "store_false" to convert attrs boolean attributes to CLI.
For this to work smoothly:

- boolean arguments must be given a default value
- boolean arguments cannot be optional
