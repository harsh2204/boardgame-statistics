from pprint import pprint
import json

def filter_dict(original):
    # refered from https://stackoverflow.com/a/33797147
    return {k: v for k, v in original.items() if v is not None}
    
def write_json(obj, filename):
    with open(f'{filename}.json', 'w') as fp:
        json.dump(obj, fp)

def get_cards():
    # Following code is ported from my old monopoly game written in Java
    # https://github.com/harsh2204/MonopolyJava
    # // ---------------------------------Java Port----------------------------------------
    chance =[]
    community = []
    # //CHANCE
    chance.append("Advance to Go (Collect $200) ")
    chance.append("Bank error in your favor – collect $75 ")
    chance.append("Insurance fees – Pay $50 ")
    chance.append("Get out of jail free – this card may be kept until needed, or sold ")
    chance.append("Holiday Fund matures - Receive $100")
    chance.append("It is your birthday Collect $10 from each player ")
    chance.append("Blue Jays opening night – collect $50 from every player for opening night seats ")
    chance.append("Income Tax refund – collect $20 ")
    chance.append("Life Insurance Matures – collect $100 ")
    chance.append("Pay Hospital Room Fees of $100 ")
    chance.append("Pay University Fees of $50 ")
    chance.append("Receive $25 Consultancy Fee ")
    chance.append("You are assessed for street winter damage – $40 per house, $115 per hotel ")
    chance.append("You have won second prize in a poutine eating contest– collect $10 ")
    chance.append("You inherit $100")
    chance.append("From sale of stock you get $50 ")
    # //COMMUNITY CHEST
    community.append("Advance to Go (Collect $200)")
    community.append("Advance to Windsor")
    community.append("Advance token to CN Tower")
    community.append("Advance token to CNR")
    community.append("Advance to St. John's – if you pass Go, collect $200")
    community.append("Bank pays you dividend of $50")
    community.append("Get out of Jail free – this card may be kept until needed, or traded/sold")
    community.append("Go back 3 spaces")
    community.append("Go directly to Jail – do not pass Go, do not collect $200")
    community.append("Make shingle repairs on all your property – for each house pay $25 – for each hotel $100")
    community.append("Pay poor tax of $15")
    community.append("Take a trip to Timmies – if you pass Go collect $200")
    community.append("Take a walk on the Niagara Falls – advance token to Niagara Falls")
    community.append("You have been elected chairman of the board – pay each player $50")
    community.append("You win a curling tournanment – collect $150")
    community.append("You have won a hockey game - collect $100")

    return {'chance':chance, 'community':community}

