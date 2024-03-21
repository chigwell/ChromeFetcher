[![PyPI version](https://badge.fury.io/py/chromefetcher.svg)](https://badge.fury.io/py/chromefetcher)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Downloads](https://static.pepy.tech/badge/chromefetcher)](https://pepy.tech/project/chromefetcher)

# ChromeFetcher

`ChromeFetcher` automates the process of fetching Chrome or ChromeDriver based on the operating system and architecture. It simplifies the task of downloading the appropriate version for your system.

## Installation

To install `ChromeFetcher`, use pip:

```bash
pip install ChromeFetcher
```

## Usage

Easily download ChromeDriver with:

```python
from ChromeFetcher.chrome_fetcher import fetch_chrome

fetch_chrome(product='chromedriver')
```

Specify `product` as `'chrome'` or `'chromedriver'` to download. Options allow unzipping and cleanup post-download.

The `fetch_chrome` function offers a comprehensive approach to automatically downloading Chrome or ChromeDriver based on the user's operating system and architecture, streamlining the setup process for web automation tasks. Here's an overview of all the parameters available in this function:

- **channel (default='Stable')**: This parameter allows users to specify the release channel of Chrome they wish to download. The default is set to 'Stable', but users can select other channels like 'Beta' or 'Dev' depending on their requirements.

- **product (default='chrome')**: Determines whether to download Chrome or ChromeDriver. By setting this parameter to 'chrome', the function will download the browser. If set to 'chromedriver', it will fetch the driver needed for automation.

- **download_path (default=os.getcwd())**: Specifies the directory where the downloaded file will be saved. By default, it uses the current working directory. Users can provide a custom path to suit their project structure.

- **unzip (default=True)**: A boolean parameter that, when set to True, automatically extracts the contents of the downloaded ZIP file. If False, the function leaves the ZIP file as is.

- **delete_zip (default=True)**: This parameter works in tandem with the unzip option. When set to True, it deletes the ZIP file after extraction to save space and keep the directory tidy. If unzip is False, this parameter has no effect.

## Features

- Automatically fetches Chrome or ChromeDriver.
- Supports different OS and architectures.
- Unzips and cleans up downloads optionally.

## Contributing

Contributions, issues, and feature requests are welcome! Check our [issues page](https://github.com/chigwell/ChromeFetcher/issues).

## License

Licensed under the [MIT License](https://choosealicense.com/licenses/mit/).
