import random
print('Willkommen!')
print()
print('Dieses Spiel können maximal 5 Personen spielen.')
print('Du navigierst mit deiner Tastatur durch dieses Spiel.')
print('Erscheint "#AKTION#" wird eine Tastatureingabe gefordert.')
print('Wähle deine Entscheidung, in dem du die der Entscheidung zugeordneten Taste aus der Frage drückst.')
print('Du wirst schon sehen, was gemeint ist. Drücke danach "Enter", um deine Entscheidung abzuschicken.')
print('Manchmal pausiert das Spiel, damit Spieler ihre Aktionen durchführen können. Mit "Enter" fährst du fort.')
print('Solltet ihr weniger als 5 Spieler sein, lass die überschüssigen Namensfelder leer, in dem du einfach "Enter" drückst.')
print('Gebe nun jeweils den Namen einer Spielerin oder eines Spielers ein und drücke danach "Enter":')
print()
player = []
while len(player) < 2:
    name_player1 = input('Name von Spielerin/Spieler 1:')
    name_player2 = input('Name von Spielerin/Spieler 2:')
    name_player3 = input('Name von Spielerin/Spieler 3:')
    name_player4 = input('Name von Spielerin/Spieler 4:')
    name_player5 = input('Name von Spielerin/Spieler 5:')
    
    player_names = {name_player1, name_player2, name_player3, name_player4, name_player5}
    player = []
    active_playernames = []
    for playersname in player_names:
        if playersname:
            player.append({'name': playersname, 'karten': [], 'kartenwerte': []})
            active_playernames.append(playersname)
    if len(player) < 2:
        print('Naaa, also alleine kannst du das Spiel nicht spielen. Gebe mehr als 1 Namen an.')
print()
print('Los gehts!')
print('Viel Spaß ' + ', '.join(active_playernames[0:-1]) + ' und ' + active_playernames[-1] + '!')
print()

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
    in_f1 = input('#AKTION# Welche Farbe hat die nächste Karte? - Rot [r] oder schwarz [s]?')
    karte = random.choice(deck)
    #print(pl['name'] + ', deine neue Karte ist: ' + karte['name'])
    print(pl['name'] + ', deine neue Karte ist: ')
    print('    ' + karte['name'])
    pl['karten'].append(karte)
    deck.remove(karte)

    if spielleitermodus:
        if karte['wert'] == 14:
            print('Ass! Trinke 1.' + ' ' + u'\u2717')
        elif in_f1 == karte['farbe']:
            print('Richtig! Verteile 1.' + ' ' + u'\u2713')
        else:
            print('Falsch! Trinke 1.' + ' ' + u'\u2717')
    input()

# Drunter/Drüber
for pl in player:
    print('------------------' + pl['name'] + ' ist dran!' + '------------------')
    print(pl['name'] + "'s bisherige Karten: ")
    for karten in pl['karten']:
        print('    ' + karten['name'])
    in_f2 = input('#AKTION# Ist der Wert der nächsten Karte niedriger [-], höher [+] oder gleich [g] deiner bisherigen Karte?')
    karte = random.choice(deck)    
    print(pl['name'] + ', deine neue Karte ist: ')
    print('    ' + karte['name'])
    pl['karten'].append(karte)
    deck.remove(karte)

    if spielleitermodus:
        if karte['wert'] == 14:
            print('Ass! Trinke 2.' + ' ' + u'\u2717')
        elif in_f2 == '+' and karte['wert'] > pl['karten'][0]['wert']:
            print('Richtig! Verteile 2.' + ' ' + u'\u2713' + ' ' + u'\u2713')
        elif in_f2 == '-' and karte['wert'] < pl['karten'][0]['wert']:
            print('Richtig! Verteile 2.' + ' ' + u'\u2713' + ' ' + u'\u2713')
        elif in_f2 == 'g' and karte['wert'] == pl['karten'][0]['wert']:
            print('Richtig! Verteile 2.' + ' ' + u'\u2713' + ' ' + u'\u2713')
        else:
            print('Falsch! Trinke 2.' + ' ' + u'\u2717' + ' ' + u'\u2717')    
    input()

