from random import randint
from random import seed

teamnamelist = ['team1', 'team2', 'team3', 'team4', 'team5', 'team6', 'team7', 'team8', 'team9', 'team10', 'team11', 'team12',
'team13', 'team14', 'team15', 'team16', 'team17', 'team18', 'team19', 'team20', 'team21', 'team22', 'team23', 'team24',
'team25', 'team26', 'team27', 'team28', 'team29', 'team30', 'team31', 'team32', 'team33', 'team34', 'team35', 'team36', 
'team37', 'team38', 'team39', 'team40', 'team41', 'team42', 'team43', 'team44', 'team45', 'team46', 'team47', 'team48',
'team49', 'team50','team51', 'team52', 'team53', 'team54', 'team55', 'team56', 'team57', 'team58', 'team59', 'team60',
'team61', 'team62', 'team63', 'team64', 'team65', 'team66', 'team67', 'team68', 'team69', 'team70', 'team71', 'team72',
'team73', 'team74', 'team75', 'team76', 'team77', 'team78', 'team79', 'team80', 'team81', 'team82', 'team83', 'team84',
'team85', 'team86', 'team87', 'team88', 'team89', 'team90', 'team91', 'team92', 'team93', 'team94', 'team95', 'team96',
'team97', 'team98', 'team99', 'team100']
class pokemon:
    def __init__(self,nm,num,typ1,typ2,hp, atk, spd, no0num):
        self.nm = nm
        self.num = num
        self.typ1 = typ1
        self.typ2 = typ2
        self.hp = hp
        self.atk = atk
        self.spd = spd
        self.no0num = no0num
        def sayname(self):
            print(self.nm)

NormalNothing = 'Ghost'
NormalStrong = ''
NormalHalfDMG = 'Rock Steel'
FireNothing = ''
FireStrong = 'Grass Ice Bug Steel'
FireHalfDMG = 'Fire Water Rock Dragon'
WaterNothing = ''
WaterStrong = 'Fire Ground Rock'
WaterHalfDMG = 'Water Grass Dragon'
ElectricNothing = 'Ground'
ElectricStrong = 'Water Flying'
ElectricHalfDMG = 'Electric Grass Dragon'
GrassNothing = ''
GrassStrong = 'Water Ground Rock'
GrassHalfDMG = 'Fire Grass Poison Flying Bug Dragon Steel'
IceNothing = ''
IceStrong = 'Grass Ground Flying Dragon'
IceHalfDMG = 'Fire Water Ice Steel'
FightingNothing = 'Ghost'
FightingStrong = 'Normal Ice Rock Dark Steel'
FightingHalfDMG = 'Poison Flying Psychic Bug'
PoisonNothing = 'Steel'
PoisonStrong = 'Grass'
PoisonHalfDMG = 'Poison Ground Rock Ghost'
GroundNothing  = 'Flying'
GroundStrong = 'Fire Electric Poison Rock'
GroundHalfDMG = 'Grass Bug'
FlyingNothing = ''
FlyingStrong = 'Grass Fighting Bug'
FlyingHalfDMG = 'Electric Rock Steel'
PsychicNothing = 'Dark'
PsychicStrong = 'Fighting Poison'
PsychicHalfDMG = 'Psychic Steel'
BugNothing = ''
BugStrong = 'Grass Psychic Dark'
BugHalfDMG = 'Fire Fighting Poison Flying Ghost Steel'
RockNothing = ''
RockStrong = 'Fire Ice Flying Bug'
RockHalfDMG = 'Fighting Ground Steel'
GhostNothing = 'Normal'
GhostStrong = 'Psychic Ghost'
GhostHalfDMG = 'Dark Steel'
DragonNothing = ''
DragonStrong = 'Dragon'
DragonHalfDMG = 'Steel'
DarkNothing = ''
DarkStrong = 'Psychic'
DarkHalfDMG = 'Fighting Dark Steel'
SteelNothing = ''
SteelStrong = 'Ice Rock'
SteelHalfDMG = 'Fire Water Electric Steel'

Normal = [NormalNothing,NormalStrong,NormalHalfDMG, 'Normal']
Fire = [FireNothing, FireStrong, FireHalfDMG, 'Fire']
Water = [WaterNothing, WaterStrong, WaterHalfDMG, 'Water']
Electric = [ElectricNothing, ElectricStrong, ElectricHalfDMG, 'Electric']
Grass = [GrassNothing, GrassStrong, GrassHalfDMG, 'Grass']
Ice = [IceNothing, IceStrong, IceHalfDMG, 'Ice']
Fighting = [FightingNothing, FightingStrong, FightingHalfDMG, 'Fighting']
Poison = [PoisonNothing, PoisonStrong, PoisonHalfDMG, 'Poison']
Ground = [GroundNothing, GroundStrong, GroundHalfDMG, 'Ground']
Flying = [FlyingNothing, FlyingStrong, FlyingHalfDMG, 'Flying']
Psychic = [PsychicNothing, PsychicStrong, PsychicHalfDMG, 'Psychic']
Bug = [BugNothing, BugStrong, BugHalfDMG, 'Bug']
Rock = [RockNothing, RockStrong, RockHalfDMG, 'Rock']
Ghost = [GhostNothing, GhostStrong, GhostHalfDMG, 'Ghost']
Dragon = [DragonNothing, DragonStrong, DragonHalfDMG, 'Dragon']
Dark = [DarkNothing, DarkStrong, DarkHalfDMG, 'Dark']
Steel = [SteelNothing, SteelStrong, SteelHalfDMG, 'Steel']


