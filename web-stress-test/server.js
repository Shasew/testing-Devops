const express = require('express');
const app = express();

// Middleware agar server bisa membaca data berformat JSON dari k6
app.use(express.json());

app.get('/login', (req, res) => {
    res.json({
        status: "success",
        message: "Server berjalan!"
    });
});

const VALID_USER = "testuser";
const VALID_PASS = "testpassword";

app.post('/login', (req, res) => {
    const { username, password } = req.body;

    if (username === VALID_USER && password === VALID_PASS) {
        return res.status(200).json({
            status: "success",
            message: "Login berhasil!"
        });
    }

    return res.status(401).json({
        status: "error",
        message: "Username atau password salah!"
    });
});

// Jalankan server di port 3000
const PORT = 3000;
app.listen(PORT, () => {
    console.log(`🚀 Server lokal siap ditembak di http://localhost:${PORT}`);
});