class PuntPlay:
    def __init__(self, start_time, duracion, end_time, game_id, teams, yards, qtr, date, time):
        self.start_time = start_time
        self.duracion = duracion
        self.end_time = end_time
        self.game_id = game_id
        self.teams = teams
        self.yards = yards
        self.qtr = qtr
        self.date = date
        self.time = time

    def __str__(self):
        return f"{self.start_time};{self.duracion};{self.end_time};{self.game_id};{self.teams};{self.yards};{self.qtr};{self.date};{self.time}"
