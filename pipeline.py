from model import prompting_model
from haystack.pipelines import Pipeline
from retriever import retriever1


prompt_node = prompting_model() 
retriever = retriever1()

pipe = Pipeline()
pipe.add_node(component=retriever, name="retriever", inputs=["Query"])
pipe.add_node(component=prompt_node, name="prompt_node", inputs=["retriever"])

output = pipe.run(query="What is the best way to reduce emissions in last -mile supply chain")

# print(output["answers"][0].answer)
print(output['results'])