# Author Name-Prayansh Mishra
import os
import tensorflow as tf #importing statements 
string = tf.Variable("this is a string", tf.string) #tensor var of string type
number = tf.Variable(324, tf.int16)#tensor var of int type
floating = tf.Variable(3.567, tf.float64)#var of float type
rank1_tensor = tf.Variable(["Test"], tf.string) 
rank2_tensor = tf.Variable([["test", "ok"], ["test", "yes"]], tf.string)
tf.rank(rank2_tensor)
rank2_tensor.shape
tensor1 = tf.ones([1,2,3])  
tensor2 = tf.reshape(tensor1, [2,3,1])
tensor3 = tf.reshape(tensor2, [3, -1])
print(tensor1)
print(tensor2)
print(tensor3)
if tf.Variable(12,tf.int16)==15:
    print("they both are fucking equal")
else:
    print("they are not equal")    