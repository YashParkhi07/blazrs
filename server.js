const http = require('http');
const fs = require('fs');
const path = require('path');

const PORT = process.env.PORT || 3000;

const MIME_TYPES = {
  '.html': 'text/html',
  '.css': 'text/css',
  '.js': 'text/javascript',
  '.png': 'image/png',
  '.jpg': 'image/jpeg',
  '.jpeg': 'image/jpeg',
  '.svg': 'image/svg+xml',
  '.json': 'application/json'
};

const server = http.createServer((req, res) => {
  // Ignore query strings
  let requestUrl = req.url.split('?')[0];
  let filePath = path.join(__dirname, requestUrl === '/' ? 'index.html' : requestUrl);
  
  // Extensionless HTML routing
  if (path.extname(filePath) === '' && !filePath.endsWith('/')) {
    filePath += '.html';
  }

  const extname = path.extname(filePath);
  const contentType = MIME_TYPES[extname] || 'application/octet-stream';

  fs.readFile(filePath, (err, content) => {
    if (err) {
      if (err.code === 'ENOENT') {
        // Fallback to index.html (like a SPA or 404 handler)
        fs.readFile(path.join(__dirname, 'index.html'), (err404, content404) => {
          if (err404) {
            res.writeHead(500);
            res.end('Server Error: index.html missing');
          } else {
            res.writeHead(200, { 'Content-Type': 'text/html' });
            res.end(content404, 'utf-8');
          }
        });
      } else {
        res.writeHead(500);
        res.end('Server Error: ' + err.code);
      }
    } else {
      res.writeHead(200, { 'Content-Type': contentType });
      res.end(content, 'utf-8');
    }
  });
});

server.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
