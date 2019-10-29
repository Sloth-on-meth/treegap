while True:
    html = urllib.request.urlopen("http://teamtrees.org")
    soup = BeautifulSoup(html, 'html.parser')
    method1 = soup.find('div', id='totalTrees')
    Treecount = (method1["data-count"])
    Treegap = (20000000-int(Treecount))
    today = datetime.date.today()
    future = datetime.date(2020,1,1)
    diff = future - today
    daystogo = diff.days
    Formatted_Treecount = ("{:,d}".format(int(Treecount)))
    Formatted_Treegap = ("{:,d}".format(int(Treegap)))
    percentage = ((int(Treecount) / int(20000000)) * 100)
    perc2 = round(percentage ,2)
