import grpc
import threading

import chat_pb2
import chat_pb2_grpc

def run(user_name):
    channel = grpc.insecure_channel('localhost:50051')
    stub = chat_pb2_grpc.ChatServiceStub(channel)

    def send_messages():
        try:
            while True:
                message = input()  # Remove prompt for cleaner UI
                chat_message = chat_pb2.ChatMessage(user=user_name, message=message)
                yield chat_message
        except KeyboardInterrupt:
            return

    def receive_messages(response_iterator):
        try:
            for response in response_iterator:
                print(f"\n{response.user}: {response.message}")
                print("Enter message: ", end='', flush=True)  # Re-display prompt
        except grpc.RpcError:
            print("\nDisconnected from server")
            return

    print(f"Connected as {user_name}. Enter messages:")
    responses = stub.Chat(send_messages())
    receive_thread = threading.Thread(target=receive_messages, args=(responses,), daemon=True)
    receive_thread.start()

    try:
        receive_thread.join()
    except KeyboardInterrupt:
        print("\nDisconnecting...")

if __name__ == '__main__':
    user_name = input("Enter your username: ")
    run(user_name)
