import sys

myticket = ""
tickets = []
fields = {}

with open(sys.argv[1], "r") as f:
    for line in f:
        line = line.rstrip()
        # print(line)
        if line == "your ticket:":
            tickettype = "your"
        elif line == "nearby tickets:":
            tickettype = "nearby"
        elif ":" in line:
            field, nums = line.split(": ")
            i1, i2 = nums.split(" or ")
            i1l, i1h = i1.split("-")
            i2l, i2h = i2.split("-")
            fields[field] = [(int(i1l), int(i1h)), (int(i2l), int(i2h))]
        elif "," in line:
            if tickettype == "your":
                myticket = line
            elif tickettype == "nearby":
                tickets.append(line)

sum = 0

validtickets = []

for ticket in tickets:
    for num in ticket.split(","):
        num = int(num)
        valid = False
        for field in fields:
            i = fields[field]
            if i[0][0] <= num <= i[0][1] or i[1][0] <= num <= i[1][1]:
                valid = True

    if valid:
        validtickets.append(ticket)

print(len(tickets))
tickets = validtickets
print(len(tickets))
