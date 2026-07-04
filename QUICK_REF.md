# Localhost to WiFi - Quick Reference

## TL;DR
1. Change your server config to listen on `0.0.0.0` instead of `localhost`
2. Find your IP: `ipconfig` (Windows) or `ifconfig` (Mac/Linux)
3. Access from other devices: `http://YOUR_IP:PORT`

---

## Framework Quick Commands

### Node.js / Express
```javascript
app.listen(3000, '0.0.0.0', () => {
  console.log('Server running on 0.0.0.0:3000');
});
```

### Next.js
```bash
npm run dev -- -H 0.0.0.0
```

### Vite
```bash
npm run dev -- --host
```

### Python FastAPI
```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

### Python Flask
```python
app.run(host='0.0.0.0', port=5000, debug=True)
```

### Django
```bash
python manage.py runserver 0.0.0.0:8000
```

---

## Get Your Local IP

**Windows:**
```powershell
ipconfig
```
Look for "IPv4 Address" (usually 192.168.x.x)

**Mac/Linux:**
```bash
ifconfig
# or
hostname -I
```

---

## Access From Other Devices

```
http://192.168.x.x:3000
```
(Replace with your actual IP and port)

---

## Troubleshooting

**Can't connect?**
- ✓ Server is running and bound to `0.0.0.0`
- ✓ IP address is correct
- ✓ Both devices on same WiFi
- ✓ Firewall isn't blocking the port

**Firewall issues (Windows)?**
- Settings → Windows Defender Firewall → Allow an app through firewall
- Add your Node.js / Python executable
