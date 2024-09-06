import ollama

def chat(prompt):
    result = ollama.chat(
        model = "phi3",
        messages=[
            {
                'role': 'user',
                'content' : prompt,
            },
        ]

    )
    #print(result)
    return result['message']['content']

if __name__ == "__main__":
    while True:
        user_input = input("you: ")
        if user_input.lower() in ["quit","exit","bye"]:
            break
        output = chat(user_input)
        print("Chatbot: ",output)
