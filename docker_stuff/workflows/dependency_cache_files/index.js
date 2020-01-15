const http = require('http')
const os = require('os')
const port = 3000

const requestHandler = (request, response) => {
  response.end('Hello from inside ' + os.hostname() + '\n')
}

const server = http.createServer(requestHandler)

server.listen(port, (err) => {
  if (err) {
    return console.log('Error happened', err)
  }

  console.log(`Server running on ${port}`)
})
