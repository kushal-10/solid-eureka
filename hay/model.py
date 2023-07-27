from haystack.nodes import PromptNode, PromptTemplate
from haystack.nodes import AnswerParser
from haystack.nodes import TransformersSummarizer
from haystack import Document




def prompting_model():
    '''
    Define a prompt node in haystack pipeline
    ''' 

    prompt_node = PromptNode(model_name_or_path="facebook/galactica-125m", default_prompt_template="deepset/question-answering-per-document")
    
    # prompt_node = PromptNode(model_name_or_path="facebook/opt-350m", default_prompt_template=lfqa_prompt)

    return prompt_node


def summarize():

    '''
    Use a summarizer node, to summarize the output of generator
    To remove redundancy/repitition
    '''

    summarizer = TransformersSummarizer(model_name_or_path="google/pegasus-xsum")

    return summarizer





    
