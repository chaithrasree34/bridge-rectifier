# bridge-rectifier
import math

# Python program for Single Phase Bridge Rectifier

Vm = float(input("Enter peak AC voltage Vm (V): "))

# Average DC output voltage for bridge rectifier
Vdc = (2 * Vm) / math.pi

print("\nBridge Rectifier")
print("Peak AC voltage =", Vm, "V")
print("Average DC output voltage =", round(Vdc, 2), "V")

Example

Input:

Enter peak AC voltage Vm (V): 230


Output:

Bridge Rectifier
Peak AC voltage = 230.0 V
Average DC output voltage = 146.42 V

Formula

For an ideal single-phase bridge rectifier:

𝑉
𝐷
𝐶
=
2
𝑉
𝑚
𝜋

where:

Vm = peak value of AC input voltage

VDC = average DC output voltage

The bridge rectifier uses four diodes to convert both half-cycles of AC into pulsating DC.
