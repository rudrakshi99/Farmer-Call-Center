# gCURL
This is a simple node module that lets you hit a grpc service just like you would use curl. 
Syntax isn't exactly like curl but is more like a CLI tool. 


## Install 
`npm install -g gcurl`

## Run example
`git clone git@github.com:nikunjy/pcurl.git`

`cd pcurl`

`npm run-script sample-server`

In another terminal run:

`cd pcurl`

`gcurl -f ./examples/protos/helloworld.proto  --host :50051 --input '{"name": "Nikunj"}' --short helloworld:Greeter:sayHello`