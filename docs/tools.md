# Faxo MCP tools

Server: `https://faxo.com/mcp` (MCP over Streamable HTTP, JSON responses, stateless).

Every tool returns its answer twice, as MCP asks: as `structuredContent` (an object) and as one `text`
content block holding the same JSON. When a tool refuses (a limit, a missing permission, nothing
found), it returns `isError: true` with `{"errors": [{"message": "…"}]}`, and the message is written to
be shown to the person as it is.

Annotations on every tool: `title`, `readOnlyHint`, `destructiveHint`, `idempotentHint` and
`openWorldHint`. Read tools are `readOnlyHint: true`; the two that publish are `destructiveHint: true`,
which is what makes assistants ask first.

A post in any answer looks like this (fields with no value are left out):

```json
{
  "id": "4469423",
  "status": "published",
  "url": "https://faxo.com/…",
  "title": "Sunrise hike",
  "content": "Woke up above the clouds this morning.",
  "thumbnail": "https://…",
  "created_at": "2026-11-25T14:03:11Z",
  "likes": 12,
  "comments": 3,
  "views": 240
}
```

Posts in the public feed and in Marketplace results also carry `author` and `author_url`.

---

## get_me

The signed-in Faxo account: its name, handle and profile link. Scope `faxo:read`. No input.

```json
{ "id": "123456", "handle": "analopez", "display_name": "Ana Lopez", "url": "https://faxo.com/analopez" }
```

## get_notifications

The person's recent notifications in plain words: who liked or commented on their posts, friend
requests and new friends, with links. Scope `faxo:read`.

| Input | Type | |
|---|---|---|
| `limit` | integer 1–50 | default 20 |

```json
{ "notifications": [
  { "who": "Kim Park", "who_url": "https://faxo.com/kimpark", "what": "liked your post",
    "post": "Sunrise hike", "post_url": "https://faxo.com/…", "at": "2026-11-25T14:20:00Z" }
] }
```

## list_my_posts

The person's own posts, newest first, a page at a time. Scope `faxo:read`.

| Input | Type | |
|---|---|---|
| `limit` | integer 1–50 | default 20 |
| `cursor` | string | `next_cursor` from the previous page; leave out for the newest |

```json
{ "posts": [ /* posts */ ], "next_cursor": "…" }
```

`next_cursor` is `null` on the last page.

## get_post

One of the person's own posts, by its id or its faxo.com link. Scope `faxo:read`.

| Input | Type | |
|---|---|---|
| `id` | string | required: the post's id or link |

Returns one post, or an error when it isn't the person's own post.

## get_public_feed

Popular public posts on Faxo right now: who posted, what it says, a thumbnail, likes, comments and a
link. **Works without signing in.** No input.

```json
{ "posts": [ /* posts, with author and author_url */ ] }
```

## search_marketplace

Search Faxo Marketplace listings (things people sell). Scope `faxo:read`.

| Input | Type | |
|---|---|---|
| `query` | string | required, e.g. `"road bike"` or `"iPhone 15"` |
| `limit` | integer 1–30 | default 20 |

```json
{ "listings": [ { /* post fields */ "price": "$350", "author": "Ana", "author_url": "https://faxo.com/…" } ] }
```

## create_post

Publish a public text post on the person's profile. Text only: no photos, drafts or scheduling.
Scope `faxo:write`. `destructiveHint: true`: assistants show the words and ask first.

| Input | Type | |
|---|---|---|
| `content` | string, up to 500 characters | required: the post exactly as it should appear |

Returns the new post.

## comment_on_post

Comment on a Faxo post as the signed-in person. Scope `faxo:write`. `destructiveHint: true`.

| Input | Type | |
|---|---|---|
| `post_id` | string | required: the post's id or faxo.com link |
| `text` | string, up to 1,000 characters | required: the comment exactly as it should appear |

```json
{ "id": "4480210", "post_id": "4469423", "post_url": "https://faxo.com/…", "comment": "Congrats!" }
```

---

## Limits

| | |
|---|---|
| Reads | 500 a day per person |
| Changes | 5 a minute; 20 posts and 50 comments a day |

Over a limit, the tool refuses with a message saying so. Posts and comments also pass Faxo's usual
spam and scam checks, which can refuse them.

## Who can connect

Adults with a Faxo account in good standing. Teen accounts and suspended accounts are refused, and
Faxo can turn assistant access down to read-only or off for everyone if it ever needs to.
