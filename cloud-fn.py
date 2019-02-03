import pandas as pd
import io
import requests
import math
import random

# Reads CSV from the web and puts it in a Panda's DataFrame
words = {}
url = "https://query.data.world/s/tbdddavnbxiqhlmi5c3dhzrtrbh4ur"
s = requests.get(url).content
df = pd.read_csv(io.StringIO(s.decode('utf-8')))

# Reading the CSV of words and their examples and adding them to a dictionary
for index, row in df.iterrows():
    word = row['Word'].lower()
    words[word] = []

    examples = [
      row["Examples/0"],
      row["Examples/1"],
      row["Examples/2"],
      row["Examples/3"],
      row["Examples/4"],
      row["Examples/5"],
      row["Examples/6"],
      row["Examples/7"],
      row["Examples/8"],
      row["Examples/9"]
    ]

    for phrase in examples:
        if (not isinstance(phrase, float)):
            words[word].append(phrase)

# Returns a random example of a word
def random_sentence(sentence_list):
    return random.choice(sentence_list)

def hello_http(request):
    """HTTP Cloud Function.
    Args:
        request (flask.Request): The request object.
        <http://flask.pocoo.org/docs/1.0/api/#flask.Request>
    Returns:
        The response text, or any set of values that can be turned into a
        Response object using `make_response`
        <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>.
    """
    request_json = request.get_json(silent=True)
    request_args = request.args

    query_param_name = 'word'

    if request_json and query_param_name in request_json:
        name = request_json[query_param_name]
    elif request_args and query_param_name in request_args:
        name = request_args[query_param_name]
    else:
        return '{"sentence":"Error: Please enter a word."}'
    return '{"sentence":"' + random_sentence(words[name]) + '"}'
