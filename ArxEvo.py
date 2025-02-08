import os
import re
import subprocess
from openai import OpenAI  # Adjust if your library import differs
import arxiv

class SelfImprovingAgent:
    def __init__(self, model="grok-2-latest", iterations=10):
        self.model = model
        self.iterations = iterations
        self.client = OpenAI(
            api_key=os.getenv("XAI_API_KEY"),
            base_url="https://api.x.ai/v1",
        )

    def extract_code(self, text):
        """
        Extracts the code from a Markdown code block if present.
        If no code block is found, returns the stripped text.
        """
        # Updated regex: removed extraneous backslash before the colon
        code_block = re.search(r"```(?:python)?\n(.*?)\n```", text, re.DOTALL)
        if code_block:
            return code_block.group(1).strip()
        return text.strip()

    def generate_code(self, prompt):
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "You are an AI code generator."},
                {"role": "user", "content": prompt}
            ]
        )
        code = response.choices[0].message.content
        return self.extract_code(code)

    def evaluate_code(self, file_name):
        try:
            result = subprocess.run(["python3", file_name], capture_output=True, text=True)
            return result.stdout, result.stderr
        except Exception as e:
            return "", str(e)

    def refine_code(self, code, feedback):
        prompt = (
            f"Refine this code based on the following feedback:\n{feedback}\n\n"
            f"Code:\n{code}"
        )
        return self.generate_code(prompt)

    def fetch_latest_papers(self, max_results=5, query="self-improving AI"):
        search = arxiv.Search(
            query=query,
            max_results=max_results,
            sort_by=arxiv.SortCriterion.SubmittedDate
        )

        # Use the new Client to get search results
        client = arxiv.Client()
        papers = []
        for result in client.results(search):
            papers.append({
                "title": result.title,
                "abstract": result.summary.replace("\n", " "),
                "link": result.entry_id
            })

        return papers

    def run(self):
        latest_papers = self.fetch_latest_papers()
        paper_summaries = "\n".join([
            f"Title: {paper['title']}\nAbstract: {paper['abstract']}" 
            for paper in latest_papers
        ])

        base_prompt = (
            f"Generate a new AI function inspired by the latest arXiv papers on self-improving AI. "
            f"Here are some of the latest findings:\n{paper_summaries}\n\n"
            f"Allow the AI to create entirely new projects instead of refining a single function."
        )

        code = self.generate_code(base_prompt)
        file_name = "generated_script.py"

        for i in range(self.iterations):
            with open(file_name, "w") as f:
                f.write(code)

            output, error = self.evaluate_code(file_name)
            feedback = error if error else f"Success! Output: {output}"
            code = self.refine_code(code, feedback)

        print("Final Version:")
        print(code)

if __name__ == "__main__":
    agent = SelfImprovingAgent()
    agent.run()
