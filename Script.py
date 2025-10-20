
# Create a simple Node.js application that uses MongoDB with a simple web interface
simple_server = """// server.js - Simple Product Catalog with MongoDB
const express = require('express');
const mongoose = require('mongoose');
const path = require('path');
const app = express();

// Middleware
app.use(express.json());
app.use(express.static('public'));

// MongoDB Connection
const MONGODB_URI = 'mongodb://localhost:27017/product-catalog';
// For MongoDB Atlas: mongodb+srv://username:password@cluster.mongodb.net/product-catalog

mongoose.connect(MONGODB_URI)
    .then(() => console.log('✅ Connected to MongoDB'))
    .catch(err => console.error('❌ MongoDB Error:', err));

// Product Schema
const productSchema = new mongoose.Schema({
    name: String,
    price: Number,
    description: String,
    category: String,
    image: String
});

const Product = mongoose.model('Product', productSchema);

// Serve the main page
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

// API Routes
app.get('/api/products', async (req, res) => {
    const products = await Product.find();
    res.json(products);
});

app.post('/api/products', async (req, res) => {
    const product = new Product(req.body);
    await product.save();
    res.json(product);
});

app.delete('/api/products/:id', async (req, res) => {
    await Product.findByIdAndDelete(req.params.id);
    res.json({ message: 'Deleted' });
});

// Seed sample data
app.get('/seed', async (req, res) => {
    await Product.deleteMany({});
    await Product.insertMany([
        { name: 'Laptop', price: 45000, description: 'High performance laptop', category: 'Electronics', image: 'https://images.unsplash.com/photo-1496181133206-80ce9b88a853?w=400' },
        { name: 'Smartphone', price: 25000, description: '5G smartphone', category: 'Electronics', image: 'https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=400' },
        { name: 'Headphones', price: 2500, description: 'Wireless headphones', category: 'Audio', image: 'https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=400' },
        { name: 'Smart Watch', price: 8000, description: 'Fitness tracker', category: 'Wearables', image: 'https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=400' },
        { name: 'Tablet', price: 30000, description: '10-inch tablet', category: 'Electronics', image: 'https://images.unsplash.com/photo-1561154464-82e9adf32764?w=400' },
        { name: 'Camera', price: 55000, description: 'DSLR camera', category: 'Photography', image: 'https://images.unsplash.com/photo-1516035069371-29a1b244cc32?w=400' }
    ]);
    res.send('✅ Database seeded with 6 products!');
});

const PORT = 3000;
app.listen(PORT, () => {
    console.log(`🚀 Server running on http://localhost:${PORT}`);
    console.log(`📦 Visit http://localhost:${PORT}/seed to add sample products`);
});
"""

simple_package = """{
  "name": "product-catalog-mongodb",
  "version": "1.0.0",
  "description": "Simple Product Catalog with MongoDB - Naan Mudhalvan",
  "main": "server.js",
  "scripts": {
    "start": "node server.js"
  },
  "dependencies": {
    "express": "^4.18.2",
    "mongoose": "^7.5.0"
  }
}
"""

