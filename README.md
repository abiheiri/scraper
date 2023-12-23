# Web Scraper Tool

A simple web scraping tool that extracts links from a given website up to a specified depth.

## Requirements

- Python 3.x
- Pipenv

## Setting Up the Environment

Before running the scraper, ensure that you have `pipenv` installed. If you do not have `pipenv`, you can install it using pip:

```bash
pip install pipenv
```

Once pipenv is installed, navigate to the directory containing the Pipfile and set up the environment:

```bash
# Navigate to the scraper directory (modify according to your actual directory)
cd path/to/scraper

# Install dependencies from Pipfile
pipenv install
```

# Usage

To use the tool, first activate the pipenv shell, then run the following command:

```bash
# Activate the pipenv environment
pipenv shell

# Run the scraper
python scrape.py [url] [-m MAX_DEPTH]

```

### Arguments and Options

url: The URL of the website you want to scrape. This is a required argument.

-m, --max_depth: Optional. Specifies the maximum depth for scraping. Defaults to 1 if not specified.

Examples
Scrape links from a website with the default depth:

```bash
python scrape.py http://example.com
```

Scrape links from a website up to a depth of 3:
```bash
python scrape.py http://example.com -m 3
```

To check the version of the tool, use the --version flag:

```bash
python scrape.py --version
```

# Author

Al Biheiri (al@forgottheaddress.com)