import random
# Vital Signs
heart_rate = 70          # bpm (beats per minute)
body_temperature = 98.6  # °F (degrees Fahrenheit)
systolic_bp = 120        # mmHg (millimeters of mercury)
diastolic_bp = 80        # mmHg (millimeters of mercury)
respiratory_rate = 12    # bpm (breaths per minute)
oxygen_saturation = 98   # % (percentage)

# Anthropometric Measurements
height_inches = 68       # inches
weight_pounds = 154      # lbs (pounds)
bmi = (weight_pounds / (height_inches ** 2)) * 703  # Body Mass Index

# Blood Values
blood_glucose = 90       # mg/dL (milligrams per deciliter)
cholesterol_total = 180  # mg/dL (milligrams per deciliter)
hdl_cholesterol = 50     # mg/dL (milligrams per deciliter)
ldl_cholesterol = 100    # mg/dL (milligrams per deciliter)
triglycerides = 150      # mg/dL (milligrams per deciliter)

# Electrolytes and Minerals
sodium = 140             # mEq/L (milliequivalents per liter)
potassium = 4            # mEq/L (milliequivalents per liter)
calcium = 9.2            # mg/dL (milligrams per deciliter)
magnesium = 2            # mEq/L (milliequivalents per liter)
phosphate = 3.5          # mg/dL (milligrams per deciliter)

# Liver Function
bilirubin_total = 0.7    # mg/dL (milligrams per deciliter)
bilirubin_direct = 0.2   # mg/dL (milligrams per deciliter)
ast = 25                 # IU/L (international units per liter)
alt = 30                 # IU/L (international units per liter)
alkaline_phosphatase = 80  # IU/L (international units per liter)

# Kidney Function
creatinine = 1.0         # mg/dL (milligrams per deciliter)
bun = 15                 # mg/dL (milligrams per deciliter)
egfr = 90                # mL/min/1.73 m² (estimated glomerular filtration rate)

# Complete Blood Count (CBC)
hemoglobin = 14          # g/dL (grams per deciliter)
hematocrit = 42          # % (percentage)
platelet_count = 200000  # cells/μL (cells per microliter)
white_blood_cells = 7000  # cells/μL (cells per microliter)

# Immunology
cd4_count = 800          # cells/μL (cells per microliter)
cd8_count = 600          # cells/μL (cells per microliter)
cd4_cd8_ratio = 1.33

# Hormones
testosterone = 500       # ng/dL (nanograms per deciliter)
estrogen = 100           # pg/mL (picograms per milliliter)
thyroid_tsh = 2.5        # mIU/L (milli-international units per liter)
thyroid_t4 = 7.5         # μg/dL (micrograms per deciliter)

# Coagulation
prothrombin_time = 12    # seconds
activated_ptt = 30       # seconds
international_normalized_ratio = 1.1

# Electrocardiogram (ECG/EKG)
pr_interval = 0.16       # seconds
qrs_duration = 0.08      # seconds
qt_interval = 0.4        # seconds
heart_axis = "normal"    # deviation from the normal axis

# Pulmonary Function
forced_vital_capacity = 4.0  # L (liters)
forced_expiratory_volume = 3.2  # L (liters)
peak_expiratory_flow_rate = 400  # L/min (liters per minute)

# Vision and Hearing
visual_acuity = 20/20    # Snellen eye chart
hearing_threshold = 20   # dB (decibels)

# Allergy Testing
allergies = ["peanuts", "penicillin", "pollen", "dust", "shellfish", "latex", "pet dander"]

# Genetic Markers
genetic_risk = "low"     # low, moderate, high

# Pain Level
pain_level = 3           # 0 to 10 scale (0 = no pain, 10 = worst pain)

# Mental Health Assessment
depression_score = 8     # 0 to 27 scale (higher scores indicate more severe depression)
anxiety_score = 5        # 0 to 21 scale (higher scores indicate more severe anxiety)

# Social Support
social_support_score = 20  # 0 to 100 scale (higher scores indicate greater social support)

# Nutrition
daily_caloric_intake = 2000  # kcal (kilocalories)
fiber_intake = 25          # g (grams)
vitamin_d_level = 30       # ng/mL (nanograms per milliliter)

