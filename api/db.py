from collections import defaultdict


def initialize_map_data(source) -> defaultdict:
    year_map = defaultdict(lambda: defaultdict(list))
    li1 = []
    for row in source:
        year_map[row['YEAR']][row['CROP']].append({
            'id': row['FIPS_CODE'],
            'acres': row['TOTAL_HARVESTED_ACRES'],
            'bushels_per_acre': row['TOTAL_YIELD'],
        })

        li1.append({
            'id': row['FIPS_CODE'],
            'acres': row['TOTAL_HARVESTED_ACRES'],
            'bushels_per_acre': row['TOTAL_YIELD'],
        })

    return year_map