simple_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Product Catalog - MongoDB Project</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
        }
        .container {
            max-width: 1200px;
            margin: 0 auto;
        }
        h1 {
            color: white;
            text-align: center;
            font-size: 3rem;
            margin-bottom: 10px;
        }
        .subtitle {
            color: white;
            text-align: center;
            font-size: 1.2rem;
            margin-bottom: 30px;
            opacity: 0.9;
        }
        .db-status {
            background: white;
            padding: 15px;
            border-radius: 10px;
            margin-bottom: 20px;
            text-align: center;
            font-weight: bold;
        }
        .add-form {
            background: white;
            padding: 25px;
            border-radius: 15px;
            margin-bottom: 30px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
        }
        .form-row {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 15px;
            margin-bottom: 15px;
        }
        input, textarea {
            padding: 12px;
            border: 2px solid #ddd;
            border-radius: 8px;
            font-size: 14px;
            width: 100%;
        }
        textarea {
            grid-column: 1 / -1;
            resize: vertical;
        }
        button {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            padding: 15px 30px;
            border-radius: 8px;
            cursor: pointer;
            font-size: 16px;
            font-weight: bold;
            width: 100%;
        }
        button:hover {
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);
        }
        .products {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
            gap: 25px;
        }
        .product-card {
            background: white;
            border-radius: 15px;
            overflow: hidden;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
            transition: transform 0.3s;
        }
        .product-card:hover {
            transform: translateY(-10px);
        }
        .product-image {
            width: 100%;
            height: 200px;
            object-fit: cover;
        }
        .product-info {
            padding: 20px;
        }
        .product-name {
            font-size: 1.3rem;
            font-weight: bold;
            margin-bottom: 8px;
        }
        .product-price {
            color: #10b981;
            font-size: 1.4rem;
            font-weight: bold;
            margin-bottom: 10px;
        }
        .product-desc {
            color: #666;
            margin-bottom: 15px;
        }
        .delete-btn {
            background: #ef4444;
            padding: 10px 20px;
            font-size: 14px;
        }
        .delete-btn:hover {
            background: #dc2626;
        }
        @media (max-width: 768px) {
            .form-row {
                grid-template-columns: 1fr;
            }
            h1 {
                font-size: 2rem;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>📦 Product Catalog</h1>
        <p class="subtitle">Naan Mudhalvan Project - Using MongoDB Database</p>
        
        <div class="db-status">
            🗄️ Database: <span id="db-status">MongoDB Connected</span> | 
            Products: <span id="count">0</span>
        </div>

        <div class="add-form">
            <h2 style="margin-bottom: 20px;">➕ Add New Product</h2>
            <form id="productForm">
                <div class="form-row">
                    <input type="text" id="name" placeholder="Product Name" required>
                    <input type="number" id="price" placeholder="Price (₹)" required>
                </div>
                <div class="form-row">
                    <input type="text" id="category" placeholder="Category">
                    <input type="url" id="image" placeholder="Image URL">
                </div>
                <textarea id="description" placeholder="Description" rows="3"></textarea>
                <button type="submit">Add to MongoDB Database</button>
            </form>
        </div>

        <div id="products" class="products"></div>
    </div>

    <script>
        const API = '/api/products';

        // Load products
        async function loadProducts() {
            const res = await fetch(API);
            const products = await res.json();
            document.getElementById('count').textContent = products.length;
            
            document.getElementById('products').innerHTML = products.map(p => `
                <div class="product-card">
                    <img src="${p.image || 'https://via.placeholder.com/300x200'}" class="product-image">
                    <div class="product-info">
                        <div class="product-name">${p.name}</div>
                        <div class="product-price">₹${p.price.toLocaleString()}</div>
                        <div class="product-desc">${p.description}</div>
                        <button class="delete-btn" onclick="deleteProduct('${p._id}')">
                            🗑️ Delete from MongoDB
                        </button>
                    </div>
                </div>
            `).join('');
        }

        // Add product
        document.getElementById('productForm').onsubmit = async (e) => {
            e.preventDefault();
            const product = {
                name: document.getElementById('name').value,
                price: document.getElementById('price').value,
                category: document.getElementById('category').value,
                description: document.getElementById('description').value,
                image: document.getElementById('image').value
            };
            
            await fetch(API, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(product)
            });
            
            e.target.reset();
            loadProducts();
            alert('✅ Product saved to MongoDB!');
        };

        // Delete product
        async function deleteProduct(id) {
            if (confirm('Delete this product from MongoDB?')) {
                await fetch(`${API}/${id}`, { method: 'DELETE' });
                loadProducts();
                alert('✅ Product deleted from MongoDB!');
            }
        }

        // Initial load
        loadProducts();
    </script>
</body>
</html>
"""

with open('server.js', 'w', encoding='utf-8') as f:
    f.write(simple_server)

with open('package.json', 'w', encoding='utf-8') as f:
    f.write(simple_package)

# Create public folder structure
import os
os.makedirs('public', exist_ok=True)

with open('public/index.html', 'w', encoding='utf-8') as f:
    f.write(simple_html)

print("✅ Simple MongoDB Project Created!")
print("\nFiles created:")
print("1. server.js - Simple server with MongoDB")
print("2. package.json - Dependencies")
print("3. public/index.html - Web interface")
