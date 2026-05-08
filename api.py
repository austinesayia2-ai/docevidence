from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Document(BaseModel):
    text: str


def simple_plagiarism_score(text):
    known_texts = [
        "Students should submit original work",
        "Education systems use AI tools",
        "Plagiarism is academic dishonesty"
    ]

    matches = 0
    for doc in known_texts:
        if doc.lower() in text.lower():
            matches += 1

    return (matches / len(known_texts)) * 100


def ai_signal(text):
    words = text.split()
    if len(words) == 0:
        return 0

    avg_word_length = sum(len(w) for w in words) / len(words)
    return min(100, avg_word_length * 10)


@app.get("/")
def home():
    return {"message": "DocEvidence API running"}


@app.post("/analyze")
def analyze(doc: Document):
    text = doc.text

    plagiarism = simple_plagiarism_score(text)
    ai = ai_signal(text)

    final = (plagiarism * 0.6) + (ai * 0.4)

    return {
        "plagiarism": plagiarism,
        "ai_signal": ai,
        "final_score": final
    }