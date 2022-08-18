import tensorflow as tf
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()
import keras
import numpy as np
from tensorflow.keras.utils import to_categorical

from textattack.models.wrappers import ModelWrapper
from textattack.datasets import HuggingFaceDataset
from textattack.attack_recipes import PWWSRen2019
import numpy as np
from tensorflow.keras.utils import to_categorical
from pyexpat import model
from textattack import AttackArgs
from textattack.datasets import Dataset
from textattack import Attacker
import textattack
from keras.models import load_model
NUM_WORDS = 1000
vocabulary = tf.keras.datasets.imdb.get_word_index(
    path='imdb_word_index.json'
)
class CustomKerasModelWrapper(ModelWrapper):
    def __init__(self, model):
        self.model = model

    def __call__(self, text_input_list):
      
      x_transform = []
      for i, review in enumerate(text_input_list):
        tokens = [x.strip(",") for x in review.split()]
        BoW_array = np.zeros((NUM_WORDS,))
        for word in tokens:
          if word in vocabulary:
            if vocabulary[word] < len(BoW_array):
              BoW_array[vocabulary[word]] += 1            
        x_transform.append(BoW_array)
      x_transform = np.array(x_transform)
      prediction = self.model.predict(x_transform)
      return prediction
def get_text(text): 
  model = load_model("./data/model_file_path.h5")
  model_wrapper = CustomKerasModelWrapper(model)
  dataset = HuggingFaceDataset("rotten_tomatoes", None, "test", shuffle=True)

  attack = PWWSRen2019.build(model_wrapper)

  attack_args = AttackArgs(num_examples=10, checkpoint_dir="checkpoints")

  attacker = Attacker(attack, dataset, attack_args)
  example = textattack.shared.attacked_text.AttackedText(text)
  output = attack.goal_function.get_output(example)
  result = attack.attack(example, output)
  # print(result)
  origin_class = str(result).split('\n')[0].split('-->')[0]
  attack_class = str(result).split('\n')[0].split('-->')[1]
  origin_sentence = str(result).split('\n')[2]
  attack_sentence = str(result).split('\n')[4]
  return origin_class,attack_class ,origin_sentence,attack_sentence 