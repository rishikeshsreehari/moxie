# Reddit Intel Scanner — Quick Start

Run this on your laptop/macOS/Linux to gather founder profiles + subreddit intel for FormBeep (and any other SapiensTech project).

## 1. Install PRAW

```bash
python3 -m pip install --upgrade praw
```

## 2. Create a Reddit App

1. Go to https://www.reddit.com/prefs/apps
2. Click “create app”
3. Fill:
   - name: `SapiensTech Intel`
   - type: **script**
   - description: `Internal research scanner for SapiensTech portfolio`
   - about url: can be blank or your site
   - redirect uri: `http://localhost:8080`
4. Click “create app”
5. Copy:
   - `client_id` (under the app name)
   - `client_secret`

## 3. Save Credentials File

Create `~/.reddit_sapiensch.json`:

```json
{
  "client_id": "YOUR_CLIENT_ID",
  "client_secret": "YOUR_CLIENT_SECRET",
  "username": "YOUR_REDDIT_USERNAME",
  "password": "YOUR_REDDIT_PASSWORD",
  "user_agent": "SapiensTechIntel/0.1 by u/YOUR_USERNAME"
}
```

Keep this file private; don’t share or commit.

## 4. Run the Scanner

```bash
cd /root/moxie_hq/products/formbeep/outreach
python3 reddit_intel_scanner.py
```

Outputs `reddit_intel_brief.md` in the same folder.

## 5. Use the Brief

The markdown contains:
- Top subreddits each founder posts in
- Copy hooks that performed well
- Signal from target subreddits (SaaS, Entrepreneur, etc.)
- Concrete posting recommendations
- Raw appendix for deeper review

## Notes

- This uses the “script” app type; token is valid ~1 hour. For repeated use, consider switching to a “web app” with refresh tokens (more secure, avoids storing password).
- The scan is read-only and complies with Reddit’s Data API policy for internal research.
- Do not automate posting from this scanner; it’s for intel only. Manual posting is already covered by the content packs.
