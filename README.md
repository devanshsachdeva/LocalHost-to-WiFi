# 🌐 Localhost to WiFi

> Access your development server from any device on your WiFi network — test on your phone, tablet, or laptop without USB.

## The Problem

Your development server runs on localhost:3000, but you can only access it from your computer. You want to:

- ✅ Test your app on your phone (responsive design, touch interactions)
- ✅ Show your work to colleagues on their devices (same WiFi)
- ✅ Test across multiple devices (phone, tablet, desktop)
- ✅ No USB cables, no setup — just open a URL

## The Solution

Bind your dev server to 0.0.0.0 instead of localhost, then access it from any device on your network using your machine's local IP.

Before:  localhost:3000         (only you, same machine)
After:   http://<YOUR_IP>:3000  (anyone on your WiFi)

---

## Quick Start

### 1. Find Your Local IP

**macOS / Linux:**
Open Terminal and find your WiFi IP address (look for something like 192.168.x.x or 10.0.x.x)

**Windows:**
Open PowerShell and find your WiFi IPv4 Address (look for something like 192.168.x.x or 10.0.x.x)

### 2. Bind Your Dev Server to 0.0.0.0

Change your dev server to listen on all network interfaces (0.0.0.0) instead of just localhost. This varies by framework:

- **Node.js / Express:** Change app.listen(3000) to include '0.0.0.0' as the host
- **Next.js:** Add --host flag to dev command or configure in next.config.js
- **Vite:** Run with --host flag
- **React (Create React App):** Set HOST=0.0.0.0 in environment
- **Python Flask:** Change app.run() to use host='0.0.0.0'
- **FastAPI + Uvicorn:** Add --host 0.0.0.0 to uvicorn command
- **Django:** Run with 0.0.0.0:8000 as server address
- **Ruby on Rails:** Run with -b 0.0.0.0 flag
- **Go:** Update http.ListenAndServe() to use "0.0.0.0" as host

For specific instructions, check your framework's official documentation on binding to all network interfaces.

### 3. Access from Another Device

On any device on the same WiFi, open:

http://<YOUR_IP>:3000

Replace <YOUR_IP> with the IP you found in step 1.

---

## Examples

### Testing Responsive Design

1. Start your dev server on 0.0.0.0
2. Open the URL on your phone
3. Test touch interactions and viewport sizes in real-time
4. Edit code on your computer and refresh phone to see changes instantly

### Demo to Your Team

1. Everyone connects to the same WiFi
2. You give them your URL
3. All of you see the same app, synchronized

### Multi-Device Testing

Test on multiple devices simultaneously:
- iPhone
- iPad
- Android phone
- Desktop browser

All using the same URL from your machine's local IP.

---

## Troubleshooting

### "Connection refused" or "Can't reach server"

1. Verify your dev server is running
2. Check you changed from localhost to 0.0.0.0
3. Verify the IP address (run the IP command again — it can change)
4. Confirm both devices are on the same WiFi network
5. Test locally first on your computer to isolate the issue

### Firewall is Blocking

Your firewall may be blocking the port.

**macOS:**
- Go to System Settings → Network → Firewall Options
- Allow incoming connections for your development tool

**Windows:**
- Go to Windows Defender Firewall → Allow an app through firewall
- Find your development tool and check "Private"

**Linux:**
- Use your firewall tool to allow the port

### IP Changed (Reconnected to WiFi)

Local IPs change when you reconnect. Run the IP command again to get the new address.

**Tip:** Set a static IP for your dev machine in router settings so it never changes.

---

## Security Notes

⚠️ Your app is now accessible to anyone on your WiFi.

- ✅ Safe on home/private WiFi (trusted devices only)
- ✅ Safe on office WiFi (controlled access)
- ⚠️ Avoid on public WiFi (coffee shops, libraries, airports)
- ⚠️ Don't put secrets in the URL (API keys, tokens, passwords)
- ✅ Use environment variables for sensitive data
- ✅ Never share your URL publicly — it exposes your local IP

---

## Common Questions

**Q: Will my internet speed be slower?**
A: No. You're on your local network (LAN), which is much faster than the internet.

**Q: Can I access it from outside my WiFi?**
A: Not directly. You'd need a VPN or port forwarding (advanced setup).

**Q: What if I forget to change it back to localhost?**
A: When you disconnect from WiFi, 0.0.0.0 still works — it just binds to all network interfaces. No problem.

**Q: Does this work on mobile hotspots?**
A: Yes! Any WiFi network (home, hotspot, office) works the same way.

---

## Framework Summary

Most modern frameworks have built-in flags to bind to all interfaces:

- Node.js / Express: Modify listen configuration
- Next.js: Use --host flag or config
- Vite: Use --host flag
- React (CRA): Set HOST environment variable
- Python frameworks: Set host parameter in run() method
- Ruby on Rails: Use -b 0.0.0.0 flag
- Go: Set host in ListenAndServe

Check your specific framework's documentation for the exact method.

---

## Tips & Tricks

### Set a Static Local IP

Prevent your IP from changing each time you reconnect:

1. Open your router settings
2. Find DHCP settings for reserved/static IPs
3. Reserve an IP for your machine's MAC address
4. Your IP stays the same

### Bookmark the URL

Add to your phone's home screen for quick access without typing the IP each time.

---

## License

MIT License — Use freely and modify as needed.

---

**Made for developers who test everywhere.** 📱💻
