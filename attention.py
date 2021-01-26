import tensorflow as tf
from tensorflow import keras

import argparse
import numpy as np
from tensorflow.python.keras.datasets import imdb
from tensorflow.python.keras.preprocessing import sequence
from zoo.orca import init_orca_context, stop_orca_context
# from zoo.orca.learn.tf2.estimator import Estimator

parser = argparse.ArgumentParser()
parser.add_argument('--cluster_mode', type=str, default="local",
                    help='The mode for the Spark cluster. local or yarn.')
args = parser.parse_args()
cluster_mode = args.cluster_mode
if cluster_mode == "local":
    init_orca_context(cluster_mode="local", cores=4, memory="3g")
elif cluster_mode == "yarn":
    init_orca_context(cluster_mode="yarn-client", num_nodes=2, cores=2, driver_memory="3g", \
                      conf={"spark.executor.extraJavaOptions": "-Xss512m",
                            "spark.driver.extraJavaOptions": "-Xss512m"})

max_features = 20000
max_len = 200

print('Loading data...')
(x_train, y_train), (x_test, y_test) = imdb.load_data(num_words=max_features)
print(len(x_train), 'train sequences')
print(len(x_test), 'test sequences')

print('Pad sequences (samples x time)')
x_train = sequence.pad_sequences(x_train, maxlen=max_len)
x_test = sequence.pad_sequences(x_test, maxlen=max_len)
print('x_train shape:', x_train.shape)
print('x_test shape:', x_test.shape)

train_pos = np.zeros((len(x_train), max_len), dtype=np.int32)
val_pos = np.zeros((len(x_test), max_len), dtype=np.int32)
for i in range(0, len(x_train)):
    train_pos[i, :] = np.arange(max_len)
    val_pos[i, :] = np.arange(max_len)
