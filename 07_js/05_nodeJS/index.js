const http = require('http');
const port = 3001;
http.createServer((req, res) => {
    res.writeHead(200, {
        'Content-type': 'text/plain', 
    });
    res.statusCode = 200;
    res.write('Lunch Time! ');
    res.end('End of respones\n');
}).listen(port);

console.log(`Server is running @ http://localhost:${port}`);
