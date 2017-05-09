class Enemy: 
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def is_alive(self):
        return self.hp > 0

class Orc(Enemy):
    def __init__(self):
        super().__init__(name="Orc Soldier", hp=12, damage=3)

class GiantSekelton(Enemy):
    def __init__(self):
        super().__init__(name="Giant Skeleton", hp=10, damage=2)

class Ogre(Enemy):
    def __init__(self):
        super().__init__(name="Ogre", hp=30, damage=15)