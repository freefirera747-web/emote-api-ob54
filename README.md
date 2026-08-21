# Ahmad Emote API — Vercel

Flask API packaged for Vercel Python Functions.

## Endpoint

`/join?tc=TEAM_CODE&uid1=UID1&uid2=UID2&uid3=UID3&uid4=UID4&emote_id=EMOTE_ID`

`uid2`, `uid3`, and `uid4` are optional. Maximum supported target UIDs per request: **4**.

Health check: `/health`

## Important deployment note

Vercel runs this as a request-based Python Function. The original always-on TCP bot loop was converted to a one-shot session for `/join`: login → connect → join team → send emotes → close connections. This avoids relying on a permanent background process.

The API's actual reachable Free Fire region is returned in the JSON response as `region`; it is determined by the bot account/login service, not hard-coded by Vercel.