poke1 = pokemon("Bulbasaur", "001", Grass, Poison, 293, 196, 188, 1)
poke2 = pokemon("Ivysaur", "002", Grass, Poison, 323, 222, 218, 2)
poke3 = pokemon("Venusaur", "003", Grass, Poison, 363, 262, 258, 3)
poke4 = pokemon("Charmander", "004", Fire, "Null", 281, 202, 228, 4)
poke5 = pokemon("Charmeleon", "005", Fire, 'Null', 319, 226, 258 , 5)
poke6 = pokemon("Charizard", "006", Fire, Flying, 359, 266, 298, 6)
poke7 = pokemon("Squirtle", "007", Water, 'Null', 291, 194, 184, 7)
poke8 = pokemon("Wartortle", "008", Water, "Null", 321, 224, 214, 8)
poke9 = pokemon("Blastoise", "009", Water, 'Null', 361, 264, 254, 9)
poke10 = pokemon("Caterpie", "010", Bug, "Null", 293, 158, 188, 10)
poke11 = pokemon("Metapod", "011", Bug, 'Null', 303, 138, 158, 11)
poke12 = pokemon("Butterfree", "012", Bug, Flying, 323, 188, 238, 12)
poke13 = pokemon("Weedle", "013", Bug, Poison, 283, 168, 198, 13)
poke14 = pokemon("Kakuna", "014", Bug, Poison, 293, 148, 168, 14)
poke15 = pokemon("Beedrill", "015", Bug, Poison, 333, 258, 248, 15)
poke16 = pokemon("Pidgey", "016", Normal, Flying, 283, 188, 210, 16)
poke17 = pokemon("Pidgeotto", "017", Normal, Flying, 329, 218, 240, 17)
poke18 = pokemon("Pidgeot", "018", Normal, Flying, 369, 258, 280, 18)
poke19 = pokemon("Rattata", "019", Normal, 'Null', 263, 210, 242, 19)
poke20 = pokemon("Raticate", "020", Normal, "Null", 313, 260, 292, 20)
poke21 = pokemon("Spearow", "021", Normal, Flying, 283, 218, 238, 21)
poke22 = pokemon("Fearow", "022", Normal, Flying, 333, 278, 298, 22)
poke23 = pokemon("Ekans", "023", Poison, 'Null', 273, 218, 178, 23)
poke24 = pokemon("Arbok", "024", Poison, "Null", 323, 268, 258, 24)
poke25 = pokemon("Pikachu", "025", Electric, 'Null',  273, 208, 278, 25)
poke26 = pokemon("Raichu", "026", Electric, "Null", 323, 278, 298, 26)
poke27 = pokemon("Sandshrew", "027", Ground, 'Null', 303, 248, 178, 27)
poke28 = pokemon("Sandslash", "028", Ground, "Null", 353, 298,228 , 28)
poke29 = pokemon("NidoranF", "029", Poison, 'Null', 313, 192, 180, 29)
poke30 = pokemon("Nidorina", "030", Poison, "Null", 343, 222, 210, 30)
poke31 = pokemon("Nidoqueen", "031", Poison, Ground, 383, 262, 250, 31)
poke32 = pokemon("NidoranM", "032", Poison, "Null", 295, 212, 198, 32)
poke33 = pokemon("Nidorino", "033", Poison, 'Null', 325, 242, 228, 33)
poke34 = pokemon("Nidoking", "034", Poison, Ground, 365, 282, 268, 34)
poke35 = pokemon("Clefairy", "035", Normal, 'Null', 343, 188, 168, 35)
poke36 = pokemon("Clefable", "036", Normal, "Null", 393, 238, 218, 36)
poke37 = pokemon("Vulpix", "037", Fire, 'Null', 279, 180, 228, 37)
poke38 = pokemon("Ninetales", "038", Fire, "Null", 349, 250, 298, 38)
poke39 = pokemon("Jigglypuff", "039", Normal, 'Null', 433, 188, 138, 39)
poke40 = pokemon("Wigglytuff", "040", Normal, "Null", 483, 238, 188, 40)
poke41 = pokemon("Zubat", "041", Poison, Flying, 283, 188, 208, 41)
poke42 = pokemon("Golbat", "042", Poison, Flying, 353, 258, 278, 42)
poke43 = pokemon('Oddish', '043', Grass, Poison, 293, 198, 158, 43)
poke44 = pokemon('Gloom', '044', Grass, Poison, 323, 228, 178, 44)
poke45 = pokemon('Vileplume', '045', Grass, Poison, 353, 258, 198, 45)
poke46 = pokemon('Paras', '046', Bug, Grass, 273, 238, 148, 46)
poke47 = pokemon('Parasect', '047', Bug, Grass, 323, 288, 158, 47)
poke48 = pokemon('Venonat', '048', Bug, Poison, 323, 208, 188, 48)
poke49 = pokemon('Venomoth', '049', Bug, Poison, 343, 228, 278, 49)
poke50 = pokemon('Diglett', '050', Ground, 'Null', 223, 208, 288, 50)
poke51 = pokemon('Dugtrio', '051', Ground, 'Null', 273, 258, 338, 51)
poke52 = pokemon('Meowth', '052', Normal, 'Null', 283, 188, 278, 52)
poke53 = pokemon('Persian', '053', Normal, 'Null', 333, 238, 328, 53)
poke54 = pokemon('Psyduck', '054', Water, 'Null',303, 202, 208, 54)
poke55 = pokemon('Golduck', '055', Water, 'Null', 363, 262, 268, 55)
poke56 = pokemon('Mankey', '056', Fighting, 'Null', 283, 258, 238, 56)
poke57 = pokemon('Primeape', '057', Fighting, 'Null', 333, 308, 288, 57)
poke58 = pokemon('Growlithe', '058', Fire, 'Null', 313, 238, 218, 58)
poke59 = pokemon('Arcanine', '059', Fire, 'Null', 383, 318, 288, 59)
poke60 = pokemon('Poliwag', '060', Water, 'Null', 283, 198, 278, 60)
poke61 = pokemon('Poliwhirl', '061', Water, 'Null', 333, 228, 278, 61)
poke62 = pokemon('Poliwrath', '062', Water, Fighting, 383, 268, 238, 62)
poke63 = pokemon('Abra', '063', Psychic, 'Null', 253, 138, 278, 63)
poke64 = pokemon('Kadabra', '064', Psychic, 'Null', 283, 168, 308, 64)
poke65 = pokemon('Alakazam', '065', Psychic, 'Null', 313, 198, 338, 65)
poke66 = pokemon('Machop', '066', Fighting, 'Null', 343, 258, 168, 66)
poke67 = pokemon('Machoke', '067', Fighting, 'Null', 363, 298, 188, 67)
poke68 = pokemon('Machamp', '068', Fighting, 'Null', 383, 358, 208, 68)
poke69 = pokemon('Bellsprout', '069', Grass, Poison, 303, 248, 178, 69)
poke70 = pokemon('Weepinbell', '070', Grass, Poison, 333, 278, 208, 70)
poke71 = pokemon('Victreebel', '071', Grass, Poison, 363, 308, 238, 71)
poke72 = pokemon('Tentacool', '072', Water, Poison, 283, 178, 238, 72)
poke73 = pokemon('Tentacruel', '073', Water, Poison, 363, 238, 298, 73)
poke74 = pokemon('Geodude', '074', Rock, Ground, 283, 258, 138, 74)
poke75 = pokemon('Graveler', '075', Rock,Ground, 313, 288, 168, 75)
poke76 = pokemon('Golem', '076', Rock, Ground, 363, 318, 188, 76)
poke77 = pokemon('Ponyta', '077', Fire, 'Null', 303, 268, 278, 77)
poke78 = pokemon('Rapidash', '078', Fire, 'Null', 333, 298, 308, 78)
poke79 = pokemon('Slowpoke', '079', Water, Psychic, 383, 228, 128, 79)
poke80 = pokemon('Slowbro', '080', Water, Psychic, 393, 248, 158, 80)
poke81 = pokemon('Magnemite', '081', Electric, 'Null', 253, 168, 188, 81)
poke82 = pokemon('Magneton', '082', Electric, 'Null', 303, 218, 238, 82)
poke83 = pokemon('Farfetchd', '083', Normal, Flying, 307, 228, 218, 83)
poke84 = pokemon('Doduo', '084', Normal, Flying, 273, 268, 248, 84)
poke85 = pokemon('Dodrio', '085', Normal, Flying, 323, 318, 298, 85)
poke86 = pokemon('Seel', '086', Water, 'Null', 333, 188, 188, 86)
poke87 = pokemon('Dewgong', '087', Water, Ice, 383, 238, 238, 87)
poke88 = pokemon('Grimer', '088', Poison, 'Null', 363, 258, 148, 88)
poke89 = pokemon('Muk', '089', Poison, 'Null', 413, 308, 198, 89)
poke90 = pokemon('Shellder', '090', Water, 'Null', 263, 228, 178, 90)
poke91 = pokemon('Cloyster', '091', Water, Ice, 303, 288, 238, 91)
poke92 = pokemon('Gastly', '092', Ghost, Poison, 263, 168, 258, 92)
poke93 = pokemon('Haunter', '093', Ghost, Poison, 293, 198, 288, 93)
poke94 = pokemon('Gengar', '094', Ghost, Poison, 323, 228, 318, 94)
poke95 = pokemon('Onix', '095', Rock, Ground, 273, 188, 238, 95)
poke96 = pokemon('Drowzee', '096', Psychic, 'Null', 323, 194, 182, 96)
poke97 = pokemon('Hypno', '097', Psychic, 'Null', 373, 244, 232, 97)
poke98 = pokemon('Krabby', '098', Water, 'Null', 263, 308, 198, 98)
poke99 = pokemon('Kingler', '099', Water, 'Null', 313, 358, 248, 99)
poke100 = pokemon('Voltorb', '100', Electric, 'Null', 283, 158, 298, 100)
poke101 = pokemon('Electrode', '101', Electric, 'Null', 323, 198, 378, 101)
poke102 = pokemon('Exeggcute', '102', Grass, Psychic, 323, 178, 178, 102)
poke103 = pokemon('Exeggutor', '103', Grass, Psychic, 393, 288, 208, 103)
poke104 = pokemon('Cubone', '104', Ground, 'Null', 303, 198, 168, 104)
poke105 = pokemon('Marowak', '105', Ground, 'Null', 323, 258, 188, 105)
poke106 = pokemon('Hitmonlee', '106', Fighting,'Null', 303, 338, 272, 106)
poke107 = pokemon('Hitmonchan', '107', Fighting, 'Null', 303, 308, 250, 107)
poke108 = pokemon('Lickitung', '108', Normal, 'Null', 383, 208, 158, 108)
poke109 = pokemon('Koffing', '109', Poison, 'Null', 283, 228, 168, 109)
poke110 = pokemon('Weezing', '110', Poison, 'Null', 333, 278, 218, 110)
poke111 = pokemon('Rhyhorn', '111', Ground, Rock, 363, 268, 148, 111)
poke112 = pokemon('Rhydon', '112', Ground, Rock, 413, 358, 178, 112)
poke113 = pokemon('Chansey', '113', Normal, 'Null', 703, 108, 198, 113)
poke114 = pokemon('Tangela', '114', Grass, 'Null', 333, 208, 218, 114)
poke115 = pokemon('Kangaskhan', '115', Normal, 'Null', 413, 288, 278, 115)
poke116 = pokemon('Horsea', '116', Water, 'Null', 263, 178, 218, 116)
poke117 = pokemon('Seadra', '117', Water, 'Null', 313, 228, 268, 117)
poke118 = pokemon('Goldeen', '118', Water, 'Null', 293, 232, 224, 118)
poke119 = pokemon('Seaking', '119', Water, 'Null', 363, 282, 234, 119)
poke120 = pokemon('Staryu', '120', Water, 'Null', 263, 188, 268, 120)
poke121 = pokemon('Starmie', '121', Water, Psychic, 323, 248, 328, 121)
poke122 = pokemon('MrMime', '122', Psychic, 'Null', 283, 188, 278, 122)
poke123 = pokemon('Scyther', '123', Bug, Flying, 343, 318, 308, 123)
poke124 = pokemon('Jynx', '124', Ice, Psychic, 333, 198, 288, 124)
poke125 = pokemon('Electabuzz', '125', Electric, 'Null', 333, 264, 308, 125)
poke126 = pokemon('Magmar', '126', Fire, 'Null', 333, 288, 284, 126)
poke127 = pokemon('Pinsir', '127', Bug, 'Null', 333, 348, 268, 127)
poke128 = pokemon('Tauros', '128', Normal, 'Null', 353, 287, 318, 128)
poke129 = pokemon('Magikarp', '129', Water, 'Null', 243, 118, 258, 129)
poke130 = pokemon('Gyarados', '130', Water, Flying, 393, 348, 260, 130)
poke131 = pokemon('Lapras', '131', Water, Ice, 463, 268, 218, 131)
poke132 = pokemon('Ditto', '132', Normal, 'Null', 299, 194, 194, 132)
poke133 = pokemon('Eevee', '133', Normal, 'Null', 313, 208, 208, 133)
poke134 = pokemon('Vaporeon', '134', Water, 'Null', 463, 228, 228, 134)
poke135 = pokemon('Jolteon', '135', Electric, 'Null', 333, 228, 358, 135)
poke136 = pokemon('Flareon', '136', Fire, 'Null', 333, 228, 358, 136)
poke137 = pokemon('Porygon', '137', Normal, 'Null', 333, 218, 178, 137)
poke138 = pokemon('Omanyte', '138', Rock, Water, 273, 178, 168, 138)
poke139 = pokemon('Omastar', '139', Rock, Water, 343, 218, 208, 139)
poke140 = pokemon('Kabuto', '140', Rock, Water, 263, 256, 278, 140)
poke141 = pokemon('Kabutops', '141', Rock, Water, 323, 328, 258, 141)
poke142 = pokemon('Aerodactyl', '142', Rock, Flying, 363, 308, 358, 142)
poke143 = pokemon('Snorlax', '143', Normal, 'Null', 523, 318, 158, 143)
poke144 = pokemon('Articuno', '144', Ice, Flying, 383, 268, 268, 144)
poke145 = pokemon('Zapdos', '145', Electric, Flying, 383, 278, 298, 145)
poke146 = pokemon('Moltres', '146', Fire, Flying, 383, 298, 278, 146)
poke147 = pokemon('Dratini', '147', Dragon, 'Null', 285, 226, 198, 147)
poke148 = pokemon('Dragonair', '148', Dragon, "Null", 325, 266, 238, 148)
poke149 = pokemon('Dragonite', '149', Dragon, Flying, 385, 366, 258, 149)
poke150 = pokemon('Mewtwo', '150', Psychic, 'Null', 415, 318, 358, 150)
poke151 = pokemon('Mew', '151', Psychic, 'Null', 403, 298, 298, 151)

