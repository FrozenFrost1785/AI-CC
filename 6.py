QUESTIONS = [
    'Do you have cough?',
    'Do you have a sore throat?',
    'Do you have a fever?',
    'Are you noticing any unexplained excessive sweating?',
    'Do you have an itchy throat?',
    'Do you have a runny nose?',
    'Do you have a stuffy nose?',
    'Do you have a headache?',
    'Do you feel tired without actually exhausting yourself?'
]

THRESHOLD = {
    'Mild': 30,
    'Severe': 50,
    'Extreme': 75
}

def expertSystem(questions, threshold):
    score = 0

    for question in questions:
        print(question + " (Y/N) ")
        ans = input("> ")
        if ans.lower() == 'y':
            print('On a scale of 1-10 how bad is it?')
            ip = input('> ')
            while (not ip.isnumeric()) or int(ip) < 1 or int(ip) > 10:
                print('Enter a valid input (1-10)!')
                ip = input('> ')
            score += int(ip)

    print("\n--- Assessment Result ---\n")

    if score >= threshold['Extreme']:
        print("You are showing symptoms of having EXTREME COVID-19")
        print("Please call +91 8112233445 immediately for immediate assistance.")
        print("Based on your symptoms, you will need immediate hospitalization.")

    elif score >= threshold['Severe']:
        print("Based on your answers, you are showing symptoms of SEVERE COVID-19.")
        print("You are advised to contact a COVID-19 specialist ASAP.")
        print("You are prescribed with Favipriavir, Dolo 650 / Crocin 500, Paracetamol, Brufane.")
        print("Also, conduct a COVID-19 lab test ASAP as this might be a false positive.")
        print("Lab Testing: https://www.metropolisindia.com/parameter/pune/covid-19-rt-pcr-test")

    elif score >= threshold['Mild']:
        print("Based on your answers, you are showing symptoms of VERY MILD COVID-19.")
        print("Please isolate yourself immediately on a precautionary basis.")
        print("As this might be a false positive, please consider testing yourself.")
        print("At-home testing using self-testing kits is recommended.")
        print("Self-testing: https://www.flipkart.com/mylab-coviself-covid-19-rapid-antigen-test-kit/p/itm4d34ea09cad97")
        print("Lab Testing: https://www.metropolisindia.com/parameter/pune/covid-19-rt-pcr-test")

    else:
        print("You are showing NO symptoms of COVID-19.")
        print("However, if you feel unsure, please get tested.")
        print("At-home testing using self-testing kits is recommended.")
        print("Self-testing: https://www.flipkart.com/mylab-coviself-covid-19-rapid-antigen-test-kit/p/itm4d34ea09cad97")

print("\n\n\t\tWelcome To The COVID-19 EXPERT SYSTEM\n")
print("\tNote: Please answer the following questions very honestly.\n\n")
expertSystem(QUESTIONS, THRESHOLD)
