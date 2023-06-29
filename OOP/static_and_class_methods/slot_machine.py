import random

class SlotMachine:
    def __init__(self):
        self.icons = ['🍒', '🍊', '🍋', '🍉', '🍇', '🍓']
        self.bet = 0
        self.balance = 0

    def play(self):
        # Check if player has enough money to make a bet
        if self.balance <= 0:
            print("Sorry, you don't have enough money to play.")
            return

        while True:
            try:
                self.bet = int(input("Please enter your bet: "))
                if self.bet <= 0 or self.bet > self.balance:
                    raise ValueError
                break
            except ValueError:
                print(f"Invalid bet. Please enter a number between 1 and {self.balance}")
                return

        # Spin the reels
        reels = [random.choice(self.icons) for i in range(3)]
        print()
        print(" ".join(reels))

        # Calculate winnings
        if reels[0] == reels[1] == reels[2]:
            winnings = self.bet * 10
            print(f"JACKPOT!!! You won {winnings} coins!")
        elif reels[0] == reels[1] or reels[1] == reels[2] or reels[0] == reels[2]:
            winnings = self.bet * 2
            print(f"You won {winnings} coins!")
        else:
            winnings = 0
            print("Sorry, you didn't win this time.")

        # Update balance
        self.balance += winnings - self.bet
        print(f"Your balance: {self.balance}")

    def add_money(self, amount):
        self.balance += amount
        print(f"Added {amount} coins to your balance. The new balance is {self.balance}")

    def remove_money(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Removed {amount} coins from your balance. The new balance is {self.balance}")
        else:
            print("Sorry, you don't have enough money.")


# Create instance of SlotMachine class
machine = SlotMachine()
print()
print("----- Welcome to Meden Rudnik Casino -----")
print()
money_amount = int(input("Please add some money: "))
machine.add_money(money_amount)

while machine.balance > 0:
    machine.play()

