from typing import Union
from fastapi import FastAPI

from generate_answer import get_answer
from embedding import compute_embedding

app = FastAPI()

@app.post("/{session_id}/question")
def read_item(session_id: int, question: Union[str, None] = None):
    answer = get_answer(question)
    return {"answer": answer}

@app.post("/{session_id}/context")
def read_item(session_id: int, context = None):
    nb_of_letters = compute_embedding(context) *1000
    return {"number of letters of the context": nb_of_letters}



