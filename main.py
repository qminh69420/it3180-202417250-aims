from aims.dvd import DigitalVideoDisc
from aims.cart import Cart
from aims import __version__

def main():
    print(f"AIMS Version: {__version__}")
    cart = Cart()

    discs = [
        DigitalVideoDisc(
            "The Lion King", "Animation", "Roger Allers", 89, 19.95
        ),
        DigitalVideoDisc(
            "Star Wars", "Science Fiction", "George Lucas", 121, 24.95
        ),
        DigitalVideoDisc(
            "Aladdin", "Animation", "John Musker", 90, 18.99
        ),
    ]

    for disc in discs:
        cart.add_digital_video_disc(disc)

    cart.print_cart()


if __name__ == "__main__":
    main()