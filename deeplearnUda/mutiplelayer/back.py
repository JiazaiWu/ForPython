import numpy as np


def sigmoid(x):
    """
    Calculate sigmoid
    """
    return 1 / (1 + np.exp(-x))


x = np.array([0.5, 0.1, -0.2])
target = 0.6
learnrate = 0.5

weights_input_hidden = np.array([[0.5, -0.6],
                                 [0.1, -0.2],
                                 [0.1, 0.7]])

weights_hidden_output = np.array([0.1, -0.3])

## Forward pass
hidden_layer_input = np.dot(x, weights_input_hidden)
hidden_layer_output = sigmoid(hidden_layer_input)

output_layer_in = np.dot(hidden_layer_output, weights_hidden_output)
output = sigmoid(output_layer_in)

## Backwards pass
## TODO: Calculate output error
error = target - output

# TODO: Calculate error term for output layer
output_error_term = error * output * (1 - output)

# TODO: Calculate error term for hidden layer
# note for output layer:
# error = real_input - we_get_input
# error_term = error*f'(h) -- in this case, f=sigmoid, f'=sigmoid*(1-sigmoid), so....
# del_w = learnrate * error_term * input
#
# then seperate the error_term by weight and to hidden layers, for example
# if output_error_term is 1, weight is [0.1, 0.3]
# error_hidden_layer is 1 x [0.1, 0.3]
hidden_error_term = output_error_term *weights_hidden_output * \
                    hidden_layer_output * (1 - hidden_layer_output)

# TODO: Calculate change in weights for hidden layer to output layer, note hidden_layer_output is the input of output_layer
delta_w_h_o = learnrate * output_error_term * hidden_layer_output

# TODO: Calculate change in weights for input layer to hidden layer
# hidden_error_term shape 1x2
# x[:,None] is x.T if x is matrix, so shape 3x1
# delta_w_i_h shape 3x2
delta_w_i_h = learnrate * hidden_error_term * x[:, None]

print('Change in weights for hidden layer to output layer:')
print(delta_w_h_o)
print('Change in weights for input layer to hidden layer:')
print(delta_w_i_h)