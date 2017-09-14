indent = 18 #amount the ELOs are shifted over in the output. Set to -1 to cancel
sortScores = 2 #0 is no sort, 1 is high to low, 2 is low to high
scoreRound = 0 #decimal places to sort to; negative rounds to nearest 10, 100, etc. Auto-converts to integer if less than or equal to 0
default = 2000 #Starting elo 

#Change these only when adding new contests
class Person:
  def __init__(self, Name, elo, newelo, Meet116, Meet216, Meet316, Meet416, Meet516, StateInvite16, StateMeet16, AMCA16, AMCB16, AIMEpercentile, HMMT16, USAMO16, ARML16, TSTST, Meet117, PUMaC16, Meet217, Meet317, Meet417):
    self.Name = Name
    self.elo = elo
    self.newelo = newelo
    self.Meet116 = Meet116
    self.Meet216 = Meet216
    self.Meet316 = Meet316
    self.Meet416 = Meet416
    self.Meet516 = Meet516
    self.StateInvite16 = StateInvite16
    self.StateMeet16 = StateMeet16
    self.AMCA16 = AMCA16
    self.AMCB16 = AMCB16
    self.AIMEpercentile = AIMEpercentile
    self.HMMT16 = HMMT16
    self.USAMO16 = USAMO16
    self.ARML16 = ARML16
    self.TSTST = TSTST
    self.Meet117 = Meet117
    self.PUMaC16 = PUMaC16
    self.Meet217 = Meet217
    self.Meet317 = Meet317
    self.Meet417 = Meet417
  def array(self):
    return [self.Meet116, self.Meet216, self.Meet316, self.Meet416, self.Meet516, self.StateInvite16, self.StateMeet16, self.AMCA16, self.AMCB16, self.AIMEpercentile, self.HMMT16, self.USAMO16, self.ARML16, self.TSTST, self.Meet117, self.PUMaC16, self.Meet217, self.Meet317, self.Meet417]
  def name(self):
    return self.Name
  def editElo(self, x):
    self.elo = x
  def editNewElo(self, x):
    self.newelo = x
weights = [14, 14, 14, 14, 14, 20, 14, 43, 43, 52, 67, 57, 22, 57, 14, 44, 14, 14, 14]
maxscore = [14, 14, 14, 14, 14, 24, 14, 150, 150, 100, 1000, 42, 10, 42, 14, 1000, 14, 14, 14]
events = len(weights)

#Change these when adding new contests or new people. Put -1 for contests in which person did not compete.
People=[
Person("Person 1",  default, default, 14, 14, 12, 14, 11, 22, 14,   129,   132, 97.95, 4.050, 14,  6, -1, 14, 168, 14, 14, 14),
Person("Person 2",  default, default, 14, 14, 14, 12, 12, 12, 14,    99, 118.5, 83.94, 2.327, -1,  5, -1, 13, 107, 14, 14, 12),
Person("Person 3",  default, default, 14, 14, 11, 13, 14, 12, 14, 106.5, 136.5, 97.95, 1.901,  2,  7, -1, 13,  61, 14, 10, 14),
Person("Person 4",  default, default, 14, 14, 11, 14, 12, 20, 10,   132,    -2,    92, 2.326, 21,  7, 21, 14,  -1, 14, 14, 14),
Person("Person 5",  default, default, 12, 14, 11, 11, 11,  9, 10, 103.5,   123,    -1,    -1, -1, -1, -1, 12,  75, 12, -1, -1),
Person("Person 6",  default, default, 14, 12, 14, 12, 12, 22, 14, 112.5, 115.5, 89.29, 2.676, -1,  6, -1, -1,  -1, -1, -1, -1),
Person("Person 7",  default, default, 13, 10, 10, 12, 10, 21, 14,    -1,    -1,    -1,    -1, -1,  4, -1,  8,  -1, -1, -1,  5),
Person("Person 8",  default, default, 11, 11, 13, 12, 11, -1,  6, 106.5,    -1,    -1,    -1, -1, -1, -1, 11,  58, -1, -1, -1),
Person("Person 9",  default, default, 14, 12, 12, 12, 11, 10, 12,    -1,    -1,    -1,    -1, -1, -1, -1, -1,  57, -1, -1, -1),
Person("Person 10", default, default, 14, 14, 11, 11, 12, 20, 14,    -1,    -1, 83.94, 2.556, -1,  4, -1, 14, 129, 14, 14, 14),
Person("Person 11", default, default, 14, 14, 12, 14, 12, 14, 14,   123,    -1, 93.43,    -1,  1,  7, -1, 14, 153, 14, 12, 14),
Person("Person 12", default, default, 14, 12, 14, 12, 14, 21, 14,    84,    -2,    -1, 2.558, -1,  4, -1, -1,  -1, -1, -1, -1),
Person("Person 13", default, default, -1, 12, 12, 10, 10, -1, 12,    -1,   102, 76.48,    -1, -1,  4, -1, 10,  -1, 12, 12, 12),
Person("Person 14", default, default, 12,  9,  6, 14, 10, -1,  8,  88.5,    -1,    -1,    -1, -1, -1, -1, -1,  -1, -1, -1, -1),
Person("Person 15", default, default, -1,  0, -1, -1,  6, -1, -1,    -1,    -1,    -1,    -1, -1, -1, -1,  6,  -1,  8,  8, -1),
Person("Person 16", default, default, 14, 14, 10, 14, 12, 22, 14,    -1, 139.5,    -1, 3.685, -1,  8, -1, 14,  -1, 14, 14, 14),
Person("Person 17", default, default, 14, 14, 14, 14, 12, 21, 14, 130.5,    -1,    -1, 2.350, -1, -1, -1, 14,  -1, -1, -1, -1),
Person("Person 18", default, default, 10, 10,  2, 12,  8, -1, 12,    -1,    -1,    -1,    -1, -1, -1, -1, 10,  -1,  8, 12, -1),
Person("Person 19", default, default, 12, 10, 10, 10, 12, -1, 12,    -1,    -1,    70,    -1, -1, -1, -1, 14,  -1, 14, 14, 14),
Person("Person 20", default, default, -1,  6,  6,  8,  5, -1, -1,    -1,    -1,    -1,    -1, -1, -1, -1, 10,  -1,  5,  9,  8),
Person("Person 21", default, default, 13,  9, 10, 11, 12, -1, 10,   105,    -1,    -1, 1.666, -1,  4, -1, 11,  -1, 14, 12, -1),
Person("Person 22", default, default, -1,  6,  9,  2,  7, -1, -1,    -1,    -1,    -1,    -1, -1, -1, -1, 12,  -1, 10, 12,  7),
Person("Person 23", default, default, 12,  6,  2,  6,  3, -1, -1,    -1,    -1,    -1,    -1, -1, -1, -1, 12,  -1,  8, 11,  6),
Person("Person 24", default, default,  7,  6, 11,  4, 10, -1, 10,    -1,    -1,    -1,    -1, -1, -1, -1,  6,  -1, 10,  9, 14),
Person("Person 25", default, default, -1,  4,  4,  0,  6, -1, -1,    -1,    -1,    -1,    -1, -1, -1, -1,  7,  -1,  6, 10,  6),
Person("Person 26", default, default, -1, -1, -1, -1, -1, -1, -1,    -1,    -1,    -1,    -1, -1, -1, -1,  8,  -1,  6,  3, 14),
Person("Person 27", default, default, 10,  8,  6,  8, 10, -1,  8,    -1,    -1,    -1,    -1, -1, -1, -1, -1,  -1, -1, -1, -1),
Person("Person 28", default, default,  8,  8,  5,  9, 10, -1,  8,    -1,    -1,    -1,    -1, -1, -1, -1, -1,  -1, -1, -1, -1),
Person("Person 29", default, default, -1, -1, -1, -1, -1, -1, -1,    -1, 103.5,    64,    -1, -1,  6, -1, 12,  -1,  8, -1, -1),
Person("Person 30", default, default, 10, 10, 14, 12, 12,  9, 12,    -1,   105,    64,    -1, -1,  4, -1, -1,  -1, -1, -1, -1),
Person("Person 31", default, default, -1, -1, -1, -1, -1, -1, -1,    -1,    -1,    -1,    -1, -1, -1, -1,  7,  -1,  6,  8,  8)
]

