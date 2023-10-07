#!/usr/bin/env python
# coding: utf-8

# In[4]:


##question1
def main():
        str_15 = ("", "", "Fizz", "", "Buzz", "Fizz", "", "", "Fizz", "Buzz", "", "Fizz", "", "", "FizzBuzz")
        str_index = 0

        for i in range(1, 101):
                if str_15[str_index] == "":
                        print(i)
                else:
                        print(str_15[str_index])
                str_index += 1
                if str_index == 15:
                        str_index = 0

main()


# In[5]:


##question2
def convert_to_float(input_str: str, default: float) -> float:
    try:
        return float(input_str)
    except ValueError:
        return default

# Example usage:
input_str = "3.14"
default_value = 0.0
result = convert_to_float(input_str, default_value)
print(result)  # Output: 3.14

input_str = "not_a_float"
result = convert_to_float(input_str, default_value)
print(result)  # Output: 0.0 (default value)


# In[1]:


##question3
def get_antihtn_meds(data_obj: dict) -> list:
    medications = data_obj.get("medications", [])
    antihtn_meds = []
    
    for medication in medications:
        drug_groups = medication.get("drugGroup", [])
        if "antihtn" in drug_groups:
            antihtn_meds.append(medication)
    
    return antihtn_meds

# Sample data
sample_data = {
    "etlUpdated": "2012-12-21T23:58:00",
    "id": "123",
    "medications": [
        {
            "ndc9": "39017-0147",
            "brandName": "AMLODIPINE BESYLATE",
            "dosageStrength": "5",
            "dosageUnit": "mg",
            "doseForm": "tablet",
            "drugGroup": [
                "ccb",
                "antihtn"
            ],
            "route": "oral",
            "quantity": "90",
            "daysSupply": "90",
            "fills": [
                {
                    "fillDate": "2012-02-18",
                    "daysSupply": "90",
                    "quantity": "90"
                },
                {
                    "fillDate": "2012-05-16",
                    "daysSupply": "90",
                    "quantity": "90"
                }
            ],
            "display": "AMLODIPINE BESYLATE 5 MG",
            "unitsPerDay": "1",
            "dosePerDay": "5"
        },
        {
            "ndc9": "60505-2671",
            "brandName": "ATORVASTATIN CALCIUM",
            "genericName": "ATORVASTATIN CALCIUM",
            "dosageStrength": "80",
            "dosageUnit": "mg",
            "doseForm": "tablet, film coated",
            "drugGroup": [
                "statin",
                "azoleddi",
                "antilipid",
                "cms_statin",
                "cms_spc_statin"
            ],
            "route": "oral",
            "quantity": "90",
            "daysSupply": "90",
            "fills": [
                {
                    "fillDate": "2012-04-10",
                    "daysSupply": "90",
                    "quantity": "90"
                },
                {
                    "fillDate": "2012-07-09",
                    "daysSupply": "90",
                    "quantity": "90"
                }
            ],
            "unitsPerDay": "1",
            "dosePerDay": "80"
        },
        {
            "ndc9": "68382-0136",
            "brandName": "LOSARTAN POTASSIUM",
            "genericName": "LOSARTAN POTASSIUM",
            "dosageStrength": "50",
            "dosageUnit": "mg",
            "doseForm": "tablet, film coated",
            "drugGroup": [
                "arb",
                "antihtn",
                "cms_rasa"
            ],
            "route": "oral",
            "quantity": "90",
            "daysSupply": "90",
            "fills": [
                {
                    "fillDate": "2012-02-25",
                    "daysSupply": "90",
                    "quantity": "90"
                },
                {
                    "fillDate": "2012-05-25",
                    "daysSupply": "90",
                    "quantity": "90"
                }
            ],
            "unitsPerDay": "1",
            "dosePerDay": "50"
        },
        {
            "ndc9": "00378-0018",
            "brandName": "METOPROLOL TARTRATE",
            "genericName": "METOPROLOL TARTRATE",
            "dosageStrength": "25",
            "dosageUnit": "mg",
            "doseForm": "tablet, film coated",
            "drugGroup": [
                "antihtn",
                "betablocker"
            ],
            "route": "oral",
            "quantity": "180",
            "daysSupply": "90",
            "fills": [
                {
                    "fillDate": "2012-02-06",
                    "daysSupply": "90",
                    "quantity": "180"
                },
                {
                    "fillDate": "2012-05-16",
                    "daysSupply": "90",
                    "quantity": "180"
                }
            ],
            "unitsPerDay": "2",
            "dosePerDay": "50"
        }
    ],
    "resourceType": "cmr"
}

