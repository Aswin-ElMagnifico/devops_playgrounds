from main import greeter_message


def test_greeter():
    assert greeter_message() == "Hello world!"
