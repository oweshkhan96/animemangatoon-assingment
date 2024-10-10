import nltk


data = {
    "what is castle swimmer about": "Castle Swimmer is about a young mermaid's journey to discover the ocean's mysteries and her destiny.",
    "who are the main characters": "Key characters include Siren, the mermaid protagonist, and ocean dwellers like Kappa, Pim, and Pagoon.",
    "tell me more about the plot": "The story explores friendship, adventure, and self-discovery as characters confront challenges, including curses and prophecies.",
    "castle swimmer chapter 83": "In Chapter 83, Siren learns he is cursed, complicating his prophesied role as savior. He vows to fight for his life despite the prophecy.",
    "castle swimmer chapter 84": "Chapter 84 reveals that a mini-god must uphold the curse. Siren reunites with friends and escapes danger.",
    "castle swimmer chapter 85": "In Chapter 85, Pim apologizes for leading them into danger. Siren shares his emotional struggles and memories of his mother with her.",
    "castle swimmer chapter 86": "Chapter 86 shows Pagoon moved by Siren's determination to break the curse. Flashbacks connect Kappa and Arp, guiding Siren's quest for answers.",
    "castle swimmer chapter 87": "Chapter 87 opens with Kappa's unsettling dreams and his discussion with Mono about uncertain futures and a new prophecy.",
    "castle swimmer chapter 88": "In Chapter 88, Kappa faces an unavoidable prophecy urged by Queen Nethimir, leading to reflections on his past with Queen Nee.",
    "castle swimmer chapter 89": "Chapter 89 features Kappa reuniting with Queen Nee, discussing recent troubles and Kappa's willingness to help fulfill a prophecy."
}

def chatbot_response(user_input):
    tokens = user_input.lower().split()
    
    for key in data:
        if any(word in key for word in tokens):
            return data[key]
    
    return "I'm sorry, I don't understand the question."



while True:
    user_input = input("You: ")
    if user_input.lower() in ['exit', 'quit']:
        print("Chatbot: Goodbye!")
        break
    response = chatbot_response(user_input)
    print("Chatbot:", response)
