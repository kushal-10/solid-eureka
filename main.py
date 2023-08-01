import argparse
from hay.retriever import generate_docs
from hay.pipeline import rg_pipeline, rs_pipeline, rsg_pipeline
from app import application


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

    parser.add_argument(
        '--rspipeline', dest='rspipeline',
        action='store_true'
    )

    parser.add_argument(
        '--conv', dest='conv',
        action='store_true'
    )

    parser.add_argument(
        '--gradio', dest='gradio',
        action='store_true'
    )

    args = parser.parse_args()

    if args.docs:
        '''
        Use this argument to generate the docs and store in DOCUMENT format
        '''
        generate_docs(overlap=10, length=100)

    if args.rgpipeline:
        '''
        Use this argument to run the base retriever generator pipeline
        '''
        question = "How to reduce emissions?"
        rg_pipeline(question)

    if args.rspipeline:
        '''
        Use this argument to run the retriever summarizer pipeline
        '''
        question = "Who are the main users in the two-sided market"
        # question = "What are the decisions made in the two-sided market? And who makes this decision? "
        # question = "What are the main effects in the two-sided market?"
        # question = "What are the main topics in these papers?"
        answer = rs_pipeline(question)     
        print(answer)

    if args.conv:
        '''
        Use this argument to run the pipeline using conversational agent class
        '''
        op = rsg_pipeline()
        print(op)
    
    if args.gradio:
        '''
        Use this argument to run the application
        '''   
        application()

    return None


if __name__ == '__main__':
    main()