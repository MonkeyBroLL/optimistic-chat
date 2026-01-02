from langchain.agents import create_agent
from langgraph.checkpoint.memory import InMemorySaver
from dotenv import load_dotenv
from src.agent.utils.model import create_deepseek_model
from src.agent.prompt.prompt_loader import load_prompt

load_dotenv()


class ChatAgent:
    def __init__(self, temperature: float = 0.7):
        self.model = create_deepseek_model(temperature=temperature)
        self.agent = create_agent(
            model=self.model,
            checkpointer=InMemorySaver(),
            system_prompt=load_prompt(),
        )

    def chat(self, message: str, thread_id: str = "1") -> str:
        config = {"configurable": {"thread_id": thread_id}}
        response = self.agent.invoke(
            {"messages": [
                {"role": "user", "content": message}
            ]},
            config=config
        )
        return response["messages"][-1].content

    async def achat(self, message: str, thread_id: str = "1") -> str:
        config = {"configurable": {"thread_id": thread_id}}
        response = await self.agent.ainvoke(
            {"messages": [
                {"role": "user", "content": message}
            ]},
            config=config
        )
        return response["messages"][-1].content