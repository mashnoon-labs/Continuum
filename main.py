
from memory import initialise_memory, save_memory, get_memory, delete_memory
from ai import ask_ai, extract_memories


def main():
    initialise_memory()

    print("\nContinuum is online.")
    print("Your AI assistant is ready.")
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
            print("\nContinuum shutting down. Goodbye!")
            break

        elif message.startswith("/remember "):
            content = message[len("/remember "):]

            if "=" not in content:
                print("\nContinuum: Use /remember key=value")
                continue

            key, value = content.split("=", 1)
            key = key.strip()
            value = value.strip()

            if not key or not value:
                print("\nContinuum: Both key and value are required.")
                continue

            save_memory(key, value)
            print(f"\nContinuum: I'll remember that {key} = {value}.")

        elif message.startswith("/recall "):
            key = message[len("/recall "):].strip()

            if not key:
                print("\nContinuum: Please provide a memory key.")
                continue

            result = get_memory(key)

            if result is not None:
                print(f"\nContinuum: {key} = {result}")
            else:
                print(f"\nContinuum: I don't have a memory for {key}.")

        elif message.startswith("/forget "):
            key = message[len("/forget "):].strip()

            if not key:
                print("\nContinuum: Please provide a memory key.")
                continue

            if delete_memory(key):
                print(f"\nContinuum: Deleted the memory for {key}.")
            else:
                print(f"\nContinuum: I couldn't find a memory for {key}.")

        else:
            try:
                # Generate the AI response
                response = ask_ai(message)
                print(f"\nContinuum: {response}")

                # Extract potential memories
                try:
                    memories = extract_memories(message)

                    automatic = memories.get("automatic", [])
                    confirmation = memories.get("confirmation", [])

                    # Process automatically approved memory candidates
                    for memory in automatic:
                        key = memory.get("key", "").strip()
                        value = memory.get("value", "").strip()

                        if not key or not value:
                            continue

                        existing = get_memory(key)

                        if existing is None:
                            save_memory(key, value)
                            print(
                                f"\nContinuum: I'll remember that "
                                f"{key} = {value}."
                            )

                        elif existing != value:
                            confirmation.append(memory)

                    # Ask before saving uncertain or conflicting memories
                    for memory in confirmation:
                        key = memory.get("key", "").strip()
                        value = memory.get("value", "").strip()

                        if not key or not value:
                            continue

                        existing = get_memory(key)

                        if existing == value:
                            continue

                        print("\nContinuum: Would you like me to remember:")
                        print(f"{key} = {value}")

                        if existing is not None:
                            print(f"Currently stored: {existing}")

                        approval = input("You (yes/no): ").strip().lower()

                        if approval in ["yes", "y"]:
                            save_memory(key, value)
                            print("\nContinuum: Memory saved.")
                        else:
                            print("\nContinuum: No problem. I haven't saved it.")

                except Exception as error:
                    print(f"\nContinuum: I couldn't process memories: {error}")

            except Exception as error:
                print(f"\nContinuum: I encountered an error: {error}")


if __name__ == "__main__":
    main()


