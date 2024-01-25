import numpy as np

def zero_forcing(channel_matrix, received_signal):
    """
    Apply Zero Forcing algorithm to recover the transmitted signal.

    Args:
    - channel_matrix (numpy array): The channel matrix H.
    - received_signal (numpy array): The received signal Y.

    Returns:
    - numpy array: The estimated transmitted signal X.
    """
    # Inverting the channel matrix
    pseudo_inverse = np.linalg.pinv(channel_matrix)
    
    # Recovering the transmitted signal
    estimated_transmitted_signal = np.dot(pseudo_inverse, received_signal)
    
    return estimated_transmitted_signal

def simulate_mimo_system(num_transmit_antennas, num_receive_antennas, noise_level):
    """
    Simulate a MIMO system with Zero Forcing.

    Args:
    - num_transmit_antennas (int): Number of transmitting antennas.
    - num_receive_antennas (int): Number of receiving antennas.
    - noise_level (float): Standard deviation of noise.

    Returns:
    - numpy array: Original transmitted signal.
    - numpy array: Estimated transmitted signal using Zero Forcing.
    """
    # Generating a random channel matrix H
    channel_matrix = np.random.randn(num_receive_antennas, num_transmit_antennas)

    # Generating a random transmitted signal X
    transmitted_signal = np.random.randn(num_transmit_antennas, 1)

    # Simulating the received signal Y = HX + N
    noise = np.random.randn(num_receive_antennas, 1) * noise_level
    received_signal = np.dot(channel_matrix, transmitted_signal) + noise

    # Applying Zero Forcing to estimate the transmitted signal
    estimated_transmitted_signal = zero_forcing(channel_matrix, received_signal)

    return transmitted_signal, estimated_transmitted_signal

# Parameters for the simulation
num_transmit_antennas = 3
num_receive_antennas = 3
noise_level = 0.1

# Simulating the MIMO system
original_signal, estimated_signal = simulate_mimo_system(num_transmit_antennas, num_receive_antennas, noise_level)

print(" original signal ")
print(original_signal)
print(" estimated signal ")
print(estimated_signal)
