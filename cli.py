import argparse
from core.logic import oblicz_wynik


def main():
    parser = argparse.ArgumentParser(description="Program CLI dla Merito")
    parser.add_argument("a", type=int, help="Pierwsza liczba")
    parser.add_argument("b", type=int, help="Druga liczba")
    args = parser.parse_args()

    wynik = oblicz_wynik(args.a, args.b)
    print(f"Wynik operacji: {wynik}")


if __name__ == "__main__":
    main()
