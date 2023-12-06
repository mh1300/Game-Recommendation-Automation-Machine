# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
#
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
#
#

# Imports for the action
import textwrap

import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('distilbert-base-nli-mean-tokens')
gameVectors = np.load('./gameData/GameVectors.npy')
gamesSummaries = pd.read_csv('./gameData/GameSummaries.csv')



# Initialize necessary models
class ActionRecommend(Action):

    def name(self) -> Text:
        return "action_recommend"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        userInput = tracker.latest_message['text']

        userInputData = [model.encode(userInput, show_progress_bar=False)]
        userVector = np.array(userInputData)

        # Add the vector the the existing list of game vectors
        combinedVectors = np.concatenate((gameVectors, userVector))

        # Get the cosine similarity for the full list of vectors
        cosineSimilarityData = pd.DataFrame(cosine_similarity(combinedVectors))

            # Retrieve the index of the best game
        topIndex = cosineSimilarityData.loc[len(cosineSimilarityData.index)-1].sort_values(ascending=False).index.tolist()[1]

        # Get the game information from the summarys dataframe
        gameName = gamesSummaries['name'].loc[topIndex]
        gameSummary = gamesSummaries['summary'].loc[topIndex]
        gameSummary = textwrap.fill(gameSummary, 64)

        ret = '------------------------------------------------------------------'
        ret += '\nGame Recomendation -- {}\n\n'.format(gameName)
        ret += '\nGame Summary:\n' + gameSummary + '\n'
        ret += '------------------------------------------------------------------'
        ret += '\n'

        dispatcher.utter_message(text=ret)


        return []
