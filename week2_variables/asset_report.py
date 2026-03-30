# Asset Report Generator
print("=================================")
print(f"Cyber Defense - Asset Report")
print("=================================")
# Week 2 – Working with Variables
# Author: <Mark Jordan>
analyst_name = "Mark Jordan"
department_name = "IT Security"
system_hostname = "SecurityServer01"
criticality = "high"

print("Analyst:", analyst_name)
print("System:", department_name)
print("System Hostname:", system_hostname)
print("Criticality Level:", criticality)

risk_score = input("Enter a risk score (1-10): ")
risk_score = int(risk_score)

if risk_score >= 8:
    print("[*] High-Risk Asset – prioritize review.")
elif risk_score >= 5:
    print("[!] Medium-Risk Asset – monitor closely.")
else:
    print("[+] Low-Risk Asset – standard monitoring.")
from datetime import datetime
report_date = datetime.now().strftime("%Y-%m-%d %H:%M")
print("Report Generated:", report_date)