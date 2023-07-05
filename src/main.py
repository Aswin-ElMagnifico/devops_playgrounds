import os


def greeter_message():
    return "Hello world!"


def print_envs():
    print(os.environ.get("API_KEY"))


if __name__ == '__main__':
    print(greeter_message())
    print_envs()
