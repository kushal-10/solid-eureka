from haystack.nodes import PromptNode, PromptTemplate
from haystack.nodes import AnswerParser

def prompting_model():
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