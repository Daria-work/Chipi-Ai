# Chipi AI - Testing Guide

## Pre-Test Checklist

Before testing, ensure you have:
- [ ] Python 3.7+ installed
- [ ] Required packages installed (`pip install -r requirements.txt`)
- [ ] Both chipi_server.py and chipi-chatbot-api.html in same directory
- [ ] Port 5000 is available
- [ ] A web browser (Chrome, Firefox, Safari, Edge)

## Test 1: Server Startup

### Steps:
1. Open PowerShell in your project directory
2. Run: `python chipi_server.py`
3. Wait for output showing "Server running at http://localhost:5000"

### Expected Result:
```
Starting Chipi AI Server...
Server running at http://localhost:5000
 * Running on http://127.0.0.1:5000
```

### If Failed:
- Error "Address already in use" → Port 5000 occupied, change to 5001 in code
- Error "ModuleNotFoundError" → Run `pip install -r requirements.txt`
- Keep PowerShell window open during testing

---

## Test 2: Browser Connection

### Steps:
1. Open chipi-chatbot-api.html in web browser
2. Look at the header area
3. Check status indicator next to "Chipi" title

### Expected Result:
- Green dot appears
- Text says "Connected to Server"
- Admin Panel button is clickable
- All UI elements load properly

### If Failed:
- Red dot / "Server Disconnected" → Python server not running
- Broken styling → Browser cache, press Ctrl+Shift+Delete to clear
- Check browser console (F12) for JavaScript errors

---

## Test 3: Basic Conversation

### Test 3a: Greeting
1. Type: `hello`
2. Press Enter or click send button

**Expected Response:**
Should get one of the greeting responses like:
- "Hello. I am Chipi. I am happy to see you today..."
- "Hi there. It is great to see you here..."
- "Hey. I am Chipi, your friendly AI assistant..."

### Test 3b: About Chipi
1. Type: `who are you`
2. Press Enter

**Expected Response:**
Should get one of the aboutMe responses explaining what Chipi is

### Test 3c: Help Request
1. Type: `can you help me`
2. Press Enter

**Expected Response:**
Should get one of the help responses offering assistance

### Test 3d: Science Question
1. Type: `tell me about atoms`
2. Press Enter

**Expected Response:**
Should get one of the science responses about atoms

### Test 3e: Goodbye
1. Type: `goodbye`
2. Press Enter

**Expected Response:**
Should get one of the goodbye responses

### If Failed:
- No response appears → Check console (F12)
- Generic fallback response → Pattern not matching correctly
- Red error message → API call failed

---

## Test 4: Admin Panel - Add Response

### Steps:
1. Click "Admin Panel" button in header
2. Scroll to "Add New Response" section
3. In Category field: `greetings`
4. In Response field: `Hey there, it's so nice to meet you!`
5. Click "Add Response" button
6. Should see success message

### Expected Result:
- Alert box says "Response added successfully to greetings!"
- Statistics update showing response count increased
- Can close modal and use new response in chat

### Test This Works:
1. Close admin panel
2. Type: `hi`
3. Send message
4. May see your new response!

---

## Test 5: Admin Panel - Add Pattern

### Steps:
1. Click "Admin Panel"
2. Scroll to "Add New Pattern" section
3. In Category field: `help`
4. In Pattern field: `assistance`
5. Click "Add Pattern" button

### Expected Result:
- Alert says "Pattern added successfully to help!"
- Now typing "I need assistance" will trigger help responses

### Test This Works:
1. Close admin panel
2. Type: `i need assistance`
3. Send message
4. Should get a help response

---

## Test 6: Admin Panel - Create Category

### Steps:
1. Click "Admin Panel"
2. Scroll to "Create New Category" section
3. Category Name: `animals`
4. Initial Patterns: `dog, cat, bird, animal`
5. Initial Response: `Animals are fascinating creatures!`
6. Click "Create Category" button

### Expected Result:
- Alert says "Category 'animals' created successfully!"
- New category appears in category list
- Statistics update

### Test This Works:
1. Close admin panel
2. Type: `I have a dog`
3. Send message
4. Should get your animal response

---

## Test 7: Refresh Data

### Steps:
1. In main chat, click "Refresh Data" button
2. Wait for success message

### Expected Result:
- Alert says "Training data refreshed from server!"
- New training data is reloaded from server

### Purpose:
Tests that data updates from Python server are working

---

## Test 8: View About Information

### Steps:
1. Click "About Chipi" button
2. Read the information
3. Scroll through all content
4. Click X to close

### Expected Result:
- Modal opens with detailed information
- Can see architecture, features, and how it works
- Can close with X button or click outside

---

## Test 9: View Contact Information

### Steps:
1. Click "Contact Us" button
2. Review all contact details
3. Verify fake contact information is displayed
4. Close modal

