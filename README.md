# Customer-service-bot
this is only a basic bot for Customer service

This code defines a responses dictionary that maps certain user inputs (like "hi", "bye", and "thanks") to corresponding chatbot responses. The chatbot_response() function takes user input, tokenizes it into individual words, and checks if any of those words match the predefined responses. If a match is found, the corresponding response is returned. If no match is found, a default response is returned.

In the main loop, the chatbot prompts the user for input and calls chatbot_response() to get a response. It then prints the response to the console. The loop continues until the user inputs "bye".
