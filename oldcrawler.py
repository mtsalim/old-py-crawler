from bs4 import BeautifulSoup
import urllib.request
import timeit

start = timeit.default_timer()  #timecounter

page0 = urllib.request.urlopen("https://sports.yahoo.com/nfl/stats/byposition?pos=QB&conference=NFL&year=season_2000&timeframe=All&qualified=1&sort=49&old_category=QB").read()
soup0 = BeautifulSoup(page0, "lxml")
f0 = open('Temp2000.csv', 'w')

page0 = soup0.find("div", { "id" : "yom-league-stats" })
for row in page0.findAll("tr", { "height" : "16" }):
    cells = row.findAllNext("td", { "class" : "yspscores" })
    cellName = row.findAllNext("a")
    if len(cells) != 0 and len(cellName) != 0:
        name = cellName[0].find(text=True)
        team = cells[1].find(text=True)
        passComplets = cells[4].find(text=True)
        passAttempts = cells[5].find(text=True)
        passYards = cells[7].find(text=True)
        tdPasses = cells[10].find(text=True)
        passIntercepts = cells[11].find(text=True)
        f0.write('\n'       + name + ";"
                            + team + ";"
                            + passComplets + ";"
                            + passAttempts + ";"
                            + passYards + ";"
                            + tdPasses + ";"
                            + passIntercepts)
f0.close()
stop = timeit.default_timer()
print ("Tempo em segundos: ", stop-start)