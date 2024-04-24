# Simulated symptom input
user_symptoms = ['Fever', 'Cough', 'Headache']

# Dummy doctor dataset (for illustration purposes)
doctors_data = {
    'DoctorName': ['Dr. Smith', 'Dr. Johnson', 'Dr. Williams', 'Dr. Brown', 'Dr. Anderson'],
    'Specialty': ['General Physician', 'Pulmonologist', 'Neurologist', 'General Surgeon', 'Infectious Disease Specialist']
}

# Simulated recommendation logic
recommended_doctors = []

for symptom in user_symptoms:
    matching_specialties = doctors_data[doctors_data['Specialty'].str.contains(symptom, case=False)]['Specialty'].tolist()
    if matching_specialties:
        for specialty in matching_specialties:
            doctors_in_specialty = doctors_data[doctors_data['Specialty'] == specialty]['DoctorName'].tolist()
            recommended_doctors.extend(doctors_in_specialty)

# Remove duplicate doctor names and display recommended doctors
recommended_doctors = list(set(recommended_doctors))  # Remove duplicates
print("Recommended Doctors based on Symptoms:")
for doctor in recommended_doctors:
    print(doctor)