# Innerhalb/Außerhalb
for pl in player:
    print('------------------' + pl['name'] + ' ist dran!' + '------------------')
    print(pl['name'] + "'s bisherige Karten: ")
    for karten in pl['karten']:
        print('    ' + karten['name'])
    in_f3 = input('#AKTION# Liegt der Wert der nächsten Karte innerhalb [i], außerhalb [a] deiner bisherigen Karten oder ist er gleich [g]?')
    karte = random.choice(deck)
    print(pl['name'] + ', deine neue Karte ist: ')
    print('    ' + karte['name'])
    pl['karten'].append(karte)
    deck.remove(karte)

    if spielleitermodus:
        if karte['wert'] == 14:
            print('Ass! Trinke 3.' + ' ' + u'\u2717' + ' ' + u'\u2717' + ' ' + u'\u2717')
        elif in_f3 == 'i' and (karte['wert'] > min(pl['karten'][0]['wert'], pl['karten'][1]['wert']) \
            and karte['wert'] < max(pl['karten'][0]['wert'], pl['karten'][1]['wert'])):
            print('Richtig! Verteile 3.' + ' ' \
                + u'\u2713' + ' ' + u'\u2713' + ' ' + u'\u2713')
        elif in_f3 == 'a' and (karte['wert'] < min(pl['karten'][0]['wert'], pl['karten'][1]['wert']) \
            or karte['wert'] > max(pl['karten'][0]['wert'], pl['karten'][1]['wert'])):
            print('Richtig! Verteile 3.' + ' ' \
                + u'\u2713' + ' ' + u'\u2713' + ' ' + u'\u2713')
        elif in_f3 == 'g' and (karte['wert'] == pl['karten'][0]['wert'] \
            or karte['wert'] == pl['karten'][1]['wert']):
            print('Richtig! Verteile 3.' + ' ' \
                + u'\u2713' + ' ' + u'\u2713' + ' ' + u'\u2713')
        else:
            print('Falsch! Trinke 3.' + ' ' \
                + u'\u2717' + ' ' + u'\u2717' + ' ' + u'\u2717')
    input()

# Muster
for pl in player:
    print('------------------' + pl['name'] + ' ist dran!' + '------------------')
    print(pl['name'] + "'s bisherige Karten: ")
    for karten in pl['karten']:
        print('    ' + karten['name'])
    in_f4 = input('#AKTION# Welches Muster hat die nächste Karte? (gebe Muster so ein: [karo], [herz], [pik] oder [kreuz])')
    karte = random.choice(deck)
    print(pl['name'] + ', deine neue Karte ist: ')
    print('    ' + karte['name'])
    pl['karten'].append(karte)
    deck.remove(karte)

    if spielleitermodus:
        if karte['wert'] == 14:
            print('Ass! Trinke 4.' + ' ' \
                + u'\u2717' + ' ' + u'\u2717' + ' ' + u'\u2717' + ' ' + u'\u2717')
        elif in_f4 == karte['muster']:
            print('Richtig! Alle sollen 1 trinken und verteile zusätzlich 4.' \
                + ' ' + u'\u2713' + ' ' + u'\u2713' + ' ' + u'\u2713' + ' ' + u'\u2713')
        else:
            print('Falsch! Trinke 4.' + ' ' \
                + u'\u2717' + ' ' + u'\u2717' + ' ' + u'\u2717' + ' ' + u'\u2717')
    input()

print('------------------' + 'ENDE RUNDE 1' + '------------------')
for pl in player:
    print('----' + pl['name'])    
    print(pl['name'] + "'s Karten: ")
    for karten in pl['karten']:        
        print('    ' + karten['name'])
        pl['kartenwerte'].append(karten['wert'])
    print()
input()

