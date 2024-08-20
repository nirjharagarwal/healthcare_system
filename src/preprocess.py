
def preprocessdata(data):
    if data["Blocks"][14]['Text'] == 'Twin City Iron Workers':
        patient_name = data["Blocks"][43]['Text']
        insured_name = data["Blocks"][41]['Text']
        claim_no = data["Blocks"][64]['Text']
        address_line1 = data["Blocks"][44]['Text']
        address_line2 = data["Blocks"][45]['Text']
        employer_name = data["Blocks"][14]['Text']
        policy_number = data["Blocks"][53]['Text']
        notice_date = data["Blocks"][35]['Text']
        provider_name = data["Blocks"][66]['Text']
        provider_number = data["Blocks"][61]['Text']
        payment_amount = data["Blocks"][143]['Text']
        service_desc = data["Blocks"][98]['Text']
        return patient_name, insured_name, claim_no, address_line1, address_line2, employer_name, policy_number, notice_date, provider_name, provider_number, payment_amount, service_desc