# Signing in

Faxo's MCP server uses OAuth 2.1 the way the MCP specification describes, so MCP clients (ChatGPT,
Claude, Claude Code, Cursor, VS Code…) handle it on their own. This page is for people building their
own client.

## Discovery

A call without a token to a tool that needs one gets `401` with a `WWW-Authenticate` header. The
metadata is public:

- Protected resource: `https://faxo.com/.well-known/oauth-protected-resource`
  (`resource: https://faxo.com/mcp`, `authorization_servers: ["https://faxo.com"]`)
- Authorization server: `https://faxo.com/.well-known/oauth-authorization-server`

| | |
|---|---|
| Authorize | `https://faxo.com/oauth/authorize` |
| Token | `https://faxo.com/oauth/token` |
| Dynamic client registration | `https://faxo.com/oauth/registration` |
| Grants | `authorization_code` (with PKCE, `S256`), `refresh_token` |
| Client auth | `none` (public clients) or `client_secret_basic` |
| Scopes | `faxo:read`, `faxo:write` |

## Scopes

- `faxo:read`: the person's account, notifications and posts, the public feed and Marketplace.
- `faxo:write`: also posting and commenting as the person.

The person chooses on Faxo's consent screen and can disconnect any client later in Faxo's
Settings › Connected Apps, which revokes its tokens.

## Calling a tool

Send the access token as a bearer token:

```sh
curl -s https://faxo.com/mcp \
  -H "Authorization: Bearer $FAXO_TOKEN" \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json, text/event-stream' \
  -d '{"jsonrpc":"2.0","id":1,"method":"tools/call","params":{"name":"get_notifications","arguments":{"limit":5}}}'
```

Never put a token in a URL, a log or a repository.
