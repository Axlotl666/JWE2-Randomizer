# JWE2-Randomizer
Python tool for randomized dino selection.

Edit config.txt in a text editor to set up the randomization scheme, then run the .py file. The png is used as a background. 
The .csv file contains dino info for use with randomizer. The tool uses Pygame for the UI, so you'll need to install that.

Example config (set up for UK Challenge mode. Banned all dinos, forced limited UK roster):
#config file is case sensitive. Set these variables to control the randomization.

#NAME is the name of this run and the name of the randomizer save file.

NAME: UK1

#TARGET is the number of species desired for your random park.

TARGET: 13

#MODE is randomization style: Select one of the following:
#True Random - random creaturess only filtered by tier and banlist
#Alphabet - random creatures filtered by tier and banlist, with one dino for each letter of the alphabet
#Balanced - random creatures filtered by tier, banlist, and an even selection across species CLASS
#Traditional - random creatures filtered by tier and banlist, with a distribution based on Jurassic Park species.

MODE: Traditional

#BANLIST is a comma separated list of words that are ban species based on JWEstats.csv entries
#Can be a species name or any other entry in the .csv file, IE hybrid, meat, noncanon
#For challenge mode, you must ban all species not in that map's roster.
#Note: spaces between entries will cause them to be ignored.

BANLIST: meat,plant,fish

#FORCED is a counterpart of BANLIST, its a list of things that override the banlist.

FORCED: Cearadactylus,Dsungaripterus,Maaradactylus,Tropeognathus,Ichthyosaurus,Liopleurodon,Tylosaurus,Attenborosaurus,Styxosaurus,Gallimimus,Dracorex,Pachycephalosaurus,Homalocephale,Apatosaurus,Olorotitan,Ouranosaurus,Nigersaurus,Diplodocus,Iguanodon,Nasutoceratops,Kentrosaurus,Nodosaurus,Chungkingosaurus,Styracosaurus,Minmi,Gigantspinosaurus,Sauropelta,Pachyrhinosaurus,Crichtonsaurus,Pentaceratops,Ankylosaurus,Therizinosaurus,Ceratosaurus,Carnotaurus,Coelophysis,Herrerasaurus,Baryonyx,Giganotosaurus,Compsognathus,Monolophosaurus,Pyroraptor,Australovenator,Tyrannosaurus,Velociraptor

#Set BLANK to True to include blank pattern in the skin randomization. False removes blank.

BLANK: False
