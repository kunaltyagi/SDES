def ufo_sightings():
    years = []
    before1985 = 0
    with open('ufo-sightings.csv') as file:
        for line in file:
            [year, sightings] = line.split(',')
            year = int(year)
            sightings = int(sightings)
            if year < 1985:
                before1985 += sightings
            if sightings > 1000:
                years.append(year)
    return [years, before1985]

def sum_series(n):
    sum = 0;
    a = 1;
    b = 3;
    for i in range(0, n):
        sum += 8.0/(a*b)
        a += 4
        b += 4
    return round(sum, 4)

