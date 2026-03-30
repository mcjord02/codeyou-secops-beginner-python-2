# Week 2 – Working with Variables
# Author: <Mark Jordan>

analyst_name = input("Enter your name: ")
system_name = input("Enter system hostname: ")
criticality = input("Enter system criticality (low, medium, high): ")

print("\n--- Asset Information ---")
print("Analyst:", analyst_name)
print("System:", system_name)
print("Criticality:", criticality)

risk_score = input("Enter a risk score (1-10): ")
risk_score = int(risk_score)
print("Numeric risk score:", risk_score)
print("Data type now:", type(risk_score))
# Logic statement to categorize risk level based on the risk score
if risk_score >= 8:
    print("[*] High-Risk Asset – prioritize review.")
elif risk_score >= 5:
    print("[!] Medium-Risk Asset – monitor closely.")
else:
    print("[+] Low-Risk Asset – standard monitoring.")