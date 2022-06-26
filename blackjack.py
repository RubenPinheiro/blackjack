import blackjack_art
import random

print(blackjack_art.logo)

def blackjack():

    def drawn():
        hand = [cards[random.randint(0, 12)], cards[random.randint(0, 12)]]
        
        return hand

    def drawn_another_card(player_hand):
        player_hand = player_hand + [(cards[random.randint(0, 12)])]
        
        return player_hand
    
    def ask_drawn(player_hand, player_count):
        player_count = count21(ace_swap(player_hand))
        if player_count > 21:
            another = 'n'
            return another
        else:
            another = input('Do you want to drawn another card? Type "y" or "n": ')
            return another
        
    def count21(hand):
        count = 0
        for i in range(len(hand)):
            count += hand[i]
        
        return count
    
    def dealer_vs_player(cpu_hand, cpu_count, player_count):
        while cpu_count <= player_count and cpu_count != 21:
            cpu_hand = cpu_hand + [(cards[random.randint(0, 12)])]
            cpu_hand = ace_swap(cpu_hand)
            cpu_count = count21(cpu_hand)

            if cpu_count < player_count and cpu_count != 21:
                count21(cpu_hand)
            elif cpu_count > 21:
                return (f'Dealer has drawn {cpu_hand}. You win!')
            elif cpu_count == player_count:
                return (f'Dealer has drawn {cpu_hand}. You drawn!')
            elif cpu_count > player_count:
                return (f'Dealer has drawn {cpu_hand}. You lose!')
            else:
                return (f'Dealer has drawn {cpu_hand}. You win!')
        else:
            return (f'Dealer has drawn {cpu_hand}. You lose!')
    
    def insta_win(player_count):
        if player_count == 21:
            return (f'You got a 21! You win!')
    
    def ace_swap(hand):
        count = count21(hand)
        for i in range(len(hand)):
            if count > 21 and hand[i] == 11:
                hand[i]= 1
            count = count21(hand)
        return hand
            
    should_continue = True
    another = ""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    #cards = [1, 11, 3, 11, 5, 11, 1, 11, 3, 11, 5, 11, 1]

    while should_continue:
        begin = input('Do you want to play a game of blackjack? Type "y" or "n": ')
        
        cpu_hand = ace_swap(drawn())
        player_hand = ace_swap(drawn())
        
        print(f'Dealer has drawn [{cpu_hand[0]},  XX]')
        print(f'You have drawn {player_hand}')
        player_count = count21(player_hand)
        cpu_count = count21(cpu_hand)
        
        #INSTA WIN
        if player_count == 21:
            print(insta_win(player_count))
            blackjack()
        
        while ask_drawn(player_hand, player_count) == 'y':
            player_hand = ace_swap(drawn_another_card(player_hand))        
            player_count = count21(player_hand)
            
            if player_count > 21:
                print(f'You have drawn {player_hand}. You lose!')
                blackjack()

            print(f'You have drawn {player_hand}')
            insta_win(player_count)
            
            
        else:
            print("")
            print(dealer_vs_player(cpu_hand, cpu_count, player_count))
            print("")
    else:
        should_continue = False
        blackjack()
blackjack()