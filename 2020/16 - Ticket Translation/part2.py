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

validtickets = []

for ticket in tickets:
    ticketvalid = True
    for num in ticket.split(","):
        num = int(num)
        valid = False
        for field in fields:
            i = fields[field]
            if i[0][0] <= num <= i[0][1] or i[1][0] <= num <= i[1][1]:
                valid = True
        if not valid:
            ticketvalid = False
            break
    if ticketvalid:
        validtickets.append(ticket)

tickets = []
tickets.append([int(i) for i in myticket.split(",")])
for t in validtickets:
    tickets.append([int(i) for i in t.split(",")])

fieldnames = {}
for i in range( 0, len(tickets[0]) ):
    fieldnames[i] = {}
    for fieldname in fields:
        fieldnames[i][fieldname] = True
        for ticket in tickets:
            within = False
            for field in fields[fieldname]:
                if field[0] <= ticket[i] <= field[1]:
                    within = True
            if not within:
                del fieldnames[i][fieldname]
                break


finalfn = {}
while len(finalfn) < len(fields):
    lastfield = ""
    for i in fieldnames:
        if len(fieldnames[i]) == 1:
            for k in fieldnames[i]:
                finalfn[k] = i
                lastfield = k

    for i in fieldnames:
        try:
            del fieldnames[i][lastfield]    
        except:
            pass

myticket = [int(i) for i in myticket.split(",")]
total = 1
for k in finalfn:
    if k.startswith("departure"):
        total *= myticket[finalfn[k]]

print(total)