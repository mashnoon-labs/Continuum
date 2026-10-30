
from memory import initialise_memory, save_memory, get_memory


def main():
    initialise_memory()

    print("Continuum is online.")

    # Test memory retrieval
    name = get_memory("name")
    print(f"Hey what's up {name}")

    print("Type 'exit' to shut me down.")

    while True:
        message = input("You: ")

        if message.lower() == "exit":
            print("Continuum shutting down. Goodbye!")
            break

        if "hello" in message.lower():
            print("Continuum: Hello! How can I help?")

        elif "how are you" in message.lower():
            print("Continuum: I'm functioning perfectly.")

        else:
            print("Continuum: I'm not sure how to respond to that yet.")


main()
