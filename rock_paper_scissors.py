import random
from prettytable import PrettyTable
import os
#Requires the environment variable OPPONENT to be set to sassy, kind or yoda
#accepts events in the form of event = {'round1':'rock', 'round2':'paper', 'round3':'scissors'}


class hand:  
    def __init__(self):
        rock_paper_scissors_options = ['rock','paper','scissors']
        hand = random.choice(rock_paper_scissors_options)
        self.hand = hand

class rps_bot:
    def __init__(self):
        round1 = hand()
        round2 = hand()
        round3 = hand()
        self.round1 = round1.hand
        self.round2 = round2.hand
        self.round3 = round3.hand

class personality:
    def __init__(self,personality):
        self.personality = personality
        if personality == 'sassy':
            self.player_win_sayings = ['...lucky','congrats you beat 3 lines of code','it\'s not my fault i\'m not programmed to win']
            self.player_loss_sayings = ['it only took 3 lines of code to beat you!','i\'m not even programmed to win and i beat you!','better luck next time...LOSER!']
            self.draw_sayings = ['you still didn\'t beat me','I lose, you lose, we all lose']
        if personality == 'kind':
            self.player_win_sayings = ['Well Played!','Do you give lessons?.... i just choose randomly','Nice!']
            self.player_loss_sayings = ['Better luck next time friend!','You can\'t win them all!','You\'ll win next time, im sure of it!']
            self.draw_sayings = ['we\'re both winners!','better then losing!']
        if personality == 'yoda':
            self.player_win_sayings = ['Judge me by my size, do you?','To answer power with power, the Jedi way this is not','Difficult to see. Always in motion is the future…']
            self.player_loss_sayings = ['The greatest teacher, failure is','You fail because you don’t believe.','If no mistake have you made, yet losing you are… a different game you should play.']
            self.draw_sayings = ['Patience you must have','A Jedi uses the Force for knowledge and defense, never for attack']


def rps_logic(bot_hand,player_hand):
    if bot_hand == 'rock':
        if player_hand == 'paper':
            winner = 'Player'
        if player_hand == 'scissors':
            winner = 'Lambda'
        if player_hand == 'rock':
            winner = 'Draw'
    if bot_hand == 'paper':
        if player_hand == 'scissors':
            winner = 'Player'
        if player_hand == 'rock':
            winner = 'Lambda'
        if player_hand == 'paper':
            winner = 'Draw'
    if bot_hand == 'scissors':
        if player_hand == 'rock':
            winner = 'Player'
        if player_hand == 'paper':
            winner = 'Lambda'
        if player_hand == 'scissors':
            winner = 'Draw'
    return winner

def bot_reply(winner):
    opponent = os.getenv("OPPONENT")
    bot_personality = personality(opponent)
    if winner == 'Lambda':
        return bot_personality.player_loss_sayings
    if winner == 'Player':
        return bot_personality.player_win_sayings
    if winner == 'Draw':
        return bot_personality.draw_sayings


def play(event):
    #setup results table
    Round_Results_Table= PrettyTable(['ROUND','PLAYER-HAND','LAMBDA-HAND','WINNER'])
    win_tally = {'Player':0,'Lambda':0,'Draw':0}
    #setup bot
    bot = rps_bot()
    opponent = os.getenv("OPPONENT")
    #round1
    play_round1 = rps_logic(bot_hand=bot.round1,player_hand=event['round1'])
    Round_Results_Table.add_row(['1',event['round1'],bot.round1,play_round1])
    win_tally[play_round1] += 1
    #round2
    play_round2 = rps_logic(bot_hand=bot.round2,player_hand=event['round2'])
    Round_Results_Table.add_row(['2',event['round2'],bot.round2,play_round2])
    win_tally[play_round2] += 1
    #round3
    play_round3 = rps_logic(bot_hand=bot.round3,player_hand=event['round3'])
    Round_Results_Table.add_row(['3',event['round3'],bot.round3,play_round3])
    win_tally[play_round3] += 1
    #determine winner
    if win_tally['Player'] > win_tally['Lambda']:
        winner = 'Player'
    if win_tally['Player'] < win_tally['Lambda']:
        winner = 'Lambda'
    if win_tally['Player'] == win_tally['Lambda']:
        winner = 'Draw'
    bot_chat = bot_reply(winner)
    bot_chat_selection = random.choice(bot_chat)
    #Print Results Table
    print ('The Winner is: ', winner)
    print (Round_Results_Table)
    print ('Lambda bot ('+ opponent + '): ', bot_chat_selection)

def lambda_handler(event,context):
    play(event)

