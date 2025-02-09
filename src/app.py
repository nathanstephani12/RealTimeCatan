def GetPlayerCount() -> int:
    num_players = -1
    while(num_players != 3 and num_players != 4):
        num_players = int(input('Input number of players (3 or 4):\n'))
    return num_players

def main():
    num_players = GetPlayerCount()
    players = []
    for i in range(num_players):
        player = input(f'Enter name of player {i + 1}: ')
        players.append(player)
    print('RealTimeCatan')
    

if __name__ == '__main__':
    main()