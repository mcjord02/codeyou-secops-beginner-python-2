# 🧩 **Week 2 – Variables, Data Types, and Input Handling**

### **Assignment Title:** *Building an Asset Tagger Script*

---

## 🧠 **Learning Objectives**

By the end of this assignment, you will:

* Understand and use basic Python data types (`str`, `int`, `float`, `bool`, `list`)
* Create and modify variables to store information
* Accept user input and convert between data types
* Begin to format and present data like a professional report
* Build a small “Asset Tagger” script that organizes system details

---

## ⚙️ **Setup**

Before starting:

* Make sure Python 3.x is installed
* Create a new folder named `week2_variables`
* Open a new file called `asset_tagger.py`

*(You’ll continue developing your skills in the same environment you used last week.)*

---

## 🧩 **Walkthrough Activity**

### **Part 1 – Understanding Variables**

In cybersecurity scripts, we store and manipulate information constantly — usernames, IP addresses, threat levels, etc.
Start with some simple variable practice:

```python
# Week 2 – Working with Variables
# Author: <Your Name>

analyst_name = "Jordan"
system_name = "workstation-01"
criticality = "high"

print("Analyst:", analyst_name)
print("System:", system_name)
print("Criticality Level:", criticality)
```

✅ **Try changing the values** and re-running the script.

💬 *Reflection:* How could these variables represent real data in an asset inventory?

---

### **Part 2 – Getting User Input**

Now let’s make it interactive so an analyst can enter asset details manually.

```python
analyst_name = input("Enter your name: ")
system_name = input("Enter system hostname: ")
criticality = input("Enter system criticality (low, medium, high): ")

print("\n--- Asset Information ---")
print("Analyst:", analyst_name)
print("System:", system_name)
print("Criticality:", criticality)
```

✅ Run it and enter a few different values.

Notice that all inputs come in as **strings** — we’ll deal with type conversion next.

---

### **Part 3 – Working with Numbers and Types**

Let’s imagine we want to assign a *risk score* (1–10) to a system.

```python
risk_score = input("Enter a risk score (1-10): ")
print("Risk score entered:", risk_score)
print("Data type of risk_score:", type(risk_score))
```

✅ Output shows `<class 'str'>`, meaning it’s text. Convert it to a number:

```python
risk_score = int(risk_score)
print("Numeric risk score:", risk_score)
print("Data type now:", type(risk_score))
```

💡 *Why does this matter?*
Later we’ll compare and calculate values (e.g., raise alerts if `risk_score > 7`).

---

### **Part 4 – Simple Logic Check**

Add a small decision-making section:

```python
if risk_score >= 8:
    print("[*] High-Risk Asset – prioritize review.")
elif risk_score >= 5:
    print("[!] Medium-Risk Asset – monitor closely.")
else:
    print("[+] Low-Risk Asset – standard monitoring.")
```

You’ve just built your first **conditional** — the backbone of automation logic.

---

## 🔍 **Challenge: “Asset Tagger Report”**

Create a new script `asset_report.py` that:

1. Prompts the analyst for:

   * Name
   * Department
   * System hostname
   * Criticality (low/medium/high)
   * Risk score (1–10)
2. Converts the risk score to an integer.
3. Prints a formatted summary like:

   ```
   ===============================
     Cyber Defense - Asset Report
   ===============================
   Analyst: Jordan
   Department: Threat Analysis
   Hostname: workstation-01
   Criticality: high
   Risk Score: 9
   Risk Assessment: High-Risk Asset – prioritize review.
   Report Generated: 2025-10-30 15:42
   ```

💡 *Hint:* Use `from datetime import datetime` to add a timestamp.

---

## 🧩 **Optional Extension**

* Store multiple assets in a list:

  ```python
  assets = []
  assets.append({"hostname": system_name, "risk": risk_score})
  print(assets)
  ```
* Try adding color to the output using ANSI escape codes (research `\033[31m` for red text).

---

## ✅ **Submission**

Submit your `asset_report.py` file in your classroom repo or LMS.
The script must:

* Run without errors
* Accept all required inputs
* Print a clearly formatted report

---

## 🧠 **Reflection Question**

> Why might SOC analysts need to store or track system criticality and risk scores in automated scripts?

---

