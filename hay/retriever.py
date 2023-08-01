from haystack.utils import convert_files_to_docs
from haystack.nodes import PreProcessor

import pyarrow as pa
import pyarrow.dataset as ds
import pandas as pd
from datasets import Dataset, load_from_disk
import pandas as pd

from haystack.nodes import BM25Retriever
from haystack.document_stores import InMemoryDocumentStore
from haystack.document_stores import FAISSDocumentStore
from haystack.nodes import DensePassageRetriever
from haystack.document_stores import InMemoryDocumentStore
from haystack.nodes import TfidfRetriever


import warnings
warnings.filterwarnings('ignore')

def generate_docs(overlap, length):

    '''
    Takes in split length and split overlap
    Saves the docs in a pandas dataframe
    '''
    all_docs = convert_files_to_docs(dir_path='data2')

    preprocessor = PreProcessor(
        clean_empty_lines=True,
        clean_whitespace=True,
        clean_header_footer=True,
        split_by="word",
        split_overlap=overlap,
        split_length=length,
        split_respect_sentence_boundary=False,
    )

    docs = preprocessor.process(all_docs)

    # print(f"n_files_input: {len(all_docs)}\nn_docs_output: {len(docs)}")

    df = pd.DataFrame(docs)
    dataset = Dataset(pa.Table.from_pandas(df))
    # dataset.save_to_disk('outputs/docs-dataset')
    dataset.save_to_disk('outputs/docs-dataset-2')

    return None


def retriever1():
    '''
    Use BM25 Retriever to retrieve data
    '''

    # dataset = load_from_disk('outputs/docs-dataset')
    dataset = load_from_disk('outputs/docs-dataset-2')

    # BM25Retriever with InMemoryDocumentStore
    document_store = InMemoryDocumentStore(use_bm25=True)
    document_store.write_documents(dataset)
    retriever = BM25Retriever(document_store=document_store, top_k=10)

    return retriever


# def retriever2():
#     document_store = FAISSDocumentStore(similarity="dot_product")
#     retriever = DensePassageRetriever(
#         document_store=document_store,
#         query_embedding_model="facebook/dpr-question_encoder-single-nq-base",
#         passage_embedding_model="facebook/dpr-ctx_encoder-single-nq-base"
#     )
#     document_store.update_embeddings(retriever)

#     return retriever
# generate_docs(20, 250)
# ret = retriever2()
