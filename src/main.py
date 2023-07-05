import os


def greeter_message():
    return "Hello world!"


def print_envs():
    if os.environ.get("API_KEY") == "abcdefg":
        print("abcdefg")
    else:
        print("encrypted")


if __name__ == '__main__':
    print(greeter_message())
    print_envs()
