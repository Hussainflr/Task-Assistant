import yaml
from pathlib import Path


class Config:
    def __init__(self, path="config/config.yaml"):
        self._path = Path(path)
        self._config = self._load()

        # -------------------------
        # LLM
        # -------------------------
        self.LLM_PROVIDER = self._config["llm"]["provider"]
        self.LLM_MODEL = self._config["llm"]["model"]
        self.LLM_API_KEY = self._config["llm"]["api_key"]
        self.LLM_BASE_URL = self._config["llm"]["base_url"]
        self.LLM_TEMPERATURE = self._config["llm"]["temperature"]
        self.LLM_MAX_TOKENS = self._config["llm"]["max_tokens"]

        # -------------------------
        # AGENTS
        # -------------------------
        self.MAX_CONSECUTIVE_AUTO_REPLY = self._config["agents"]["max_consecutive_auto_reply"]
        self.PLANNER_MAX_TURNS = self._config["agents"]["planner"]["max_turns"]
        self.PLANNER_MAX_AUTO_REPLY = self._config["agents"]["planner"]["max_auto_reply"]

        self.WORKER_MAX_TURNS = self._config["agents"]["worker"]["max_turns"]
        self.WORKER_MAX_AUTO_REPLY = self._config["agents"]["worker"]["max_auto_reply"]

        self.WRITER_MAX_TURNS = self._config["agents"]["writer"]["max_turns"]
        self.WRITER_MAX_AUTO_REPLY = self._config["agents"]["writer"]["max_auto_reply"]

        # -------------------------
        # MEMORY
        # -------------------------
        self.SHORT_TERM_MAX_MSG = self._config["memory"]["short_term"]["max_messages"]

        self.LONG_TERM_TOP_K = self._config["memory"]["long_term"]["top_k"]
        self.LONG_TERM_ENABLED = self._config["memory"]["long_term"]["enable"]

        # -------------------------
        # TOOLS
        # -------------------------
        self.ENABLE_SEARCH = self._config["tools"]["enable_search"]
        self.ENABLE_CALCULATOR = self._config["tools"]["enable_calculator"]

        # -------------------------
        # PERFORMANCE
        # -------------------------
        self.FAST_MODE = self._config["performance"]["fast_mode"]
        self.SIMPLE_KEYWORDS = self._config["performance"]["simple_task_keywords"]
        self.SKIP_MEMORY_SIMPLE = self._config["performance"]["skip_memory_for_simple"]
        self.SKIP_TOOLS_SIMPLE = self._config["performance"]["skip_tools_for_simple"]

        # -------------------------
        # DEBUG
        # -------------------------
        self.VERBOSE = self._config["debug"]["verbose_logs"]
        self.PRINT_CHAT = self._config["debug"]["print_chat_history"]

    def _load(self):
        if not self._path.exists():
            raise FileNotFoundError(f"Config file not found: {self._path}")

        with open(self._path, "r") as f:
            return yaml.safe_load(f)

    # -------------------------
    # Helper Functions
    # -------------------------
    def is_simple_task(self, text: str) -> bool:
        return any(k in text.lower() for k in self.SIMPLE_KEYWORDS)

    def get_llm_config(self):
        return {
            "config_list": [
                {
                    "model": self.LLM_MODEL,
                    "base_url": self.LLM_BASE_URL,
                    "api_key": self.LLM_API_KEY
                }
            ]
        }


# -------------------------
# Singleton Instance
# -------------------------
CONFIG = Config()