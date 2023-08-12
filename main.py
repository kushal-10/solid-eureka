import argparse
from hay.retriever import generate_docs
from hay.pipeline import rg_pipeline, rs_pipeline, rsg_pipeline
from app import application

d = 'data2'

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
        generate_docs(overlap=10, length=100, d=d)

    if args.rgpipeline:
        '''
        Use this argument to run the base retriever generator pipeline
        '''
        question = "What is the reachability problem in the Physical Internet network, and how does it differ from the Digital Internet?"


        rg_pipeline(question, d)

    if args.rspipeline:
        '''
        Use this argument to run the retriever summarizer pipeline
        '''
        # question = "the reachability problem is?"
        # question = "Does the DI requires significant energy"
        question = "What does the current model illustrate?"

        # question = "How to solve the Last Mile Problem?"
        # question = "How to reduce Carbon Emissions?"
        # question = "What are the main topics of these research papers?"

        # question = "Who are the main users in the two-sided market"
        # question = "What are the decisions made in the two-sided market? And who makes this decision? "
        # question = "What are the main effects in the two-sided market?"
        # question = "What are the main topics in these papers?"
        answer = rs_pipeline(question, d)     
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