#Computations
people = len(People)

for k in range(0, events):
  #Determine which people competed in event k
  CompetedInEventK = []
  for i in range(0, people):
    if ((People[i]).array())[k] > -1:
      CompetedInEventK.append(People[i])
  totalEloShift = 0  
  competitors=len(CompetedInEventK)
  for i in range(0, competitors):
    #Calculating Expected before event k for person i
    expected = -1/2
    for j in range(0, competitors):
      expected = expected + 1/(1 + 10**(((CompetedInEventK[j]).elo - (CompetedInEventK[i]).elo)/400))
    #Calculating Actual of event k for person i
    actual = -1/2
    for j in range(0, competitors):
      if ((CompetedInEventK[i]).array())[k] > ((CompetedInEventK[j]).array())[k]:
        actual = actual + 1
      if ((CompetedInEventK[i]).array())[k] == ((CompetedInEventK[j]).array())[k]:
        if ((CompetedInEventK[i]).array())[k] == maxscore[k]:
          actual = actual + 1/(1 + 10**(((CompetedInEventK[j]).elo - (CompetedInEventK[i]).elo)/400))
        else:
          actual = actual + 1/2
    #Determining K-factor
    EventsiCompetedIn = 1
    for j in range(0, k):
      if (CompetedInEventK[i].array())[j] > -1:
        EventsiCompetedIn = EventsiCompetedIn + 1
    kfactor = (25/((EventsiCompetedIn))) + weights[k]
    #Calculating new Elo
    toBeAssigned = (CompetedInEventK[i]).elo + kfactor*(actual - expected) #edit?
    totalEloShift = totalEloShift + kfactor*(actual - expected)
    (CompetedInEventK[i]).editNewElo(toBeAssigned)
  for i in range(0, competitors):
    (CompetedInEventK[i]).editElo((CompetedInEventK[i]).newelo - totalEloShift/len(CompetedInEventK))

#Printing Elos
total = 0
if sortScores>0:
  report=sorted(People, key=lambda Person: Person.elo)
entries=[]
def niceRound(num,amt):
  if(amt>0):
    return round(num,amt)
  elif amt==0:
    return int(round(num,0))
  else:
    amt=-amt
    return int(round(num/(10**amt),0))*(10**amt)
for i in range(0, people):
  if sortScores==0:
    entries=[People[i].name(),niceRound(People[i].elo,scoreRound)]
  elif sortScores==1:
    entries=[report[i].name(),niceRound(report[i].elo,scoreRound)]
  elif sortScores==2:
    entries=[report[people-i-1].name(),niceRound(report[people-i-1].elo,scoreRound)]
  if indent>=0:
    print(entries[0], " "*(indent-len(entries[0])), entries[1])
  else:
    print(entries[0], entries[1])
  total = total + round(People[i].elo, 0)
print("\nTotal gain of ", round(total/people - default, 1), " Melo points on average per person.")