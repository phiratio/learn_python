const http = require('http')
const os = require('os')
const port = 3000
const fs = require('fs')

const requestHandler = (request, response) => {
  fs.readFileSync('/etc/passwd')
  response.end('Hello from app with I/O\n')
}

const server = http.createServer(requestHandler)

server.listen(port, (err) => {
  if (err) {
    return console.log('Error happened', err)
  }

  console.log(`Server running on ${port}`)
})
