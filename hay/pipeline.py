from hay.model import prompting_model
from haystack.pipelines import Pipeline
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






