
from memory import initialise_memory, save_memory, get_memory, delete_memory


def main():
    initialise_memory()

    print("\nContinuum is online.")
    print("Commands:")
    print("  /remember key=value")
    print("  /recall key")
    print("  /forget key")
    print("  exit")

    while True:
        message = input("\nYou: ").strip()

        if not message:
            continue

        if message.lower() == "exit":
            print("Continuum shutting down. Goodbye!")
            break

        elif message.startswith("/remember "):
            content = message[len("/remember "):]
            
            if "=" not in content:
                print("Continuum: Use /remember key=value")
                continue

            key, value = content.split("=", 1)
            key = key.strip()
            value = value.strip()

            if not key or not value:
                print("Continuum: Both key and value are required.")
                continue

            save_memory(key, value)
            print(f"Continuum: I'll remember that {key} = {value}.")

        elif message.startswith("/recall "):
            key = message[len("/recall "):].strip()

            if not key:
                print("Continuum: Please provide a memory key.")
                continue

            result = get_memory(key)

            if result is not None:
                print(f"Continuum: {key} = {result}")
            else:
                print(f"Continuum: I don't have a memory for {key}.")

        elif message.startswith("/forget "):
            key = message[len("/forget "):].strip()

            if not key:
                print("Continuum: Please provide a memory key.")
                continue

            if delete_memory(key):
                print(f"Continuum: Deleted the memory for {key}.")
            else:
                print(f"Continuum: I couldn't find a memory for {key}.")

        elif message.lower() == "hello":
            print("Continuum: Hello! How can I help?")

        elif message.lower() == "how are you":
            print("Continuum: I'm functioning perfectly.")

        else:
            print("Continuum: I don't understand that command yet.")


if __name__ == "__main__":
    main()
