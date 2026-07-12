import ollama


def ask_llama(prompt):
    """
    Sends a prompt to the local Llama model.
    """

    response = ollama.chat(
        model="llama3.2",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]