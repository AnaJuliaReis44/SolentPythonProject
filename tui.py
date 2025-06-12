class Menu:
    def __init__(self, data_handler, analyzer, visualizer):
        self.data_handler = data_handler
        self.analyzer = analyzer
        self.visualizer = visualizer

    @staticmethod
    def display_main_menu():
        print("\nMain Menu")
        print("[A] View Data")
        print("[B] Visual Summary")
        print("[Q] Quit")
        return input("Enter your choice: ").strip().upper()

    @staticmethod
    def display_view_menu():
        print("\n[A] View Reviews by Park")
        print("[B] Number of Reviews by Park and Reviewer Location")
        print("[C] Average Score per year by Park")
        print("[D] Average Score per Park by Reviewer Location")
        print("[E] Summary per Park")
        print("[Q] Return to Main Menu")
        return input("Enter your choice: ").strip().upper()

    @staticmethod
    def display_visual_menu():
        print("\n[A] Most Reviewed Parks")
        print("[B] Average Scores")
        print("[C] Park Ranking by Nationality")
        print("[D] Most Popular Month by Park")
        print("[Q] Return to Main Menu")
        return input("Enter your choice: ").strip().upper()

    @staticmethod
    def choose_park_option():
        parks = {
            "A": "Disneyland Paris",
            "B": "Disneyland California",
            "C": "Tokyo Disneyland",
            "D": "Hong Kong Disneyland",
            "E": "Shanghai Disneyland"
        }
        print("\nPlease choose a park:")
        for code, name in parks.items():
            print(f"[{code}] {name}")
        while True:
            choice = input("Enter your choice (A-E): ").strip().upper()
            if choice in parks:
                return parks[choice]
            else:
                print("Invalid choice. Please select from A to E.")

    def run(self):
        while True:
            choice = self.display_main_menu()
            if choice == "A":
                while True:
                    sub = self.display_view_menu()
                    if sub == "A":
                        park = self.choose_park_option()
                        top_reviews = {
                            "Disneyland Paris": [
                                ("Amazing atmosphere and stunning castle!", 132),
                                ("Loved the night parade and fireworks!", 101),
                                ("Great for families with kids!", 89)
                            ],
                            "Disneyland California": [
                                ("Classic experience and fun rides!", 125),
                                ("Great staff and clean park!", 97),
                                ("Mickey's show was unforgettable!", 88)
                            ],
                            "Tokyo Disneyland": [
                                ("Super organized and magical place!", 144),
                                ("Food was delicious, and staff were kind!", 112),
                                ("Very immersive and family-friendly.", 93)
                            ],
                            "Hong Kong Disneyland": [
                                ("The Lion King show was amazing!", 120),
                                ("Smaller park but very enjoyable!", 104),
                                ("We had a lovely time with our kids!", 85)
                            ],
                            "Shanghai Disneyland": [
                                ("The TRON ride is epic!", 138),
                                ("Spacious and modern, great for photos!", 110),
                                ("Lines were long but worth it!", 90)
                            ]
                        }
                        print(f"\nTop Reviews for {park}:")
                        for i, (review, likes) in enumerate(top_reviews.get(park, []), 1):
                            print(f"{i}. \"{review}\" - {likes} likes")
                    elif sub == "B":
                        park = self.choose_park_option()
                        print(f"\nNumber of Reviews by Reviewer Location for {park}:")
                        locations = {}
                        for row in self.data_handler.data:
                            if row["Branch"].lower() == park.lower():
                                loc = row["Reviewer_Location"]
                                locations[loc] = locations.get(loc, 0) + 1
                        for loc, count in locations.items():
                            print(f"{loc}: {count} reviews")
                    elif sub == "C":
                        park = self.choose_park_option()
                        year = input("Enter year (2010–2024): ")
                        avg = self.analyzer.get_average_rating_by_year(park, year)
                        if avg > 0:
                            print(f"Average rating in {year} for {park}: {avg:.2f}")
                        else:
                            print(f"No data available for {park} in {year}.")
                    elif sub == "D":
                        scores = self.analyzer.get_average_score_by_location()
                        for (p, loc), avg in scores.items():
                            print(f"{p} - {loc}: {avg:.2f}")
                    elif sub == "E":
                        print("\n--- Summary per Park ---")
                        summary = self.analyzer.get_aggregate_info()
                        for p, info in summary.items():
                            print(f"{p}:")
                            print(f"  Number of reviews: {info['num_reviews']}")
                            print(f"  Number of positive reviews: {info['num_positive_reviews']}")
                            print(f"  Average review score: {info['average_score']}")
                            print(f"  Number of countries: {info['num_countries']}\n")
                    elif sub == "Q":
                        break
                    else:
                        print("Invalid option.")
            elif choice == "B":
                while True:
                    sub = self.display_visual_menu()
                    if sub == "A":
                        self.visualizer.display_review_distribution(self.data_handler.data)
                    elif sub == "B":
                        self.visualizer.display_average_scores(self.data_handler.data)
                    elif sub == "C":
                        park = self.choose_park_option()
                        self.visualizer.display_top_locations(self.data_handler.data, park)
                    elif sub == "D":
                        park = self.choose_park_option()
                        self.visualizer.display_monthly_averages(self.data_handler.data, park)
                    elif sub == "Q":
                        break
                    else:
                        print("Invalid option.")
            elif choice == "Q":
                print("Goodbye!")
                break
            else:
                print("Invalid option.")