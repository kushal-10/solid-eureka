import argparse
from hay.retriever import generate_docs
from hay.pipeline import rg_pipeline


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '--docs', dest='docs',
        action = 'store_true'
    )

    parser.add_argument(
        '--rgpipeline', dest='rgpipeline',
        action = 'store_true'
    )

    args = parser.parse_args()

    if args.docs:
        '''
        Use this argument to generate the docs and store in DOCUMENT format
        '''
        generate_docs(overlap=50, length=512)

    if args.rgpipeline:
        '''
        Use this argument to run the base retriever generator pipeline
        '''
        question = "How to reduce emissions?"
        rg_pipeline(question)

    return None


if __name__ == '__main__':
    main()