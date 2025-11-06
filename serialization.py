import json


input_file = "C:\Work\OCL_Eclipse\greenProd\model\Constraint_Validation_Constraint_Violated.txt"
#input_file = "C:\Work\OCL_Eclipse\greenProd\model\Constraint_Validation_Successful.txt"
output_file = "C:\Work\OCL_Eclipse\greenProd\model\Constraint_Validation_Constraint_Violated.json"



violations = []


current = {}

with open(input_file, "r", encoding="utf-8") as f:
    for line in f:
        if "Total number of evaluated constraints" in line:
            number_str1 = line.split(":")[1].strip()
        if "Number of Success" in line:
            number_str2 = line.split(":")[1].strip()
            number_str3= int(number_str1)-int(number_str2)
            number_str3=str(number_str3)
            break
        
with open(input_file, "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if line.startswith("Invariant:"):
            current["ConstraintName"] = line.split("Invariant:")[1].strip()
            current["Result"]="Constraint Violated"

        elif line.startswith("-------------"):
                if current:
                    violations.append(current)
                    current = {}
if violations:            
    output_data = {
        "ValidationSummary": {
            "Number of evaluated constraints": number_str1,
            "Number of successful constraints": number_str2,
            "Number of violated constraints": number_str3,
            "Violations": violations
        }}
else:
    output_data = {
        "ValidationSummary": {
            "Number of evaluated constraints": number_str1,
            "Number of successful constraints": number_str2,
            "Number of violated constraints": number_str3
        }}


with open(output_file, "w", encoding="utf-8") as f:
    json.dump(output_data, f, indent=4)

print(f"✅ JSON file created: {output_file}")
