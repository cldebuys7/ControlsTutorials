"""Program 2-1 from Modern Control Engineering - Ogata, 5th Edition (p. 21)

This code demonstrates the ability of the Python Control Systems Library (control) to combine transfer functions in
series, in parallel, and in a feedback or closed-loop configuration. This is a Matlab example from Ogata's book,
converted into Python. Note that the Python methods do not seem to support the entry of numerator and denominator
coefficients as in Matlab, so the transfer functions G(s) and H(s) are created first.
"""

import control as ct

# Create two transfer functions, G(s) and H(s)
numerator1 = [10]
denominator1 = [1, 2, 10]
G_s = ct.tf(numerator1, denominator1)
numerator2 = [5]
denominator2 = [1, 5]
H_s = ct.tf(numerator2, denominator2)

# Combine the blocks (transfer functions) in series
#
# Input --> [ G(s) ] --> [ H(s) ] --> Output
#
seriesSystem = ct.series(G_s, H_s)
print('Series System')
print(seriesSystem)

# Combine the blocks in parallel
#          ---->[ G(s) ]-----
#          |                |
# Input ---|                +----> Output
#          |                |
#          ---->[ H(s) ]-----
#
parallelSystem = ct.parallel(G_s, H_s)
print('Parallel System')
print(parallelSystem)

# Combine the blocks considering G(s) to be the feedforward and H(s) to be the feedback transfer functions, respectively
#
# Input ---> + -----[ G(s) ]--------> Output
#            |                   |
#            |                   |
#            ---<---[ H(s) ]<-----
#
closedLoopSystem = ct.feedback(G_s, H_s)
print('Closed-Loop System')
print(closedLoopSystem)
