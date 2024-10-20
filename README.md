# Real-Time Chat Application using gRPC

This project demonstrates a simple real-time chat application using gRPC. The application allows multiple clients to send and receive messages in real-time, showcasing the power of gRPC's bidirectional streaming capabilities.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This real-time chat application is built using gRPC and Protocol Buffers. It demonstrates how to implement a bidirectional streaming service that allows multiple clients to communicate with each other in real-time. The project is designed to be simple and easy to understand, making it a great starting point for learning gRPC and real-time communication.

## Features

- Real-time messaging using gRPC's bidirectional streaming.
- Multi-client support.
- Simple and efficient message serialization using Protocol Buffers.
- Easy to extend and modify.

## Prerequisites

Before you begin, ensure you have the following prerequisites installed:

- Python 3.10+
- venv

### Setting Up the Virtual Environment

1. **Create a Virtual Environment**

   First, create a virtual environment. This will create a virtual environment named `venv` in your project directory.
   `python -m venv venv`

1. **Activate the Virtual Environment**

   Depending on your operating system, activate the virtual environment:

   - **macOS and Linux**: `source venv/bin/activate`

   - **Windows**: `venv\Scripts\activate`

1. **Install Dependencies**
With the virtual environment activated, install the required dependencies: `pip install -r requirements.txt`

### Generate the Python code from the .proto file:
```bash
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. chat.proto
```

## Usage
1. Start the gRPC server:
`python server.py`

1. Open another terminal and start the gRPC client:
`python client.py`

1. Enter messages in the client terminal. The messages will be sent to the server and broadcasted to all connected clients.