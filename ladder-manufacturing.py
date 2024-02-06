import math, datetime, pytz

def start():
    global ladder_type
    global ladder_height
    global ladder_length
    global landing_space
    global handrails
    while True:
        temp = input('Ladder height (mm)?:')
        if temp == (''):
            temp = ('')
        else:
            ladder_type = temp[0]
        try:
            ladder_height = round(float(temp[1:]))
        except ValueError:
            print('Prefix number with f or p')
        else:
            if ladder_type.lower() == 'f' and ladder_height in range(500, 5501):
                break
            elif ladder_type.lower() == 'p' and ladder_height in range(500, 5501):
                break
            elif ladder_type.lower() == 'f' or ladder_type.lower() == 'p' and ladder_height not in range(500, 5501):
                print('Out of range (500mm - 5500mm)')
            elif ladder_type.lower() != 'f' or ladder_type.lower() != 'p':
                print('Prefix with f or p')
    while True:
        if ladder_height < 2000:
            break
        elif ladder_height >= 2000:
            handrails = input('Handrails obstructed? Y/N:')
            if handrails.lower() == 'y' or handrails.lower() == 'n':
                break
            elif handrails.lower() != 'y' or handrails.lower() != 'n':
                print('Enter Y/N')

    ladder_length = round(float(ladder_height / math.sin(math.radians(70))))
    landing_space = round(float(ladder_height / math.tan(math.radians(70))))

def ladder_details():
    tz = pytz.timezone('Pacific/Auckland')
    nz_time = datetime.datetime.now(tz).strftime('%d/%m/%Y %#I:%M%p')
    print('Timestamp:', nz_time)
    if ladder_type.lower() == 'f':
        print('Ladder type: Fixed ladder')
    elif ladder_type.lower() == 'p':
        print('Ladder type: Pivotal ladder')
    print('Ladder height:', round(float(ladder_height)))
    print('Ladder length:', round(float(ladder_length)))
    print('Landing space:', round(float(landing_space + 106)))
    print('Ladder angle: 70°')

def ladder_details_pivotal():
    print('Stored height:', round(float(ladder_length + 36)))

def manufacturing():
    print('Stringer:', round(float(ladder_length - 8.5)))
    if ladder_height < 2000:
        print('Handrails: Not required')
    elif ladder_height >= 2000 and handrails.lower() == 'y':
        print('Handrails (obstructed):', round(float(ladder_length - 957.75)))
    elif ladder_height >= 2000 and handrails.lower() == 'n':
        print('Handrails (unobstructed):', round(float(ladder_length - 957.75 + 1064.17)))

def manufacturing_pivotal():
    if ladder_height <= 1000:
        print('Sliding bar: 160')
    elif ladder_height <= 1500:
        print('Sliding bar: 200')
    elif ladder_height <= 2000:
        print('Sliding bar: 240')
    elif ladder_height <= 3000:
        print('Sliding bar: 300')
    elif ladder_height <= 4000:
        print('Sliding bar: 360')
    elif ladder_height <= 5000:
        print('Sliding bar: 420')
    elif ladder_height <= 6000:
        print('Sliding bar: 480')

def tread_spacing():
    x = 1
    while True:
        if round(float(ladder_length / x)) in range(212, 267):
            break
        elif x < 4 and round(float(ladder_length / x)) in range(200, 301):
            break
        x = x + 1
    y = ladder_length / x
    for i in range(x):
        line = str(round(float(i + 1))) + ') ' + str(round(float(y)))
        print(line)
        y += ladder_length / x

def main():
    print('-----------------------------')
    start()
    print('-----------------------------')
    if ladder_type.lower() == 'f':
        ladder_details()
        print('-----------------------------')
        manufacturing()
        print('-----------------------------')
        tread_spacing()

    elif ladder_type.lower() == 'p':
        ladder_details()
        ladder_details_pivotal()
        print('-----------------------------')
        manufacturing()
        manufacturing_pivotal()
        print('-----------------------------')
        tread_spacing()

main()
