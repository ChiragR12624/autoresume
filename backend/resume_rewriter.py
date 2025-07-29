from transformers import pipeline

# Load summarization model (will download the first time)
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

def rewrite_section(text):
    if len(text.split()) < 30:
        return "Text too short for summarization"
    
    result = summarizer(text, max_length=60, min_length=30, do_sample=False)
    return result[0]['summary_text']

if __name__ == "__main__":
    # Example Objective section text
    sample_objective = """
    A highly motivated and detail-oriented computer science graduate with a strong foundation in software development,
    data structures, and algorithms. Seeking an entry-level position where I can apply my knowledge and contribute to innovative projects.
    """

    rewritten = rewrite_section(sample_objective)
    print("\n🔹 Original Objective:\n", sample_objective)
    print("\n✅ Rewritten Objective:\n", rewritten)