# Runde 2
print('------------------' + 'BEGINN RUNDE 2' + '------------------')
for i in range(1,6):
    print('Spalte ' + str(i) + ' von 5')
    
    input('#AKTION# ' + str(i) + ' SELBER TRINKEN für: [Drücke enter]')
    karte = random.choice(deck)
    print('    ' + karte['name'])
    deck.remove(karte)

    if spielleitermodus:
        for pl in player:
            if pl['kartenwerte'].count(karte['wert']) > 0:
                print(pl['name'] + ' trinkt: ' + str(pl['kartenwerte'].count(karte['wert'])*i))
                for spielerkarten in pl['karten']:
                    if spielerkarten['wert'] == karte['wert']:
                        pl['karten'].remove(spielerkarten)
    input()

    input('#AKTION# ' + str(i) + ' VERTEILEN für: [Drücke enter]')
    karte = random.choice(deck)
    print('    ' + karte['name'])
    deck.remove(karte)

    if spielleitermodus:
        for pl in player:
            if pl['kartenwerte'].count(karte['wert']) > 0:
                print(pl['name'] + ' verteilt: ' + str(pl['kartenwerte'].count(karte['wert'])*i))
                for spielerkarten in pl['karten']:
                    if spielerkarten['wert'] == karte['wert']:
                        pl['karten'].remove(spielerkarten)
    input()

print('------------------' + 'ENDE RUNDE 2' + '------------------')
for pl in player:
    print('----' + pl['name'])    
    print(pl['name'] + "'s verbleibende Karten: ")
    for karten in pl['karten']:        
        print('    ' + karten['name'])
    print()
        

# Runde 3 - FINALE
print('------------------' + 'BEGINN FINALE' + '------------------')
print()
deck = deck_init.copy()
k1 = random.choice(deck)
deck.remove(k1)
k2 = random.choice(deck)
deck.remove(k2)
k3 = random.choice(deck)
deck.remove(k3)
k4 = random.choice(deck)
deck.remove(k4)
k5 = random.choice(deck)
deck.remove(k5)
win = False
while len(deck) >= 5 and win == False:    
    print('Es liegen:')
    print('1: ' + k1['name'])
    print('2: ' + k2['name'])
    print('3: ' + k3['name'])
    print('4: ' + k4['name'])
    print('5: ' + k5['name'])
    print()
    print('Verbleibende Karten im Deck: ' + str(len(deck)))    
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
        input()    
        print('Du bist bei Karte ' + str(k) + ' des Finales:')        
        print('    ' + curr_karte['name'])
        in_ff = input('#AKTION#  Ist der Wert der nächsten gezogenen Karte niedriger [-], höher [+] oder gleich [g] der liegenden Karte?')
        karte = random.choice(deck)
        print('Die gezogene Karte ist: ')
        print('    ' + karte['name'])   
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
            print('Ass! Zurück zum Start.' + ' ' + u'\u2717')
            input()  
            break
        elif in_ff == '+' and karte['wert'] > curr_karte['wert']:
            print('Richtig!' + ' ' + u'\u2713')
        elif in_ff == '-' and karte['wert'] < curr_karte['wert']:
            print('Richtig!' + ' ' + u'\u2713')
        elif in_ff == 'g' and karte['wert'] == curr_karte['wert']:
            print('Richtig!' + ' ' + u'\u2713')
        else:
            print('Falsch! Zurück zum Start' + ' ' + u'\u2717')
            input()  
            break
        if k == 5:
            print()
            print('Du hast gewonnen!' + ' ' \
                + u'\u2713' + ' ' + u'\u2713' + ' ' + u'\u2713' + ' ' + u'\u2713')
            win = True
            break

if len(deck) < 5 and win == False:
    print()
    print('Du hast verloren! Das Ende des Kartendecks ist erreicht.' \
        + ' ' + u'\u2717' + ' ' + u'\u2717' + ' ' + u'\u2717' + ' ' + u'\u2717')