team1 = []
team2 = [] 
team3 = [] 
team4 = [] 
team5 = []
team6 = []
team7 = []
team8 = [] 
team9 = []
team10 = []
team11 = []
team12 = []
team13 = []
team14 = []
team15 = []
team16 = []
team17 = []
team18 = []
team19 = []
team20 = []
team21 = []
team22 = []
team23 = []
team24 = []
team25 = []
team26 = []
team27 = []
team28 = []
team29 = []
team30 = []
team31 = []
team32 = []
team33 = []
team34 = []
team35 = []
team36 = []
team37 = []
team38 = []
team39 = []
team40 = []
team41 = []
team42 = []
team43 = []
team44 = []
team45 = []
team46 = []
team47 = []
team48 = []
team49 = []
team50 = []
team51 = []
team52 = [] 
team53 = [] 
team54 = [] 
team55 = []
team56 = []
team57 = []
team58 = [] 
team59 = []
team60 = []
team61 = []
team62 = []
team63 = []
team64 = []
team65 = []
team66 = []
team67 = []
team68 = []
team69 = []
team70 = []
team71 = []
team72 = []
team73 = []
team74 = []
team75 = []
team76 = []
team77 = []
team78 = [poke103, poke103, poke103, poke103, poke103, poke103]
team79 = [poke47, poke47, poke47, poke47, poke47, poke47]
team80 = [poke12, poke12, poke12, poke12, poke12, poke12]
team81 = [poke3, poke3, poke3, poke3, poke3, poke3]
team82 = [poke38, poke38, poke38, poke38, poke38, poke38]
team83 = [poke114, poke114, poke114, poke114, poke114, poke114]
team84 = [poke115, poke115, poke115, poke115, poke115, poke115]
team85 = [poke9, poke9, poke9, poke9, poke9, poke9]
team86 = [poke18, poke18,poke18, poke18, poke18, poke18]
team87 = [poke24, poke24, poke24, poke24, poke24, poke24]
team88 = [poke101, poke101, poke101, poke101, poke101, poke101]
team89 = [poke105, poke105, poke105, poke105, poke105, poke105]
team90 = [poke106, poke106, poke106, poke107, poke107, poke107]
team91 = [poke110, poke110, poke110, poke110, poke110, poke110]
team92 = [poke149, poke149, poke149, poke149, poke149, poke149]
team93 = [poke150, poke150, poke150, poke151, poke151, poke151]
team94 = [poke87, poke87, poke87, poke87, poke87, poke87]
team95 = [poke102, poke102, poke102, poke102, poke102, poke102]
team96 = [poke144, poke145, poke146, poke149, poke150, poke143]
team97 = [poke34, poke36, poke45, poke49, poke68, poke94]
team98 = [poke94, poke94, poke94, poke94, poke94, poke94]
team99 = [poke143, poke143, poke143, poke143, poke143, poke143]
team100 = [poke150, poke150, poke150, poke150, poke150, poke150]