# Fitness Assessment
cardiovascular_endurance = "good"  # poor, fair, good, excellent
muscular_strength = "fair"        # poor, fair, good, excellent
flexibility_level = "excellent"   # poor, fair, good, excellent

# Environmental Exposures
pollution_exposure = "moderate"   # low, moderate, high
sun_exposure = "moderate"         # low, moderate, high

# Personal Habits
smoking_status = "non-smoker"     # non-smoker, ex-smoker, current smoker
alcohol_consumption = "moderate"  # none, moderate, heavy

# Genetic History
family_history_diabetes = "yes"   # yes, no
family_history_hypertension = "no"  # yes, no
family_history_heart_disease = "yes"  # yes, no
family_history_cancer = "no"        # yes, no

# Occupation
occupation = "office worker"    # job title or category

# Stress and Coping
perceived_stress_level = 4       # 0 to 10 scale (0 = no stress, 10 = extreme stress)
coping_strategy = "exercise"    # stress management strategy

# Health-related Quality of Life
hrqol_score = 75       # 0 to 100 scale (higher scores indicate better quality of life)

# Health Insurance Coverage
health_insurance = "yes"   # yes, no

# Medications
current_medications = ["aspirin", "lisinopril", "levothyroxine"]

# Vaccination Status
vaccination_status = {
    "COVID-19": "fully vaccinated",
    "Influenza": "up to date",
    "Tetanus": "up to date",
    "Measles, Mumps, Rubella (MMR)": "up to date",
    "Hepatitis B": "not received",
    "Pneumococcal": "partially vaccinated",
    "Human Papillomavirus (HPV)": "not received",
    "Meningococcal": "up to date",
    "Varicella (Chickenpox)": "up to date",
    "Other Vaccines": "not received"
}

# Travel History
travel_history = ["United States", "Canada", "Mexico", "Europe", "Asia", "Africa", "South America"]

# Infectious Diseases
infectious_diseases = ["influenza", "COVID-19", "common cold", "tuberculosis", "hepatitis"]

# Blood Donation Status
blood_donation = "eligible"   # eligible, ineligible

# Sleep Disorders
sleep_apnea = "no"            # yes, no
insomnia = "no"              # yes, no

# Screen Time
screen_time_hours = 3        # hours per day

# Exercise Training History
exercise_training_years = 5  # years of regular exercise training

# Substance Abuse History
substance_abuse_history = "none"  # none, alcohol, drugs

# Sexual Health
sexual_activity = "active"     # active, inactive
number_of_sexual_partners = 2  # number of sexual partners in the past year

# Safety
seatbelt_use = "always"        # always, sometimes, rarely, never
helmet_use = "always"          # always, sometimes, rarely, never

# Social Standing Score
social_standing_score = 8.5   # 0 to 10 scale (higher scores indicate higher social standing)

# Social Circles
social_circles = ["family", "work colleagues", "close friends", "hobby group"]

