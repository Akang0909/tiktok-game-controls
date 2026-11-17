TIKTOK LIVE STUDIO — HOSTED GAME CONTROLS OVERLAY

IMPORTANT
A hosted static webpage cannot directly read keyboard input from your PC.
This setup hosts the visual overlay online, while a local Python helper reads
only the game keys you listed. A Cloudflare Quick Tunnel securely relays those
events to the hosted page. The tunnel URL is temporary and may change whenever
you restart it, so update WS_URL in overlay.html and republish when it changes.

PART 1 — PUBLISH THE WEBSITE FOR FREE
1. Sign in or create a free account at https://github.com/
2. Create a new PUBLIC repository named: tiktok-game-controls
3. Upload overlay.html from this folder to the repository root.
4. Open the repository's Settings > Pages.
5. Under "Build and deployment", choose "Deploy from a branch".
6. Select branch "main" and folder "/ (root)", then Save.
7. Wait for GitHub Pages to publish. Your page will be:
   https://YOUR-GITHUB-USERNAME.github.io/tiktok-game-controls/
   (Replace YOUR-GITHUB-USERNAME with your GitHub username.)

PART 2 — RUN THE LOCAL KEYBOARD TRACKER
1. Install Python 3 from https://www.python.org/downloads/
2. Open Command Prompt in this extracted folder.
3. Run:
   py -m pip install pynput websockets
4. Start the helper:
   py input_helper.py
   Keep this window open.

PART 3 — CREATE A SECURE CONNECTION
1. Download Cloudflare's cloudflared for Windows:
   https://developers.cloudflare.com/cloudflare-one/connections/connect-networks/downloads/
2. Open a SECOND Command Prompt window.
3. Run (if cloudflared is in your PATH):
   cloudflared tunnel --url http://localhost:8765
4. Wait for a URL ending in .trycloudflare.com, shown in the terminal.
5. Copy the hostname and change the first part from https:// to wss://.
   Example: https://abc.trycloudflare.com becomes
            wss://abc.trycloudflare.com
6. Open overlay.html in a text editor and replace:
   wss://YOUR-TUNNEL-NAME.trycloudflare.com
   with your actual wss:// URL.
7. Save overlay.html, upload the updated file to the same GitHub repository,
   and wait for Pages to redeploy.

PART 4 — ADD IT TO TIKTOK LIVE STUDIO
1. Open TikTok LIVE Studio.
2. Add a Browser Source (sometimes listed under Sources > Add source > Browser).
3. Paste your GitHub Pages URL:
   https://YOUR-GITHUB-USERNAME.github.io/tiktok-game-controls/
4. Set width to 1000 and height to 430.
5. Position and resize the overlay on your stream layout.

WHEN YOU STREAM AGAIN
- Start input_helper.py.
- Start cloudflared tunnel in the second Command Prompt.
- If the Quick Tunnel URL changed, update WS_URL in overlay.html and republish.
- Open/refresh the Browser Source in TikTok LIVE Studio.

NOTES
- GitHub Pages hosting is free for public repositories.
- Cloudflare Quick Tunnels are free for testing and do not require a domain, but
  their random hostname is not a permanent fixed URL.
- The helper listens only for A, D, W, S, Space, R, F, E and 1–5.
- It does not save or transmit keystrokes to an unrelated service. The tunnel
  carries only the key names and pressed/released state to the overlay.
- Do not share your tunnel URL publicly; anyone who knows it could connect to
  the relay while it is running.
- Some games or anti-cheat systems may block global keyboard hooks.
