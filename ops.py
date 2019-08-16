# collection of all operations that are needed

import numpy as np
import tensorflow as tf

#help function for weights init
def init_weights(shape):
        return tf.Variable(tf.random_normal(shape=shape, stddev=0.02))
#def init