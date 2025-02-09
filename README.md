# RealTimeCatan
## Welcome to Real-time Catan!
This python script allows you to play Catan in real-time! Rather than players taking turns in a circle, 
all players can construct, trade, or buy development cards at anytime. A dice roll will be periodically 
generated (with the interval input by the user) to keep the game moving. When a 7 is rolled, a random 
player will be assigned to move and play the robber.
## Using the script
To run the script, run /src/app.py on a computer with python installed. The will open a command line prompt 
to input the number of players (3 or 4) and their names. You will then be prompted to input the time interval 
between dice rolls, in seconds (recommend to start with 30). The script will then countdown until the next roll 
is generated and print the roll, indefinitely. To stop the script, close the terminal or use Ctrl + C to interrupt 
execution.