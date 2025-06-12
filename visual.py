from collections import defaultdict, Counter

class Visualizer:
    def __init__(self):
        pass

    @staticmethod
    def display_review_distribution(data):
        counts = Counter([row["Branch"] for row in data])
        print("\n--- Most Reviewed Parks ---")
        for park, count in counts.items():
            print(f"{park}: {count} reviews")

    @staticmethod
    def display_average_scores(data):
        scores = defaultdict(list)
        for row in data:
            scores[row["Branch"]].append(int(row["Rating"]))
        print("\n--- Average Scores ---")
        for park, ratings in scores.items():
            avg = sum(ratings) / len(ratings)
            print(f"{park}: {avg:.2f}")

    @staticmethod
    def display_top_locations(data, park):
        scores = defaultdict(list)
        for row in data:
            if row["Branch"].lower() == park.lower():
                scores[row["Reviewer_Location"]].append(int(row["Rating"]))
        if not scores:
            print("No data for that park.")
            return
        averages = {loc: sum(r) / len(r) for loc, r in scores.items()}
        top_10 = sorted(averages.items(), key=lambda x: -x[1])[:10]
        print(f"\n--- Top Locations by Rating for {park} ---")
        for loc, avg in top_10:
            print(f"{loc}: {avg:.2f}")

    @staticmethod
    def display_monthly_averages(data, park):
        scores = defaultdict(list)
        for row in data:
            if row["Branch"].lower() == park.lower():
                ym = row["Year_Month"]
                if "-" in ym:
                    month = ym.split("-")[1]
                    scores[month].append(int(row["Rating"]))
        if not scores:
            print("No data for that park.")
            return
        print(f"\n--- Monthly Average Ratings for {park} ---")
        for month in sorted(scores, key=lambda m: int(m)):
            avg = sum(scores[month]) / len(scores[month])
            print(f"Month {month}: {avg:.2f}")
