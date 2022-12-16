![example workflow](https://github.com/florianmahner/toml_argparse/actions/workflows/tests.yml/badge.svg)
[![codecov](https://codecov.io/gh/florianmahner/toml_argparse/branch/main/graph/badge.svg?token=75FIYZG8BD)](https://codecov.io/gh/florianmahner/torch_multipletests)
![code style](https://img.shields.io/badge/code%20style-black-black)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)


# :honeybee: toml_argparse

This module is a convenience wrapper around argparse.ArgumentParser that accepts TOML files as input.

## Features

`toml_argparse` accepts --config and --section arguments to specify the path to a configuration file in TOML format and the name of a section in the configuration file, respectively.
Uses the following hierarchy of arguments:
    
- Arguments passed through the command line are selected over TOML arguments, even in both are passed
- Arguments from the TOML file are preferred over the default arguments
- Arguments from the TOML with a section override the arguments without a section


## Example Usage


Say we create a python file `example.py` with the following content:

```python 
parser = ArgumentParser()
parser.add_argument("--value_1", type=int, default=0, help="Input value")
parser.add_argument("--string_1", type=str, default="", help="Input string")

if __name__ == '__main__':
    # Parse arguments from the command line
    args = parser.parse_args()
    print(args.value_1)
```

And the following `config.toml` file:

```toml
value_1 = 1
string_1 = "./misc"

[section_1]
value_1 = 2
```

We can now parse the `config.toml` file to the argument parser:

```bash
python example.py --config "config.toml"
```

This will print `value_1` from the general section of the TOML file (i.e. 1). We can also manually
override this value directly from the command line and set it to e.g. 100:

```bash
python example.py --config "config.toml" --value_1 100
```

We can also override the general TOML value with the ones from a specific section, i.e.

```bash
python example.py --config "config.toml" --section "section_1"
```

This will print the value from the section and override the general value, i.e. it prints 2. Even when passing the
section, it will also include `string_1` from the general section.
