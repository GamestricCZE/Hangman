import random
import os
import time

words = "into","week","setting","jack","scale","program","double","due","meat","model","fifth","thirty","compound","press","measure","perfect","cost","steel","consonant","lonely","beneath","flew","blanket","silly","general","anybody","captain","out","century","halfway","directly","beginning","usual","funny","satellites","sugar","government","rapidly","worker","push","more","cake","ill","horn","bark","only","high","dress","quiet"
"down","primitive","tales","eleven","small","giving","from","cool","valley","stiff","speak","toy","favorite","warn","differ","voice","fat","lying","properly","wash","move","down","merely","elephant","football","fort","direct","enjoy","halfway","pile","separate","pound","mad","mouth","wife","chair","post","per","blank","suppose","under","little","physical","five","stop","particles","typical","family","since"
"ice","sitting","various","full","sitting","captain","final","regular","blind","green","toy","having","slight","wood","more","afternoon","anything","up","gone","rope","old","also","our","wild","central","mysterious","up","final","however","crowd","fallen","wood","feet","stream","eager","herself","dirt","mill","single","station","prepare","different","being","political","tape","exciting","loss","constantly","question"
"gently","goose","interest","something","repeat","broad","cent","into","divide","experiment","vote","barn","further","number","author","chapter","happily","before","difference","announced","merely","coast","direction","field","reader","jack","mass","finally","soap","wind","cause","central","it","forward","hospital","where","former","arrangement","angry","supper","frog","steam","manner","fell","music","record","step","determine","ball"
"lake","acres","been","changing","garden","volume","expect","though","protection","organization","burn","give","better","else","else","greatly","thick","example","south","base","butter","account","operation","divide","opinion","hair","zoo","between","charge","tie","greatest","another","rate","ahead","make","first","electric","practice","lost","pull","tea","let","our","see","fast","appearance","electric","variety","area"
"hope","declared","fell","prize","plenty","plural","peace","automobile","string","little","chance","examine","yourself","rule","development","bend","know","perfect","like","shoot","on","worried","where","its","person","dear","rush","somebody","can","leave","desert","new","here","map","view","vessels","president","tool","gate","spread","bush","love","electricity","fact","mental","support","knife","depth","whom"
"each","given","settlers","slight","team","factory","customs","run","cloth","been","smoke","beat","again","plates","fine","while","gift","health","go","nine","layers","equally","material","rough","older","drive","curve","too","connected","studying","longer","avoid","find","son","nearly","explain","drop","floating","great","easier","produce","lost","tea","noise","account","company","actually","write","themselves"


print("Welcome to hangman game !!! \n")


time.sleep(3)

Attemps = 8


ThatWord = (random.choice(words))


while True:

    ThatWordChar = list(ThatWord)
    dashes = " _ "*len(ThatWord)
    
    print('Guess this!\n' + dashes + "\n")
    print("You got " + str(Attemps) + " attemps!")
    
    PlayersGuess = input()

    if PlayersGuess in ThatWordChar:
        print("correct!")
    else:
        print("too bad, man!")
        Attemps -= 1

    
    




    if Attemps <= 0:
        print("Game Over!\n You suck!")
        break