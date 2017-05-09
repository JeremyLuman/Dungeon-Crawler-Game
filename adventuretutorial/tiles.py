import items, enemies
#MapTile sets the parameters for the rooms in the game world 
class MapTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def intro_text(self):
        raise NotImplementedError()

    def modify_player(self, player):
        raise NotImplementedError()

class StartingRoom(MapTile):
    def intro_text(self):
        return "You find yourself if a cave with a flickering torch on the wall. You can make out four paths, each equally as dark and foreboding."

    def modify_player(self, player):
        #Room has no action on player
        pass

class LootRoom(MapTile):
    def __init__(self, x, y, item):
        self.item = item
        super().__init__(x, y)

    def add_loot(self, player):
        player.inventory.append(self.item)

    def modify_player(self, player):
        self.add_loot(player)

class EnemyRoom(MapTile):
    def __init__(self, x, y, enemy):
        self.enemy = enemy
        super().__init__(x, y)

    def modify_player(self, the_player):
        if self.enemy.is_alive():
        the_player.hp = the_player.hp - self.enemy.damage
            print("Enemy does {} damage. You have {} HP remaining.".format(self.enemy.damage, the_player.hp))

class EmptyCavePath(MapTile):
    def intro_text(self):
        return "Another unremarkable part of the cave. You must forge onwards."
    def modify_player(self, player):
        #Room has no action on player
        pass

class GiantSkeletonRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.GiantSkeleton())

    def intro_text(self):
        if self.enemy.is_alive():
            return "A giant skeleton jumps down from a coffin in front of you! His teeth rattle."
        else:
            return "The bones of the skeleton blast in all directions, clattering around for a few seconds, and all is still."

class FindDaggerRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Dagger())

    def intro_text(self):
        return "Your notice something shiny in the corner. It's a dagger! You pick it up. Semlls like bones."