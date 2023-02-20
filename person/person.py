class Person:
    def __init__(self, name, race, level, xp, next_level, max_hp, hp, stamina, magicka, damage, magickal_damage, armor_rating, weapon, armor, spell, magic_resist) -> None:
        self.name = name
        self.race = race
        self.level = level
        self.xp = xp
        self.next_level = next_level
        self.max_hp = max_hp
        self.hp = hp
        self.stamina = stamina
        self.magicka = magicka
        self.damage = damage
        self.magickal_damage = magickal_damage
        self.armor_rating = armor_rating
        self.weapon = weapon
        self.armor = armor
        self.spell = spell
        self.magic_resist = magic_resist
        
    def calc_damage(self) -> int:
        total_damage = self.damage + self.weapon
        return total_damage
    
    def calc_magickal_damage(self) -> int:
        total_damage = self.magickal_damage + self.spell
        return total_damage
    
    def took_damage(self, damage) -> None:
        calculated_damage = damage * 4 - self.armor_rating * 2
        self.hp - calculated_damage
        if self.hp <= 0:
            self.death()

    def took_magickal_damage(self, magickal_damage) -> None:
        calculated_damage = magickal_damage * 4 - self.magic_resist * 2
        self.hp - calculated_damage
        if self.hp <= 0:
            self.death()

    def death(self) -> None:
        print("You died")

    def gain_experience(self, xp_gained) -> None:
        self.xp += xp_gained
        if self.xp >= self.next_level:
            excessive = self.xp - self.next_level
            self.level_up()
            self.xp = excessive
            self.next_level += 100

    def level_up(self) -> None:
        self.level =+ 1