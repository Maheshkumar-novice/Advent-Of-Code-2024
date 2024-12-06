with open('sample.txt', 'r') as f:
	reports = [map(int, line.split()) for line in f.readlines()]

def _is_safe(report, ignore_idx):
    desc = False
    asc = False
    prev = None
    for idx, level in enumerate(report):
        if idx == ignore_idx:
            continue

        if not prev:
            prev = level
            continue

        if prev < level:
            asc = True
            if abs(prev - level) > 3:
                return False

        if prev > level:
            desc = True
            if abs(prev - level) > 3:
                return False

        if prev == level:
            return False
        
        if asc and desc:
            return False
    
        prev = level
    return True

def is_safe(report):
    report = list(report)
    for i in range(len(report)):
        if _is_safe(report, i):
            return True
    return False
    

print(sum(is_safe(report) for report in reports))
