def getNthHighestSalary(salaries, n):
    unique = list(set(salaries))
    unique.sort(reverse=True)
    return unique[n-1] if n <= len(unique) else None