# Information about Friends
friends = [
    {"name": "John", "age": 32, "occupation": "engineer", "relationship": "close friend"},
    {"name": "Emma", "age": 28, "occupation": "teacher", "relationship": "close friend"},
    {"name": "Michael", "age": 30, "occupation": "graphic designer", "relationship": "close friend"},
    # Add more friends and their information here
]
# Dictionary with variable names as keys and their values counting up from 0
variable_count_dict = {
    "heart_rate": 0,
    "body_temperature": 1,
    "systolic_bp": 2,
    "diastolic_bp": 3,
    "respiratory_rate": 4,
    "oxygen_saturation": 5,
    "height_inches": 6,
    "weight_pounds": 7,
    "bmi": 8,
    "blood_glucose": 9,
    "cholesterol_total": 10,
    "hdl_cholesterol": 11,
    "ldl_cholesterol": 12,
    "triglycerides": 13,
    "sodium": 14,
    "potassium": 15,
    "calcium": 16,
    "magnesium": 17,
    "phosphate": 18,
    "bilirubin_total": 19,
    "bilirubin_direct": 20,
    "ast": 21,
    "alt": 22,
    "alkaline_phosphatase": 23,
    "creatinine": 24,
    "bun": 25,
    "egfr": 26,
    "hemoglobin": 27,
    "hematocrit": 28,
    "platelet_count": 29,
    "white_blood_cells": 30,
    "cd4_count": 31,
    "cd8_count": 32,
    "cd4_cd8_ratio": 33,
    "testosterone": 34,
    "estrogen": 35,
    "thyroid_tsh": 36,
    "thyroid_t4": 37,
    "prothrombin_time": 38,
    "activated_ptt": 39,
    "international_normalized_ratio": 40,
    "pr_interval": 41,
    "qrs_duration": 42,
    "qt_interval": 43,
    "heart_axis": 44,
    "forced_vital_capacity": 45,
    "forced_expiratory_volume": 46,
    "peak_expiratory_flow_rate": 47,
    "visual_acuity": 48,
    "hearing_threshold": 49,
    "allergies": 50,
    "genetic_risk": 51,
    "pain_level": 52,
    "depression_score": 53,
    "anxiety_score": 54,
    "social_support_score": 55,
    "daily_caloric_intake": 56,
    "fiber_intake": 57,
    "vitamin_d_level": 58,
    "cardiovascular_endurance": 59,
    "muscular_strength": 60,
    "flexibility_level": 61,
    "pollution_exposure": 62,
    "sun_exposure": 63,
    "smoking_status": 64,
    "alcohol_consumption": 65,
    "family_history_diabetes": 66,
    "family_history_hypertension": 67,
    "family_history_heart_disease": 68,
    "family_history_cancer": 69,
    "occupation": 70,
    "perceived_stress_level": 71,
    "coping_strategy": 72,
    "hrqol_score": 73,
    "health_insurance": 74,
    "current_medications": 75,
    "vaccination_status": 76,
    "travel_history": 77,
    "infectious_diseases": 78,
    "blood_donation": 79,
    "sleep_apnea": 80,
    "insomnia": 81,
    "screen_time_hours": 82,
    "exercise_training_years": 83,
    "substance_abuse_history": 84,
    "sexual_activity": 85,
    "number_of_sexual_partners": 86,
    "seatbelt_use": 87,
    "helmet_use": 88,
    "social_standing_score": 89,
    "social_circles": 90,
    "friends": 91
}
# Dictionary with numerical ID as keys and lists of different values as values
variable_values_dict = {
    0: [70, 75, 80, 65, 78, 72, 85, 90, 95, 88],
    1: [98.6, 98.2, 98.8, 98.9, 98.4, 98.7, 98.3, 98.5, 99.0, 99.2],
    2: [120, 118, 122, 125, 119, 117, 123, 126, 121, 124],
    3: [80, 85, 78, 82, 79, 83, 81, 84, 77, 76],
    4: [12, 14, 11, 13, 15, 16, 10, 9, 8, 17],
    5: [98, 97, 99, 97.5, 98.5, 98.2, 98.8, 98.6, 99.5, 97.8],
    6: [68, 70, 69, 72, 67, 71, 73, 66, 74, 65],
    7: [154, 160, 148, 165, 152, 158, 147, 155, 162, 150],
    8: [38.9, 39.2, 38.5, 39.1, 38.7, 38.8, 39.3, 38.6, 38.4, 39.0],
    9: [90, 95, 100, 85, 92, 87, 93, 88, 98, 91],
    10: [180, 185, 178, 190, 183, 179, 187, 182, 175, 188],
    11: [50, 52, 48, 53, 49, 51, 47, 54, 46, 55],
    12: [100, 105, 98, 108, 102, 96, 110, 99, 103, 106],
    13: [150, 155, 145, 160, 148, 165, 140, 158, 147, 152],
    14: [140, 135, 142, 138, 133, 141, 137, 139, 136, 134],
    15: [4, 4.2, 3.8, 4.5, 4.1, 3.9, 4.3, 4.4, 3.7, 4.6],
    16: [9.2, 9.0, 9.4, 9.1, 9.5, 9.3, 9.6, 9.7, 9.8, 8.9],
    17: [2, 1.9, 2.1, 1.8, 2.2, 2.3, 2.4, 1.7, 1.6, 1.5],
    18: [3.5, 3.4, 3.6, 3.7, 3.3, 3.2, 3.8, 3.1, 3.9, 3.0],
    19: [0.7, 0.6, 0.8, 0.5, 0.9, 1.0, 0.4, 0.3, 0.2, 0.1],
    20: [0.2, 0.1, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.0],
    21: [25, 24, 26, 23, 27, 22, 28, 29, 30, 21],
    22: [30, 28, 32, 29, 31, 33, 34, 27, 35, 26],
    23: [80, 85, 78, 82, 79, 83, 81, 84, 77, 86],
    24: [1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9],
    25: [15, 14, 16, 13, 17, 18, 19, 12, 11, 20],
    26: [90, 95, 85, 80, 100, 105, 110, 115, 75, 70],
    27: [14, 15, 13, 16, 12, 17, 11, 18, 10, 19],
    28: [42, 41, 43, 40, 44, 39, 45, 38, 46, 37],
    29: [200000, 205000, 210000, 195000, 215000, 190000, 220000, 185000, 225000, 230000],
    30: [7000, 6500, 7500, 6000, 8000, 5500, 8500, 5000, 9000, 9500],
    31: [800, 820, 780, 830, 790, 770, 840, 760, 850, 880],
    32: [600, 620, 580, 630, 590, 640, 570, 650, 560, 660],
    33: [1.33, 1.35, 1.31, 1.36, 1.32, 1.37, 1.30, 1.38, 1.29, 1.39],
    34: [500, 520, 480, 530, 490, 470, 540, 460, 550, 570],
    35: [100, 105, 95, 110, 90, 115, 120, 85, 125, 130],
    36: [2.5, 2.6, 2.4, 2.7, 2.3, 2.8, 2.2, 2.9, 2.1, 3.0],
    37: [7.5, 7.6, 7.4, 7.7, 7.3, 7.8, 7.2, 7.9, 7.1, 8.0],
    38: [12, 12.5, 11.5, 13, 11, 13.5, 10.5, 14, 10, 14.5],
    39: [30, 31, 29, 32, 28, 33, 27, 34, 26, 35],
    40: [1.1, 1.2, 1.0, 1.3, 0.9, 1.4, 0.8, 1.5, 0.7, 1.6],
    41: [0.16, 0.15, 0.17, 0.18, 0.14, 0.19, 0.13, 0.20, 0.12, 0.21],
    42: [0.08, 0.07, 0.09, 0.10, 0.06, 0.11, 0.05, 0.12, 0.04, 0.13],
    43: [0.4, 0.39, 0.41, 0.38, 0.42, 0.37, 0.43, 0.36, 0.44, 0.35],
    44: ["normal", "left deviation", "right deviation"],
    45: [4.0, 3.8, 4.2, 3.7, 4.3, 3.6, 4.4, 3.5, 4.5, 3.9],
    46: [3.2, 3.1, 3.3, 3.4, 3.0, 3.5, 2.9, 3.6, 2.8, 3.7],
    47: [400, 380, 420, 370, 430, 360, 440, 350, 450, 340],
    48: ["20/20", "20/40", "20/30", "20/50", "20/60", "20/70", "20/80", "20/90", "20/100", "20/110"],
    49: [20, 19, 21, 18, 22, 17, 23, 16, 24, 15],
    50: ["peanuts", "penicillin", "pollen", "dust", "shellfish", "latex", "pet dander", "mold", "insect stings", "medications"],
    51: ["low", "moderate", "high"],
    52: [3, 6, 8, 4, 7, 9, 5, 10, 2, 11],
    53: [8, 12, 7, 13, 6, 14, 5, 15, 4, 16],
    54: [5, 7, 4, 8, 3, 9, 2, 10, 1, 11],
    55: [20, 50, 80, 30, 60, 90, 40, 70, 10, 100],
    56: [2000, 1800, 2200, 1600, 2400, 1400, 2600, 1200, 2800, 3000],
    57: [25, 30, 20, 35, 15, 40, 10, 45, 5, 50],
    58: [30, 25, 35, 20, 40, 15, 45, 10, 50, 5],
    59: ["good", "excellent", "fair", "poor"],
    60: ["fair", "good", "excellent"],
    61: ["excellent", "good"],
    62: ["low", "moderate", "high"],
    63: ["low", "moderate", "high"],
    64: ["non-smoker", "ex-smoker", "current smoker", "occasional smoker", "social smoker"],
    65: ["none", "moderate", "heavy"],
    66: ["yes", "no"],
    67: ["yes", "no"],
    68: ["yes", "no"],
    69: ["yes", "no"],
    70: ["office worker", "teacher", "engineer", "doctor", "police officer", "nurse", "chef", "artist", "architect", "lawyer"],
    71: [4, 7, 3, 8, 2, 9, 1, 10, 0, 11],
    72: ["exercise", "meditation", "journaling", "yoga", "socializing", "music", "gardening", "reading", "traveling", "cooking"],
    73: [75, 80, 70, 85, 65, 90, 60, 95, 55, 100],
    74: ["yes", "no", "undecided"],
    75: ["aspirin", "lisinopril", "levothyroxine", "atorvastatin", "metformin", "omeprazole", "losartan", "hydrochlorothiazide", "atorvastatin", "simvastatin"],
    76: [
        ["fully vaccinated", "partially vaccinated", "not received", "undecided"],
        ["up to date", "not received", "undecided"],
        ["up to date", "not received", "undecided"],
        ["up to date", "not received", "undecided"],
        ["up to date", "not received", "undecided"],
        ["not received", "partially vaccinated", "fully vaccinated", "undecided"],
        ["not received", "partially vaccinated", "fully vaccinated", "undecided"],
        ["up to date", "not received", "undecided"],
        ["up to date", "not received", "undecided"],
        ["not received", "undecided"],
    ],
    77: ["United States", "Canada", "Mexico", "Europe", "Asia", "Africa", "South America", "Australia", "New Zealand", "Caribbean"],
    78: ["influenza", "COVID-19", "common cold", "tuberculosis", "hepatitis", "malaria", "cholera", "dengue fever", "zika virus", "yellow fever"],
    79: ["eligible", "ineligible"],
    80: ["no", "yes"],
    81: ["no", "yes"],
    82: [3, 5, 2, 6, 1, 7, 0, 8],
    83: [5, 4, 6, 3, 7, 2, 8, 1, 9],
    84: ["none", "alcohol", "drugs", "tobacco", "opioids", "marijuana", "stimulants", "sedatives", "hallucinogens", "inhalants"],
    85: ["inactive", "active"],
    86: [1, 2, 3, 0, 4, 5, 6, 7, 8, 9],
    87: ["always", "sometimes", "rarely", "never"],
    88: ["always", "sometimes", "rarely", "never"],
    89: [8.5, 7.5, 9.0, 7.0, 9.5, 6.5, 10, 6.0, 5.5, 10],
    90: [["family", "work colleagues", "close friends", "hobby group", "sports team", "volunteer group", "book club", "religious community", "support group", "online community"]],
    91: [
        {"name": "John", "age": 32, "occupation": "engineer", "relationship": "close friend"},
        {"name": "Emma", "age": 28, "occupation": "teacher", "relationship": "close friend"},
        {"name": "Michael", "age": 30, "occupation": "graphic designer", "relationship": "close friend"},
        {"name": "Sophia", "age": 29, "occupation": "nurse", "relationship": "close friend"},
        {"name": "Daniel", "age": 34, "occupation": "lawyer", "relationship": "close friend"},
        {"name": "Olivia", "age": 27, "occupation": "writer", "relationship": "close friend"},
        {"name": "James", "age": 31, "occupation": "software engineer", "relationship": "close friend"},
        {"name": "Ava", "age": 26, "occupation": "artist", "relationship": "close friend"},
        {"name": "William", "age": 33, "occupation": "doctor", "relationship": "close friend"},
        {"name": "Isabella", "age": 25, "occupation": "marketing manager", "relationship": "close friend"},
    ],
}


def change_variable_value(random_id):
    variable_name = list(variable_count_dict.keys())[list(variable_count_dict.values()).index(random_id)]

    # Pick a random value from the second dictionary
    random_value = random.choice(variable_values_dict[random_id])

    # Change the corresponding variable to the new value
    globals()[variable_name] = random_value

# Loop to demonstrate changes in multiple variables
for _ in range(5):  # Change the value 5 times
    # Generate a random ID for each iteration
    random_id = random.choice(list(variable_count_dict.values()))
    variable_name = list(variable_count_dict.keys())[list(variable_count_dict.values()).index(random_id)]

    # Print the initial value
    print(f"Initial value ({variable_name}): {globals()[variable_name]}")

    # Call the function to change the variable
    change_variable_value(random_id)

    # Print the updated value
    print(f"After change ({variable_name}): {globals()[variable_name]}")
    print("---")