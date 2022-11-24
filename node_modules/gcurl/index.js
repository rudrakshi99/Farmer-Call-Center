#!/usr/bin/env node
var protobuf = require("protobufjs");
var grpc = require('grpc');
var program = require('commander');
var fs = require('fs');
program
.version('0.1.0')
.option('-f, --proto [proto file path]', 'Proto file')
.option('-m, --method [method name]', 'Service method to hit')
.option('-s, --service [service name]', 'Service to hit')
.option('-p, --package [package name]', 'Package name')
.option('-h, --host [host:port]', 'Host port to hit')
.option('-i, --input [input]', 'Input in valid JSON')
.option('-x, --short [package:service:method]', 'Short hand like pacakge:service:method')
.option('-d, --payload [payload]', 'Specify input by giving a file name that has the input')
.parse(process.argv);

function validate() {
	if (!program.proto) {
		throw 'Proto file not specified';
		}
	if (!fs.existsSync(program.proto)) {
		throw 'Proto file not found';
	}
	if (program.payload) {
		if (!fs.existsSync(program.payload)) {
			throw 'Specified payload file doesn not exist';
		}
		let data = fs.readFileSync(program.payload, 'utf-8');
		program.input = data;
	}

	var obj = JSON.parse(program.input);
	if (program.short) {
		let splits = program.short.split(':');
		if (splits.length != 3) {
			throw 'Short hand is <package path>:service:method';
		}
		program.package = splits[0];
		program.service = splits[1];
		program.method = splits[2];
	}
	if (!program.method) {
		throw 'Method not specified';
	}
	if (!program.service) {
		throw 'Service not specified';
	}
	if (!program.host) {
		throw 'Host address not speicified';
	}
}

try {
	validate();
} catch(e) {
	console.log('\nError! :  ', e);
	process.exit(1);
}

function validateService(service) {
	let availServs = [];
	for (let s in service) {
		if (service[s].service) {
			availServs.push(s);
		}
	}
	if (!service[program.service]) {
		throw `Your specified service doesn't exist, available services:\n ${availServs}`;
	}
	service = service[program.service];
	if (!service.service) {
		throw `Name you specified is not a service: ${program.service}, available services:\n ${availServs}`;
	}
	return service;
}

var fileName = program.proto;
var protoFile = grpc.load(fileName);
var splits = program.package.split('.');
var service = protoFile;
for (var i = 0; i < splits.length; i++) {
	service = service[splits[i]];
}

try {
	service = validateService(service);
} catch(e) {
	console.log(e);
	process.exit(1);
}

if (!service.service[program.method]) {
	console.log("Your specified method doesn't exist, methods available in this service are:");
	console.log(Object.keys(service.service));
	process.exit(1);
}

var method = service.service[program.method].requestType.name;
var packageName = program.package;
var struct = packageName + '.' + method;
if (!program.package) {
	struct = method;
}

var client = new service(program.host, grpc.credentials.createInsecure());
protobuf.load(fileName, function(err, root) {
    if (err) {
        throw err;
    }
    var msg = root.lookupType(struct);
    var payload = JSON.parse(program.input);
    var errMsg = msg.verify(payload);
    if (errMsg) {
        throw errMsg;
    }
    var message = msg.create(payload);
	client[program.method](message, function(err, data) {
		if (err) {
			console.log(`Error calling method:\n ${err}`);
			process.exit(1);
		}
		console.log(JSON.stringify(data));
	});
})