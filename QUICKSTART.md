# Chipi AI - Quick Start Guide

## What You Have

Three main files have been created:

1. **chipi_server.py** - Python Flask backend
2. **chipi-chatbot-api.html** - Web interface with API connection
3. **training_data.json** - AI training data (auto-created)

Plus support files:
- requirements.txt - Python dependencies
- README.md - Full documentation

## Fast Setup (3 Steps)

### Step 1: Install Dependencies
Open PowerShell in your project folder and run:
```powershell
pip install -r requirements.txt
```

### Step 2: Start Python Server
```powershell
python chipi_server.py
```

You should see:
```
Starting Chipi AI Server...
Server running at http://localhost:5000
```

### Step 3: Open Chipi in Browser
Open **chipi-chatbot-api.html** in your web browser.

You should see:
- Green dot in header = "Connected to Server"
- Chat interface ready for interaction
- Admin Panel button available

## Testing the Connection

1. Type a message like "hello"
2. Chipi should respond from the server
3. Click "Admin Panel" to add new training data
4. Refresh data to test live updates

## Common Issues

**Problem**: "Server Disconnected" message
- Make sure Python server is running
- Open PowerShell and check `python chipi_server.py` is still running

**Problem**: "Address already in use" error
- Port 5000 is occupied
- Either close other applications or change port in chipi_server.py (and update API_URL in HTML)

## Admin Panel Usage

Click the "Admin Panel" button to:

1. **Add Response** - Add new answers to existing topics
   - Category: `help`
   - Response: `I would be happy to assist you`

2. **Add Pattern** - Add keywords that trigger responses
   - Category: `greetings`
   - Pattern: `wassup`

3. **Create Category** - Create entirely new topics
   - Name: `sports`
   - Patterns: `football, soccer, basketball`
   - Response: `Sports are great for fitness!`

## How the System Works

```
Browser (chipi-chatbot-api.html)
    ↓
    ↓ User types message
    ↓
JavaScript pattern matching
    ↓
    ↓ Looks in training data from server
    ↓
Python Flask API (chipi_server.py)
    ↓
    ↓ Manages training_data.json
    ↓
Returns response
    ↓
Display in chat
```

## Two Versions of Chipi

### Version 1: With Python Backend (Recommended)
- File: **chipi-chatbot-api.html**
- Requires: Python server running
- Features: Live updates, Admin panel, Dynamic data
- Good for: Development, testing, learning

### Version 2: Standalone (Original)
- File: **chipi-chatbot.html**
- Requires: Just a browser
- Features: Works offline, no server needed
- Good for: Simple use, no setup required

## Example Workflow

1. **Start conversation**
   - Open chipi-chatbot-api.html
   - Chat with Chipi about available topics

2. **Want to add something new?**
   - Click "Admin Panel"
   - Create new category or add response
   - Refresh data
   - Test immediately in chat

3. **Build over time**
   - Each time you add data, it persists
   - Server keeps all changes
   - No code editing needed

## Server APIs (For Developers)

You can interact with the server directly using curl or your favorite HTTP client:

### Get all training data:
```bash
curl http://localhost:5000/api/data
```

### Add response to greeting category:
```bash
curl -X POST http://localhost:5000/api/data/add-response/greetings \
  -H "Content-Type: application/json" \
  -d '{"response": "Hey there!"}'
```

### Create new category:
```bash
curl -X POST http://localhost:5000/api/data/create-category \
  -H "Content-Type: application/json" \
  -d '{
    "name": "music",
    "patterns": ["music", "song", "artist"],
    "responses": ["Music is wonderful!", "I love music!"]
  }'
```

### Get statistics:
```bash
curl http://localhost:5000/api/stats
```

## Next Steps

1. ✅ Complete the setup above
2. ✅ Test basic conversation
3. ✅ Use Admin Panel to customize
4. ✅ Add more categories for your use case
5. ⏭️ Consider adding database (optional)

## Files Location

All files should be in:
```
c:\Users\daria\OneDrive\Desktop\My programming practice;)\
├── chipi_server.py
├── chipi-chatbot-api.html
├── chipi-chatbot.html (original)
├── training_data.json (created by server)
├── requirements.txt
├── README.md
└── QUICKSTART.md (this file)
```

## Features Summary

✅ Real AI-like conversations using pattern matching
✅ Dynamic training data from Python server
✅ Admin panel to update data without coding
✅ Beautiful blue-green gradient interface
✅ Mobile responsive design
✅ Server connection status monitoring
✅ Multiple pre-built categories (8+)
✅ Easy to extend with new topics

## Need Help?

- Check README.md for detailed documentation
- Look at training_data.json to see data format
- Check browser console (F12) for errors
- Make sure server is running on localhost:5000

---

**Ready to start? Run: `python chipi_server.py`** 🚀
