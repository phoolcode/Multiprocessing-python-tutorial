import multiprocessing

def send_message(queue):
    message = "Hello, team!"
    queue.put(message)  # Sending message through the queue
    print(f"Sent: {message}")

def receive_message(queue):
    message = queue.get()  # Receiving message from the queue
    print(f"Received: {message}")

if __name__ == "__main__":
    # Create a queue
    queue = multiprocessing.Queue()

    # Create two processes: one for sending messages and one for receiving messages
    sender_process = multiprocessing.Process(target=send_message, args=(queue,))
    receiver_process = multiprocessing.Process(target=receive_message, args=(queue,))

    sender_process.start()
    receiver_process.start()

    sender_process.join()
    receiver_process.join()

    print("done.")