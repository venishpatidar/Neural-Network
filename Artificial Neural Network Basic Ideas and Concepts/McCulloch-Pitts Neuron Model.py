import numpy as np

# Creating neuron function 
def neuron(inputs,weights,threshold):
    # calculating weights 
    z = (inputs*weights)
    z = np.sum(z)

    output = 0
    # Condition for firing the neuron if summation is over threshold
    if z>=threshold:
        output=1
    else:
        output=0
    return output

# intializing inputs, weights and threshold
inputs = np.array([1,2,3])
weights = np.array([-1,-5,6])
threshold = 10

# firing neuron
print(neuron(inputs,weights,threshold))