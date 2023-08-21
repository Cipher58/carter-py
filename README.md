# Eureka-Py: Library for interaction with the Eureka API.

Original Package:

```
[GitHub](https://github.com/LazyLyrics/carter-py) | [PyPI](https://pypi.org/project/carter-py/) | [Change Log](https://github.com/LazyLyrics/carter-py/blob/main/CHANGELOG.md)| [Docs](https://lazylyrics.gitbook.io/carter-py-v1/)
```

`carter-py` is a Python package that provides a simple wrapper for the Eureka API. It is based on LazyLyrics' `carter-py` wrapper library, with high elements of their original code included. Citing `https://github.com/LazyLyrics/carter-py/tree/main` - Big thanks to them for their work!

Due to Carter sunsetting their API (incredibly smart move, even plankton would be astonished!) the original wrapper won't be able to utilise it, and so for those who wish to migrate from Carter to the alpha-stage Eureka AI, this library should be similar enough to ease the process of transitioning.

DISCLAIMER: This project is not intended to replace, steal or discredit LazyLyrics' original work, they deserve all the recognition for the code used in this library, so please support them and join LazyLyrics' [discord](https://discord.gg/4w2Hs9QU)!

## Installation

``` bash
pip install Eureka-py
```

## Usage

``` python

from eurekapy import Eureka


# Replace YOUR_API_KEY with your actual API key

eureka = Eureka("YOUR_API_KEY", "YOUR_AGENTS_NAME")

# Send a message to the API

response = eureka.say("Hello, world!", "player123")

# Print the response text

print(response)

```