def get_properties():
    prop = []
    keys = {'propName', 'desc1', 'desc2', 'price', 'priceHouse',
        'rent1', 'rent2', 'rent3', 'rent4', 'rentH', 'buyable', 'type', 'color'}
    for _ in range(36):
        prop.append(dict([(key, None) for key in keys]))
    # Following code is ported from my old monopoly game written in Java
    # https://github.com/harsh2204/MonopolyJava
    # // ---------------------------------Java Port----------------------------------------
    prop[0]['propName'] = "Start"
    prop[0]['buyable'] = False
    prop[0]['type'] = "ST"

    prop[1]['propName'] = "Oriental Ave."
    prop[1]['price'] = 60
    prop[1]['rent1'] = 10
    prop[1]['rent2'] = 30
    prop[1]['rent3'] = 90
    prop[1]['rent4'] = 160
    prop[1]['rentH'] = 250
    prop[1]['priceHouse'] = 50

    prop[1]['buyable'] = True
    prop[1]['type'] = "N"

    prop[2]['propName'] = "Vermont Ave."
    prop[2]['price'] = 60
    prop[2]['rent1'] = 20
    prop[2]['rent2'] = 60
    prop[2]['rent3'] = 180
    prop[2]['rent4'] = 320
    prop[2]['rentH'] = 450
    prop[2]['priceHouse'] = 50

    prop[2]['buyable'] = True
    prop[2]['type'] = "N"


    prop[3]['propName'] = "Special 1"
    prop[3]['desc1'] = "Rent = 25x roll & +25 "
    prop[3]['desc2'] = "rent on all properties"
    prop[3]['price'] = 325

    prop[3]['buyable'] = True
    prop[3]['type'] = "STH"


    prop[4]['propName'] = "Connecticut Ave."
    prop[4]['price'] = 80
    prop[4]['rent1'] = 30
    prop[4]['rent2'] = 90
    prop[4]['rent3'] = 220
    prop[4]['rent4'] = 350
    prop[4]['rentH'] = 500
    prop[4]['priceHouse'] = 50

    prop[4]['buyable'] = True
    prop[4]['type'] = "N"

    prop[5]['propName'] = "Income Tax"
    prop[5]['buyable'] = False

    prop[5]['type'] = "IT"

    prop[6]['propName'] = "Chance"
    prop[6]['buyable'] = False

    prop[6]['type'] = "CH"



    prop[7]['propName'] = "St. Charles Place."
    prop[7]['price'] = 100
    prop[7]['rent1'] = 30
    prop[7]['rent2'] = 90
    prop[7]['rent3'] = 270
    prop[7]['rent4'] = 400
    prop[7]['rentH'] = 550
    prop[7]['priceHouse'] = 75

    prop[7]['buyable'] = True
    prop[7]['type'] = "N"

    prop[8]['propName'] = "States Ave."
    prop[8]['price'] = 120
    prop[8]['rent1'] = 40
    prop[8]['rent2'] = 100
    prop[8]['rent3'] = 300
    prop[8]['rent4'] = 450
    prop[8]['rentH'] = 600
    prop[8]['priceHouse'] = 75

    prop[8]['buyable'] = True
    prop[8]['type'] = "N"

    prop[9]['propName'] = "Jail"
    prop[9]['buyable'] = False

    prop[9]['type'] = "J"

    prop[10]['propName'] = "Virginia Ave."
    prop[10]['price'] = 120
    prop[10]['rent1'] = 40
    prop[10]['rent2'] = 100
    prop[10]['rent3'] = 260
    prop[10]['rent4'] = 420
    prop[10]['rentH'] = 580
    prop[10]['priceHouse'] = 75

    prop[10]['buyable'] = True
    prop[10]['type'] = "N"



    prop[11]['propName'] = "St. James Place."
    prop[11]['price'] = 140
    prop[11]['rent1'] = 50
    prop[11]['rent2'] = 150
    prop[11]['rent3'] = 450
    prop[11]['rent4'] = 625
    prop[11]['rentH'] = 700
    prop[11]['priceHouse'] = 100

    prop[11]['buyable'] = True
    prop[11]['type'] = "N"


    prop[12]['propName'] = "Special"
    prop[12]['desc1'] = "Rent = 25x roll, 50x roll "
    prop[12]['desc2'] = "if Avengers Base is owned"
    prop[12]['price'] = 375

    prop[12]['buyable'] = True
    prop[12]['type'] = "S1230"

    prop[13]['propName'] = "Tennesse Ave."
    prop[13]['price'] = 150
    prop[13]['rent1'] = 60
    prop[13]['rent2'] = 170
    prop[13]['rent3'] = 480
    prop[13]['rent4'] = 650
    prop[13]['rentH'] = 750
    prop[13]['priceHouse'] = 100

    prop[13]['buyable'] = True
    prop[13]['type'] = "N"

    prop[14]['propName'] = "Pennsylvania Ave."
    prop[14]['price'] = 180
    prop[14]['rent1'] = 80
    prop[14]['rent2'] = 180
    prop[14]['rent3'] = 500
    prop[14]['rent4'] = 680
    prop[14]['rentH'] = 900
    prop[14]['priceHouse'] = 100

    prop[14]['buyable'] = True
    prop[14]['type'] = "N"


    prop[15]['propName'] = "Kentucky Ave."
    prop[15]['desc1'] = "Rent = 25x roll, 50x roll "
    prop[15]['desc2'] = " if Arkhum Asylum is owned"
    prop[15]['price'] = 375

    prop[15]['buyable'] = True
    prop[15]['type'] = "S1533"

    prop[16]['buyable'] = False

    prop[16]['type'] = "CO"




    prop[17]['propName'] = "Indiana Ave."
    prop[17]['price'] = 200
    prop[17]['rent1'] = 100
    prop[17]['rent2'] = 200
    prop[17]['rent3'] = 520
    prop[17]['rent4'] = 700
    prop[17]['rentH'] = 910
    prop[17]['priceHouse'] = 150

    prop[17]['buyable'] = True
    prop[17]['type'] = "N"

    prop[18]['buyable'] = False

    prop[18]['type'] = "FP"

    prop[19]['propName'] = "Illinois Ave."
    prop[19]['price'] = 220
    prop[19]['rent1'] = 110
    prop[19]['rent2'] = 220
    prop[19]['rent3'] = 540
    prop[19]['rent4'] = 725
    prop[19]['rentH'] = 925
    prop[19]['priceHouse'] = 150

    prop[19]['buyable'] = True
    prop[19]['type'] = "N"

    prop[20]['propName'] = "Atlantic Ave."
    prop[20]['price'] = 220
    prop[20]['rent1'] = 110
    prop[20]['rent2'] = 220
    prop[20]['rent3'] = 540
    prop[20]['rent4'] = 725
    prop[20]['rentH'] = 925
    prop[20]['priceHouse'] = 150

    prop[20]['buyable'] = True
    prop[20]['type'] = "N"


    prop[21]['propName']="Special"
    prop[21]['desc1'] = "Rent = 25x roll & tax rebate"
    prop[21]['price'] = 325

    prop[21]['buyable'] = True
    prop[21]['type'] = "SRBC"


    prop[22]['propName'] = "Ventnor Ave."
    prop[22]['price'] = 250
    prop[22]['rent1'] = 125
    prop[22]['rent2'] = 250
    prop[22]['rent3'] = 550
    prop[22]['rent4'] = 750
    prop[22]['rentH'] = 950
    prop[22]['priceHouse'] = 150

    prop[22]['buyable'] = True
    prop[22]['type'] = "N"

    prop[23]['propName'] = "Blank"
    prop[23]['buyable'] = False

    prop[23]['type'] = "HT"

    prop[24]['buyable'] = False

    prop[24]['type'] = "CH"



    prop[25]['propName'] = "Marvin Gardens"
    prop[25]['price'] = 260
    prop[25]['rent1'] = 140
    prop[25]['rent2'] = 300
    prop[25]['rent3'] = 750
    prop[25]['rent4'] = 975
    prop[25]['rentH'] = 1000
    prop[25]['priceHouse'] = 200

    prop[25]['buyable'] = True
    prop[25]['type'] = "N"

    prop[26]['propName'] = "Pacific Ave."
    prop[26]['price'] = 290
    prop[26]['rent1'] = 150
    prop[26]['rent2'] = 350
    prop[26]['rent3'] = 800
    prop[26]['rent4'] = 1000
    prop[26]['rentH'] = 1100
    prop[26]['priceHouse'] = 200

    prop[26]['buyable'] = True
    prop[26]['type'] = "N"

    prop[27]['buyable'] = False

    prop[27]['type'] = "JK"


    prop[28]['propName'] = "North Carolina Ave."
    prop[28]['price'] = 290
    prop[28]['rent1'] = 150
    prop[28]['rent2'] = 350
    prop[28]['rent3'] = 800
    prop[28]['rent4'] = 1000
    prop[28]['rentH'] = 1100
    prop[28]['priceHouse'] = 200

    prop[28]['buyable'] = True
    prop[28]['type'] = "N"

    prop[29]['propName'] = "New York Ave."
    prop[29]['price'] = 325
    prop[29]['rent1'] = 170
    prop[29]['rent2'] = 400
    prop[29]['rent3'] = 850
    prop[29]['rent4'] = 1100
    prop[29]['rentH'] = 1200
    prop[29]['priceHouse'] = 200

    prop[29]['buyable'] = True
    prop[29]['type'] = "N"


    prop[30]['propName'] ="Special"  
    prop[30]['desc1'] = "Rent = 25x roll, 50x "
    prop[30]['desc2'] = "roll if S.H.I.E.L.D. Headquarters is owned"
    prop[30]['price'] = 375

    prop[30]['buyable'] = True
    prop[30]['type'] = "S1230"

    prop[31]['buyable'] = False

    prop[31]['type'] = "CO"


    prop[32]['propName'] = "New York Ave."
    prop[32]['price'] = 375
    prop[32]['rent1'] = 175
    prop[32]['rent2'] = 500
    prop[32]['rent3'] = 1100
    prop[32]['rent4'] = 1300
    prop[32]['rentH'] = 1500

    prop[32]['priceHouse'] = 300
    prop[32]['buyable'] = True
    prop[32]['type'] = "N"


    prop[33]['propName']="Special"
    prop[33]['desc1'] = "Rent = 25x roll, 50x roll "
    prop[33]['desc2'] = " if Watch Tower is owned"
    prop[33]['price'] = 375

    prop[33]['buyable'] = True
    prop[33]['type'] = "S1533"


    prop[34]['propName'] = "Park Place"
    prop[34]['price'] = 400
    prop[34]['rent1'] = 200
    prop[34]['rent2'] = 600
    prop[34]['rent3'] = 1400
    prop[34]['rent4'] = 1700
    prop[34]['rentH'] = 2000
    prop[34]['priceHouse'] = 300

    prop[34]['buyable'] = True
    prop[34]['type'] = "N"

    prop[35]['propName'] = "Boardwalk"
    prop[35]['price'] = 500
    prop[35]['rent1'] = 250
    prop[35]['rent2'] = 750
    prop[35]['rent3'] = 1500
    prop[35]['rent4'] = 1850
    prop[35]['rentH'] = 2100
    prop[35]['priceHouse'] = 300

    prop[35]['buyable'] = True
    prop[35]['type'] = "N"

    # Color definitions
    prop[1]['color'] = "Color.YELLOW"
    prop[2]['color'] = "Color.YELLOW"
    prop[3]['color'] = "Color.WHITE"
    prop[4]['color'] = "Color.YELLOW"
    prop[5]['color'] = "Color.GRAY"
    prop[6]['color'] = "Color.GRAY"
    prop[7]['color'] = "Color.BLUE"
    prop[8]['color'] = "Color.BLUE"
    prop[9]['color'] = "Color.BLACK"
    prop[10]['color'] = "Color.BLUE"
    prop[11]['color'] = "Color.PURPLE"
    prop[12]['color'] = "Color.WHITE"
    prop[13]['color'] = "Color.PURPLE"
    prop[14]['color'] = "Color.PURPLE"
    prop[15]['color'] = "Color.WHITE"
    prop[16]['color'] = "Color.GRAY"
    prop[17]['color'] = "Color.GREEN"
    prop[18]['color'] = "Color.GRAY"
    prop[19]['color'] = "Color.GREEN"
    prop[20]['color'] = "Color.GREEN"
    prop[21]['color'] = "Color.WHITE"
    prop[22]['color'] = "Color.GREEN"
    prop[23]['color'] = "Color.WHITE"
    prop[24]['color'] = "Color.GRAY"
    prop[25]['color'] = "Color.RED"
    prop[26]['color'] = "Color.RED"
    prop[27]['color'] = "Color.GRAY"
    prop[28]['color'] = "Color.RED"
    prop[29]['color'] = "Color.RED"
    prop[30]['color'] = "Color.WHITE"
    prop[31]['color'] = "Color.GRAY"
    prop[32]['color'] = "Color.ORANGE"
    prop[33]['color'] = "Color.WHITE"
    prop[34]['color'] = "Color.ORANGE"
    prop[35]['color'] = "Color.ORANGE"
    # // ---------------------------------End of Port----------------------------------------

    # Removing redundant keys
    for _prop in prop:
        fixed = filter_dict(_prop)
        _prop.clear()
        _prop.update(fixed)
    
    return prop

if __name__ == "__main__":
    prop = get_properties()
    cards = get_cards()
    board = {"board":{
        "properties": prop,
        "cards": cards
    }}
    write_json(board, "properties")
    # pprint(prop, indent=15)
