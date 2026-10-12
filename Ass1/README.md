
●      Data Structure Justification: What data structure design was used to store the quiz questions and why is the best for the application? Explain the design quality goals for this? E.g. readability by human, easy to read from a file, etc. Do not simply list the goals. Explain them relative to storing quiz questions.


The data structure design I used to store the quiz questions was that I stored the questions, options, and answers in a seperate .json file to ensure that my code and data is seaprated. How it is used is that is that the Interquiz.py file retrived the data/ information from the questions.json file and uses the info to output the questions, list the answer options and inform the user if they are correct or not. This seperation of information and code causes for less confusion when updating information for the quiz itself and when needing to update or change the code. It prevents errors in usage on both sides and prevents a mix up of data and code. It also improves the organization and readability between the 2 as they are clearly seperated. The json is the best structure for the sapplication design asthe speration of data makes it easyer for people to read, makes it easy to edit questions without touching code, and easily allows the program to retrieve the quiz content.



●      Function Design: Why did you design your non-trivial custom function the way you did, and what specific problem does it solve in the application?

I didn't really have a specific method to designing my custom function. What I did was first look at what my task was asking for, for the first on it was allowing for multiple correct answers. I then looked at my code to find where it listed the correct answers, which on the raw would be correct_answer = alternatives[0], then to make it out put multiple changed it to: correct_answer = (alternatives[0], alternatives[1]) which makes the first and second listed "answers" the correct ones making multiple correct answers for each question.

For the seccond task I had which was Add explanations for why the correct answer is the correct answer I started by look for the line that prints out the response correct when the user answered a correct answer which was: print(f"Correct!"). I then sort of copied it making a sub line and making a new variable called correct response: correct_response = question_data["correct_response"]  print(f"{correct_response}"). I then used Copilot to figure out how to add to the questions.json file for the Interquiz.py to pull the new variable in response to a correct answer.


●      Control Flow: A brief explanation of how the application handles invalid user inputs (e.g., preventing inputs outside of "a-d") and why you chose that validation loop structure. Explain the design quality goals for this? E.g. Do not simply list the goals. Explain them relative to storing quiz questions[RK1] .



●      Use of AI: You must also include a statement on how you used AI (Copilot or any other tool) in the creation of this assignment.  Be honest: if we ask you to explain your code and you cannot, that will mean that you relied too heavily on AI.