autoteam = [team1, team2, team3, team4, team5, team6, team7, team8, team9, team10, team11, team12,
team13, team14, team15, team16, team17, team18, team19, team20, team21, team22, team23, team24,
team25, team26, team27, team28, team29, team30, team31, team32, team33, team34, team35, team36, 
team37, team38, team39, team40, team41, team42, team43, team44, team45, team46, team47, team48,
team49, team50,team51, team52, team53, team54, team55, team56, team57, team58, team59, team60,
team61, team62, team63, team64, team65, team66, team67, team68, team69, team70, team71, team72,
team73, team74, team75, team76, team77, team78, team79, team80, team81, team82, team83, team84,
team85, team86, team87, team88, team89, team90, team91, team92, team93, team94, team95, team96,
team97, team98, team99, team100]
battlingteam = autoteam

poke = [poke1, poke2, poke3, poke4, poke5, poke6, poke7, poke8, poke9, poke10, poke11, poke12,
poke13, poke14, poke15, poke16, poke17, poke18, poke19, poke20, poke21, poke22, poke23, poke24,
poke25, poke26, poke27, poke28, poke29, poke30, poke31, poke32, poke33, poke34, poke35, poke36,
poke37, poke38, poke39, poke40, poke41, poke42, poke43, poke44, poke45, poke46, poke47, poke48,
poke49, poke50, poke51, poke52, poke53, poke54, poke55, poke56, poke57, poke58, poke59, poke60, 
poke61, poke62, poke63, poke64, poke65, poke66, poke67, poke68, poke69, poke70, poke71, poke72, 
poke73, poke74, poke75, poke76, poke77, poke78, poke79, poke80, poke81, poke82, poke83, poke84,
poke85, poke86, poke87, poke88, poke89, poke90, poke91, poke92, poke93, poke94, poke95, poke96, 
poke97, poke98, poke99, poke100, poke101, poke102, poke103, poke104, poke105, poke106, poke107,
poke108, poke109, poke110, poke111, poke112, poke113, poke114, poke115, poke116, poke117, poke118,
poke119, poke120, poke121, poke122, poke123, poke124, poke125, poke126, poke127, poke128, poke129, 
poke130, poke131, poke132, poke133, poke134, poke135, poke136, poke137, poke138, poke139, poke140,
poke141, poke142, poke143, poke144, poke145, poke146, poke147, poke148, poke149, poke150, poke151]


