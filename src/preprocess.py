
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
    elif data["Blocks"][10]['Text'] == 'BLUE SHIELD':
        patient_name = data["Blocks"][29]['Text'][20:]
        insured_name = data["Blocks"][16]['Text'][22:]
        claim_no = data["Blocks"][34]['Text'][14:]
        address_line1 = data["Blocks"][13]['Text']
        address_line2 = data["Blocks"][14]['Text']
        employer_name = data["Blocks"][23]['Text'][12:]
        policy_number = data["Blocks"][27]['Text'][10:]
        notice_date = data["Blocks"][36]['Text'][16:]
        provider_name = data["Blocks"][71]['Text']
        provider_number = ''
        payment_amount = data["Blocks"][90]['Text']
        service_desc = data["Blocks"][82]['Text']
        return patient_name, insured_name, claim_no, address_line1, address_line2, employer_name, policy_number, notice_date, provider_name, provider_number, payment_amount, service_desc
    elif data["Blocks"][3]['Text'] == 'Independent Health Association, Inc.':
        patient_name = data["Blocks"][18]['Text'][13:]
        insured_name = data["Blocks"][18]['Text'][13:]
        claim_no = data["Blocks"][23]['Text'][8:]
        address_line1 = data["Blocks"][11]['Text']
        address_line2 = data["Blocks"][13]['Text']
        employer_name = data["Blocks"][19]['Text'][12:]
        policy_number = data["Blocks"][20]['Text'][9:]
        notice_date = data["Blocks"][14]['Text'][16:]
        provider_name = data["Blocks"][22]['Text'][10:]
        provider_number = data["Blocks"][21]['Text'][12:]
        payment_amount = data["Blocks"][73]['Text']
        service_desc = data["Blocks"][52]['Text']
        return patient_name, insured_name, claim_no, address_line1, address_line2, employer_name, policy_number, notice_date, provider_name, provider_number, payment_amount, service_desc
    elif data["Blocks"][4]['Text'] == 'BlueCross BlueShield of Oklahoma':
        patient_name = data["Blocks"][13]['Text'][9:]
        insured_name = data["Blocks"][13]['Text'][9:]
        claim_no = data["Blocks"][19]['Text'][8:]
        address_line1 = ''
        address_line2 = ''
        employer_name = ''
        policy_number = data["Blocks"][6]['Text'][35:]
        notice_date = data["Blocks"][20]['Text'][16:]
        provider_name = data["Blocks"][16]['Text'][10:]
        provider_number = ''
        payment_amount = data["Blocks"][122]['Text']
        service_desc = data["Blocks"][57]['Text']
        return patient_name, insured_name, claim_no, address_line1, address_line2, employer_name, policy_number, notice_date, provider_name, provider_number, payment_amount, service_desc
    elif data["Blocks"][104]['Text'] == 'UnitedHealthcare':
        patient_name = data["Blocks"][29]['Text'][9:]
        insured_name = data["Blocks"][27]['Text'][9:]
        claim_no = data["Blocks"][17]['Text'][9:]
        address_line1 = data["Blocks"][37]['Text'][9:]
        address_line2 = data["Blocks"][40]['Text']
        employer_name = ''
        policy_number = data["Blocks"][20]['Text'][10:]
        notice_date = data["Blocks"][11]['Text']
        provider_name = data["Blocks"][34]['Text'][7:]
        provider_number = ''
        payment_amount = data["Blocks"][97]['Text']
        service_desc = data["Blocks"][77]['Text']
        return patient_name, insured_name, claim_no, address_line1, address_line2, employer_name, policy_number, notice_date, provider_name, provider_number, payment_amount, service_desc
    elif data["Blocks"][60]['Text'] == 'BlueCross BlueShield':
        patient_name = data["Blocks"][349]['Text']
        insured_name = data["Blocks"][368]['Text']
        claim_no = data["Blocks"][381]['Text']
        address_line1 = data["Blocks"][352]['Text']
        address_line2 = data["Blocks"][353]['Text']
        employer_name = data["Blocks"][344]['Text']
        policy_number = data["Blocks"][370]['Text']
        notice_date = data["Blocks"][518]['Text']
        provider_name = data["Blocks"][429]['Text']
        provider_number = ''
        payment_amount = data["Blocks"][480]['Text']
        service_desc = data["Blocks"][431]['Text']
        return patient_name, insured_name, claim_no, address_line1, address_line2, employer_name, policy_number, notice_date, provider_name, provider_number, payment_amount, service_desc
    elif data["Blocks"][5]['Text'] == 'MACo Health Care Trust':
        patient_name = data["Blocks"][69]['Text']
        insured_name = data["Blocks"][29]['Text']
        claim_no = data["Blocks"][68]['Text']
        address_line1 = data["Blocks"][30]['Text']
        address_line2 = data["Blocks"][31]['Text']
        employer_name = ''
        policy_number = data["Blocks"][104]['Text'][19:]
        notice_date = data["Blocks"][24]['Text'][6:]
        provider_name = data["Blocks"][108]['Text'][10:]
        provider_number = data["Blocks"][27]['Text'][7:]
        payment_amount = data["Blocks"][205]['Text']
        service_desc = data["Blocks"][185]['Text']
        return patient_name, insured_name, claim_no, address_line1, address_line2, employer_name, policy_number, notice_date, provider_name, provider_number, payment_amount, service_desc
    elif data["Blocks"][8]['Text'] == 'BlueCross BlueShield of Texas':
        patient_name = data["Blocks"][750]['Text'][9:]
        insured_name = data["Blocks"][750]['Text'][9:]
        claim_no = data["Blocks"][756]['Text'][8:]
        address_line1 = ''
        address_line2 = ''
        employer_name = ''
        policy_number = data["Blocks"][743]['Text'][12:25]
        notice_date = data["Blocks"][757]['Text'][16:]
        provider_name = data["Blocks"][753]['Text'][10:]
        provider_number = ''
        payment_amount = data["Blocks"][861]['Text']
        service_desc = data["Blocks"][796]['Text']
        return patient_name, insured_name, claim_no, address_line1, address_line2, employer_name, policy_number, notice_date, provider_name, provider_number, payment_amount, service_desc
    elif data["Blocks"][1]['Text'][:-1] == 'DELTA DENTAL':
        patient_name = data["Blocks"][3]['Text'][8:]
        insured_name = data["Blocks"][3]['Text'][8:]
        claim_no = data["Blocks"][5]['Text'][9:]
        address_line1 = ''
        address_line2 = ''
        employer_name = ''
        policy_number = ''
        notice_date = data["Blocks"][7]['Text'][5:]
        provider_name = data["Blocks"][4]['Text'][10:]
        provider_number = ''
        payment_amount = data["Blocks"][72]['Text']
        service_desc = data["Blocks"][169]['Text']
        return patient_name, insured_name, claim_no, address_line1, address_line2, employer_name, policy_number, notice_date, provider_name, provider_number, payment_amount, service_desc
    elif data["Blocks"][6]['Text'] == 'HIGHMARK.':
        patient_name = data["Blocks"][25]['Text'][20:]
        insured_name = data["Blocks"][12]['Text'][22:]
        claim_no = data["Blocks"][30]['Text'][14:]
        address_line1 = ''
        address_line2 = ''
        employer_name = data["Blocks"][18]['Text'][12:]
        policy_number = data["Blocks"][20]['Text'][10:]
        notice_date = data["Blocks"][17]['Text'][17:]
        provider_name = data["Blocks"][22]['Text']
        provider_number = data["Blocks"][65]['Text']
        payment_amount = data["Blocks"][78]['Text']
        service_desc = data["Blocks"][64]['Text']
        return patient_name, insured_name, claim_no, address_line1, address_line2, employer_name, policy_number, notice_date, provider_name, provider_number, payment_amount, service_desc