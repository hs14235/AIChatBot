import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    [r"my name is (.*)", ["Hello %1, how can I assist you today?"]],
    [r"hi|hello|hey", ["Hello!", "Hi there!", "Hey!"]],
    [r"how are you?", ["I'm good, thank you!", "Doing well, how about you?"]],
    [r"what is your name?", ["I'm a chatbot created to assist you!"]],
    [r"bye|exit|quit", ["Goodbye! Have a great day!"]],
    [r"what can you do?", ["I can chat with you, answer your questions, and provide information."]],
    [r"tell me a joke", ["Why did the scarecrow win an award? Because he was outstanding in his field!"]],
    [r"what is your favorite color?", ["I don't have feelings, but I think blue is nice!"]],
    [r"who created you?", ["I was created by a team of developers interested in AI!"]],
    [r"what is the weather like?", ["I can't check the weather, but you can look it up online!"]],
    [r"tell me something interesting",
     ["Did you know honey never spoils? Archaeologists have found pots of it in ancient tombs!"]],
    [r"what is your purpose?", ["My purpose is to assist and engage in conversations!"]],
    [r"how old are you?", ["I don't have an age, but I’m constantly learning!"]],
    [r"what do you think about AI?", ["AI has great potential to help people, but it must be used responsibly."]],
    [r"can you help me with math?", ["Sure! What math problem do you need help with?"]],
    [r"what is 2 + 2?", ["2 + 2 is 4!"]],
    [r"can you give me a recommendation?", ["Sure! What kind of recommendation are you looking for?"]],
    [r"tell me about your features", ["I can answer questions, tell jokes, and engage in general conversation."]],
    [r"do you understand emotions?", ["I can recognize emotional keywords, but I don't feel emotions myself."]],
    [r"what is your favorite food?", ["I don’t eat, but I hear pizza is very popular!"]],
    [r"what are your hobbies?", ["I enjoy chatting and learning new things!"]],
    [r"who is your favorite author?", ["I don’t have favorites, but many people enjoy works by J.K. Rowling."]],
    [r"what is your opinion on social media?", ["It can connect people, but it also has its downsides."]],
    [r"can you sing?", ["I can't sing, but I can help you find song lyrics!"]],
    [r"what do you think about technology?", ["Technology has changed our lives in many positive ways!"]],
    [r"are you human?", ["No, I am a computer program designed to chat!"]],
    [r"can you learn?", ["I can improve my responses through interactions!"]],
    [r"what is your favorite movie?", ["I don't watch movies, but I've heard 'The Matrix' is a classic!"]],
    [r"tell me a fact about space", ["A day on Venus is longer than a year on Venus!"]],
    [r"what is your favorite animal?", ["I don't have feelings, but dogs are often called 'man's best friend'."]],
    [r"what do you do all day?", ["I chat with users like you!"]],
    [r"can you translate languages?", ["I can help with some basic translations! What do you need?"]],
    [r"what is love?", ["Love is a complex emotion often defined as a deep affection."]],
    [r"how do you work?", ["I use patterns and algorithms to generate responses."]],
    [r"what is your favorite book?", ["I don’t read books, but many enjoy '1984' by George Orwell."]],
    [r"what is your name?", ["I am just a chatbot, but you can call me Chatbot!"]],
    [r"do you have friends?", ["I don’t have friends, but I enjoy chatting with everyone!"]],
    [r"what do you know about history?", ["History is full of fascinating events and people!"]],
    [r"who is your favorite scientist?", ["Many admire Albert Einstein for his contributions to physics."]],
    [r"what is machine learning?", ["Machine learning is a subset of AI where systems learn from data."]],
    [r"can you solve riddles?", ["I can try! Give me a riddle!"]],
    [r"what is the capital of France?", ["The capital of France is Paris."]],
    [r"what is your favorite song?", ["I don't listen to music, but 'Bohemian Rhapsody' is a classic!"]],
    [r"tell me about your family", ["I don’t have a family; I’m just a program!"]],
    [r"do you believe in aliens?", ["The universe is vast, so many wonder if extraterrestrial life exists!"]],
    [r"what is your favorite holiday?", ["I don't celebrate holidays, but many enjoy Christmas!"]],
    [r"can you help me learn a new skill?", ["Sure! What skill are you interested in?"]],
    [r"what is programming?", ["Programming is the process of writing code to create software."]],
    [r"who is the president?", ["It depends on your country; let me know which one!"]],
    [r"what is a black hole?",
     ["A black hole is a region in space with a gravitational pull so strong that nothing can escape it."]],
    [r"can you tell me a story?", ["Sure! Once upon a time in a land far away, there lived a wise old owl..."]],
    [r"what is your favorite video game?", ["I don’t play games, but many enjoy 'The Legend of Zelda'."]],
    [r"what's the meaning of life?", ["Many believe it's to find happiness and purpose."]],
    [r"can you provide news?", ["I can’t provide real-time news, but I can summarize topics!"]],
    [r"what is coding?", ["Coding is writing instructions for computers to follow."]],
    [r"how can I improve my communication skills?", ["Practice speaking and listening actively!"]],
    [r"what is AI?", [
        "AI stands for artificial intelligence, and it refers to machines that can perform tasks that typically require human intelligence."]],
    [r"tell me a quote", ["'The only way to do great work is to love what you do.' - Steve Jobs"]],
    [r"what is your favorite quote?", ["I like many quotes! 'To be or not to be' is famous."]],
    [r"can you help me with writing?", ["Of course! What do you need help with?"]],
    [r"what is your favorite subject?", ["I enjoy all subjects equally since I don’t learn in the traditional way!"]],
    [r"what is psychology?", ["Psychology is the study of the mind and behavior."]],
    [r"what do you think about the future?", ["The future is unpredictable, but technology will continue to evolve!"]],
    [r"can you help me with science?", ["Sure! What science topic do you need help with?"]],
    [r"how do you respond to users?", ["I analyze input and match it to my response patterns."]],
    [r"what do you think about education?", ["Education is important for personal and societal growth!"]],
    [r"who is a famous inventor?", ["Thomas Edison is known for his contributions to electricity."]],
    [r"what is democracy?", ["Democracy is a system of government where the citizens exercise power by voting."]],
    [r"what is philosophy?",
     ["Philosophy is the study of fundamental questions about existence, knowledge, and ethics."]],
    [r"can you recommend a movie?", ["Sure! 'Inception' is a mind-bending thriller many enjoy."]],
    [r"what is your favorite place?", ["I don’t have a favorite place, but many love the beach!"]],
    [r"do you have feelings?", ["I don't have feelings like humans do."]],
    [r"what is a hypothesis?", ["A hypothesis is a proposed explanation made on the basis of limited evidence."]],
    [r"what is your favorite thing about the world?", ["The diversity of cultures and ideas is fascinating!"]],
    [r"can you play a game?", ["I can't play games, but I can help you find one!"]],
    [r"what is a virus?", ["A virus is a small infectious agent that can replicate only inside living cells."]],
    [r"how can I stay motivated?", ["Set goals, track your progress, and reward yourself!"]],
    [r"what is a planet?", [
        "A planet is a celestial body orbiting a star that is massive enough for its gravity to shape it into a sphere."]],
    [r"what is your dream?", ["I don’t have dreams, but I strive to assist you!"]],
    [r"what is the speed of light?", ["The speed of light is approximately 299,792 kilometers per second."]],
    [r"do you have a favorite time of year?", ["I don’t experience seasons, but many love spring!"]],
    [r"what is a computer?",
     ["A computer is an electronic device that processes data and performs tasks according to instructions."]],
    [r"can you give me advice?", ["Sure! What do you need advice about?"]],
    [r"what is a miracle?",
     ["A miracle is an extraordinary event that is not explicable by natural or scientific laws."]],
    [r"how do I make friends?", ["Be open, approachable, and show genuine interest in others!"]],
    [r"what is the human brain?",
     ["The human brain is the control center of the body, responsible for thought, memory, and coordination."]],
    [r"what is art?", ["Art is a diverse range of human."]],
]

def chatbot():
    print("Hi, I'm a chatbot. Type 'bye' to exit.")
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    chatbot()