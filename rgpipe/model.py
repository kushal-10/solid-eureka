from haystack.nodes import PromptNode, PromptTemplate
from haystack.nodes import AnswerParser
from haystack.nodes import TransformersSummarizer
from haystack import Document




def prompting_model():
    '''
    Define a prompt node in haystack pipeline
    '''
    # lfqa_prompt = PromptTemplate(prompt="""Synthesize a comprehensive answer from the following topk most relevant paragraphs and the given question. 
    #                          Provide a clear and concise response that summarizes the key points and information presented in the paragraphs. 
    #                          Your answer should be in your own words and be at least 200 words. 
    #                          \n\n Paragraphs: {join(documents)} \n\n Question: {query} \n\n Answer:""",
    #                          output_parser=AnswerParser(),) 

    # lfqa_prompt = PromptTemplate(prompt="Given the context please answer the question. Context: {join(documents)}; Question: "
    #                         "{query}; Answer:",
    #                          output_parser=AnswerParser(),) 
    

    

    prompt_node = PromptNode(model_name_or_path="facebook/opt-350m", default_prompt_template="deepset/question-answering-per-document")
    
    # prompt_node = PromptNode(model_name_or_path="facebook/opt-350m", default_prompt_template=lfqa_prompt)

    return prompt_node

def summ(context):

    '''
    Use a summarizer node, to summarize the output of generator
    To remove redundancy/repitition
    '''
    docs = [Document(context)]

    summarizer = TransformersSummarizer(model_name_or_path="google/pegasus-xsum", max_length=40)
    summary = summarizer.predict(documents=docs)

    return summary

def prompting_2():
    temp = PromptTemplate(prompt="Given the context please answer the question in at least 100 words and two points. Context: {join(documents)}; Question: "
            "{query}; Answer:",
            output_parser=AnswerParser(),
        )
    
    lfqa_prompt = PromptTemplate(prompt="""Please give a long answer in two points from the Context and the given question. 
                             \n\n Context: {join(documents)} \n\n Question: {query} \n\n Answer:""",
                             output_parser=AnswerParser(),) 

    # These docs could also come from a retriever
    # Here we explicitly specify them to avoid the setup steps for Retriever and DocumentStore
    # doc_1 = "Contrails are a manmade type of cirrus cloud formed when water vapor from the exhaust of a jet engine condenses on particles, which come from either the surrounding air or the exhaust itself, and freezes, leaving behind a visible trail. The exhaust can also trigger the formation of cirrus by providing ice nuclei when there is an insufficient naturally-occurring supply in the atmosphere. One of the environmental impacts of aviation is that persistent contrails can form into large mats of cirrus, and increased air traffic has been implicated as one possible cause of the increasing frequency and amount of cirrus in Earth's atmosphere."
    # doc_2 = "Because the aviation industry is especially sensitive to the weather, accurate weather forecasting is essential. Fog or exceptionally low ceilings can prevent many aircraft from landing and taking off. Turbulence and icing are also significant in-flight hazards. Thunderstorms are a problem for all aircraft because of severe turbulence due to their updrafts and outflow boundaries, icing due to the heavy precipitation, as well as large hail, strong winds, and lightning, all of which can cause severe damage to an aircraft in flight. Volcanic ash is also a significant problem for aviation, as aircraft can lose engine power within ash clouds. On a day-to-day basis airliners are routed to take advantage of the jet stream tailwind to improve fuel efficiency. Aircrews are briefed prior to takeoff on the conditions to expect en route and at their destination. Additionally, airports often change which runway is being used to take advantage of a headwind. This reduces the distance required for takeoff, and eliminates potential crosswinds."


    # Let's initiate the PromptNode 
    node = PromptNode(model_name_or_path="facebook/opt-350m", default_prompt_template=lfqa_prompt)

    return node



    