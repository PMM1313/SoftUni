from project import Guild
from project import Player

player = Player("George", 50, 100)
player2 = Player("Pesho", 50, 100)
print(player2.add_skill("Shield Break", 20))
print(player.add_skill("Shield Break", 20))
print(player.add_skill("Shield Slam", 20))
print(player2.player_info())
print(player.player_info())

guild = Guild("UGT")

print(guild.assign_player(player))

print(guild.guild_info())
print(guild.kick_player("George"))
print(guild.guild_info())
print(player.player_info())
print(guild.guild_info())
