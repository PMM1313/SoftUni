from project import Player

class Guild:
    def __init__(self, name):
        self.name = name
        self.players = []

    def assign_player(self, player: Player):
        if player.guild == "Unaffiliated":
            self.players.append(player)
            player.guild = self.name
            return f"Welcome player {player.name} to the guild {self.name}"

        if player.guild == self.name:
            return f"Player {player.name} is already in the guild."

        if player.guild != "Unaffiliated" and player.guild != self.name:
            return f"Player {player.name} is in another guild."

    def kick_player(self, player: str):
        p = next((p for p in self.players if p.name == player), None)
        if p:
            p.guild = "Unaffiliated"
            self.players.remove(p)
            return f"Player {player} has been removed from the guild."
        return f"Player {player} is not in the guild."

    def guild_info(self):
        return f"Guild: {self.name}\n" + "\n".join(player.player_info() for player in self.players)
