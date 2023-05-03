import openai_secret_manager
import openai
import time

# Load the API key from your secrets
secrets = openai_secret_manager.get_secret("openai")

# Authenticate with the OpenAI API
openai.api_key = secrets["api_key"]

# Define the Sec function
def Sec(query):
    # Set up the prompt
    prompt = "Sec: " + query + "\nUser:"

    # Generate a response from the OpenAI API
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    # Return the response text
    return response.choices[0].text.strip()

# Set up a loop that waits for user input
while True:
    # Get input from the user
    user_input = input("User:")

    # Check if the user wants to activate Sec mode
    if user_input.lower() == "sec":
        print("Sec mode activated.")
        
        # Loop until the user deactivates Sec mode
        while True:
            # Get input from the user
            user_input = input("Sec:")
            
            # Check if the user wants to deactivate Sec mode
            if user_input.lower() == "sec no!":
                print("Sec mode deactivated.")
                break
            
            # Call the Sec function with the user's input
            response = Sec(user_input)
            print(response)
    else:
        # Call the Sec function with the user's input
        response = Sec(user_input)
        print(response)

    # Add a delay to prevent rate limiting
    time.sleep(1)
