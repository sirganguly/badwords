import random #import for randomizing
 
print(" Type '1' for ENGLISH and '2' for HINDI")
choice = input(' 1 or 2?')
 
bad_words_hindi1 = ['Choot', 'ma', 'lund', 'chutiya', 'choot ', 'choot', 'Randi', 'Randwe', 'goumutra', 'kutte', 'bhosadchod', 'loda', 'kattey', 'bhakadchod', 'bund', 'Tere tatto', 'Chikni', 'Tu loda ', 'Aaja teri ', 'Kutte', 'Maa ki', 'Shaitan', 'Lauda', 'Lund']
bad_words_hindi2 = ['Ke', 'ka', 'ke', 'ka', 'ki', 'phek', 'lund', 'saala', 'maar', 'choot ', 'bhosade']
bad_words_hindi3 = [' Pakode', ' bhosda', 'fakeer', 'gandu', 'pujari', 'paseena', ' beej', 'aulaad', 'baasi boond', 'muthh', 'marunga', 'tukda', 'ganda', 'lunga', 'kaat donnga', 'choot', 'choos mera', 'maaru', 'aankh', 'bhosade', 'paad', 'lahsun', 'keede']
 
bad_words_hindi = [bad_words_hindi1,bad_words_hindi2,bad_words_hindi3] #all lists in one
random_words_hindi = [random.choice(i) for i in bad_words_hindi] #generate random words form 3 lists
 
bad_words_english1 = ['Fucking', 'fucking', 'bitch ass ', 'cock', 'go piss', 'OP is a', 'son of a', 'hijo', 'motherfucken', 'yo mamma so fa-..', 'Retarded', 'Cockadee', 'cunt', 'Anal', 'Shit', 'Poop', 'stupid', 'certified', 'dick']
bad_words_english2 = ['Retard', 'bitch', 'motherfucker', 'breath', 'on a butt', 'faggot', 'de puta', 'assface', "yo mamma's a fucken bitch", 'clown', 'doo', 'Sucker', 'digger', 'shit', 'taster', 'idiot', 'fuckface', 'cunt', 'vagina', 'cock', 'dick', 'face']
 
bad_words_english = [bad_words_english1,bad_words_english2] #all lists in one
random_words_english = [random.choice(i) for i in bad_words_english] #generate random words form 2 lists
 
if choice == 1:
    print(' '.join(random_words_english)) #prints the result
else:
    print(' '.join(random_words_hindi)) #prints the result
 
#End
