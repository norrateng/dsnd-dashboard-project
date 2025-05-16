import pickle
from pathlib import Path

# Using the Path object, create a `project_root` variable
# set to the absolute path for the root of this project directory
#### YOUR CODE HERE
ROOT_DIR = Path(__file__).resolve().parent.parent  
project_root = ROOT_DIR
# print(project_root)
 
# Using the `project_root` variable
# create a `model_path` variable
# that points to the file `model.pkl`
# inside the assets directory
#### YOUR CODE HERE
model_path = project_root/ 'assets/model.pkl'
# print(model_path)

def load_model():

    with model_path.open('rb') as file:
        model = pickle.load(file)

    return model