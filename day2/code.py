def countSafeReports(filePath):
    def isSafeReport(report):
        levels = list(map(int, report.split()))

        differences = [levels[i + 1] - levels[i] for i in range(len(levels) - 1)]

        if all(diff > 0 for diff in differences):
            direction = "increasing"
        elif all(diff < 0 for diff in differences):
            direction = "decreasing"
        else:
            return False

        if direction == "increasing":
            return all(1 <= diff <= 3 for diff in differences)
        elif direction == "decreasing":
            return all(-3 <= diff <= -1 for diff in differences)

    with open(filePath, "r") as file:
        data = file.readlines()

    return sum(1 for report in data if isSafeReport(report.strip()))

print(countSafeReports(r'C:\Users\x\Desktop\AoC\day2input.txt'))
