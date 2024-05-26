# K Windfuhr, D While, N Kapur, D M Ashcroft, E Kontopantelis, M J Carr, J Shaw, L Applyby, R T Webb, 2024.

import sys, csv, re

codes = [{"code":"589021","system":"multilex"},{"code":"94971020","system":"multilex"},{"code":"88668020","system":"multilex"},{"code":"78912020","system":"multilex"},{"code":"337021","system":"multilex"},{"code":"94973020","system":"multilex"},{"code":"84528020","system":"multilex"},{"code":"83403020","system":"multilex"},{"code":"73441020","system":"multilex"},{"code":"709021","system":"multilex"},{"code":"83398020","system":"multilex"},{"code":"83397020","system":"multilex"},{"code":"713021","system":"multilex"},{"code":"711021","system":"multilex"},{"code":"83404020","system":"multilex"},{"code":"88666020","system":"multilex"},{"code":"81015020","system":"multilex"},{"code":"10469020","system":"multilex"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('atypical-apds-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["atypical-apds-975mg---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["atypical-apds-975mg---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["atypical-apds-975mg---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
