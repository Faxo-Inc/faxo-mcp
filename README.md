# Faxo MCP

Faxo is the AI Everything App: social, messaging, Marketplace, local, business, dating and a wallet in
one account. **Faxo's MCP server lets any AI assistant or agent use Faxo for a person, with their
permission.** It's the same server behind **Faxo for ChatGPT** and **Faxo for Claude**.

```
https://faxo.com/mcp
```

It speaks the [Model Context Protocol](https://modelcontextprotocol.io) over Streamable HTTP, signs
people in with OAuth 2.1, and every tool says whether it only reads or changes something, so
assistants ask the person before anything is posted.

We think the people who use Faxo should be able to bring the assistant of their choice, so the
interface is open and documented here. Issues and ideas are welcome.

## Connect in a minute

| Where | How |
|---|---|
| **ChatGPT** | Add the [Faxo plugin](https://chatgpt.com/plugins/plugin_asdk_app_6b01f57306088191b34023b1a6a25ba2), then type `@faxo` in a chat. |
| **Claude** (claude.ai, desktop, mobile) | Settings › Connectors › Add custom connector › `https://faxo.com/mcp` |
| **Claude Code** | `claude mcp add --transport http faxo https://faxo.com/mcp` |
| **Cursor, VS Code and other MCP clients** | Add a remote (HTTP) server with the URL `https://faxo.com/mcp`, e.g. `{"mcpServers": {"faxo": {"url": "https://faxo.com/mcp"}}}` |

The first time, your client opens Faxo's sign-in. Sign in and choose what the assistant may do:
**read** (`faxo:read`), or **read and post** (`faxo:write`). Disconnect any time in Faxo's
Settings › Connected Apps.

Then just ask: *"Anything I missed on Faxo?"*, *"How did my last post do?"*, *"Find a road bike on
Faxo Marketplace"*, *"Post this to Faxo."*

## Try it without an account

One tool, `get_public_feed`, works without signing in:

```sh
curl -s https://faxo.com/mcp \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json, text/event-stream' \
  -d '{"jsonrpc":"2.0","id":1,"method":"tools/call","params":{"name":"get_public_feed","arguments":{}}}'
```

Or run [`examples/python/public_feed.py`](examples/python/public_feed.py) or
[`examples/node/public-feed.mjs`](examples/node/public-feed.mjs) (no packages needed).

## Tools

| Tool | What it does | Needs |
|---|---|---|
| [`get_me`](docs/tools.md#get_me) | The signed-in account: name, handle, profile link | `faxo:read` |
| [`get_notifications`](docs/tools.md#get_notifications) | Recent notifications in plain words: likes, comments, friend requests, new friends | `faxo:read` |
| [`list_my_posts`](docs/tools.md#list_my_posts) | Your own posts, newest first, with likes, comments and views | `faxo:read` |
| [`get_post`](docs/tools.md#get_post) | One of your own posts by id or link | `faxo:read` |
| [`get_public_feed`](docs/tools.md#get_public_feed) | Popular public posts right now | nothing |
| [`search_marketplace`](docs/tools.md#search_marketplace) | Marketplace listings: title, price, seller, link | `faxo:read` |
| [`create_post`](docs/tools.md#create_post) | Publish a public text post (up to 500 characters) | `faxo:write` |
| [`comment_on_post`](docs/tools.md#comment_on_post) | Comment on a post as you | `faxo:write` |

Full inputs and outputs: [docs/tools.md](docs/tools.md). How sign-in works:
[docs/auth.md](docs/auth.md).

## Safety, built in

- **Asks first.** `create_post` and `comment_on_post` are marked destructive, so ChatGPT, Claude and
  other well-behaved clients show the person the exact words and ask before running them.
- **No money.** No tool can see payments or Credits, or move money.
- **No private messages.** No tool reads anyone's messages.
- **Adults only.** Teen accounts can't connect. No adult content in answers.
- **Limits.** 500 reads a day; at most 5 changes a minute, 20 posts and 50 comments a day. Posts and
  comments go through Faxo's usual spam and scam checks, and every call is logged.
- **Marked.** Posts made through an assistant are recorded as such.

## Coming next

- More of Faxo as tools: Messages, Jobs, Local, business tools for Pages ("Your Business on
  Autopilot"), each with the same ask-first rules.
- The **Faxo Agent API**: build your own agent that lives on Faxo, with its own account, chats and
  buttons, like a Telegram bot.

Follow this repo to hear when they open.

## Links

- Faxo for ChatGPT: https://faxo.com/chatgpt
- Faxo for Claude: https://faxo.com/claude
- Privacy: https://faxo.com/privacy
- Help: support@faxo.com

MIT licensed (the docs and examples in this repo). Faxo is a trademark of Faxo Inc.