antihtn_meds_list = get_antihtn_meds(sample_data)

for medication in antihtn_meds_list:
    print(medication["brandName"])


# In[5]:


##question4
def get_tablet_meds(data_obj: dict) -> list:
    medications = data_obj.get("medications", [])
    tablet_meds = []

    for medication in medications:
        dose_form = medication.get("doseForm", "")
        if "tablet" in dose_form.lower():
            tablet_meds.append(medication)

    return tablet_meds

# Sample data
data_obj = {
    "etlUpdated": "2012-12-21T23:58:00",
    "id": "123",
    "medications": [
        {
            "ndc9": "39017-0147",
            "brandName": "AMLODIPINE BESYLATE",
            "dosageStrength": "5",
            "dosageUnit": "mg",
            "doseForm": "tablet",
            "drugGroup": [
                "ccb",
                "antihtn"
            ],
            "route": "oral",
            "quantity": "90",
            "daysSupply": "90",
            "fills": [
                {
                    "fillDate": "2012-02-18",
                    "daysSupply": "90",
                    "quantity": "90"
                },
                {
                    "fillDate": "2012-05-16",
                    "daysSupply": "90",
                    "quantity": "90"
                }
            ],
            "display": "AMLODIPINE BESYLATE 5 MG",
            "unitsPerDay": "1",
            "dosePerDay": "5"
        },
        {
            "ndc9": "60505-2671",
            "brandName": "ATORVASTATIN CALCIUM",
            "genericName": "ATORVASTATIN CALCIUM",
            "dosageStrength": "80",
            "dosageUnit": "mg",
            "doseForm": "tablet, film coated",
            "drugGroup": [
                "statin",
                "azoleddi",
                "antilipid",
                "cms_statin",
                "cms_spc_statin"
            ],
            "route": "oral",
            "quantity": "90",
            "daysSupply": "90",
            "fills": [
                {
                    "fillDate": "2012-04-10",
                    "daysSupply": "90",
                    "quantity": "90"
                },
                {
                    "fillDate": "2012-07-09",
                    "daysSupply": "90",
                    "quantity": "90"
                }
            ],
            "unitsPerDay": "1",
            "dosePerDay": "80"
        },
        {
            "ndc9": "68382-0136",
            "brandName": "LOSARTAN POTASSIUM",
            "genericName": "LOSARTAN POTASSIUM",
            "dosageStrength": "50",
            "dosageUnit": "mg",
            "doseForm": "tablet, film coated",
            "drugGroup": [
                "arb",
                "antihtn",
                "cms_rasa"
            ],
            "route": "oral",
            "quantity": "90",
            "daysSupply": "90",
            "fills": [
                {
                    "fillDate": "2012-02-25",
                    "daysSupply": "90",
                    "quantity": "90"
                },
                {
                    "fillDate": "2012-05-25",
                    "daysSupply": "90",
                    "quantity": "90"
                }
            ],
            "unitsPerDay": "1",
            "dosePerDay": "50"
        },
        {
            "ndc9": "00378-0018",
            "brandName": "METOPROLOL TARTRATE",
            "genericName": "METOPROLOL TARTRATE",
            "dosageStrength": "25",
            "dosageUnit": "mg",
            "doseForm": "tablet, film coated",
            "drugGroup": [
                "antihtn",
                "betablocker"
            ],
            "route": "oral",
            "quantity": "180",
            "daysSupply": "90",
            "fills": [
                {
                    "fillDate": "2012-02-06",
                    "daysSupply": "90",
                    "quantity": "180"
                },
                {
                    "fillDate": "2012-05-16",
                    "daysSupply": "90",
                    "quantity": "180"
                }
            ],
            "unitsPerDay": "2",
            "dosePerDay": "50"
        }
    ],
    "resourceType": "cmr"
}

