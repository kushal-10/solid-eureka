from hay.model import prompting_model, summarize
from haystack.pipelines import Pipeline, SearchSummarizationPipeline
from hay.retriever import retriever1

def rg_pipeline(question):
    '''
    Defines a pipeline of retriever and generator and generates output for the given question
    '''

    prompt_node = prompting_model() 
    retriever = retriever1()

    pipe = Pipeline()
    pipe.add_node(component=retriever, name="retriever", inputs=["Query"])
    pipe.add_node(component=prompt_node, name="prompt_node", inputs=["retriever"])

    output = pipe.run(query=question)

    for i in range(1, len(output['results'])):
        print("Value at  " + str(i))
        print(output["results"][i])

    return None


def rs_pipeline(question):
    '''
    Defines a pipeline of retriever and summarizer and generates output for the given question
    '''

    retriever = retriever1()
    summarizer = summarize()

    # Get top 10 results from the retriever and summarize them
    pipeline = SearchSummarizationPipeline(summarizer=summarizer, retriever=retriever)
    result = pipeline.run(query=question, params={"Retriever": {"top_k": 10}})

    output = ''
    for i in range(len(result['documents'])):
        output += result['documents'][i].meta['summary']

    print(output)
    
    return None