typelist = ['Normal', 'Fire', 'Water', 'Electric', 'Grass', 'Ice', 'Fighting', 'Poison', 'Ground', 'Flying', 'Psychic', 'Bug', 'Rock', 'Ghost', 'Dragon']

def getatkmod(atktype,deftype):
    if(deftype[3] in atktype[0]):
        modifier = 0 
    elif(deftype[3] in atktype[1]):
        modifier = 2
    elif(deftype[3] in atktype[2]):
        modifier = .5
    else:
        modifier = 1
    return modifier

def clearteams():
    w = 0
    while w < 50:
        autoteam[w].clear()
        w = w + 1

def maketeams():
    clearteams()
    h = 0
    t = 0
    while h < 78:
        t = 0
        while(t < 6):
            randonum = randint(1,151)
            randonum = randonum - 1
            autoteam[h].append(poke[randonum])
            t = t+1
        h = h + 1

userteam = []
userteamnames = []

class returnscores:
        def __init__(selfvar, firstscore, secondscore):
            selfvar.firstscore = firstscore
            selfvar.secondscore = secondscore
child1 = []
child2 = []
child3 = []
child4 = []
child5 = []
child6 = []
child7 = []
child8 = []
child9 = []
child10 = []
child11 = []
child12 = []
child13 = []
child14 = []
child15 = []
child16 = []
child17 = []
child18 = []
child19 = []
child20 = []
child21 = []
child22 = []
child23 = []
child24 = []
child25 = []
child26 = []
child27 = []
child28 = []
child29 = []
child30 = []
child31 = []
child32 = []
child33 = []
child34 = []
child35 = []
child36 = []
child37 = []
child38 = []
child39 = []
child40 = []
child41 = []
child42 = []
child43 = []
child44 = []
child45 = []
child46 = []
child47 = []
child48 = []
child49 = []
child50 = []
child51 = []
child52 = []
child53 = []
child54 = []
child55 = []
child56 = []
child57 = []
child58 = []
child59 = []
child60 = []
child61 = []
child62 = []
child63 = []
child64 = []
child65 = []
child66 = []
child67 = []
child68 = []
child69 = []
child70 = []
child71 = []
child72 = []
child73 = []
child74 = []
child75 = []
child76 = []
child77 = []
child78 = []
child79 = []
child70 = []
child71 = []
child72 = []
child73 = []
child74 = []
child75 = []
child76 = []
child77 = []
child78 = []
child79 = []
child80 = []
child81 = []
child82 = []
child83 = []
child84 = []
child85 = []
child86 = []
child87 = []
child88 = []
child89 = []
child90 = []

children = [child1, child2, child3, child4, child5, child6, child7, child8, child9, child10,
child11, child12, child13, child14, child15, child16, child17, child18, child19, child20, 
child21, child22, child23, child24, child25, child26, child27, child28, child29, child30, 
child31, child32, child33, child34, child35, child36, child37, child38, child39, child40,
child41, child42, child43, child44, child45, child46, child47, child48, child49, child50,
child51, child52, child53, child54, child55, child56, child57, child58, child59, child60, 
child61, child62, child63, child64, child65, child66, child67, child68, child69, child70,
child71, child72, child73, child74, child75, child76, child77, child78, child79, child80,
child81, child82, child83, child84, child85, child86, child87, child88, child89, child90]
def crossover(parent1, parent2, childnum):
    countvar = 0
    while countvar < 5:    
        crossoverpoint = randint(1, 5)
        if crossoverpoint == 1:
            children[((childnum*5) + countvar)].append(parent1[0])
            children[((childnum*5) + countvar)].append(parent2[1])
            children[((childnum*5) + countvar)].append(parent2[2])
            children[((childnum*5) + countvar)].append(parent2[3])
            children[((childnum*5) + countvar)].append(parent2[4])
            children[((childnum*5) + countvar)].append(parent2[5])
        elif crossoverpoint == 2:    
            children[((childnum*5) + countvar)].append(parent1[0])
            children[((childnum*5) + countvar)].append(parent1[1])
            children[((childnum*5) + countvar)].append(parent2[2])
            children[((childnum*5) + countvar)].append(parent2[3])
            children[((childnum*5) + countvar)].append(parent2[4])
            children[((childnum*5) + countvar)].append(parent2[5])
        elif crossoverpoint == 3:
            children[((childnum*5) + countvar)].append(parent1[0])
            children[((childnum*5) + countvar)].append(parent1[1])
            children[((childnum*5) + countvar)].append(parent1[2])
            children[((childnum*5) + countvar)].append(parent2[3])
            children[((childnum*5) + countvar)].append(parent2[4])
            children[((childnum*5) + countvar)].append(parent2[5])
        elif crossoverpoint == 4:
            children[((childnum*5) + countvar)].append(parent1[0])
            children[((childnum*5) + countvar)].append(parent1[1])
            children[((childnum*5) + countvar)].append(parent1[2])
            children[((childnum*5) + countvar)].append(parent1[3])
            children[((childnum*5) + countvar)].append(parent2[4])
            children[((childnum*5) + countvar)].append(parent2[5])
        elif crossoverpoint == 5:
            children[((childnum*5) + countvar)].append(parent1[0])
            children[((childnum*5) + countvar)].append(parent1[1])
            children[((childnum*5) + countvar)].append(parent1[2])
            children[((childnum*5) + countvar)].append(parent1[3])
            children[((childnum*5) + countvar)].append(parent1[4])
            children[((childnum*5) + countvar)].append(parent2[5])
        countvar = countvar + 1

thescores = returnscores('x', 'secondscore')


