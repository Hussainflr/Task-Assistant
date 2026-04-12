from autogen import AssistantAgent
from config.config_loader import CONFIG
from tools.tool_registry import TOOLS
def create_planner():
    return AssistantAgent(
        name="Planner",
        llm_config=CONFIG.get_llm_config(),
        system_message="""
        You are a planner.
        Break tasks into simple, clear steps.
        """
    )


def create_worker():
    def tool_handler(message):
        for tool_name, tool_func in TOOLS.items():
            if tool_name in message.lower():
                return tool_func(message)
        return "No tool used"

    return AssistantAgent(
        name="Worker",
        llm_config=CONFIG.get_llm_config(),
        system_message="""
        You execute tasks.
        If a task involves calculation, use calculator.
        If it involves finding info, use search.
        """,
        function_map={
            "search": TOOLS["search"],
            "calculator": TOOLS["calculator"]
        }
    )


def create_writer():
    return AssistantAgent(
        name="Writer",
        llm_config=CONFIG.get_llm_config(),
        system_message="""
        You generate clean, structured final answers.
        """
    )