from autogen import UserProxyAgent
from agents import create_planner
from agents import create_worker
from agents import create_writer

from memory.short_term import ShortTermMemory
from memory.long_term import LongTermMemory
from config.config_loader import CONFIG

def run_multi_agent(user_input, logs):

    # Memory
    short_mem = ShortTermMemory()
    long_mem = LongTermMemory()

    # Retrieve past context
    past_context = long_mem.query(user_input)

    # Add to short-term
    short_mem.add("user", user_input)

    # Create agents
    planner = create_planner()
    worker = create_worker()
    writer = create_writer()

    user = UserProxyAgent(
        name="User",
        human_input_mode="NEVER",
        code_execution_config=False,
        max_consecutive_auto_reply=CONFIG.MAX_CONSECUTIVE_AUTO_REPLY,  #  prevents loops
    )

    # -------------------------
    # Planner
    # -------------------------
    logs.append(" Planner started...")
    plan_chat = user.initiate_chat(
        planner,
        message=f"""
        Context:
        {past_context}

        Task:
        {user_input}
        """,
        max_turns=CONFIG.PLANNER_MAX_TURNS  #  CRITICAL
    )
    plan = plan_chat.summary
    short_mem.add("planner", plan)

    # -------------------------
    # Worker
    # -------------------------
    logs.append(" Worker executing...")
    work_chat = user.initiate_chat(
        worker,
        message=f"""
        Plan:
        {plan}
        """,
        max_turns=CONFIG.WORKER_MAX_TURNS   #  CRITICAL
    )
    work = work_chat.summary
    short_mem.add("worker", work)

    # -------------------------
    # Writer
    # -------------------------
    logs.append(" Writer generating...")
    final_chat = user.initiate_chat(
        writer,
        message=f"""
        Context:
        {short_mem.get_context()}

        Generate final answer
        """,
        max_turns=CONFIG.WRITER_MAX_TURNS   #  CRITICAL
    )
    final = final_chat.summary

    # -------------------------
    # Store in long-term memory
    # -------------------------
    long_mem.add(final, metadata={"type": "final_output"})

    logs.append("Completed")

    return plan, work, final