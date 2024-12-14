# Marp AI - Generate slides using Ollama AI

>This is just a simple proof of concept to generate slides using Ollama AI.

## How to use

1. Clone this repository
2. Use pip to install the required packages `pip install -r requirements.txt`	
3. Download Marp from [Github](https://github.com/marp-team/marp-cli/releases)
4. Make sure ollama is running on your local machine
5. Run the script `python main.py`

## How it works

The script generates a markdown file with the content from the Ollama API and then uses Marp to generate the slides. It's really that simple.

## Example

There is an example in the `demo` folder.

## Disclaimer

This is just a proof of concept and should not be used in production. The code is not optimized and there are no error handling. Use at your own risk. Always make sure to check the generated slides before using them in a presentation.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Ollama](https://ollama.com/)
- [Marp](https://marp.app/)