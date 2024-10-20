import grpc
from concurrent import futures
import time
import threading
import chat_pb2_grpc


class ChatService(chat_pb2_grpc.ChatServiceServicer):
    def __init__(self):
        self.message_queues = {}
        self.lock = threading.Lock()  # Add thread lock for safety

    def Chat(self, request_iterator, context):
        client_id = id(context)
        self.message_queues[client_id] = []
        
        def process_incoming_messages():
            try:
                for message in request_iterator:
                    print(f"Server received from {message.user}: {message.message}")
                    with self.lock:
                        for cid, queue in self.message_queues.items():
                            if cid != client_id:
                                queue.append(message)
            except Exception as e:
                print(f"Error processing messages: {e}")
            finally:
                with self.lock:
                    if client_id in self.message_queues:
                        del self.message_queues[client_id]

        # Start message processing in a separate thread
        threading.Thread(target=process_incoming_messages, daemon=True).start()

        try:
            while True:  # Continuously check for messages
                if client_id in self.message_queues and self.message_queues[client_id]:
                    with self.lock:
                        if self.message_queues[client_id]:
                            next_message = self.message_queues[client_id].pop(0)
                            yield next_message
                time.sleep(0.1)  # Add small delay to prevent CPU overload
        except Exception as e:
            print(f"Error in message loop: {e}")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    chat_pb2_grpc.add_ChatServiceServicer_to_server(ChatService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server started on port 50051")
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()
