import fetch from 'node-fetch'
import { createRequire } from "module";
const require = createRequire(import.meta.url);
const WebSocket = require('ws')
const express = require('express')
const app =express()

let finalMessage=''
app.use(express.urlencoded({ extended: true }))
const server = require('http').createServer(app)
const wss =new WebSocket.Server({server})

const speech = require('@google-cloud/speech')
const client = new speech.SpeechClient()
let transcriptionLanguage='en-GB'
const request={
    config:{
        encoding:"MULAW",
        sampleRateHertz:8000,
        languageCode:transcriptionLanguage
    },
    interimResults:true
}
let recognizeStream=null
wss.on('connection',(ws)=>{
    console.log('New connection')
    ws.on('message',message=>{
        const msg = JSON.parse(message)
        switch(msg.event){
            case 'connected':
                console.log('Call is connected')
                
                break;
            case 'start':
                console.log('Start media stream')
                recognizeStream = client
                .streamingRecognize(request)
                .on("error", console.error)
                .on("data", (data) => {
                    console.log(data.results[0].alternatives[0].transcript);
                    wss.clients.forEach((client) => {
                    if (client.readyState === WebSocket.OPEN) {
                        client.send(
                        JSON.stringify({
                            event: "interim-transcription",
                            text: data.results[0].alternatives[0].transcript,
                        })
                        );
                    }
                    });
                    finalMessage=data.results[0].alternatives[0].transcript

                });
                
            break;
            case 'media':
                // console.log('Receiving media stream')
                recognizeStream.write(msg.media.payload);
                // finalMessage=recognizeStream.write(msg.media.payload)
                break;
            case 'stop':
                console.log('Call ended')
                recognizeStream.destroy()
                break;
        }
    })
})
app.post('/',(req,res)=>{
    res.set("Content-Type", "text/xml");
  res.send(
    `<Response>
        <Start>
        <Stream url='wss://${req.headers.host}' />
        </Start>
        <Say>Welcome to Krashak dot AI please leave a query and wait for a while as we process it.</Say> 
       <Pause length='15' />
       <Say>

       </Say>
    </Response>`
  );
})



server.listen(8080)
console.log('listening to port 8080')








