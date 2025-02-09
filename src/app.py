import random
import time

def GetPlayerCount() -> int:
    num_players = -1
    while(num_players != 3 and num_players != 4):
        num_players = int(input('Input number of players (3 or 4): '))
    return num_players

def GetPlayers(a_num_players):
    players = []
    for i in range(a_num_players):
        player = input(f'Enter name of player {i + 1}: ')
        players.append(player)
    return players

def GetCountdownInterval() -> int:
    interval = -1
    while(interval <= 0):
        interval = int(input('Enter countdown interval in seconds: '))
    return interval

def Roll() -> int:
    return random.randint(1, 6) + random.randint(1, 6)
    
def Countdown(a_interval):
    while a_interval:
        print(f'{a_interval}')
        time.sleep(1)
        a_interval -= 1
    print(f'Next roll: {Roll()}')


def main():
    num_players = GetPlayerCount()
    players = GetPlayers(num_players)
    countdown_interval = GetCountdownInterval()
    Countdown(countdown_interval)
    print('RealTimeCatan')
    

if __name__ == '__main__':
    main()