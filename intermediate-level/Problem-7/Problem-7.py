from collections import Counter

def top_ips(logfile):
    counter = Counter()
    with open(logfile, 'r') as f:
        for line in f:
            ip = line.split()[0]
            counter[ip] += 1
    return counter.most_common(3)


print(top_ips("access.log"))