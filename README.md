# Self-Improving AI Code Agent

![Python](https://img.shields.io/badge/language-Python-blue)


This project, based on [SelfImprovingAgent](https://github.com/NullLabTests/SelfImprovingAgent) contains a Python-based self-improving agent that uses AI to generate, evaluate, and iteratively refine code. The agent leverages the OpenAI API to produce new code and the arXiv API to incorporate inspiration from the latest research on self-improving AI. If implemented in a loop ( PLEASE USE CONTAINERIZED ENVs AND USE CAUTION ) this should allow an AI to continue to improve with the latest research pulled from arXiv. 

I have tested it with 10-100 iterations and it costs about 1 USD at current rates for 10 iterations ( depends on scope of your prompt ) but you can easily use local models and the OpenAI libs support grok ( as you will see in this working code in this repo. ) So far I was able to build out some prototypes which I plan to share here.

## Features

- **AI-Driven Code Generation:** Uses a language model to generate Python code based on a prompt.
- **Iterative Refinement:** Evaluates the generated code by executing it and uses any errors or outputs as feedback for further improvements.
- **Research Integration:** Fetches the latest research papers on self-improving AI from arXiv to guide the code generation process.
- **Automation:** The entire process is automated in an iterative loop, allowing the agent to improve its output over multiple iterations.

## Requirements

- **Python 3.7+**
- **Python Libraries:**
  - `openai` (for interacting with the OpenAI API)
  - `arxiv` (for fetching research papers)
  - Standard libraries: `os`, `re`, `subprocess`

You can install the required external libraries using pip:

```bash
pip install openai arxiv
```

## Setup

### Clone the Repository:

```bash
git clone <repository-url>
cd <repository-directory>
```

### Set the Environment Variable:

Make sure to set your API key for OpenAI, Grok, etc. For example:

```bash
export XAI_API_KEY="your_openai_api_key_here"
```

## Running the Agent

The main script is contained in `ArxEvo.py`. You can run it using:

```bash
python3 ArxEvo.py
```

Watch the agent iterate over its generated code and eventually print the final version to the console.

## Demo Videos

Check out these demo videos to see the project in action:

- [Demo Video 1](https://i.imgur.com/gYkEQUK.mp4)
- [Demo Video 2](https://i.imgur.com/oX8QDlI.mp4)


## Contributing

Feel free to open issues or submit pull requests if you have suggestions or improvements.

