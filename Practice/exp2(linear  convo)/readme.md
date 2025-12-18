near convolution is a mathematical operation used to find the output of a Linear Time-Invariant (LTI) system for a given input signal and its impulse response.

It works by:

Time shifting one signal

Overlapping both signals

Multiplying corresponding samples

Summing the products

Linear convolution directly follows the convolution sum equation.

📐 MATHEMATICAL EXPRESSION (WRITE LIKE THIS)

y[n] = x[n] * h[n]
y[n] = sum over k of x[k] · h[n − k]

Where:
x[n] → input signal
h[n] → impulse response
y[n] → output signal

📏 LENGTH OF LINEAR CONVOLUTION (VERY IMPORTANT)

If:
Length of x[n] = N1
Length of h[n] = N2

Then:
Length of y[n] = N1 + N2 − 1

⚠️ Very common viva question

🔹 METHOD 1: Linear Convolution Using Zero Padding
Concept

Both signals are padded with zeros so that their lengths become equal before convolution.

Zero padding prevents loss of samples and helps obtain correct linear convolution.

Algorithm (WRITE THIS IN EXAM)

Read input sequences x[n] and h[n]

Find lengths N1 and N2

Pad both sequences with zeros

Perform convolution

Display the result