---
name: localhost-to-wifi
description: Expose localhost development servers to your WiFi network. Use this when you need to access a development server (localhost:3000, etc.) from other devices on your home network, test on mobile devices, or share your work with others on the same WiFi. The skill detects your project type (Node.js, Python/Flask, Python/FastAPI, etc.) and provides framework-specific configuration instructions, network setup guidance, and firewall troubleshooting.
compatibility: Works with any framework that has a development server. Requires Node.js, Python, or similar runtime already installed.
---

# Localhost to WiFi

Make your development server accessible to all devices on your network.

## Quick Start

1. **Detect your project** — The skill will identify your framework based on project files
2. **Configure binding** — Update your server config to listen on `0.0.0.0` instead of `localhost`
3. **Find your IP** — Get your machine's local network IP address
4. **Access from other devices** — Open `http://<YOUR_IP>:PORT` on any device on the same WiFi

---

## Framework Detection & Configuration

Paste or describe your project structure, or answer these questions:

**What files do you see in your project root?**
- `package.json` + `server.js` / `index.js` → **Node.js/Express**
- `requirements.txt` + `app.py` → **Python/Flask or Django**
- `pyproject.toml` + `main.py` + `from fastapi` → **Python/FastAPI**
- `next.json` or `.next/` → **Next.js**
- `vite.config.js` → **Vite**
- Other?

Once identified, the skill will provide the exact code change needed.

---

## Node.js / Express

**In your main server file (e.g., `server.js`, `index.js`, `app.js`):**

```javascript
// BEFORE (default - only accessible on localhost)
app.listen(3000, () => {
  console.log('Server running on localhost:3000');
});

// AFTER (accessible on all interfaces)
app.listen(3000, '0.0.0.0', () => {
  console.log('Server running on 0.0.0.0:3000');
});
```

**Alternative with host variable:**
```javascript
const HOST = '0.0.0.0';
const PORT = 3000;
app.listen(PORT, HOST, () => {
  console.log(`Server running on ${HOST}:${PORT}`);
});
```

---

## Python / Flask

**In your Flask app file (e.g., `app.py`):**

```python
# BEFORE
if __name__ == '__main__':
    app.run(debug=True)

# AFTER
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)
```

Or use environment variables:
```python
import os
HOST = os.getenv('HOST', '0.0.0.0')
PORT = int(os.getenv('PORT', 3000))
app.run(host=HOST, port=PORT, debug=True)
```

---

## Python / FastAPI

**Using `uvicorn` directly:**

```bash
uvicorn main:app --host 0.0.0.0 --port 3000 --reload
```

**In your code:**
```python
import uvicorn

if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=3000, reload=True)
```

---

## Next.js / Vite / SvelteKit / Other Modern Frameworks

Most modern frameworks have a `--host` flag or config option:

**Next.js (dev mode):**
```bash
npm run dev -- -H 0.0.0.0
```
Or in `next.config.js`:
```javascript
module.exports = {
  // ... other config
  server: {
    host: '0.0.0.0'
  }
}
```

**Vite:**
```bash
npm run dev -- --host
```

**SvelteKit:**
```bash
npm run dev -- --host 0.0.0.0
```

Check your framework's docs for the equivalent flag.

---

## Finding Your Local IP Address

Once your server is bound to `0.0.0.0`, you need to find what IP address other devices should use.

**Windows (PowerShell):**
```powershell
ipconfig
```
Look for the "IPv4 Address" under your active WiFi adapter. Typically looks like: `192.168.x.x` or `10.0.x.x`

**Mac / Linux:**
```bash
ifconfig
# or
hostname -I
```
Look for your WiFi adapter (en0, wlan0, etc.) and the `inet` or `inet addr` value.

**Quick browser method:**
1. Go to `http://localhost:3000` on your machine (confirm it works)
2. Open a terminal on another device on the same WiFi
3. Ping your machine's hostname: `ping COMPUTERNAME.local`
4. Use the IP from the ping response

---

## Access from Other Devices

On **any device on the same WiFi network**:

```
http://YOUR_LOCAL_IP:3000
```

**Examples:**
- `http://192.168.1.50:3000`
- `http://10.0.0.42:3000`

### Common Issues

**"Connection refused" or "Cannot reach server"**
- Double-check your server is running and bound to `0.0.0.0`
- Verify the IP address is correct (rerun `ipconfig` / `ifconfig`)
- Check that both devices are on the same WiFi network
- Try pinging: `ping YOUR_LOCAL_IP` from the other device

**Server won't start after changes**
- Check for typos in the host/port config
- Make sure no other process is using port 3000: 
  - Windows: `netstat -ano | findstr :3000`
  - Mac/Linux: `lsof -i :3000`
- Try a different port (e.g., 5000, 8000)

---

## Firewall & Network Permissions

If the connection times out or is blocked:

**Windows Defender Firewall:**
1. Settings → Privacy & Security → Windows Defender Firewall
2. Click "Allow an app through firewall"
3. Find your Node.js, Python, or application in the list
4. Check both "Private" and "Public" (or just "Private" if you only use home WiFi)
5. Click OK

**Mac Firewall:**
1. System Settings → Network → Firewall Options
2. Add your app or allow incoming connections for port 3000

**Linux (ufw):**
```bash
sudo ufw allow 3000/tcp
```

---

## For Peachron, OPENROAD, and Other Projects

**Next.js (Peachron frontend):**
```bash
npm run dev -- -H 0.0.0.0
```

**FastAPI (Peachron backend, OPENROAD backend):**
In your startup script or terminal:
```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

Now you can test your app from your phone or another laptop on the same network!

---

## Pro Tips

1. **Use a `.env` file for flexibility:**
   ```
   HOST=0.0.0.0
   PORT=3000
   ```
   Then reference in your code — this lets you switch between localhost and network access easily.

2. **Test responsive design:** Open your app on a phone/tablet while developing to catch layout issues early.

3. **Consistent port naming:** Document which ports your services use:
   - Frontend: 3000 (Next.js)
   - Backend: 8000 (FastAPI)
   - Database: 5432 (Postgres)

4. **Keep your IP handy:** If you're developing frequently, bookmark or note your local IP so you don't have to look it up each time.

