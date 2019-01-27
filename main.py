# Made by Kit Matthewson, Version 3.3

from time import sleep

try:
    from wikipedia import summary as wikiSummary
    
    inp = input('Type [Yes] if you would like to enable Wikipedia\n>>> ').upper()

    if (inp == 'YES'):
        wikipedia = True
        print('Wikipedia Enabled\n')
    else:
        wikipedia = False
        print('Wikipedia Disabled\n')
except:
    print('Wikipedia Module Not Found\n')
    wikipedia = False

print('Atom Calculator\nMade by Kit Matthewson\n')

elements = (
    'Hydrogen', 'Helium', 'Lithium', 'Beryllium', 'Boron',
    'Carbon', 'Nitrogen', 'Oxygen', 'Fluorine', 'Neon', 'Sodium',
    'Magnesium', 'Aluminum', 'Silicon', 'Phosphorus', 'Sulfur',
    'Chlorine', 'Argon', 'Potassium', 'Calcium', 'Scandium',
    'Titanium', 'Vanadium', 'Chromium', 'Manganese', 'Iron',
    'Cobalt', 'Nickel', 'Copper', 'Zinc', 'Gallium', 'Germanium',
    'Arsenic', 'Selenium', 'Bromine', 'Krypton', 'Rubidium',
    'Strontium', 'Yttrium', 'Zirconium', 'Niobium', 'Molybdenum',
    'Technetium', 'Ruthenium', 'Rhodium', 'Palladium', 'Silver',
    'Cadmium', 'Indium', 'Tin', 'Antimony', 'Tellurium', 'Iodine',
    'Xenon', 'Cesium', 'Barium', 'Lanthanum', 'Cerium',
    'Praseodymium', 'Neodymium', 'Promethium', 'Samarium',
    'Europium', 'Gadolinium', 'Terbium', 'Dysprosium', 'Holmium',
    'Erbium', 'Thulium', 'Ytterbium', 'Lutetium', 'Hafnium',
    'Tantalum', 'Tungsten', 'Rhenium', 'Osmium', 'Iridium',
    'Platinum', 'Gold', 'Mercury', 'Thallium', 'Lead', 'Bismuth',
    'Polonium', 'Astatine', 'Radon', 'Francium', 'Radium',
    'Actinium', 'Thorium', 'Protactinium', 'Uranium', 'Neptunium',
    'Plutonium', 'Americium', 'Curium', 'Berkelium', 'Californium',
    'Einsteinium', 'Fermium', 'Mendelevium', 'Nobelium',
    'Lawrencium', 'Rutherfordium', 'Dubnium', 'Seaborgium',
    'Bohrium', 'Hassium', 'Meitnerium', 'Darmstadtium',
    'Roentgenium', 'Copernicium', 'Nihonium', 'Flerovium',
    'Moscovium', 'Livermorium', 'Tennessine', 'Oganesson'
)

symbols = (
    'H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne',
    'Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar', 'K',
    'Ca', 'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni',
    'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr', 'Rb',
    'Sr', 'Y', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd',
    'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te', 'I', 'Xe', 'Cs',
    'Ba', 'La', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd',
    'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu', 'Hf', 'Ta',
    'W', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg', 'Tl', 'Pb',
    'Bi', 'Po', 'At', 'Rn', 'Fr', 'Ra', 'Ac', 'Th', 'Pa',
    'U', 'Np', 'Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm',
    'Md', 'No', 'Lr', 'Rf', 'Db', 'Sg', 'Bh', 'Hs', 'Mt',
    'Ds', 'Rg', 'Cn', 'Nh', 'Fl', 'Mc', 'Lv', 'Ts', 
    'Og'
)

massList = (
    '1', '4', '7', '9', '11', '12', '14', '16', '19', '20',
    '23', '24', '27', '28', '31', '32', '35', '40', '39',
    '40', '45', '48', '51', '52', '55', '56', '59', '59',
    '64', '65', '70', '73', '75', '79', '80', '84', '85',
    '88', '89', '91', '93', '96', '98', '101', '103', '106',
    '108', '112', '115', '119', '122', '128', '127', '131',
    '133', '137', '139', '140', '141', '144', '145', '150',
    '152', '157', '159', '163', '165', '167', '169', '173',
    '175', '178', '181', '184', '186', '190', '192', '195',
    '197', '201', '204', '207', '209', '209', '210', '222',
    '223', '226', '227', '232', '231', '238', '237', '244',
    '243', '247', '247', '251', '252', '257', '258', '259',
    '262', '261', '262', '266', '264', '277', '268', '271',
    '272', '285', '286', '289', '289', '293', '294', '294'
)

