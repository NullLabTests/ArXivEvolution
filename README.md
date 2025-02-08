# Self-Improving AI Code Agent

This project contains a Python-based self-improving agent that uses AI to generate, evaluate, and iteratively refine code. The agent leverages the OpenAI API to produce new code and the arXiv API to incorporate inspiration from the latest research on self-improving AI.

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
Setup
Clone the Repository:

bash
Copy
Edit
git clone <repository-url>
cd <repository-directory>
Set the Environment Variable:

Make sure to set your API key for OpenAI. For example:

bash
Copy
Edit
export XAI_API_KEY="your_openai_api_key_here"
Running the Agent
The main script is contained in ArxEvo.py. You can run it using:

bash
Copy
Edit
python3 ArxEvo.py
Watch the agent iterate over its generated code and eventually print the final version to the console.

Demo Videos
Check out these demo videos to see the project in action:

Demo Video 1
Demo Video 2
Contributing
Feel free to open issues or submit pull requests if you have suggestions or improvements.


