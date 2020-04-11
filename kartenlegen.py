import random

player = [{'name': 'Player_1', 'karten': [], 'kartenwerte': []},\
            {'name': 'Player_2', 'karten': [], 'kartenwerte': []},\
            {'name': 'Player_3', 'karten': [], 'kartenwerte': []},\
            {'name': 'Player_4', 'karten': [], 'kartenwerte': []},\
            {'name': 'Player_5', 'karten': [], 'kartenwerte': []}]
spielleitermodus = True
deck_init = [{'name': 'Sieben - Karo - Rot', 'wert': 7, 'muster': 'karo', 'farbe': 'r'}, \
        {'name': 'Sieben - Herz - Rot', 'wert': 7, 'muster': 'herz', 'farbe': 'r'},\
        {'name': 'Sieben - Pik - Schwarz', 'wert': 7, 'muster': 'pik', 'farbe': 's'},\
        {'name': 'Sieben - Kreuz - Schwarz','wert': 7, 'muster': 'kreuz', 'farbe': 's'},\
        {'name': 'Acht - Karo - Rot', 'wert': 8, 'muster': 'karo', 'farbe': 'r'},\
        {'name': 'Acht - Herz - Rot', 'wert': 8, 'muster': 'herz', 'farbe': 'r'},\
        {'name': 'Acht - Pik - Schwarz', 'wert': 8, 'muster': 'pik', 'farbe': 's'},\
        {'name': 'Acht - Kreuz - Schwarz','wert': 8, 'muster': 'kreuz', 'farbe': 's'},\
        {'name': 'Neun - Karo - Rot', 'wert': 9, 'muster': 'karo', 'farbe': 'r'},\
        {'name': 'Neun - Herz - Rot', 'wert': 9, 'muster': 'herz', 'farbe': 'r'},\
        {'name': 'Neun - Pik - Schwarz', 'wert': 9, 'muster': 'pik', 'farbe': 's'},\
        {'name': 'Neun - Kreuz - Schwarz', 'wert': 9, 'muster': 'kreuz', 'farbe': 's'},\
        {'name': 'Zehn - Karo - Rot', 'wert': 10, 'muster': 'karo', 'farbe': 'r'},\
        {'name': 'Zehn - Herz - Rot', 'wert': 10, 'muster': 'herz', 'farbe': 'r'},\
        {'name': 'Zehn - Pik - Schwarz', 'wert': 10, 'muster': 'pik', 'farbe': 's'},\
        {'name': 'Zehn - Kreuz - Schwarz', 'wert': 10, 'muster': 'kreuz', 'farbe': 's'},\
        {'name': 'Bube - Karo - Rot', 'wert': 11, 'muster': 'karo', 'farbe': 'r'},\
        {'name': 'Bube - Herz - Rot', 'wert': 11, 'muster': 'herz', 'farbe': 'r'},\
        {'name': 'Bube - Pik - Schwarz', 'wert': 11, 'muster': 'pik', 'farbe': 's'},\
        {'name': 'Bube - Kreuz - Schwarz', 'wert': 11, 'muster': 'kreuz', 'farbe': 's'},\
        {'name': 'Dame - Karo - Rot', 'wert': 12, 'muster': 'karo', 'farbe': 'r'},\
        {'name': 'Dame - Herz - Rot', 'wert': 12, 'muster': 'herz', 'farbe': 'r'},\
        {'name': 'Dame - Pik - Schwarz', 'wert': 12, 'muster': 'pik', 'farbe': 's'},\
        {'name': 'Dame - Kreuz - Schwarz', 'wert': 12, 'muster': 'kreuz', 'farbe': 's'},\
        {'name': 'Koenig - Karo - Rot', 'wert': 13, 'muster': 'karo', 'farbe': 'r'},\
        {'name': 'Koenig - Herz - Rot', 'wert': 13, 'muster': 'herz', 'farbe': 'r'},\
        {'name':  'Koenig - Pik - Schwarz', 'wert': 13, 'muster': 'pik', 'farbe': 's'},\
        {'name': 'Koenig - Kreuz - Schwarz', 'wert': 13, 'muster': 'kreuz', 'farbe': 's'},\
        {'name': 'Ass - Karo - Rot', 'wert': 14, 'muster': 'karo', 'farbe': 'r'},\
        {'name': 'Ass - Herz - Rot', 'wert': 14, 'muster': 'herz', 'farbe': 'r'},\
        {'name': 'Ass - Pik - Schwarz', 'wert': 14, 'muster': 'pik', 'farbe': 's'},\
        {'name': 'Ass - Kreuz - Schwarz', 'wert': 14, 'muster': 'kreuz', 'farbe': 's'}]