def electronShells(Electrons):
    'Returns positions of Electrons in Shells as list'

    Shells = []

    # Shell 1
    if (Electrons <= 2):
        Shells.append(Electrons)

    # Shell 2
    elif (Electrons > 2 and Electrons <= 10):
        Shells.append(2)
        Shells.append(Electrons - 2)

    # Shell 3
    elif (Electrons > 10 and Electrons <= 28):
        Shells.append(2)
        Shells.append(8)
        Shells.append(Electrons - 10)

    # Shell 4
    elif (Electrons > 28 and Electrons <= 60):
        Shells.append(2)
        Shells.append(8)
        Shells.append(18)
        Shells.append(Electrons - 28)

    # Shell 5
    elif (Electrons > 60 and Electrons <= 110):
        Shells.append(2)
        Shells.append(8)
        Shells.append(18)
        Shells.append(32)
        Shells.append(Electrons - 60)

    # Shell 6
    elif (Electrons > 110):
        Shells.append(2)
        Shells.append(8)
        Shells.append(18)
        Shells.append(32)
        Shells.append(50)
        Shells.append(Electrons - 110)

    # If Helium
    else:
        Shells.append(1)

    return Shells

class element:

    def __init__(self, name):

        self.atomicNumber = elements.index(name) + 1
        self.atomicMass = massList[self.atomicNumber - 1]

        self.name = name
        self.symbol = symbols[self.atomicNumber - 1]

        self.neutrons = int(self.atomicMass) - int(self.atomicNumber)
        self.protons = int(self.atomicNumber)
        self.electrons = self.atomicNumber

        self.shells = electronShells(self.electrons)

        if (wikipedia == True):
            self.elementInfo = wikiSummary(self.name)

    def printAtom(self):

        print('\n-----  %s, %s, %s -----' %(self.name, self.symbol, self.atomicNumber))
        print('\nAtomic Mass: %s' %(self.atomicMass))
        print('Atomic Number: %s' %(self.atomicNumber))
        print('\nNucleus:')
        print('  Neutrons: %s' %(self.neutrons))
        print('  Protons: %s' %(self.protons))
        print('\nElectrons: %s' %(self.electrons))

        # Prints the Shells
        
        Empty = abs(len(electronShells(self.electrons)) - 6)
        ShellNames = ['K', 'L', 'M', 'N', 'O', 'P']
        
        for i in range(len(electronShells(self.electrons))):
            print('  Shell %s (%s): %s Electrons' %(str(i + 1), ShellNames[i], str(self.shells[i])))
            
        for i in range(Empty):
            print('  Shell %s (%s): 0 Electrons (Empty)' %(str(len(electronShells(self.electrons)) + i + 1), ShellNames[len(electronShells(self.electrons)) + i]))

        # Prints Element Information
        if (wikipedia == True):
            print('\nInformation:\n%s\nSource: Wikipedia' %(self.elementInfo))

        # Adds the end line
        length = 14 + len(self.name) + len(self.symbol)
        x = '-'
        for i in range(length - 1):
            x = x + '-'
        print('\n%s\n' %(x))


def nameSearch():
    inp = input('Enter Element name or Symbol\n>>> ').title()

    try:
        element(inp).printAtom()
    except ValueError:
        try:
            element(elements[symbols.index(inp)]).printAtom()
        except ValueError:
            print('That Element could not be found. Try again.\n')
            nameSearch()
    menu()

def numberSearch():  
    inp = input('Enter Atomic Number (Protons)\n>>> ')
    try:
        element(elements[int(inp) - 1]).printAtom()
        menu()
    except ValueError:
        print('That Element could not be found. Try again.\n')
        numberSearch()

def listAll():
    for i in range(len(elements) + 1):
        element(elements[i]).printAtom()
        sleep(1)
    menu()

def menu():
    if (wikipedia == False):
        inp = input('Do you want to search by [Name], [Number] or list [All] Elements?\n>>> ').upper()
    else:
        inp = input('Do you want to search by [Name] or [Number]?\n>>> ').upper()
    if (inp == 'NAME'):
        print('\nSearching by Name\n')
        nameSearch()
    elif (inp == 'NUMBER'):
        print('\nSearching by Atomic Mass and Atomic Number\n')
        numberSearch()
    elif (inp == 'ALL' and wikipedia == False):
        print('Listing All Elements\n')
        listAll()
    else:
        print('That command was not recognised. Type one of the words in square brackets.\n')
        menu()

menu()
