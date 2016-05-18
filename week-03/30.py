ac = 8
time = 120
out = ''

#1
if ac % 4 == 0 and time <= 200:
    out = "Check"
elif time > 200:
    out = "Time out"
else:
    out = "Run Forest Run!"

print(out)


#2
if time > 200:
    out = "time out"
elif ac % 4 == 0:
    out = "Check"
else:
    out = "Run Forest Run!"


# if ac is dividable by 4
# and time is not more than 200
# set out to 'check'
# if time is more than 200
# set out to 'Time out'
# otherwise set out to 'Run Forest Run!'
