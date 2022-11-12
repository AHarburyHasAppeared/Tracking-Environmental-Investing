# Tracks environmental harm of top ten global companies
# authors: Becky Marcus, Alex Harbury, Elizaveta Kozlova, Fevronia Van Sickle
# version: 11/12/22

class Tracker:
    def __init__(self, company, location):
        self.company = company
        # we can switch out location for investments later, this is just to provide context for now
        self.location = location


# top US companies
walmart = Tracker("Walmart", "USA")
amazon = Tracker("Amazon", "USA")
apple = Tracker("Apple", "USA")
unitedHealth = Tracker("United Health", "USA")

# top 9 harmful companies to invest in
peabodyEnergy = Tracker("Peabody Energy", "unknown")
kuwaitPetroleumCorp = Tracker("Kuwait Petroleum Corp", "unknown")
conocoPhillips = Tracker("ConocoPhillips", "unknown")
Chevron = Tracker("Chevron", "unknown")
saudiAramco = Tracker("Chevron", "unknown")
exxonMobil = Tracker("ExxonMobil", "unknown")
shell = Tracker("Shell", "unknown")
bp = Tracker("BP", "unknown")
natIranOil = Tracker("National Iranian Oil Co", "unknown")
rDutchShell = Tracker("Royal Dutch Shell", "unknown")

# dictionary of top US companies and location (can be investments later)
usCompDict = {walmart: 'USA', amazon: 'USA',
              apple: 'USA', unitedHealth: 'USA'}

# dictionary of harmful companies to invest in and location?
envHarmDict = {peabodyEnergy: 'unknown', kuwaitPetroleumCorp: 'unknown', conocoPhillips: 'unknown', Chevron: 'unknown',
               saudiAramco: 'unknown', exxonMobil: 'unknown',  shell: 'unknown', natIranOil: 'unknown', rDutchShell: 'unknown', }