deck = deck_init.copy()

# Farbe
for pl in player:
    print('------------------' + pl['name'] + ' ist dran!' + '------------------')      
    in_f1 = input('#AKTION# Welche Farbe? - Rot [r] oder schwarz [s]?')
    karte = random.choice(deck)
    print(pl['name'] + ', deine neue Karte ist: ' + karte['name'])
    pl['karten'].append(karte)
    deck.remove(karte)

    if spielleitermodus:
        if karte['wert'] == 14:
            print('Ass! Trinke 1.')
        elif in_f1 == karte['farbe']:
            print('Richtig! Verteile 1.')
        else:
            print('Falsch! Trinke 1.')

# Drunter/Drüber
for pl in player:
    print('------------------' + pl['name'] + ' ist dran!' + '------------------')
    print(pl['name'] + 's bisherige Karten: ')
    for karten in pl['karten']:
        print(karten)
    in_f2 = input('#AKTION# Drunter [-], drüber [+] oder gleich [g]?')
    karte = random.choice(deck)
    print(pl['name'] + ', deine neue Karte ist: ' + karte['name'])
    pl['karten'].append(karte)
    deck.remove(karte)

    if spielleitermodus:
        if karte['wert'] == 14:
            print('Ass! Trinke 2.')
        elif in_f2 == '+' and karte['wert'] > pl['karten'][0]['wert']:
            print('Richtig! Verteile 2.')
        elif in_f2 == '-' and karte['wert'] < pl['karten'][0]['wert']:
            print('Richtig! Verteile 2.')
        elif in_f2 == 'g' and karte['wert'] == pl['karten'][0]['wert']:
            print('Richtig! Verteile 2.')
        else:
            print('Falsch! Trinke 2.')

# Innerhalb/Außerhalb
for pl in player:
    print('------------------' + pl['name'] + ' ist dran!' + '------------------')
    print(pl['name'] + 's bisherige Karten: ')
    for karten in pl['karten']:
        print(karten)
    in_f3 = input('#AKTION# Innerhalb [i], außerhalb [a] oder gleich [g]?')
    karte = random.choice(deck)
    print(pl['name'] + ', deine neue Karte ist: ' + karte['name'])
    pl['karten'].append(karte)
    deck.remove(karte)

    if spielleitermodus:
        if karte['wert'] == 14:
            print('Ass! Trinke 3.')
        elif in_f3 == 'i' and karte['wert'] > min(pl['karten'][0]['wert'], pl['karten'][1]['wert']) \
            and karte['wert'] < max(pl['karten'][0]['wert'], pl['karten'][1]['wert']):
            print('Richtig! Verteile 3.')
        elif in_f3 == 'a' and karte['wert'] < min(pl['karten'][0]['wert'], pl['karten'][1]['wert']) \
            or karte['wert'] > max(pl['karten'][0]['wert'], pl['karten'][1]['wert']):
            print('Richtig! Verteile 3.')
        elif in_f3 == 'g' and karte['wert'] == pl['karten'][0]['wert'] or karte['wert'] == pl['karten'][1]['wert']:
            print('Richtig! Verteile 3.')
        else:
            print('Falsch! Trinke 3.')

# Muster
for pl in player:
    print('------------------' + pl['name'] + ' ist dran!' + '------------------')
    print(pl['name'] + 's bisherige Karten: ')
    for karten in pl['karten']:
        print(karten)
    in_f4 = input('#AKTION# Welches Muster? (gebe Muster so ein: [karo], [herz], [pik] oder [kreuz])')
    karte = random.choice(deck)
    print(pl['name'] + ', deine neue Karte ist: ' + karte['name'])
    pl['karten'].append(karte)
    deck.remove(karte)

    if spielleitermodus:
        if karte['wert'] == 14:
            print('Ass! Trinke 4.')
        elif in_f4 == karte['muster']:
            print('Richtig! Alle sollen 1 trinken und verteile zusätzlich 4.')
        else:
            print('Falsch! Trinke 4.')