### Expected Result:
- Shows email addresses, phone, address
- Shows social media handles
- Shows office hours
- Professional layout maintained

---

## Test 10: Admin Stats Display

### Steps:
1. Click "Admin Panel"
2. Look at "Current Statistics" section at top

### Expected Result:
Should show:
- Number of Categories (starts with 8)
- Number of Patterns (starts with ~60)
- Number of Responses (~90)
- List of all categories displayed as tags

### If You Added Data:
- Numbers should reflect your additions
- New categories should appear in category list

---

## Test 11: Mobile Responsiveness

### Desktop Testing:
1. Open chipi-chatbot-api.html on desktop browser
2. Verify layout looks good

### Mobile Testing:
1. Open on phone/tablet browser
2. Check that:
   - Chat box is readable
   - Buttons are clickable
   - Text input works
   - Messages display properly
   - No text is cut off

---

## Test 12: Conversation Persistence

### Steps:
1. Have a conversation with Chipi
2. Type several messages back and forth
3. Verify conversation history shows correctly

### Expected Result:
- User messages appear on right with blue gradient
- Bot responses appear on left with green gradient
- All messages visible in order
- Can scroll through conversation

---

## Test 13: Edge Cases

### Test Scrolling:
1. Have long conversation to test scroll
2. Scroll up and down in message area

### Test Empty Input:
1. Click send with empty message
2. Should do nothing (not send)

### Test Special Characters:
1. Type: `What's the @ symbol?`
2. Should process normally

### Test Long Messages:
1. Type very long message
2. Should word-wrap properly

### Test Unknown Topics:
1. Type something completely random: `xyzabc123`
2. Should get generic fallback response

---

## Test 14: Connection Loss Simulation

### Steps:
1. Start conversation normally
2. Stop the Python server (Ctrl+C in PowerShell)
3. Try sending a new message
4. Check status indicator

### Expected Result:
- Status indicator changes to red
- Text says "Server Disconnected"
- Conversation may still work (using default responses)

### Recovery:
1. Restart Python server
2. Click "Refresh Data" button
3. Status should return to green
4. Normal operation resumes

---

## Test 15: JSON File Verification

### Steps:
1. Open `training_data.json` in text editor
2. Look for your additions (if you made any)
3. Verify JSON formatting is valid

### Expected Structure:
```json
{
  "category_name": {
    "patterns": [...],
    "responses": [...]
  }
}
```

### If You Added Data:
Your new category should appear in the file

---

## Performance Tests

### Response Time:
- Average response: <100ms
- With admin panel open: <500ms
- Refresh data: <1s

### Memory Usage:
- Page load: ~5-10MB
- After conversation: ~10-15MB
- No memory leaks with long conversations

### Stress Test:
1. Send 50+ messages rapidly
2. Add responses while chatting
3. Open/close admin panel multiple times
4. Should handle without crashing

---

## Troubleshooting During Tests

| Problem | Solution |
|---------|----------|
| Server won't start | Check port 5000 availability |
| Connection refused | Ensure Python server is running |
| No responses in chat | Check browser console (F12) for errors |
| Admin panel won't open | Try refresh (F5) and try again |
| Styling looks broken | Clear browser cache (Ctrl+Shift+Del) |
| Status shows red/disconnected | Restart Python server |
| JSON syntax error | Check training_data.json with JSON validator |
| Getting timeout errors | Python server may be slow, check terminal |

---

## Successful Test Completion Checklist

- [ ] Server starts without errors
- [ ] Browser shows green connection indicator  
- [ ] Can send messages and receive responses
- [ ] All greeting/help/science responses work
- [ ] Admin panel opens and displays stats
- [ ] Can add new responses successfully
- [ ] Can add new patterns successfully
- [ ] Can create new categories successfully
- [ ] About and Contact pages display
- [ ] Refresh Data button works
- [ ] Mobile layout looks good
- [ ] Conversation displays properly
- [ ] Can handle edge cases
- [ ] JSON file saves correctly

---

## Next Steps After Testing

If all tests pass:

1. ✅ System is working correctly
2. ✅ Ready for customization
3. ✅ Can start adding your own training data
4. ✅ Ready for production (with security additions)

If tests fail:

1. Check error messages in browser console (F12)
2. Review Python server output in terminal
3. Verify files are in correct location
4. Check requirements.txt installed correctly
5. Try restarting both browser and server
6. Check README.md for detailed troubleshooting

---

**Test Results: [Document your results here]**

Server Status: ✅ / ❌
Connection: ✅ / ❌  
Chat Works: ✅ / ❌
Admin Panel: ✅ / ❌
Data Persistence: ✅ / ❌

---

Have fun testing Chipi AI! 🚀
