from get_skinport_prices.get_skinport_prices import get_skinport_price


def main():
    """
    The main logic of the script.
    """

    # Test Inputs
    skin = "awp wildfire"

    # TODO: This represents field tested right now but eventually an ENUM should probably be used.
    condition = 3
    is_stattrack = False

    print(get_skinport_price(skin, condition, is_stattrack))


if __name__ == "__main__":
    main()
