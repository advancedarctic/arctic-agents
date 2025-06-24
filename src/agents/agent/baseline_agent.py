"""
Tiny baseline agent using LangGraph + a dummy tool.
No external model downloads or training.
"""

from typing import TypedDict, List
from langgraph.graph import StateGraph, END
from langchain_core.messages import HumanMessage, AIMessage, ToolMessage
from src.agents.tools.web_search import web_search

class AgentState(TypedDict):
    messages: List

def llm_node(state: AgentState):
    # Simulate a tool call request based on last user message
    user_text = state["messages"][-1].content
    simulated_ai = AIMessage(
        content=f"I will search the web for: {user_text}",
        tool_calls=[{"name": "web_search", "args": {"query": user_text}, "id": "tc1"}],
    )
    return {"messages": state["messages"] + [simulated_ai]}

def tools_node(state: AgentState):
    last = state["messages"][-1]
    if isinstance(last, AIMessage) and getattr(last, "tool_calls", None):
        for tc in last.tool_calls:
            if tc["name"] == "web_search":
                q = tc["args"]["query"]
                hits = web_search(q)
                return {"messages": state["messages"] + [ToolMessage(str(hits), tool_call_id=tc["id"])]}
    return END

def finalizer(state: AgentState):
    text = "Here are some (simulated) search hits: " + str(state["messages"][-1].content)
    return {"messages": state["messages"] + [AIMessage(content=text)]}

def main():
    graph = StateGraph(AgentState)
    graph.add_node("llm", llm_node)
    graph.add_node("tools", tools_node)
    graph.add_node("final", finalizer)
    graph.set_entry_point("llm")
    graph.add_edge("llm", "tools")
    graph.add_edge("tools", "final")
    app = graph.compile()

    state = {"messages": [HumanMessage(content="recent LoRA finetuning uses")]}
    out = app.invoke(state)
    print(out["messages"][-1].content)

if __name__ == "__main__":
    main()
