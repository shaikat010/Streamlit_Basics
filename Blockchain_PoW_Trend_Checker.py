import time
import streamlit as st
import numpy as np
import hashlib


# st.title("Blockchain Proof of Work Checker")

x_axis = [1,2,3,4]
y_axis = []


def _to_digest(Data, new_proof, previous_proof) -> bytes:
    to_digest = str(new_proof ** 2 - previous_proof ** 2 + Data)
    return to_digest.encode()


def Proof_of_Work_01(Data):
    start_time = time.time()
    print(start_time)

    nonce = 1
    to_digest = f'({Data} + {nonce})'.encode('utf-8')

    hash_value = hashlib.sha256(to_digest).hexdigest()
    print(hash_value)

    while (hash_value[:1] != "0"):
        nonce = nonce + 1
        to_digest = f'({Data} + {nonce})'.encode('utf-8')
        hash_value = hashlib.sha256(to_digest).hexdigest()
        print(hash_value)

    end_time = time.time()
    print(end_time)
    duration = end_time - start_time
    y_axis.append(duration)
    return f'This is the accepted hash \n  {hash_value}'



def Proof_of_Work_02(Data):
    start_time = time.time()
    print(start_time)

    nonce = 1
    to_digest = f'({Data} + {nonce})'.encode('utf-8')

    hash_value = hashlib.sha256(to_digest).hexdigest()
    print(hash_value)

    while (hash_value[:2] != "00"):
        nonce = nonce + 1
        to_digest = f'({Data} + {nonce})'.encode('utf-8')
        hash_value = hashlib.sha256(to_digest).hexdigest()
        print(hash_value)

    end_time = time.time()
    print(end_time)
    duration = end_time - start_time
    y_axis.append(duration)

    return f'This is the accepted hash \n {hash_value}'




def Proof_of_Work_03(Data):
    start_time = time.time()
    print(start_time)

    nonce = 1
    to_digest = f'({Data} + {nonce})'.encode('utf-8')

    hash_value = hashlib.sha256(to_digest).hexdigest()
    print(hash_value)

    while (hash_value[:3] != "000"):
        nonce = nonce + 1
        to_digest = f'({Data} + {nonce})'.encode('utf-8')
        hash_value = hashlib.sha256(to_digest).hexdigest()
        print(hash_value)

    end_time = time.time()
    print(end_time)
    duration = end_time - start_time
    y_axis.append(duration)
    return f'This is the accepted hash \n {hash_value}'


def Proof_of_Work_04(Data):
    start_time = time.time()
    print(start_time)

    nonce = 1
    to_digest = f'({Data} + {nonce})'.encode('utf-8')

    hash_value = hashlib.sha256(to_digest).hexdigest()
    print(hash_value)

    while (hash_value[:4] != "0000"):
        nonce = nonce + 1
        to_digest = f'({Data} + {nonce})'.encode('utf-8')
        hash_value = hashlib.sha256(to_digest).hexdigest()
        print(hash_value)

    end_time = time.time()
    print(end_time)
    duration = end_time - start_time
    y_axis.append(duration)
    return f'This is the accepted hash \n {hash_value}'



# 'Starting a long computation...'
# # Add a placeholder
# latest_iteration = st.empty()
# bar = st.progress(0)
# for i in range(100):
# #Update the progress bar with each iteration.
#     latest_iteration.text(f'Iteration {i+1}')
#     bar.progress(i + 1)
#     time.sleep(0.1)
# '...and now we\'re done!'

print(Proof_of_Work_01("Sample Data 01"))
print(Proof_of_Work_02("Sample Data 01"))
print(Proof_of_Work_03("Sample Data 01"))
print(Proof_of_Work_04("Sample Data 01"))

print( f" x-axis: {x_axis}")
print( f" y-axis: {y_axis}")

# importing the required module
import matplotlib.pyplot as plt


# plotting the points
plt.plot(x_axis, y_axis)

# naming the x axis
plt.xlabel('x - axis')
# naming the y axis
plt.ylabel('y - axis')

# giving a title to my graph
plt.title('Proof of work trend checker')

# function to show the plot
plt.show()


