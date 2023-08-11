import os
import speedtest

# ANSI color codes
GREEN_TEXT = "\033[92m"
RESET_TEXT = "\033[0m"


def print_green(text):
    """Prints the given text in green color."""
    print(f"{GREEN_TEXT}{text}{RESET_TEXT}")

def print_red(text):
    print("\033[91m" + text + "\033[0m")


def clear_console():
    """Clears the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')


def test_speed():
    """Tests and prints the internet speed."""
    try:
        st = speedtest.Speedtest()
        st.get_best_server()

        print_green("Testing download speed...")
        download_speed = st.download() / 10 ** 6
        print_green(f"Download speed: {download_speed:.2f} Mbps")

        print_green("Testing upload speed...")
        upload_speed = st.upload() / 10 ** 6
        print_green(f"Upload speed: {upload_speed:.2f} Mbps")
    except speedtest.ConfigRetrievalError as e:
        print_red(f"Error connecting to the server. {e}")
    except Exception as e:
        print_red(f"An unexpected error occurred. {e}")


def get_user_choice():
    """Prompts the user to choose a mode and returns the choice."""
    print_green("Choose mode:")
    print_green("1 - single (recommended)")
    print_green("2 - multi")
    return input().strip()


def main():
    """Main function to run the speed test."""
    while True:
        clear_console()
        mode = None

        while mode not in ['1', '2']:
            mode = get_user_choice()
            if mode not in ['1', '2']:
                print_green('Wrong mode selection! Try again.')

        test_speed()

        retry = input("Do you want to retry the speed test? (y/n): ").strip().lower()
        if retry != 'y':
            clear_console()
            break


if __name__ == '__main__':
    main()
