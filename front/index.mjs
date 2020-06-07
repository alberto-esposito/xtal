import http from 'http'
import fs from 'fs'

const index = fs.readFileSync('./front/src/index.html')

const paint = fs.readFileSync('./front/src/paint.js')

const values = fs.readFileSync('./front/src/indexValues.mjs')

const server = http.createServer((req, res) => {
  console.log(req.url)
  switch (req.url) {
    case '/':
      res.write(index)
      break
    case '/compute':
      console.log('compute...\n')
      res.write('{a: 2}')
      break
    case '/paint.js':
      res.setHeader('content-type', 'text/javascript')
      res.write(paint)
      break
    case '/indexValues.mjs':
      res.setHeader('content-type', 'text/javascript')
      res.write(values)
      break
  }
  res.end()
})

server.on('clientError', (err, socket) => {
  console.log({ err })
  socket.end('HTTP/1.1 400 Bad Request\r\n\r\n')
})

server.listen(8000)
