"""What's popular on Faxo right now, through Faxo's MCP server. No account, no packages.

    python3 public_feed.py
"""
import json
import urllib.request

FAXO_MCP = "https://faxo.com/mcp"


def call_tool(name, arguments=None):
    body = json.dumps({
        "jsonrpc": "2.0",
        "id": 1,
        "method": "tools/call",
        "params": {"name": name, "arguments": arguments or {}},
    }).encode()
    request = urllib.request.Request(FAXO_MCP, data=body, headers={
        "Content-Type": "application/json",
        "Accept": "application/json, text/event-stream",
    })
    with urllib.request.urlopen(request, timeout=30) as response:
        result = json.load(response)["result"]
    if result.get("isError"):
        raise RuntimeError(result["structuredContent"]["errors"][0]["message"])
    return result["structuredContent"]


if __name__ == "__main__":
    for post in call_tool("get_public_feed")["posts"][:10]:
        words = (post.get("title") or post.get("content") or "").replace("\n", " ")[:70]
        print(f"{post.get('likes', 0):>5} likes  {post.get('author', '')}: {words}")
        print(f"             {post['url']}")
