# Web Scraper Tool

A simple web scraping tool that extracts links from a given website up to a specified depth. It now includes functionality to filter the results by file extension.

## Requirements

- Python 3.x
- Pipenv
- Docker (optional, for running in a Docker container)

## Setting Up the Environment

Before running the scraper, ensure that you have `pipenv` installed. If you do not have `pipenv`, you can install it using pip:

```
pip install pipenv
```

Once pipenv is installed, navigate to the directory containing the Pipfile and set up the environment:

```
# Navigate to the scraper directory (modify according to your actual directory)
cd path/to/scraper

# Install dependencies from Pipfile
pipenv install
```

## Usage

To use the tool locally, first activate the pipenv shell, then run the following command:

```
# Activate the pipenv environment
pipenv shell

# Run the scraper
python scrape.py [url] [-m MAX_DEPTH] [-f FILE_EXTENSION]
```

### Arguments and Options

- `url`: The URL of the website you want to scrape. This is a required argument.
- `-m`, `--max_depth`: Optional. Specifies the maximum depth for scraping. Defaults to 1 if not specified.
- `-f`, `--filter`: Optional. Filter results by a specific file extension, e.g., 'mkv'.

### Examples

Scrape links from a website with the default depth:

```
python scrape.py http://example.com
```

Scrape links from a website up to a depth of 3:

```
python scrape.py http://example.com -m 3
```

Scrape links from a website, filtering for a specific file extension (e.g., .mkv files):

```
python scrape.py http://example.com -m 3 -f mkv
```

To check the version of the tool, use the `--version` flag:

```
python scrape.py --version
```

## Running in a Docker Container

You can also run the web scraper tool in a Docker container. Here's how to do it:

### Building the Docker Image

Ensure that you have Docker installed on your machine. Then, navigate to the directory containing your Dockerfile and run the following command to build the Docker image:

```
docker build -t scraper:1.0 .
```

### Running the Docker Container

Once the image is built, you can run the Docker container with the following command:

```
docker run scraper:1.0 [url] [-m MAX_DEPTH] [-f FILE_EXTENSION]
```

Replace `[url]`, `[-m MAX_DEPTH]`, and `[-f FILE_EXTENSION]` with your desired arguments.

**Example:**

```
docker run scraper:1.0 http://example.com -m 3 -f mkv
```

## Author

Al Biheiri (al@forgottheaddress.com)
