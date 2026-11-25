# Faxo MCP tools: v2 preview

These tools are rolling out. They're live for testers now and open to everyone once v2 is
approved in ChatGPT's and Claude's directories. Same server, same sign-in: `https://faxo.com/mcp`.

Tools that change something are marked `destructiveHint: true`, so assistants show the person
exactly what will happen and ask before running them, and they need the `faxo:write` scope.
Every tool answers with `{"result": "…"}` (plain words to show the person), or `isError: true`
with `{"errors": [{"message": "…"}]}`.

_Generated from Faxo's action list (FaxoActions). Don't edit by hand._

## search_jobs

Search jobs on Faxo by title or skill and place (a city, or "remote"), posted in the last 2 weeks. Returns up to 5 with title, company, place and pay.

- **Changes something:** no (`faxo:read`)
- **Who:** Adults

| Input | Type | |
|---|---|---|
| `query` | string | required: Job title or skill, e.g. "product manager" |
| `where` | string | A city, or "remote"; leave out for anywhere |

## whats_waiting

What is waiting for the person on Faxo right now: people whose messages they haven't read (names), customers waiting on their business Pages, friend requests, new notifications.

- **Changes something:** no (`faxo:read`)
- **Who:** Everyone

## find_places

Restaurants, cafes, bars, shops and other places near the person on Faxo (or in a city they name), with address, hours, live deals and whether the place takes bookings on Faxo.

- **Changes something:** no (`faxo:read`)
- **Who:** Everyone

| Input | Type | |
|---|---|---|
| `query` | string | What kind of place, e.g. "thai food", "coffee", "barber" |
| `city` | string | A city, e.g. "Austin" or "Austin, TX"; leave out for near them |

## find_events

Events on Faxo in the next two weeks near the person (or in a city they name): name, day and time, and place.

- **Changes something:** no (`faxo:read`)
- **Who:** Everyone

| Input | Type | |
|---|---|---|
| `query` | string | A word to match, e.g. "comedy" or "jazz"; leave out for all |
| `city` | string | A city; leave out for near them |

## apply_to_job

Apply to a job posted on Faxo (one marked Easy Apply on Faxo, by its job id) with the person’s Faxo profile and an optional short note to the employer.

- **Changes something:** yes (asks first; `faxo:write`)
- **Who:** Adults

| Input | Type | |
|---|---|---|
| `job_id` | integer | required: The Faxo job id from the job search |
| `note` | string | A short note to the employer in the person’s words; leave out if none |

## rsvp_event

Mark the person as Going to an event on Faxo (by its id from the event search), so they get its reminders and chat.

- **Changes something:** yes (asks first; `faxo:write`)
- **Who:** Everyone

| Input | Type | |
|---|---|---|
| `event_id` | integer | required: The event id from the event search |

## start_plan

Start a plan with the person’s Faxo friends: a title, up to 3 times to vote on and up to 3 places. The friends named are invited and vote in Faxo.

- **Changes something:** yes (asks first; `faxo:write`)
- **Who:** Everyone

| Input | Type | |
|---|---|---|
| `title` | string | required: What it is, e.g. "Dinner" |
| `times` | list of string | Up to 3 times, in their local time, as "YYYY-MM-DD HH:MM" |
| `friends` | list of string | required: Friends’ names to invite |
| `places` | list of string | Up to 3 place names to vote on; leave out for none |

## reply_to_chat

Send a message to someone the person already has a chat with on Faxo (by name, e.g. from what is waiting), as the person. Only people they already chat with; never someone new.

- **Changes something:** yes (asks first; `faxo:write`)
- **Who:** Everyone

| Input | Type | |
|---|---|---|
| `name` | string | required: The person’s name as Faxo shows it, e.g. "Kim Park" or "Kim" |
| `text` | string | required: The message exactly as it should be sent |

