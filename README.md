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

2) Running the whole retriever generator pipeline and print the output

```
python3 main.py --rgpipeline
```

If CUDA out of memory error occurs, use the following script to clear GPU cache:
```
python3 clear.py
```

## Results

Result of an example question, which can be changed in main.py

Q = "What are the main topics from all these papers"
A = 1. Consumer waste is a major issue in the food
industry. The food industry is a major contributor
to food waste. The food industry is responsible for
over 80% of the food waste in the United States.
2. Consumers are responsible for over 80% of the
food waste in the United States. The food industry
is responsible for over 80% of the food waste in the
United States.
3. Consumers are responsible for over 80% of the
food