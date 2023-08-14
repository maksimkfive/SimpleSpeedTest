import os
import speedtest
import datetime

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
        best_server = st.get_best_server()

        # Display server information
        print_green(f"Testing using server: {best_server['sponsor']} ({best_server['name']}, {best_server['country']})")
        print_green("--------------------------------------------------")

        # Ping test (converted to integer)
        ping_val = int(st.results.ping)
        print_green(f"Ping: {ping_val} ms")

        print_green("Testing download speed...")
        download_speed = st.download() / 10 ** 6
        print_green(f"Download speed: {download_speed:.2f} Mbps")

        print_green("Testing upload speed...")
        upload_speed = st.upload() / 10 ** 6
        print_green(f"Upload speed: {upload_speed:.2f} Mbps")

        # Prompt to save results
        save = input("Do you want to save the results? (y/n): ").strip().lower()
        if save == 'y':
            with open("speedtest_results.txt", "a") as f:
                f.write(f"Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write(f"Server: {best_server['sponsor']} ({best_server['name']}, {best_server['country']})\n")
                f.write(f"Ping: {ping_val} ms\n")
                f.write(f"Download speed: {download_speed:.2f} Mbps\n")
                f.write(f"Upload speed: {upload_speed:.2f} Mbps\n")
                f.write("--------------------------------------------------\n")
            print_green("Results saved!")

    except speedtest.ConfigRetrievalError as e:
        print_red(f"Error connecting to the server. {e}")
    except Exception as e:
        print_red(f"An unexpected error occurred. {e}")


def main():
    """Main function to run the speed test."""
    while True:
        clear_console()

        test_speed()

        retry = input("Do you want to retry the speed test? (y/n): ").strip().lower()
        if retry == 'n':
            clear_console()
            break


if __name__ == '__main__':
    main()
