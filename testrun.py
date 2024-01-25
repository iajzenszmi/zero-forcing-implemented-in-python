ian@ian-Latitude-E7440:~$ python3 zeroforcing.py
 original signal 
[[2.15109068]
 [0.3074536 ]
 [0.70122262]]
 estimated signal 
[[1.82355481]
 [0.4099515 ]
 [0.68453414]]
ian@ian-Latitude-E7440:~$ cat zeroforcing.py
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
ian@ian-Latitude-E7440:~$ sloccount zeroforcing.py
Have a non-directory at the top, so creating directory top_dir
Adding /home/ian/zeroforcing.py to top_dir
Categorizing files.
Finding a working MD5 command....
Found a working MD5 command.
Computing results.


SLOC	Directory	SLOC-by-Language (Sorted)
20      top_dir         python=20


Totals grouped by language (dominant language first):
python:          20 (100.00%)




Total Physical Source Lines of Code (SLOC)                = 20
Development Effort Estimate, Person-Years (Person-Months) = 0.00 (0.04)
 (Basic COCOMO model, Person-Months = 2.4 * (KSLOC**1.05))
Schedule Estimate, Years (Months)                         = 0.06 (0.73)
 (Basic COCOMO model, Months = 2.5 * (person-months**0.38))
Estimated Average Number of Developers (Effort/Schedule)  = 0.05
Total Estimated Cost to Develop                           = $ 444
 (average salary = $56,286/year, overhead = 2.40).
SLOCCount, Copyright (C) 2001-2004 David A. Wheeler
SLOCCount is Open Source Software/Free Software, licensed under the GNU GPL.
SLOCCount comes with ABSOLUTELY NO WARRANTY, and you are welcome to
redistribute it under certain conditions as specified by the GNU GPL license;
see the documentation for details.
Please credit this data as "generated using David A. Wheeler's 'SLOCCount'."
ian@ian-Latitude-E7440:~$ 
