from langchain_core.runnables import RunnableLambda

runnable = RunnableLambda(lambda x: x.upper())
res = runnable.invoke("hello")  # "HELLO"

print(res)

print(runnable.batch(["a", "b", "c"]) )
for chunk in runnable.stream("hello"):
    print(chunk)