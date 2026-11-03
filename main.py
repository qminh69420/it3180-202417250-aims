from aims.dvd import DigitalVideoDisc
from aims.cart import Cart


def main():
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

    print(f"Total cost: {cart.total_cost():.2f} $")


if __name__ == "__main__":
    main()
