ab = 123
credits = 100
is_bonus = False

#1
if not is_bonus and credits > 50:
    ab -= 2
elif not is_bonus and credits <= 50:
    ab -= 1

#2
if not is_bonus:
    if credits > 50:
        ab -= 2
    else:
        ab -= 1

#3
if is_bonus:
    pass
elif credits > 50:
    ab -= 2
else:
    ab -= 1


# if credits are at least 50,
# and is_bonus is False decrement ab by 2
# if credits are smaller than 50,
# and is_bonus is False decrement ab by 1
# if is_bonus is True ab should remain the same
