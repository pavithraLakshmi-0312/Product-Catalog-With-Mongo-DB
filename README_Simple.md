# Product Catalog with MongoDB
## Naan Mudhalvan Project

![MongoDB](https://img.shields.io/badge/MongoDB-4EA94B?logo=mongodb&logoColor=white)
![Node.js](https://img.shields.io/badge/Node.js-339933?logo=node.js&logoColor=white)

## 📋 Project Overview

A **simple Product Catalog system** that uses **MongoDB database** for storing products.

**Topic**: Product Catalog with MongoDB

## 🎯 What This Project Has:

✅ **MongoDB Database** - Real database storage (the main requirement!)  
✅ **Add Products** - Save products to MongoDB  
✅ **Delete Products** - Remove from MongoDB  
✅ **View Products** - Display from MongoDB  
✅ **Simple Web Interface** - Easy to use  
✅ **Data Persistence** - Products saved permanently in MongoDB  


## 🛠️ Tech Stack

- **Database**: MongoDB (main focus!)
- **Server**: Node.js + Express (minimal, just to connect to MongoDB)
- **Frontend**: Simple HTML/CSS/JS (just for display)

**The important part is MongoDB - that's the concept!**


## ⚡ Quick Setup (20 Minutes)

### Step 1: Install MongoDB

**Option A: MongoDB Atlas (Cloud - Easiest)**
1. Go to: https://www.mongodb.com/cloud/atlas/register
2. Create free account
3. Create cluster (free tier)
4. Get connection string
5. Update in server.js line 9:
   ```javascript
   const MONGODB_URI = 'your_connection_string_here';
   ```

**Option B: Local MongoDB**
1. Download: https://www.mongodb.com/try/download/community
2. Install MongoDB
3. Keep default: `mongodb://localhost:27017/product-catalog`

### Step 2: Install Node.js

1. Download from: https://nodejs.org/
2. Install LTS version
3. Verify: `node --version`

### Step 3: Setup Project

```bash
# Install dependencies
npm install

# Start server
npm start
```

### Step 4: Add Sample Data

Visit: http://localhost:3000/seed

### Step 5: Use the App

Open: http://localhost:3000


## 📁 Project Structure

```
product-catalog-mongodb/
├── server.js           # Server + MongoDB connection
├── package.json        # Dependencies
└── public/
    └── index.html      # Web interface
```


## 💻 How It Works

1. **MongoDB** stores all product data
2. **Server** connects to MongoDB and provides simple routes
3. **Web page** displays products from MongoDB
4. **Add/Delete** operations save directly to MongoDB

**The key concept: Everything is stored in MongoDB!**

## 🧪 Testing

1. Start server: `npm start`
2. Visit: http://localhost:3000/seed (adds sample products)
3. Open: http://localhost:3000
4. Add a product - check MongoDB
5. Delete a product - check MongoDB
6. Refresh page - products persist (because they're in MongoDB!)

## 📤 GitHub Submission

Upload these files:
- server.js
- package.json  
- public/index.html
- README.md (this file)
- screenshots/

## 🎓 What is Demonstrated

✅ **MongoDB Integration** - Real database connection  
✅ **CRUD Operations** - Create, Read, Delete with MongoDB  
✅ **Data Persistence** - MongoDB stores data permanently  
✅ **Database Concepts** - Schema, collections, documents  


