import argparse
from retriever import generate_docs


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '--docs', dest='docs',
        action = 'store_true'
    )

    args = parser.parse_args()

    if args.docs:
        generate_docs(overlap=50, length=512)

    return None


if __name__ == '__main__':
    main()