def breed(oneteam, twoteam, threeteam, fourteam, fiveteam, sixteam, seventeam, eightteam, nineteam, tenteam):
    crossover(oneteam, twoteam, 0)
    crossover(twoteam, threeteam, 1)
    crossover(threeteam, fourteam, 2)
    crossover(fourteam, fiveteam, 3)
    crossover(fiveteam, sixteam, 4)
    crossover(sixteam, seventeam, 5)
    crossover(seventeam, eightteam, 6)
    crossover(eightteam, nineteam, 7)
    crossover(nineteam, tenteam, 8)
    crossover(oneteam, tenteam, 9)
    crossover(oneteam, nineteam, 10)
    crossover(oneteam, eightteam, 11)
    crossover(oneteam, seventeam, 12)
    crossover(oneteam, sixteam, 13)
    crossover(oneteam, fiveteam, 14)
    crossover(oneteam, fourteam, 15)
    crossover(oneteam, threeteam, 16)
    crossover(twoteam, fourteam, 17)
    
def battleindv(pkteam1, pkteam2, printaval):
        u = 0
        m = 0
        temphealthlist1 = [pkteam1[0].hp,pkteam1[1].hp,pkteam1[2].hp,pkteam1[3].hp,pkteam1[4].hp,pkteam1[5].hp]
        temphealthlist2 = [pkteam2[0].hp,pkteam2[1].hp,pkteam2[2].hp,pkteam2[3].hp,pkteam2[4].hp,pkteam2[5].hp]
        if printaval == True:
            print("Enemy team: " + pkteam2[0].nm + ' ' + pkteam2[1].nm + ' ' +  pkteam2[2].nm + ' ' + pkteam2[3].nm + ' ' + pkteam2[4].nm + ' '+ pkteam2[5].nm)
        while True:  
            if(temphealthlist1[u] > 0 and temphealthlist2[m] > 0):
                if(pkteam1[u].spd > pkteam2[m].spd):
                    if(pkteam2[m].typ2 != "Null"):
                        teamval = (getatkmod(pkteam1[u].typ1, pkteam2[m].typ1)) * (getatkmod(pkteam1[u].typ1, pkteam2[m].typ2))
                    else:
                        teamval = (getatkmod(pkteam1[u].typ1, pkteam2[m].typ1))
                    mod1 = teamval
                    temphealthlist2[m] = (temphealthlist2[m] - (teamval * pkteam1[u].atk))
                    if temphealthlist2[m] <= 0:
                            temphealthlist2[m] = 0
                    else:
                        if(pkteam1[u].typ2 != "Null"):
                            teamval = (getatkmod(pkteam2[m].typ1, pkteam1[u].typ1)) * (getatkmod(pkteam2[m].typ1, pkteam1[u].typ2))
                        else:
                            teamval = getatkmod(pkteam2[m].typ1, pkteam1[u].typ1)
                        temphealthlist1[u] = (temphealthlist1[u] - (teamval * pkteam2[m].atk))
                        mod2 = teamval
                elif(pkteam2[m].spd > pkteam1[u].spd):
                    if(pkteam1[u].typ2 != "Null"):
                        teamval = (getatkmod(pkteam2[m].typ1, pkteam1[u].typ1) * getatkmod(pkteam2[m].typ1, pkteam1[u].typ2))
                    else:
                        teamval = getatkmod(pkteam2[m].typ1, pkteam1[u].typ1)
                    mod1 = teamval
                    temphealthlist1[u] = (temphealthlist1[u] - (teamval * pkteam2[m].atk))
                    if temphealthlist1[u] <= 0:
                        temphealthlist1[u] = 0
                    else:
                        if(pkteam2[m].typ2 != "Null"):
                            teamval = (getatkmod(pkteam1[u].typ1, pkteam2[m].typ1)) * (getatkmod(pkteam1[u].typ1, pkteam2[m].typ2))
                        else:    
                            teamval = getatkmod(pkteam1[u].typ1, pkteam2[m].typ1)
                        mod2 = teamval
                        temphealthlist2[m] = (temphealthlist2[m] - (teamval * pkteam1[u].atk)) 
                else:
                    
                    if(userteam[u] != "Null"):
                        teamval = (getatkmod(pkteam2[m].typ1, pkteam1[u].typ1)) * (getatkmod(pkteam2[m].typ1, pkteam1[u].typ2))
                    else:
                        teamval = getatkmod(pkteam2[m].typ1, pkteam1[u].typ1)
                    mod1 = teamval
                    temphealthlist1[u] = (temphealthlist1[u] - (getatkmod(pkteam2[m].typ1, pkteam1[u].typ1) * pkteam2[m].atk))
                    
                    if(pkteam2[m].typ2 != "Null"):
                        teamval = (getatkmod(pkteam1[u].typ1, pkteam2[m].typ1)) * (getatkmod(pkteam1[u].typ1, pkteam2[m].typ2))
                    else:    
                        teamval = getatkmod(pkteam1[u].typ1, pkteam2[m].typ1)
                    
                    mod2 = teamval
                    temphealthlist2[m] = (temphealthlist2[m] - (getatkmod(pkteam1[u].typ1, pkteam2[m].typ1) * pkteam1[u].atk))
            if(mod1 == 0) and (mod2 == 0):
                roundedscore1 = 0
                roundedscore2 = 0
                break
            if(temphealthlist1[u] <= 0):
                temphealthlist1[u] = 0
                if(temphealthlist2[m] <= 0 ):
                    temphealthlist2[m] = 0
                if u < 5:
                    u = u + 1
                else:
                    break
            elif(temphealthlist2[m] <= 0 ):
                temphealthlist2[m] = 0
                if(temphealthlist1[u] <= 0):
                    temphealthlist1[u] = 0
                if m < 5:
                    m = m+1
                else:
                    break
        if((mod1 == 0) and (mod2 == 0)):
            if printaval == True:
                print('Stalemate!')
        else:
            u = 0
            m = 0
            score1 = ((temphealthlist1[0] + temphealthlist1[1] + temphealthlist1[2] + temphealthlist1[3] + temphealthlist1[4] + temphealthlist1[5])/(pkteam1[0].hp + pkteam1[1].hp + pkteam1[2].hp + pkteam1[4].hp + pkteam1[5].hp)*100)
            score2 = ((temphealthlist2[0] + temphealthlist2[1] + temphealthlist2[2] + temphealthlist2[3] + temphealthlist2[4] + temphealthlist2[5])/(pkteam2[0].hp + pkteam2[1].hp + pkteam2[2].hp + pkteam2[3].hp + pkteam2[4].hp + pkteam2[5].hp) * 100)
            roundedscore1 = round(score1, 2)
            roundedscore2 = round(score2, 2)
            thescores.firstscore = roundedscore1
            thescores.secondscore = roundedscore2
        if printaval == True:
            print("Your score: " + str(roundedscore1))
            print("Opposing team's score: " + str(roundedscore2))

