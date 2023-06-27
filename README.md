---

# OpenAI GPT-3 Concurrent JSON Processor

This Python script uses OpenAI's GPT-3 API to transform fields of a JSON array concurrently. This script is helpful when dealing with large JSON files and significantly speeds up the processing time.

## Dependencies

- Python 3.x
- OpenAI Python

The OpenAI Python client can be installed via pip:

```bash
pip install openai
```

## Setup

Before running the script, make sure to set your OpenAI API key. You can find your API key in the OpenAI dashboard. Set it at the top of the `script.py` file:

```python
openai.api_key = 'your-api-key'
```

## Usage

To use the script, provide the prompt, the input filename, and the output filename as command-line arguments:

```bash
python3 script.py '<prompt>' '<input-filename>' '<output-filename>'
```

For example:

```bash
python3 script.py 'Paraphrase this text' 'input.json' 'output.json'
```

The script will transform the 'description' and 'name' fields of each object in the input file according to the provided prompt, and will write the updated JSON array to the output file.

The output file will be formatted with an indentation of 4 spaces.

## License

This project is open source and available under the MIT License.

