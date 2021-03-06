#!/usr/bin/env python

from random import seed
from random import randint
from hashlib import sha256

# survey topic white space stripped raw text reverse chronological order of final proposal
seed = seed(sha256(b'UbjVtbgnjnljvguvg:BWFvzcfbaifPnebyrOnfxva,npbzcnengvir nanylfvfNerjryvivatvanfvzhyngvba(cymnethrlrf)Snibevgrgifubjnaqrcvfbqrnaqjulgurevfrbsgurrzbwvuvfgbel,cebcre&vzcebcrehfntr,nygreangvirzrnavatfbsfbzrrzbwvf,uvfgbelbsrzbwvf,pbairefngvbafhfvatrkpyhfvirylrzbwvf,rgp.Nerjrvanfvzhyngvba?Jungnerbgurejnlfgbfnavgnevyljvcrlbheohggvsjrehabhgbsgbvyrgcncre?Ubjqbfgnesvfuercebqhpr?jurerqbrfzlryrpgevpvglpbzrsebz?').hexdigest())

# reverse chronological order of final proposal
peeps = ['Mckenna', 'Aud', 'Shirin', 'Jess', 'Lexi', 'Mel', 'Casey', 'John']
seen = set()

for i, peep in enumerate(peeps):
    i += 1
    topic = randint(1, len(peeps))

    while topic in seen or topic == i:
        topic = randint(1, len(peeps))

    seen.add(topic)
    print(i, peep, topic)

