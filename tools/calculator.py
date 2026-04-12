def calculator_tool(expression: str) -> str:
    try:
        result = eval(expression)
        return f"Result: {result}"
    except Exception:
        return "Invalid calculation"