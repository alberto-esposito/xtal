import http from 'http'
import fs from 'fs'
import util from 'util'
import {spawn, exec} from 'child_process'

const asyncExec = util.promisify(exec)

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
      // console.log( process.env.PATH )
      const python = spawn('./python/wrapper.sh')

      python.stdout.on('data', (data) => console.log(` ${data}`))

      python.stderr.on('data', (data) => console.log(`error ${data}`))

      python.on('close', (code) => console.log(`\ncompute ended with code ${code}`))

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
