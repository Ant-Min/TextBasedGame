# Anthony Minunni

print('Welcome to the game!')
print('An alien has invaded your spaceship and killed all your crew members.')
print('Go from room to room and collect all 6 items before escaping in the escape pod.')
print('If you run into the alien before collecting all items, GAME OVER.')
print('Commands: go North, go South, go East, go West, get item')
print('------------------------------')

def main():

    # dictionary of rooms in the game
    rooms = {
        'the Bridge': {'North': 'the Lab', 'item': 'none'},
        'the Lab': {'North': 'Communications', 'South': 'the Bridge', 'East': 'Medical', 'West': 'the Kitchen',
                    'item': 'Data Drive'},
        'Communications': {'South': 'the Lab', 'item': 'Radio'},
        'the Kitchen': {'North': 'Maintenance', 'East': 'the Lab', 'item': 'Food Ration'},
        'Maintenance': {'South': 'the Kitchen', 'item': 'Toolbox'},
        'Medical': {'North': 'the Escape Pod', 'South': 'the Quarters', 'West': 'the Lab', 'item': 'Cattle Prod'},
        'the Quarters': {'North': 'Medical', 'item': 'Spacesuit'},
        'the Escape Pod': {'South': 'Medical', 'item': 'Alien'}  # the enemy; cannot be collected
    }

    # starts the player in the main room
    currentRoom = 'the Bridge'
    inventory = []

    run = True

    while run:
        place = rooms[currentRoom]  # This accesses the nested dictionary associated with currentRoom
        getter = place['item']  # reads item of the room
        print('You are in ' + currentRoom + '.')
        print('Item in room: ' + getter)
        print('Inventory:', inventory)
        if getter == 'Alien' and len(inventory) != 6:
            print('It\'s the alien! You don\'t have all the items you need to make your escape. '
                  'You end up like the rest of your crew. GAME OVER')
            print('Thank you for playing. Try again if you\'re feeling brave.')
            break  # break instead of setting run to false because the code would ask for the next move before exiting
        if getter == 'Alien' and len(inventory) == 6:
            print('The alien! It\'s in the escape pod! Good thing you have everything. '
                  'You defend yourself against the alien and successfully escape. YOU WIN!')
            print('Thanks for playing!')
            break  # break instead of setting run to false because the code would ask for the next move before exiting

        choice = input('Enter your move\n')
        if choice != 'go North' and choice != 'go South' and choice != 'go East' and choice != 'go West' \
                and choice != 'get item':
            print('Invalid move')
        else:
            sep = choice.split(' ')
            direction = sep[1]
            if direction == 'item' and getter != 'none':
                inventory.append(getter)
                place['item'] = 'none'
                print('Item picked up')
            elif direction == 'item' and getter == 'none':
                print('No item in room')
            else:
                validity = 0  # This is to determine the player's update properly about their choice of direction
                for i in place.keys():
                    if direction == i:
                        currentRoom = place[i]
                        validity = 1  # if player entered a valid direction, validity reflects
                                      # this for if statement below
                if validity == 0:
                    print('Not a valid direction')
        print('------------------------------')

if __name__ == "__main__":
    main()
