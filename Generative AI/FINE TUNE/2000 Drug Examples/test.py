import os 
import openai

def init_api():
    with open(".env") as env:
        for line in env:
            if "=" in line:
                key, value = line.strip().split("=")
                os.environ[key] = value

    openai.api_key = os.environ.get('OPENAI_API_KEY')


init_api()

# Configure the model ID. Change this to your model ID.
model = "ada:ft-personal:drug-malady-data-2023-11-21-21-18-39"


# # Let's use a drug from each class
# drugs = [
#     "A CN Gel(Topical) 20gmA CN Soap 75gm",  # Class 0
#     "Addnok Tablet 20'S",  # Class 1
#     "ABICET M Tablet 10's",  # Class 2
# ]


# # Returns a drug class for each drug
# for drug_name in drugs:
#     prompt = "Drug: {}\nMalady:".format(drug_name)


#     response = openai.Completion.create(
#         model=model,
#         prompt=prompt,
#         temperature=1,
#         max_tokens=1,
#     )


#     # Print the generated text
#     drug_class = response.choices[0].text
#     print(drug_class)
drugs = [
    "What is 'A CN Gel(Topical) 20gmA CN Soap 75gm' used for?",  # Class 0
    "What is 'Addnok Tablet 20'S' used for?",  # Class 1
    "What is 'ABICET M Tablet 10's' used for?",  # Class 2
]

class_map = {
    0: "Acne",
    1: "Adhd",
    2: "Allergies",
    # ...
}

for drug_name in drugs:
    prompt = "Drug: {}\nMalady:".format(drug_name)

    response = openai.Completion.create(
        model=model,
        prompt=prompt,
        temperature=1,
        max_tokens=1,
    )
    
    response = response.choices[0].text
    try: 
        print(drug_name + " is used for " + class_map[int(response)])
    except:
        print("I don't know what " + drug_name + " is used for.")
    print()
