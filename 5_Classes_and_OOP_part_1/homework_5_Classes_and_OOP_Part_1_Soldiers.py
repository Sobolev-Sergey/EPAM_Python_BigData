"""
Разработайте программу по следующему описанию и следуя принципам ООП.

В некой игре-стратегии есть солдаты и герои (все они являются воинами).
У всех есть уникальный номер объекта и принадлежность к команде.
У солдат есть метод "иду за героем", который в качестве аргумента принимает объект типа "герой".
У героев есть метод увеличения собственного уровня.

Всего существует 3 команды, каждая со своим цветом ("red", "yellow", "green").
У каждой команды есть 1 свой герой.

В цикле генерируются объекты-солдаты (1 000 шт).
Их принадлежность к команде определяется случайно.
Солдаты разных команд добавляются в разные списки.

Измеряется длина списков солдат противоборствующих команд и выводится на экран.

    >> Team 'red' has '315' soldiers.
    >> Team 'yellow' has '376' soldiers.
    >> Team 'green' has '309' soldiers.
    >> Team 'yellow' has more soldiers than others.

У героя, принадлежащего команде с более длинным списком, поднимается уровень на +1.
Изначально у каждого героя произвольный уровень от 0 до 1.
У солдат уровня нет.

Для команды с героем максимального уровня создайте разведывательный отряд из героя и 3х произвольных солдат его команды, которые следуют за ним.
Выведите на экран состав участников отряда.

  >> Scout: Soldier(idx=56, color=yellow, hero=Hero(idx=1, color=yellow, level=2))
  >> Scout: Soldier(idx=505, color=yellow, hero=Hero(idx=1, color=yellow, level=2))
  >> Scout: Soldier(idx=770, color=yellow, hero=Hero(idx=1, color=yellow, level=2))
  >> Scout: Hero(idx=1, color=yellow, level=2)

    (Для красивого вывода можно переписать метод "__repr__".)

На этом подготовка к битве закончена.


Для базовой проверки и форматирования кода используйте: isort, black, pylint.
ДЗ нужно выполнить до следующей лекции.

"""

from random import randint, choice

ALL_SOLDIERS = 1000
COUNT_SOLDIERS_FOR_SCOUT = 3
NAME_TEAMS = ("red", "yellow", "green")

# possible minimum and maximum hero level on initialization
MIN_LEVEL = 0
MAX_LEVEL = 1


class Warrior:
    """
    Main class for heroes and soldiers
    """

    all_warrior = 0

    def __init__(self, name):
        Warrior.all_warrior += 1
        self.idx = Warrior.all_warrior
        self.team_name = name


class Hero(Warrior):
    """
    Hero
    """

    def __init__(self, name_team):
        super().__init__(name=name_team)
        self.level = randint(MIN_LEVEL, MAX_LEVEL)

    def level_increase(self):
        """
        Up level for hero
        """
        self.level += 1

    def __repr__(self):
        """
        String representation for hero

        :return: String with parameters
        """
        return (
            f"{self.__class__.__name__}"
            f"(idx={self.idx}, color={self.team_name}, level={self.level})"
        )


class Soldier(Warrior):
    """
    Soldier
    """

    def __init__(self, name_team):
        super().__init__(name=name_team)
        self.my_hero = None

    def set_follow_hero(self, hero: Hero):
        """
        The soldier follows the hero
        :param hero: object Hero
        """
        self.my_hero = hero

    def __repr__(self):
        """
        String representation for soldier

        :return: String with parameters
        """
        return (
            f"{self.__class__.__name__}(idx={self.idx}, color={self.team_name},"
            f" hero={self.my_hero.__class__.__name__}"
            f"(idx={self.my_hero.idx}, color={self.my_hero.team_name}, level={self.my_hero.level}))"
        )


def main():
    """
    Main program
    """

    # Creating teams and hero for teams
    heroes = {}
    teams = {}
    for name_team in NAME_TEAMS:
        teams.setdefault(name_team, [])
        heroes.setdefault(name_team, Hero(name_team))

    # Creating soldiers
    for i in range(ALL_SOLDIERS):
        name_team = NAME_TEAMS[randint(0, len(NAME_TEAMS) - 1)]
        soldier = Soldier(name_team)
        team = teams.get(name_team)
        team.append(soldier)
        teams.update({name_team: team})

    # Search for a team with the maximum number of soldiers
    max_number_soldiers = 0
    name_max_team = ""
    for i in range(len(NAME_TEAMS)):
        name_team = NAME_TEAMS[i]
        number_soldiers = len(teams.get(name_team))
        print(f"Team '{name_team}' has '{number_soldiers}' soldiers.")
        if number_soldiers > max_number_soldiers:
            max_number_soldiers = number_soldiers
            name_max_team = name_team

    # Uplevel on +1 for the hero from the team with the maximum number of soldiers
    heroes[name_max_team].level_increase()
    print(f"Team '{name_max_team}' has more soldiers than others")

    # Creating scout
    scouts = []
    for i in range(COUNT_SOLDIERS_FOR_SCOUT):
        team = teams.get(name_max_team)
        soldier = choice(team)
        soldier.set_follow_hero(heroes[name_max_team])
        scouts.append(soldier)
    scouts.append(heroes[name_max_team])

    # Print the scout members.
    for scout in scouts:
        print(f"Scout: {scout.__repr__()}")


main()


"""
Output run:

Team 'red' has '315' soldiers.
Team 'yellow' has '352' soldiers.
Team 'green' has '333' soldiers.
Team 'yellow' has more soldiers than others
Scout: Soldier(idx=625, color=yellow, hero=Hero(idx=2, color=yellow, level=2))
Scout: Soldier(idx=41, color=yellow, hero=Hero(idx=2, color=yellow, level=2))
Scout: Soldier(idx=875, color=yellow, hero=Hero(idx=2, color=yellow, level=2))
Scout: Hero(idx=2, color=yellow, level=2)

"""
