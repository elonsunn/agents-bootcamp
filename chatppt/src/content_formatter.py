from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

from logger import LOG


class ContentFormatter:
    """Format raw user content into ChatPPT markdown using prompt template."""

    def __init__(
        self,
        prompt_file="./prompts/content_formatter.txt",
        model="gpt-4o-mini",
        api_key=None,
        base_url=None,
    ):
        self.prompt_file = prompt_file
        self.prompt = self.load_prompt()
        self.model = self.create_model(model=model, api_key=api_key, base_url=base_url)
        self.chain = self.create_chain()

    def load_prompt(self):
        with open(self.prompt_file, "r", encoding="utf-8") as file:
            return file.read().strip()

    def create_model(self, model, api_key=None, base_url=None):
        kwargs = {
            "model": model,
            "temperature": 0.3,
            "max_tokens": 4096,
            "timeout": 60,
            "max_retries": 2,
        }
        if api_key:
            kwargs["api_key"] = api_key
        if base_url:
            kwargs["base_url"] = base_url
        return ChatOpenAI(**kwargs)

    def create_chain(self):
        prompt = ChatPromptTemplate.from_messages([
            ("system", self.prompt),
            ("human", "{input}"),
        ])
        return prompt | self.model

    def format(self, raw_content):
        response = self.chain.invoke({"input": raw_content})
        LOG.info("Content formatted with LLM")
        return response.content
