# Использование %:
team1_name = "Мастера кода,"
team2_name = "Волшебники данных,"
team1_num = 5
team2_num = 6
print("В команде %s участников: %d" % (team1_name,team1_num ))
print("В команде %s участников: %d" % (team2_name,team2_num ))
print("Итого сегодня в командах участников: %d и %d" % (team1_num, team2_num))

# Использование format():
score1 = 40
score2 = 42
team1_time = 1552.512
team2_time = 18015.2
print("Команда {} решила задачь: {}".format(team2_name, score2))
print("{} решили задачи за {} c!".format(team2_name, team2_time))

# Использование f - строки:
print(f"Команды решили {score1} и {score2}, задачь.")

challenge_result = team1_name.replace(",", "") if (score1 > score2 or
                                                   score1 == score2 and
                                                   team1_time > team2_time) else team2_name.replace(",", "")


tasks_total = score1 + score2
time_avg = sum([team1_time, team2_time]) / tasks_total

print(f"Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!.")
print(f"Результат битвы: победа команды {challenge_result}")
