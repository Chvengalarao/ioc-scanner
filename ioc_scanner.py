file = open("logs.txt","r")
ioc_file = open("iocs.txt","r")

iocs = []

for line in ioc_file:
    iocs.append(line.strip())

print("=== IOC Scan Report ===\n")

for log in file:
    for ioc in iocs:
        if ioc in log:
            print("IOC DETECTED")
            print("Indicator :", ioc)
            print("Log Entry :", log.strip())
            print("-----------------------")