thebattlingteam = autoteam

def battleall(numteams,battlingteam, gennum):
    b = 0
    o = 0
    newgen = []
    if(len(userteam) < 6):
        print("Not enough pokemon, try again")
    else:
        while b < gennum:
            pokenamelistthing = []
            indexforbestteams = []
            temphealthlist1 = []
            temphealthlist2 = []
            enemyscores = []
            max10 = []
            bestteams = []
            pokelistthing = []
            myscores = []
            m = 0
            u = 0
            while o < numteams:
                battleindv(userteam, battlingteam[o], False)
                pokelistthing.append(battlingteam[o])
                enemyscores.append(thescores.secondscore)
                myscores.append(thescores.firstscore)
                o = o + 1
            otherlist = enemyscores
            e = 0
            while e < 10:
                newmax = max(enemyscores)
                max10.append(newmax)
                indexforbestteams.append(otherlist.index(newmax))
                enemyscores.remove(newmax)
                e = e+1
            
            bestteamnames = [teamnamelist[indexforbestteams[1]], teamnamelist[indexforbestteams[1]],
            teamnamelist[indexforbestteams[2]], teamnamelist[indexforbestteams[3]], teamnamelist[indexforbestteams[4]],
            teamnamelist[indexforbestteams[5]], teamnamelist[indexforbestteams[6]], teamnamelist[indexforbestteams[7]],
            teamnamelist[indexforbestteams[8]], teamnamelist[indexforbestteams[9]]]
            if b != (gennum-1):
                
                breed(battlingteam[indexforbestteams[0]], battlingteam[indexforbestteams[1]], battlingteam[indexforbestteams[2]], battlingteam[indexforbestteams[3]],
                battlingteam[indexforbestteams[4]], battlingteam[indexforbestteams[5]], battlingteam[indexforbestteams[6]], battlingteam[indexforbestteams[7]], 
                battlingteam[indexforbestteams[8]], battlingteam[indexforbestteams[9]])
                
                newgen = [battlingteam[indexforbestteams[0]], battlingteam[indexforbestteams[1]], battlingteam[indexforbestteams[2]],
                battlingteam[indexforbestteams[3]], battlingteam[indexforbestteams[4]], battlingteam[indexforbestteams[5]], battlingteam[indexforbestteams[6]],
                battlingteam[indexforbestteams[7]], battlingteam[indexforbestteams[8]], battlingteam[indexforbestteams[9]],child1, child2, child3,
                child4, child5, child6, child7, child8, child9, child10,
                child11, child12, child13, child14, child15, child16, child17, child18, child19, child20, 
                child21, child22, child23, child24, child25, child26, child27, child28, child29, child30, 
                child31, child32, child33, child34, child35, child36, child37, child38, child39, child40,
                child41, child42, child43, child44, child45, child46, child47, child48, child49, child50,
                child51, child52, child53, child54, child55, child56, child57, child58, child59, child60, 
                child61, child62, child63, child64, child65, child66, child67, child68, child69, child70,
                child71, child72, child73, child74, child75, child76, child77, child78, child79, child80,
                child81, child82, child83, child84, child85, child86, child87, child88, child89, child90]
                battlingteam = newgen
            else:
                print('')
                print('The best teams were: ')
                print(battlingteam[indexforbestteams[0]][0].nm + ' ' + battlingteam[indexforbestteams[0]][1].nm + ' ' + battlingteam[indexforbestteams[0]][2].nm + ' ' + battlingteam[indexforbestteams[0]][3].nm + ' ' + battlingteam[indexforbestteams[0]][4].nm + ' ' + battlingteam[indexforbestteams[0]][5].nm + ' With ' + str(max10[0]) + '% Health Remaining' )
                print(battlingteam[indexforbestteams[1]][0].nm + ' ' + battlingteam[indexforbestteams[1]][1].nm + ' ' + battlingteam[indexforbestteams[1]][2].nm + ' ' + battlingteam[indexforbestteams[1]][3].nm + ' ' + battlingteam[indexforbestteams[1]][4].nm + ' ' + battlingteam[indexforbestteams[1]][5].nm + ' With ' + str(max10[1]) + '% Health Remaining')
                print(battlingteam[indexforbestteams[2]][0].nm + ' ' + battlingteam[indexforbestteams[2]][1].nm + ' ' + battlingteam[indexforbestteams[2]][2].nm + ' ' + battlingteam[indexforbestteams[2]][3].nm + ' ' + battlingteam[indexforbestteams[2]][4].nm + ' ' + battlingteam[indexforbestteams[2]][5].nm + ' With ' + str(max10[2]) + '% Health Remaining' )
                print(battlingteam[indexforbestteams[3]][0].nm + ' ' + battlingteam[indexforbestteams[3]][1].nm + ' ' + battlingteam[indexforbestteams[3]][2].nm + ' ' + battlingteam[indexforbestteams[3]][3].nm + ' ' + battlingteam[indexforbestteams[3]][4].nm + ' ' + battlingteam[indexforbestteams[3]][5].nm + ' With ' + str(max10[3]) + '% Health Remaining')
                print(battlingteam[indexforbestteams[4]][0].nm + ' ' + battlingteam[indexforbestteams[4]][1].nm + ' ' + battlingteam[indexforbestteams[4]][2].nm + ' ' + battlingteam[indexforbestteams[4]][3].nm + ' ' + battlingteam[indexforbestteams[4]][4].nm + ' ' + battlingteam[indexforbestteams[4]][5].nm + ' With ' + str(max10[4]) + '% Health Remaining')
                print(battlingteam[indexforbestteams[5]][0].nm + ' ' + battlingteam[indexforbestteams[5]][1].nm + ' ' + battlingteam[indexforbestteams[5]][2].nm + ' ' + battlingteam[indexforbestteams[5]][3].nm + ' ' + battlingteam[indexforbestteams[5]][4].nm + ' ' + battlingteam[indexforbestteams[5]][5].nm + ' With ' + str(max10[5]) + '% Health Remaining')
                print(battlingteam[indexforbestteams[6]][0].nm + ' ' + battlingteam[indexforbestteams[6]][1].nm + ' ' + battlingteam[indexforbestteams[6]][2].nm + ' ' + battlingteam[indexforbestteams[6]][3].nm + ' ' + battlingteam[indexforbestteams[6]][4].nm + ' ' + battlingteam[indexforbestteams[6]][5].nm + ' With ' + str(max10[6]) + '% Health Remaining')
                print(battlingteam[indexforbestteams[7]][0].nm + ' ' + battlingteam[indexforbestteams[7]][1].nm + ' ' + battlingteam[indexforbestteams[7]][2].nm + ' ' + battlingteam[indexforbestteams[7]][3].nm + ' ' + battlingteam[indexforbestteams[7]][4].nm + ' ' + battlingteam[indexforbestteams[7]][5].nm + ' With ' + str(max10[7]) + '% Health Remaining')
                print(battlingteam[indexforbestteams[8]][0].nm + ' ' + battlingteam[indexforbestteams[8]][1].nm + ' ' + battlingteam[indexforbestteams[8]][2].nm + ' ' + battlingteam[indexforbestteams[8]][3].nm + ' ' + battlingteam[indexforbestteams[8]][4].nm + ' ' + battlingteam[indexforbestteams[8]][5].nm + ' With ' + str(max10[8]) + '% Health Remaining')
                print(battlingteam[indexforbestteams[9]][0].nm + ' ' + battlingteam[indexforbestteams[9]][1].nm + ' ' + battlingteam[indexforbestteams[9]][2].nm + ' ' + battlingteam[indexforbestteams[9]][3].nm + ' ' + battlingteam[indexforbestteams[9]][4].nm + ' ' + battlingteam[indexforbestteams[9]][5].nm + ' With ' + str(max10[9]) + '% Health Remaining')

            o = 0
            b = b + 1


