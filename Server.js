// server.js - Simple Product Catalog with MongoDB
const express = require('express');
const mongoose = require('mongoose');
const path = require('path');
const app = express();

// Middleware
app.use(express.json());
app.use(express.static('public'));

// MongoDB Connection
const MONGODB_URI = 'mongodb://localhost:27017/product-catalog'; // Local
// For MongoDB Atlas, replace above with your Atlas connection string:
// const MONGODB_URI = mongodb+srv://priyanka_db_user:ST2D5O2otnnmZe40@productcatalog.yjoom38.mongodb.net/?retryWrites=true&w=majority&appName=ProductCatalog

mongoose.connect(MONGODB_URI, {
    useNewUrlParser: true,
    useUnifiedTopology: true,
})
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
