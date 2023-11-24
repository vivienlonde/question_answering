from typing import Union
from fastapi import FastAPI

from generate_answer import get_answer

app = FastAPI()

@app.post("/{session_id}/question")
def read_item(session_id: int, question: Union[str, None] = None):
    answer = get_answer(question)
    return {"answer": answer}

@app.post("/{session_id}/context")
def read_item(session_id: int, question: Union[str, None] = None):
    # todo
    return {"number of tokens of the context": 5}



