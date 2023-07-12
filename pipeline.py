from model import prompting_model, summ, prompting_2
from haystack.pipelines import Pipeline
from retriever import retriever1
from haystack import Document

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

    # for i in range(1, len(output['results'])):
    #     context = output["results"][i]
    #     s = summ(context)
    #     print("Value at  " + str(i))
    #     print(s[0].meta["summary"])

    for i in range(1, len(output['results'])):
        print("Value at  " + str(i))
        print(output["results"][i])

    return None