# Call the function with the sample data
tablet_medications = get_tablet_meds(data_obj)

# Print the result
for med in tablet_medications:
    print(med["brandName"])


# In[14]:


##question5
from typing import Optional

def get_latest_med_ndc(data_obj: dict) -> Optional[str]:
    medications = data_obj.get("medications", [])
    
    if not medications:
        return None

    latest_fill_date = None
    latest_ndc = None

    for medication in medications:
        fills = medication.get("fills", [])
        for fill in fills:
            fill_date = fill.get("fillDate")
            if not latest_fill_date or fill_date > latest_fill_date:
                latest_fill_date = fill_date
                latest_ndc = medication.get("ndc9")

    return latest_ndc

# Sample data
data_obj = {
    "etlUpdated": "2012-12-21T23:58:00",
    "id": "123",
    "medications": [
        {
            "ndc9": "39017-0147",
            "brandName": "AMLODIPINE BESYLATE",
            "dosageStrength": "5",
            "dosageUnit": "mg",
            "doseForm": "tablet",
            "drugGroup": [
                "ccb",
                "antihtn"
            ],
            "route": "oral",
            "quantity": "90",
            "daysSupply": "90",
            "fills": [
                {
                    "fillDate": "2012-02-18",
                    "daysSupply": "90",
                    "quantity": "90"
                },
                {
                    "fillDate": "2012-05-16",
                    "daysSupply": "90",
                    "quantity": "90"
                }
            ],
            "display": "AMLODIPINE BESYLATE 5 MG",
            "unitsPerDay": "1",
            "dosePerDay": "5"
        },
        {
            "ndc9": "60505-2671",
            "brandName": "ATORVASTATIN CALCIUM",
            "genericName": "ATORVASTATIN CALCIUM",
            "dosageStrength": "80",
            "dosageUnit": "mg",
            "doseForm": "tablet, film coated",
            "drugGroup": [
                "statin",
                "azoleddi",
                "antilipid",
                "cms_statin",
                "cms_spc_statin"
            ],
            "route": "oral",
            "quantity": "90",
            "daysSupply": "90",
            "fills": [
                {
                    "fillDate": "2012-04-10",
                    "daysSupply": "90",
                    "quantity": "90"
                },
                {
                    "fillDate": "2012-07-09",
                    "daysSupply": "90",
                    "quantity": "90"
                }
            ],
            "unitsPerDay": "1",
            "dosePerDay": "80"
        },
        {
            "ndc9": "68382-0136",
            "brandName": "LOSARTAN POTASSIUM",
            "genericName": "LOSARTAN POTASSIUM",
            "dosageStrength": "50",
            "dosageUnit": "mg",
            "doseForm": "tablet, film coated",
            "drugGroup": [
                "arb",
                "antihtn",
                "cms_rasa"
            ],
            "route": "oral",
            "quantity": "90",
            "daysSupply": "90",
            "fills": [
                {
                    "fillDate": "2012-02-25",
                    "daysSupply": "90",
                    "quantity": "90"
                },
                {
                    "fillDate": "2012-05-25",
                    "daysSupply": "90",
                    "quantity": "90"
                }
            ],
            "unitsPerDay": "1",
            "dosePerDay": "50"
        },
        {
            "ndc9": "00378-0018",
            "brandName": "METOPROLOL TARTRATE",
            "genericName": "METOPROLOL TARTRATE",
            "dosageStrength": "25",
            "dosageUnit": "mg",
            "doseForm": "tablet, film coated",
            "drugGroup": [
                "antihtn",
                "betablocker"
            ],
            "route": "oral",
            "quantity": "180",
            "daysSupply": "90",
            "fills": [
                {
                    "fillDate": "2012-02-06",
                    "daysSupply": "90",
                    "quantity": "180"
                },
                {
                    "fillDate": "2012-05-16",
                    "daysSupply": "90",
                    "quantity": "180"
                }
            ],
            "unitsPerDay": "2",
            "dosePerDay": "50"
        }
    ],
    "resourceType": "cmr"
}

latest_ndc = get_latest_med_ndc(data_obj)
print("Latest NDC:", latest_ndc)

