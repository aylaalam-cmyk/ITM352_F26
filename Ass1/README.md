
●      Data Structure Justification: What data structure design was used to store the quiz questions and why is the best for the application? Explain the design quality goals for this? E.g. readability by human, easy to read from a file, etc. Do not simply list the goals. Explain them relative to storing quiz questions.


The data structure design I used to store the quiz questions was that I stored the questions, options, and answers in a seperate .json file to ensure that my code and data is seaprated. How it is used is that is that the Interquiz.py file retrived the data/ information from the questions.json file and uses the info to output the questions, list the answer options and inform the user if they are correct or not. This seperation of information and code causes for less confusion when updating information for the quiz itself and when needing to update or change the code. It prevents errors in usage on both sides and prevents a mix up of data and code. It also improves the organization and readability between the 2 as they are clearly seperated. The json is the best structure for the sapplication design asthe speration of data makes it easyer for people to read, makes it easy to edit questions without touching code, and easily allows the program to retrieve the quiz content.



●      Function Design: Why did you design your non-trivial custom function the way you did, and what specific problem does it solve in the application?


●      Control Flow: A brief explanation of how the application handles invalid user inputs (e.g., preventing inputs outside of "a-d") and why you chose that validation loop structure. Explain the design quality goals for this? E.g. Do not simply list the goals. Explain them relative to storing quiz questions[RK1] .



●      Use of AI: You must also include a statement on how you used AI (Copilot or any other tool) in the creation of this assignment.  Be honest: if we ask you to explain your code and you cannot, that will mean that you relied too heavily on AI.
