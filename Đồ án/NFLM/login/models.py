from django.db import models

class User(models.Model):
    userid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    priority = models.PositiveIntegerField()
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    dob = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.username, self.password, self.priority
    
class Position(models.Model):
    positionid = models.AutoField(primary_key=True)
    positionname = models.CharField(max_length=20)

    def __str__(self):
        return self.positionname

class Team(models.Model):
    teamid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    sponsor = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name, self.country, self.sponsor

class Team_Stat(models.Model):
    teamstatid = models.AutoField(primary_key=True)
    standing = models.PositiveIntegerField()
    goals = models.PositiveIntegerField()
    goalsconceded = models.PositiveIntegerField()
    wins = models.PositiveIntegerField()
    loses = models.PositiveIntegerField()
    team = models.OneToOneField(Team, on_delete=models.CASCADE, related_name='team_stat')

    def __str__(self):
        return self.standing, self.goals, self.goalsconceded, self.wins, self.loses

class Coach(models.Model):
    coachid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    nationality = models.CharField(max_length=255)
    phone = models.CharField(max_length=10)
    email = models.EmailField()
    dob = models.DateField(auto_now_add=True)
    team = models.OneToOneField(Team, on_delete=models.CASCADE, related_name='coach')

    def __str__(self):
        return self.name, self.nationality, self.team, self.email

class Player(models.Model):
    playerid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    nationality = models.CharField(max_length=255)
    phone = models.CharField(max_length=10)
    email = models.EmailField()
    dob = models.DateField(auto_now_add=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)

    def __str__(self):
        return self.name, self.nationality, self.phone, self.email, self.dob

class Player_Stat(models.Model):
    playerstatid = models.AutoField(primary_key=True)
    numberofgoals = models.PositiveIntegerField()
    numberofassists = models.PositiveIntegerField()
    apperances = models.PositiveIntegerField()
    redcards = models.PositiveIntegerField()
    yellowcards = models.PositiveIntegerField()
    player = models.OneToOneField(Player, on_delete=models.CASCADE, related_name='player_stat')
    
    def __str__(self):
        return self.numberofgoals, self.numberofgoals, self.apperances, self.redcards, self.yellowcards
    
class Tournament(models.Model):
    tournamentid = models.AutoField(primary_key=True)
    totalprizepool = models.PositiveIntegerField()
    sponsor = models.CharField(max_length=255)

    def __str__(self):
        return self.totalprizepool, self.sponsor
    
class Fan(models.Model):
    fanid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    nationality = models.CharField(max_length=255)
    phone = models.CharField(max_length=10)
    email = models.EmailField()
    dob = models.DateField(auto_now_add=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    def __str__(self):
        return self.name, self.nationality, self.teamid
    
class Stadium(models.Model):
    stadiumid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.name, self.address
    
class Referee(models.Model):
    refereeid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    nationality = models.CharField(max_length=255)
    phone = models.CharField(max_length=10)
    email = models.EmailField()
    dob = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name, self.nationality, self.email
    
class Match(models.Model):
    matchid = models.AutoField(primary_key=True)
    day = models.DateTimeField(auto_now_add=True)
    attacker = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='attacker')
    defender = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='defender')
    stadium = models.ForeignKey(Stadium, on_delete=models.CASCADE)
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    referee = models.ForeignKey(Referee, on_delete=models.CASCADE)

    def __str__(self):
        return self.day, self.attacker, self.defender, self.stadium, self.referee

class Result(models.Model):
    resultid = models.AutoField(primary_key=True)
    attackerpts = models.PositiveIntegerField()
    defenderpts = models.PositiveIntegerField()
    match = models.ForeignKey(Match, on_delete=models.CASCADE)

    def __str__(self):
        return self.attackerpts, self.defenderpts

class Practice(models.Model):
    practiceid = models.AutoField(primary_key=True)
    stadium = models.ForeignKey(Stadium, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    def __str__(self):
        return self.stadium, self.team
    
class ParticipateIn(models.Model):
    participateid = models.AutoField(primary_key=True)
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    def __str__(self):
        return self.tournament, self.team

