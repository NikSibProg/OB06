import random

class Hero:
    def __init__(self, name, health=100, attack_power=20):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other):
        print(f"{self.name} атакует {other.name} и наносит {self.attack_power} урона!")
        other.health -= self.attack_power
        if other.health < 0:
            other.health = 0
        print(f"У {other.name} осталось {other.health} здоровья.\n")

    def is_alive(self):
        return self.health > 0

class Game:
    def __init__(self, player, computer):
        self.player = player
        self.computer = computer

    def start(self):
        print("Начинаем битву героев!")
        while self.player.is_alive() and self.computer.is_alive():
            # Ход игрока
            self.player.attack(self.computer)
            if not self.computer.is_alive():
                print(f"{self.player.name} победил!")
                break

            # Ход компьютера
            self.computer.attack(self.player)
            if not self.player.is_alive():
                print(f"{self.computer.name} победил!")
                break

# Пример запуска игры
player_hero = Hero(name="Игрок")
computer_hero = Hero(name="Компьютер")

game = Game(player=player_hero, computer=computer_hero)
game.start()
