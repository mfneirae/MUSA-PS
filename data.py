#
# #############################################################################
#       Copyright (c) 2019 mfneirae.com All Rights Reserved.
#
#                This work  is licensed under a Creative Commons
#       Attribution-NonCommercial - ShareAlike 4.0 International
#       License and MIT Licence.
#
#       by Manuel Neira Embus.
#
#       For more information write me to jai@mfneirae.com
#       Or visit my webpage at https://mfneirae.com/
# #############################################################################
#

def importdata(CODE):
    import gspread
    # import pprint
    from oauth2client.service_account import ServiceAccountCredentials
    # Variables
    global ID
    global EST
    global EFT
    global DURATION
    global LST
    global LFT
    global ATTRIBUTES
    global OPERATIONS
    # Extract
    scope = ['https://spreadsheets.google.com/feeds',
            'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('MUSA-BD.json', scope)
    client = gspread.authorize(creds)
    sheet = client.open('MUSA-BD').sheet1
    ID = sheet.cell(CODE,1).value
    EST = sheet.cell(CODE,7).value
    EFT = sheet.cell(CODE,8).value
    DURATION = sheet.cell(CODE,14).value
    LST = sheet.cell(CODE,9).value
    LFT = sheet.cell(CODE,10).value
    ATTRIBUTES = sheet.cell(CODE,4).value
    OPERATIONS = sheet.cell(CODE,5).value
    # pp = pprint.PrettyPrinter()
    # pp.pprint(result)
