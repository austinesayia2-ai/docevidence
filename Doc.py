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

    score = min(100, avg_word_length * 10)

    return round(score, 2)


def analyze(text):
    plagiarism = simple_plagiarism_score(text)
    ai = ai_signal(text)

    final = (plagiarism * 0.6) + (ai * 0.4)

    return {
        "plagiarism": plagiarism,
        "ai_signal": ai,
        "final_score": final
    }


# TEST
print(analyze("Students should submit original work in exams"))