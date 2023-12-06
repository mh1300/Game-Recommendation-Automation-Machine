# Rasa Chatbot
## How to Use
1) Open up two terminal instances
2) In both terminals navigate to the './RasaChatbot' folder
3) Create a new virtual environment - example shown using conda(works with pip)
```
conda create --name game_rasa_env python=3.8
```
4) Activate the new environment in both terminals
```
conda activate game_rasa_env
```
5) Install required packages from requirements.txt
```
pip install -r requirements.txt
```
6) If you want to update and retrain the model, run the following command  
(Note: skip this step if you are not trying to retrain the model. A trained  
instance can be found in './models')
```
rasa train
```
7) Start up the actions server in one of the terminals
```
rasa run actions
```
8) In the other terminal, start the chatbot
```
rasa shell
```
9) Start interacting with the Chatbot

## Files and Folders
### Rasa folders and files
- actions - Contains files necessary to run the actions, includes implementation  
of game recommendation model
- data - Contains information about Rasa intents, stories, and rules
- models - Contains the pre-trained Rasa model and any models trained after
- tests - Contains test cases for Rasa built in testing - not modified/used
- config.yml - Contains information about the model specifics
- credentials.yml - File for if you are using other API's with your chatbot
- domain.yml - Contains the list of all possible intents, responses, and actions  
for your chatbot
- endpoints.yml - Contains different endpoints your model can use. The only  
endpoint used in this model is for the actions

### Other folders and files
- gameData - Contains game summary and game summary vector information used  
by the model
- evaluation - Contains the generated/written test cases and the metrics from  
the tests
- requirements.txt - Contains the list of all packages needed in order to run  
the chatbot
