

def check_games():
    import requests
    from bs4 import BeautifulSoup as bs
    import datetime

    now = datetime.datetime.now()
    ppe_website = "http://www.ppe.pl/premiery/" + str(now.year) + "/" + str(now.month)
    print(ppe_website)
    ppe_data = requests.get(ppe_website)
    ppe_data = bs(ppe_data.text, "html.parser")
    #print(ppe_data)

    dlugosc = len(ppe_data.findAll('div', {'class': 'weekdayDay'}))
    first = ppe_data.find('div', {'class': 'weekdayDay'})
    print(first.get_text())
    sec = ppe_data.find('ul', {'class': 'premiery'})
    for cos2 in sec.findAll('a', {'class': 'nag title'}):
        print(cos2.get_text().replace("	", ""))
    #print(dlugosc)
    #print(first.get_text())
    for cos in range(dlugosc-1):
        first = first.find_next('div', {'class': 'weekdayDay'})
        print(first.get_text())
        sec = sec.find_next('ul', {'class': 'premiery'})
        for cos2 in sec.findAll('a', {'class': 'nag title'}):
            print(cos2.get_text().replace("	", ""))