import os

from inventory.Item import FixtureSpec


class WelcomeSign(FixtureSpec):
    def __init__(self):
        neighborhood = os.getcwd().split("/")[-1]
        self.message = f"🏪 Welcome to the {neighborhood} Bodega! 🏪"

    def __str__(self) -> str:
        return self.message

    def use(self) -> str:
        self.__str__()


def main():
    sign = WelcomeSign()
    print(sign)


if __name__ == "__main__":
    main()
