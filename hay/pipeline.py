from hay.model import prompting_model, summarize
from hay.model import prompting_model_2
from haystack.pipelines import Pipeline, SearchSummarizationPipeline
from haystack.agents.memory import ConversationSummaryMemory
# from haystack.agents.conversational import 
from haystack import Document
from hay.retriever import retriever1

def rg_pipeline(question, d):
    '''
    Defines a pipeline of retriever and generator and generates output for the given question
    '''

    prompt_node = prompting_model() 
    retriever = retriever1(d)

    pipe = Pipeline()
    pipe.add_node(component=retriever, name="retriever", inputs=["Query"])
    pipe.add_node(component=prompt_node, name="prompt_node", inputs=["retriever"])

    output = pipe.run(query=question)

    for i in range(1, len(output['results'])):
        print("Value at  " + str(i))
        print(output["results"][i])

    return None


def rs_pipeline(question, d):
    '''
    Defines a pipeline of retriever and summarizer and generates output for the given question
    '''

    retriever = retriever1(d)
    summarizer = summarize()

    # Get top 10 results from the retriever and summarize them
    pipeline = SearchSummarizationPipeline(summarizer=summarizer, retriever=retriever)
    result = pipeline.run(query=question, params={"Retriever": {"top_k": 2}})

    output = ''
    for i in range(len(result['documents'])):
        output += result['documents'][i].meta['summary']

    # print(output)
    
    return output

# Try this later
def conv_agent(question="How to reduce carbon emissions?"):
    # '''
    # Defines a pipeline using the conversational agent class
    # '''
    # prompt_node = prompting_model()
    # summary_memory = ConversationSummaryMemory(prompt_node=prompt_node)
    # conversational_agent = ConversationalAgent(prompt_node=prompt_node, memory=summary_memory)


    output = None
    return output

def rsg_pipeline(question, d):

    '''
    Defines a pipeline using the summarization pipeline with an additional prompt node
    '''
    # retriever = retriever1(d)
    # summarizer = summarize()
    # pipeline = SearchSummarizationPipeline(summarizer=summarizer, retriever=retriever)
    # result = pipeline.run(query=question, params={"Retriever": {"top_k": 5}})

    # output = ''
    # for i in range(len(result['documents'])):
    #     output += result['documents'][i].meta['summary']

    output = "In recent years, a number of papers have examined the impact of incentives on firms to reduce carbon emissions.The European Union's (EU) Emissions Trading Scheme (ETS) aims to reduce greenhouse gas (GHG) emissions by trading carbon dioxide emissions from major emitters.The aim of this article is to provide a reference for managers to improve the attractiveness of their stores to consumers and for the gov- ernment to design carbon policy.In this paper, we discuss how the number of retail stores in a market affects the carbon emissions in the supply chain, and present our mathematical models to illustrate how retail store density can affect the carbon emissions in the supply chain, accounting for consumers’ emissions and transportation cost.KeyTakeaways:"
    node = prompting_model_2()
    pipe = Pipeline()
    pipe.add_node(component=node, name="prompt_node", inputs = ["Query"])

    f_output = pipe.run(query=question, documents=[Document(output)])    
    # op = [a.answer for a in f_output["answers"]]

    return f_output





