import multiprocessing

def send_message(conn):
    message = "Hello, team!"

    conn.send(message)  # Sending message through the pipe
    print(f"Sent: {message}")

    conn.close()

def receive_message(conn):
    message = conn.recv()  # Receiving message from the pipe
    print(f"Received: {message}")

if __name__ == "__main__":
    # Create a pipe
    parent_conn, child_conn = multiprocessing.Pipe()

    # Create two processes: one for sending messages and one for receiving messages
    sender_process = multiprocessing.Process(target=send_message, args=(parent_conn,))
    receiver_process = multiprocessing.Process(target=receive_message, args=(child_conn,))

    sender_process.start()
    receiver_process.start()

    sender_process.join()
    receiver_process.join()

    print("done.")
