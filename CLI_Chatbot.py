import google.generativeai as genai#to use Gemini API   
API_KEY ="YOUR_API_KEY_HERE"#replace with your actual API key
genai.configure(api_key=API_KEY)# Configure the API key
model=genai.GenerativeModel("gemini-2.0-flash")# Initialize the Gemini model
chat=model.start_chat()# Start a chat session
print("Chat with Gemini! Type 'exit' to quit.")# Instructions for the user
while True:# Chat loop
    user_input = input("You: ")# Get user input
    if user_input.lower() == 'exit':# Exit condition
        print("Exiting chat. Goodbye!")
        break
    response = chat.send_message(user_input)# Send user input to Gemini
    print("Gemini: " + response.text)# Print Gemini's response