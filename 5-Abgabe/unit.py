pick_unit_sym = {
    'catrat':'kt',
    'ounce':'oz',
    'pound':'lb',
    'tonne':'t',
    'newton':'N'
    
}

#NOTE: Achtung jenachdem wo man nach schaut kann es unterschiedliche Angaben
#zu den umrechnungsfaktoren geben. Eine sehr vollsgändige Liste findet sich 
#unter https://www.smartconversion.com/unit_conversion/mass_unit_conversion_table.aspx
#Daher können die Ergebmisse die dieses Scritp liefert etwas von den Ihren
#Abweichen. Vorallem bei Karat, Pfund und Unze bei Bedarf kann die Variable
#die auf _factor endet mit den anderen werten überschrieben werden. Alle
#Werte rechnen auf Gramm um nicht Kilogramm
carat_factor = 2.591956E-1
carat_metric = 2E-1
pound_factor = 500
pound_av = 453.59237 
ounce_factor = 31.1034768
ounce_av = 28.349523125

# NOTE: Newton(s) entspricht 1/Ergbeschleuingung in kg bzw 1000/Ergbeschleuingung in g
#
# folglich ist 1 N = 1/9.80665 = 101.971621297793 Gramm

class Unit():
    # Standardlösung vpn mir. alles was darüberhinaus geht siehe Unit2
    # bitte grün markieren
    def __init__(self,value,unit=None):
        if unit is None:
            value = value.strip()
            startparse = 1 if len(value) > 2 and value[0] in '+-' else 0
            for end,digit in enumerate(value[startparse:],startparse):
                if digit in '0123456789.':
                    continue
                unit = value[end:].strip()
                value = float(value[:end])
                break
        if not unit:
            raise ValueError("unit must consist of at lease one character")
        # mg, g, kg, carat, ounce (oz), pound (lb), tonne (t), newton

        if unit != 'g':
            if unit not in ['mg','kg','carat','kt','ounce','oz','pound','lb','tonne','t','newton','N']:
                raise ValueError("unit must be one of ['mg','g','carat','ounce','oz','pound','lb','tonne','t','newton']")
        self.value = value
        self.unit = pick_unit_sym.get(unit,unit)

    def convert(self,to_unit):
        to_unit = pick_unit_sym.get(to_unit,to_unit)
        if to_unit == self.unit:
            return self
        if to_unit == 'mg':
            return Unit(self.convert_2_g() * 1000,to_unit)
        if to_unit == 'g':
            return Unit(self.convert_2_g() ,to_unit)
        if to_unit == 'kg':
            return Unit(self.convert_2_g()/1000,to_unit)
        if to_unit == 'kt':
            return Unit(self.convert_2_g() / carat_factor,to_unit)
        if to_unit == 'oz':
            return Unit(self.convert_2_g() / ounce_factor,to_unit)
        if to_unit == 'lb':
            return Unit(self.convert_2_g() /pound_factor,to_unit)
        if to_unit == 't':
            return Unit(self.convert_2_g() / 1e6,to_unit)
        if to_unit != 'N':
            raise ValueError("unit must be one of ['mg','g','carat','ounce','oz','pound','lb','tonne','t','newton','N']")
        return Unit(self.convert_2_g() / 101.971621,to_unit)

    def convert_2_g(self):
        #    if unit not in ['mg','g','carat','ounce','oz','pound','lb','tonne','t','newton']:
        if self.unit == 'g':
            return self.value
        if self.unit == 'mg':
            return self.value / 1000
        if self.unit == 'kg':
            return self.value * 1000
        if self.unit == 'kt':
            return self.value * carat_factor
        if self.unit == 'oz':
            return self.value * ounce_factor
        if self.unit == 'lb':
            return self.value * pound_factor
        if self.unit == 't':
            return self.value * 1e6
        # newton 101.971621
        return self.value * 101.971621

    def __add__(self,other):
        return Unit(self.value + other.convert(self.unit).value,self.unit)

    def __str__(self):
       return "{:.6} {}".format(self.value,self.unit)

class Unit2(object):
    # Auf Basis von Beispielen aus den Hausübungen, 
    _g_conversion_factors = {
         'g': 1,
        'mg': 0.001,
        'kg': 1000,
        #'kt': carat_factor,
        'kt': carat_metric,#carat_factor,
        #'oz': ounce_factor,#31.1034768 ,
        'oz': ounce_av,#ounce_factor,#31.1034768 ,
        #'lb': pound_factor,
        'lb': pound_av,#pound_factor,
        't': 1e6,
        'N': 101.971621
    }
    def __init__(self,value,unit=None):
        if unit is None:
            value = value.strip()
            startparse = 1 if len(value) > 2 and value[0] in '+-' else 0
            for end,digit in enumerate(value[startparse:],startparse):
                if digit in '0123456789.':
                    continue
                unit = value[end:].strip()
                value = float(value[:end])
                break
        if not unit:
            raise ValueError("unit must consist of at lease one character")
        unit = pick_unit_sym.get(unit,unit)
        if Unit2._g_conversion_factors.get(unit,None) is None:
            raise ValueError("unit must be one of [{},{}]".format(", ".join(Unit2._g_conversion_factors.keys()),", ".join(pick_unit_sym.keys())))
        self.value = value
        self.unit = unit

    def convert(self,to_unit):
        unit = pick_unit_sym.get(to_unit,to_unit)
        if to_unit == self.unit:
            return self
        conversionfactor = Unit2._g_conversion_factors.get(to_unit,None)
        if conversionfactor is None:
            raise ValueError("unit must be one of [{},{}]".format(", ".join(Unit2._g_conversion_factors.keys()),", ".join(pick_unit_sym.keys())))
        convertedvalue = self.value
        if self.unit != 'g':
            convertedvalue = self.value * Unit2._g_conversion_factors[self.unit]
        if to_unit != 'g':
            convertedvalue /= conversionfactor
        return Unit2(convertedvalue,to_unit)

    def __add__(self,other):
        return Unit2(self.value + other.convert(self.unit).value,self.unit)

    def __str__(self):
       return "{:.6f} {}".format(self.value,self.unit)

def main():
    unitvalue1 = None
    while not unitvalue1:
        unitvalue1 = input("Geben sie das erste Gewicht incl. Einheit ein: ")
        try:
            unitvalue1 = Unit2(unitvalue1)
        except ValueError as msg:
            print(msg)
            unitvalue1 = None
    unitvalue2 = None
    while not unitvalue2:
        unitvalue2 = input("Geben sie das zweite Gewicht incl. Einheit ein: ")
        try:
            unitvalue2 = Unit2(unitvalue2)
        except ValueError as msg:
            print(msg)
            unitvalue2 = None
    result = unitvalue1 + unitvalue2
    backmap = {val:key for key,val in pick_unit_sym.items()}
    resultstring = "{} + {} = {} ({})".format(unitvalue1,unitvalue2,result,backmap.get(result.unit,result.unit))
    convertformat = ( " " * resultstring.index('=') ) + "= {} ({})" 
    print(resultstring)
    for convertto in ['mg','g','kg','kt','oz','lb','t','N']:
        if convertto == result.unit:
            continue
        print(convertformat.format(result.convert(convertto),backmap.get(convertto,convertto)))

if __name__ == '__main__':
    main()

    
                
