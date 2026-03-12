from time import sleep


def install():
    print("Example plugin install hook, waiting for 3 seconds...")
    sleep(3)
    print("Example plugin install hook complete")


def uninstall():
    print("Example plugin uninstall hook, waiting for 3 seconds...")
    sleep(3)
    print("Example plugin uninstall hook complete")