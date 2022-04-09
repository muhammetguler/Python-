years = int(input())
yearsToSecond = years * 365 * 24 * 3600
months = int(input())
monthsToSecond = months * 30 * 24 * 3600
days = int(input())
daysToSecond = days * 24 * 3600
hours = int(input())
hoursToSecond = hours * 3600
minutes = int(input())
minutesToSecond = minutes * 60


sum_seconds = minutesToSecond + hoursToSecond + daysToSecond + monthsToSecond + yearsToSecond

print(sum_seconds)
