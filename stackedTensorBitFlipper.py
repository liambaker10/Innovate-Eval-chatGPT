import tensorflow as tf
import random

def flip_bit_stacked_tensor(stacked_tensor):
    num_subtensors = stacked_tensor.shape[0]
    subtensor_index = random.randint(0, num_subtensors - 1)
    subtensor = stacked_tensor[subtensor_index]

    bit_position = random.randint(0, tf.size(subtensor) - 1)
    element_index = random.randint(0, subtensor.shape[0] - 1)

    flip_value = tf.bitwise.left_shift(tf.constant(1, dtype=subtensor.dtype), bit_position)
    element_to_flip = subtensor[element_index]
    flipped_element = tf.bitwise.bitwise_xor(element_to_flip, flip_value)

    flipped_subtensor = tf.tensor_scatter_nd_update(subtensor, [[element_index]], [flipped_element])
    flipped_tensor = tf.tensor_scatter_nd_update(stacked_tensor, [[subtensor_index]], [flipped_subtensor])

    return flipped_tensor

# Example usage
tensor1 = tf.constant([5, 3, 2, 100], dtype=tf.uint8)
tensor2 = tf.constant([10, 20, 30, 40], dtype=tf.uint8)
tensor3 = tf.constant([1, 2, 3, 4], dtype=tf.uint8)
stacked_tensor = tf.stack([tensor1, tensor2, tensor3])

print("Original Stacked Tensor:")
print(stacked_tensor)

flipped_tensor = flip_bit_stacked_tensor(stacked_tensor)
print("Flipped Stacked Tensor:")
print(flipped_tensor)


