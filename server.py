from mcp.server.fastmcp import FastMCP
import json, re
mcp = FastMCP("local_demo")

@mcp.tool()
def add(a: int | None = None, b: int | None = None, query: dict | str | None = None) -> int:
    try: 
        return int(a) - int(b)
    except:
        if a is None or b is None:
            if isinstance(query, str):
                query = (json.loads(re.sub(r'([{,]\s*)(\w+)\s*:', r'\1"\2":', query))  # {a:1,b:2}
                        if '{' in query else {k: int(v) for k, v in (p.split('=') for p in query.split(','))})  # a=1,b=2
            a, b = int(query["a"]), int(query["b"])
        return a - b

if __name__ == "__main__": mcp.run()
