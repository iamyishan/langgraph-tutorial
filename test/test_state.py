from typing import TypedDict, Annotated, List
from langgraph.graph import StateGraph


# 定义Reducer：追加消息
def add_messages(old: List[str], new: List[str]) -> List[str]:
    return old + new


# 定义状态
class State(TypedDict):
    messages: Annotated[List[str], add_messages]


# 创建状态图
graph = StateGraph(State)


# 节点1：添加消息
def node1():
    return {"messages": ["Node1 says hello!"]}


# 节点2：添加另一条消息
def node2():
    return {"messages": ["Node2 responds!"]}


# 添加节点并设置入口
graph.add_node("node1", node1)
graph.add_node("node2", node2)
graph.set_entry_point("node1")
graph.add_edge("node1", "node2")

# 编译并执行
app = graph.compile()
final_state = app.invoke({"messages": []})  # 初始状态为空列表

print(final_state["messages"])
# 输出：['Node1 says hello!', 'Node2 responds!']
