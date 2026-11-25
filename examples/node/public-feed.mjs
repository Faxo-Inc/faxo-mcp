// What's popular on Faxo right now, through Faxo's MCP server. No account, no packages (Node 18+).
//
//   node public-feed.mjs

const FAXO_MCP = 'https://faxo.com/mcp';

async function callTool(name, args = {}) {
  const response = await fetch(FAXO_MCP, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json', Accept: 'application/json, text/event-stream' },
    body: JSON.stringify({ jsonrpc: '2.0', id: 1, method: 'tools/call', params: { name, arguments: args } }),
  });
  const { result } = await response.json();
  if (result.isError) throw new Error(result.structuredContent.errors[0].message);
  return result.structuredContent;
}

const { posts } = await callTool('get_public_feed');
for (const post of posts.slice(0, 10)) {
  const words = (post.title || post.content || '').replace(/\n/g, ' ').slice(0, 70);
  console.log(`${String(post.likes ?? 0).padStart(5)} likes  ${post.author ?? ''}: ${words}`);
  console.log(`             ${post.url}`);
}
