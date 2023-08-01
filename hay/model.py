from haystack.nodes import PromptNode, PromptTemplate
from haystack.nodes import AnswerParser
from haystack.nodes import TransformersSummarizer

def prompting_model():
    '''
    Define a prompt node in haystack pipeline
    ''' 

    # prompt_node = PromptNode(model_name_or_path="facebook/galactica-125m", default_prompt_template="deepset/question-answering-per-document")
    
    prompt_node = PromptNode(model_name_or_path="facebook/galactica-125m")

    return prompt_node

def prompting_model_2():
    '''
    Define a prompt node in haystack pipeline, with detailed prompt
    '''

    custom_prompt = PromptTemplate(prompt = """ You are a helpful and knowledgeable agent. To achieve your goal of answering complex questions,
                                                 you have access to the following paragraph :
                                                {join(documents)}

                                                Your output should be a detailed summary of the paragraph
                                                 """)
    
    summarization_template = PromptTemplate("deepset/summarization")
                                   
    prompt_node = PromptNode(model_name_or_path="facebook/galactica-125m", default_prompt_template=custom_prompt)

    return prompt_node

def summarize():

    '''
    Use a summarizer node, to summarize the output of generator
    To remove redundancy/repitition
    '''

    summarizer = TransformersSummarizer(model_name_or_path="google/pegasus-xsum")

    return summarizer





    
