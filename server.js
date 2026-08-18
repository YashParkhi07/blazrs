const express = require('express');
const path = require('path');

const app = express();
const PORT = process.env.PORT || 3000;

// Serve static files from the current directory
app.use(express.static(__dirname));

// Also explicitly handle extensionless HTML routing
app.use((req, res, next) => {
    if (req.path.indexOf('.') === -1) {
        let file = path.join(__dirname, req.path + '.html');
        res.sendFile(file, (err) => {
            if (err) next();
        });
    } else {
        next();
    }
});

// Fallback to index.html
app.get('*', (req, res) => {
    res.sendFile(path.join(__dirname, 'index.html'));
});

app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