def pickrandteam():
    userteamnames.clear()
    userteam.clear()
    t = 0
    while t < 6:
        randonum = randint(1,151)
        randonum = randonum - 1
        userteam.append(poke[randonum])
        userteamnames.append(poke[randonum].nm)
        t = t+1
    print("Your team is: ")
    print(userteamnames)

def userteamadder():
    z = 0
    while z < 151:
        if(a == poke[z].nm) or (a == str(poke[z].no0num)) or (a == str(poke[z].num)):
            if len(userteam) > 5:
                print("Team Full!")    
                break
            x = 1
            userteam.append(poke[z])
            userteamnames.append(poke[z].nm)
            print(poke[z].nm + " added to your team")
            if len(userteam) == 6:
                print('')
                print("Team Complete!")
                print('')
            break
        else:
            z = z + 1
        if z == 151:
            print("Invalid Input")

def pokepicker():
    z = 0
    while z < 151:
        if(a == poke[z].nm) or (a == str(poke[z].no0num)) or (a == str(poke[z].num)):
            print('')
            print('')
            print('')
            x = 1
            print(poke[z].nm + ":")
            print("Number: " + poke[z].num)
            print("Type: " + poke[z].typ1[3])
            if(poke[z].typ2 != Null):
                print("Second Type: " + poke[z].typ2[3])
            print("Attack: " + str(poke[z].atk))
            print("Speed: " + str(poke[z].spd))
            print("Health: " + str(poke[z].hp))
        else:
            x = 2
            z = z + 1
        if x == 1:
            break
        if z == 151:
            print("Invalid Input")

def printmyteam():
    print(userteamnames)

def clearuserteam():
    userteam.clear()
    userteamnames.clear()
    print("Team Cleared")

def helpmetext():
    print('')
    print("Commands:")
    print("To add pokemon to your team, type addteam or teamadd and whatever pokemon you want")
    print("This can be in number form, such as 5, or it can be something such as 005")
    print("or you can use the name of the pokemon. (be sure to capitalize the name)")
    print("to clear your team, type clearmyteam. To view your team, type printmyteam")
    print("to make your team random instead of picking it, type randteam")
    print("to battle using the genetic algorithm, type tourney")
    print("to battle one specific team, type battle team and then the team number")
    print("to view the pokemon in a specific team, type printteam and then the team number")
    print("To end the program, type stop")
    print("To view the stats of the pokemon, type getstat and then the name")
    print("(make sure to capitalize.). both number forms are accepted as well. i.e (005 or 5)")
    print("to see this message again, type help")
    print('')

print("Welcome! For commands, type help.")

def printdateam():
    if z > 100:
        print('Invalid Input')
    else:
        print(teamnamelist[z])
        print(str(autoteam[z][0].nm) + ' ' + str(autoteam[z][1].nm) + ' ' + str(autoteam[z][2].nm) + ' ' + str(autoteam[z][3].nm) + ' ' + str(autoteam[z][4].nm) + ' ' + str(autoteam[z][5].nm))

maketeams()
while True:
    printotherteam = 'printteam'
    ranteam = "randteam"
    battles = 'tournament'
    clearmyteam = "clearmyteam"
    helpcmd = "help"
    teamadd = "eamadd"
    b = "etstat"
    Null = "Null"
    stop = "Stop"
    printateam = "printmyteam"
    makeAteam = "makenewteams"
    addteam = "ddteam"
    battlething = 'battle team'
    a = input("")
    a = a.replace("stop", 'Stop')
    if(b in a):
        a = a.replace('Getstat', 'getstat')
        a = a.replace('Getstats', 'getstat')
        a = a.replace("getstats", '')
        a = a.replace(" ", '')
        a = a.replace("getstat", '')
        pokepicker()
    elif (stop in a):
        exit()        
    elif(printotherteam in a):
        a = a.replace('printteam', '')
        a = a.replace(' ', '')
        z = int(a)
        z = z-1
        printdateam()
    elif(ranteam in a):
        pickrandteam()
    elif(battlething in a):
        a = a.replace('battle team', '')
        a = a.replace(' ', '')
        v = int(a)
        v = v-1
        battleindv(userteam, autoteam[v], True)
    elif(battles in a):
        battleall(100, thebattlingteam, 1000)
    elif(helpcmd in a):
        helpmetext()
    elif clearmyteam in a:
        clearuserteam()
    elif makeAteam in a:
        maketeams()
        print("Done!")
    elif(addteam in a) or (teamadd in a):
        a = a.replace('teamadd', '')
        a = a.replace('teamadd', '')
        a = a.replace('Addteam', '')
        a = a.replace('addteam', '')
        a = a.replace(' ', '')
        userteamadder()   
    elif(printateam in a):
        if len(userteamnames) < 1:
            print("Team is empty!")
        else:
            printmyteam()
    else:
        print("Invalid Input")
        
        
        
        
        


