from awesome_project.mean import take_average


if __name__ == '__main__':
    with open('/dev/stdin') as f:
        xs = [int(x) for x in f.read().split()]
    print(take_average(xs))
