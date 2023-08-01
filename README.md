# solid-eureka

## Introduction

This project aims to build a closed domain question answering system (CDQA) targeting the specific domain of Supply Chain Management. 
The target is to provide a model with 100-1000 Research Papers around a specific topic, and then ask the model questions about them.
This type of models can be used by academics and researchers to know the latest topics around a specific field and clear any doubts of user, if any.

## Usage

After cloning this repository, two functionalities are provided.

1) Running a script to preprocess the PDF files, and generate the DOCUMENTS for haystack pipeline.

```
python3 main.py --docs
```

2) Running the retriever generator pipeline and print the output

```
python3 main.py --rgpipeline
```
3) Running the retriever summarizer pipeline and print the output

```
python3 main.py --rspipeline
```

4) Running the chatbot application on LocalHost (7860)

```
python3 main.py --gradio
```

If CUDA out of memory error occurs, use the following script to clear GPU cache:
```
python3 clear.py
```

## Results