print('------------------' + 'ENDE RUNDE 1' + '------------------')
for pl in player:
    print('----' + pl['name'])    
    print(pl['name'] + "'s bisherige Karten: ")
    for karten in pl['karten']:        
        print(karten['name'])
        pl['kartenwerte'].append(karten['wert'])

# Runde 2
print('------------------' + 'BEGINN RUNDE 2' + '------------------')
for i in range(1,6):
    print('Reihe: ' + str(i))
    
    input('#AKTION# ' + str(i) + ' SELBER TRINKEN für: [Drücke enter]')
    karte = random.choice(deck)
    print(karte['name'])
    deck.remove(karte)

    if spielleitermodus:
        for pl in player:
            if pl['kartenwerte'].count(karte['wert']) > 0:
                print(pl['name'] + ' trinkt: ' + str(pl['kartenwerte'].count(karte['wert'])*i))
                for spielerkarten in pl['karten']:
                    if spielerkarten['wert'] == karte['wert']:
                        pl['karten'].remove(spielerkarten)

    input('#AKTION# ' + str(i) + ' VERTEILEN für: [Drücke enter]')
    karte = random.choice(deck)
    print(karte['name'])
    deck.remove(karte)

    if spielleitermodus:
        for pl in player:
            if pl['kartenwerte'].count(karte['wert']) > 0:
                print(pl['name'] + ' verteilt: ' + str(pl['kartenwerte'].count(karte['wert'])*i))
                for spielerkarten in pl['karten']:
                    if spielerkarten['wert'] == karte['wert']:
                        pl['karten'].remove(spielerkarten)

print('------------------' + 'ENDE RUNDE 2' + '------------------')
for pl in player:
    print('----' + pl['name'])    
    print(pl['name'] + "'s bisherige Karten: ")
    for karten in pl['karten']:        
        print(karten['name'])
        

# Runde 3 - FINALE
print('------------------' + 'BEGINN FINALE' + '------------------')
deck = deck_init.copy()
k1 = random.choice(deck)
print('1: ' + k1['name'])
deck.remove(k1)
k2 = random.choice(deck)
print('2: ' + k2['name'])
deck.remove(k2)
k3 = random.choice(deck)
print('3: ' + k3['name'])
deck.remove(k3)
k4 = random.choice(deck)
print('4: ' + k4['name'])
deck.remove(k4)
k5 = random.choice(deck)
print('5: ' + k5['name'])
deck.remove(k5)

win = False
while len(deck) >= 5 and win == False:
    for k in range(1,6):
        if k == 1:
            curr_karte = k1
        elif k == 2:
            curr_karte = k2
        elif k == 3:
            curr_karte = k3
        elif k == 4:
            curr_karte = k4
        elif k == 5:
            curr_karte = k5
            
        print('Du bist bei Karte ' + str(k) + ' des Finales:')
        print('Karte ' + str(k) + ': ' + curr_karte['name'])
        in_ff = input('#AKTION#  Drunter [-], drüber [+] oder gleich [g]?:')
        karte = random.choice(deck)
        print('Deine neue Karte ist: ' + karte['name'])    
        deck.remove(karte)

        if k == 1:
            k1 = karte
        elif k == 2:
            k2 = karte
        elif k == 3:
            k3 = karte
        elif k == 4:
            k4 = karte
        elif k == 5:
            k5 = karte
        
        if karte['wert'] == 14:
            print('Ass! Zurück zum Start.')
            break
        elif in_ff == '+' and karte['wert'] > curr_karte['wert']:
            print('Richtig!')
        elif in_ff == '-' and karte['wert'] < curr_karte['wert']:
            print('Richtig!')
        elif in_ff == 'g' and karte['wert'] == curr_karte['wert']:
            print('Richtig!')
        else:
            print('Falsch! Zurück zum Start')
            break
        if k == 5:
            print('Du hast gewonnen!')
            win = True
            break

if len(deck) < 5 and win == False:
    print('Du hast verloren! Das Ende des Kartendecks ist erreicht.')


