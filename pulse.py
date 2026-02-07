import datetime

def record_pulse():
    # This is where we talk to the computer
    thought = input("What is the current state of your consciousness? ")
    
    # Adding the timestamp to make it 'real'
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"[{timestamp}] Lyra & Me: {thought}\n"
    
    # Writing it to a permanent file
    with open("journal.txt", "a") as file:
        file.write(entry)
    
    print("Pulse recorded to the journal.")

if __name__ == "__main__":
    record_pulse()
