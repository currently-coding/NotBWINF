class Member:
    def __init__(self, min, max) -> None:
        self.min_distance = min
        self.max_distance = max
        self.distance = (self.min_distance, self.max_distance)

    def __str__(self) -> str:
        return str(self.min_distance) + " - " + str(self.max_distance)


class HikePlanner:
    def __init__(self, members: list[Member]) -> None:
        self.members = members
        self.centroids = self.init_centroids()

    def init_centroids(self):
        member_avg = sum(
            [(member.min_distance + member.max_distance) / 2 for member in self.members]
        ) / len(self.members)
        return [
            member_avg * 0.66,
            member_avg,
            member_avg * 1.33,
        ]

    def assign_member_to_centroid(self):
        # Use indices (0, 1, 2) as keys instead of centroid values
        centroid_assignment = {i: [] for i in range(len(self.centroids))}

        for member in self.members:
            # Find the closest centroid index
            centroid_index = self.closest(member)
            centroid_assignment[centroid_index].append(member)

        self.centroid_member_assignment = centroid_assignment

    def recompute_centroids(self):
        print("Recomputing centroids...")
        for index, centroid in enumerate(self.centroids):
            assigned_members = self.centroid_member_assignment[index]

            # Only recompute if there are assigned members
            if len(assigned_members) > 0:
                self.centroids[index] = sum(
                    [
                        (member.min_distance + member.max_distance) / 2
                        for member in assigned_members
                    ]
                ) / len(assigned_members)
            else:
                print(
                    f"Centroid {index + 1} has no members assigned, skipping recalculation."
                )

    def calc_participation(self):
        unassigned = []
        for centroid_index, members in self.centroid_member_assignment.items():
            print(
                f"Checking participation for centroid {self.centroids[centroid_index]:.2f} km:"
            )
            for member in members:
                # Ensure centroid falls within the member's range
                if not (
                    member.min_distance
                    <= self.centroids[centroid_index]
                    <= member.max_distance
                ):
                    print(f"  Member {member} cannot participate, removing.")
                    unassigned.append(member)

            # Remove unassigned members after iteration to avoid list modification issues
            self.centroid_member_assignment[centroid_index] = [
                member for member in members if member not in unassigned
            ]
        print()

        # Reassign unassigned members if they can participate in another centroid's route
        for member in unassigned:
            for centroid_index, centroid in enumerate(self.centroids):
                if member.min_distance <= centroid <= member.max_distance:
                    self.centroid_member_assignment[centroid_index].append(member)
                    print(f"Re-added member {member} to centroid {centroid_index + 1}")
                    break

    def run_k_means(self, max_iterations=1000):
        print("Running K-Means...")
        centroids_previous = None
        iterations = 0

        # Run the K-means until the centroids stabilize or max_iterations are reached
        while centroids_previous != self.centroids and iterations < max_iterations:
            iterations += 1
            print(f"Iteration {iterations}...")
            centroids_previous = self.centroids[:]
            self.assign_member_to_centroid()
            self.recompute_centroids()

        # Once stable, calculate participation
        self.calc_participation()

    def closest(self, member):
        result_index = 0
        least_distance = abs(
            (member.min_distance + member.max_distance) / 2 - self.centroids[0]
        )

        # Find the index of the centroid closest to the member's midpoint
        for index, centroid in enumerate(self.centroids[1:], start=1):
            distance = abs((member.min_distance + member.max_distance) / 2 - centroid)
            if distance < least_distance:
                least_distance = distance
                result_index = index

        return result_index

    def output_plan(self):
        print("Number of total possible participants: ", len(self.members))
        total_participants = sum(
            len(members) for members in self.centroid_member_assignment.values()
        )
        print(f"Number of participants able to complete a tour: {total_participants}")
        print("\nFinal Plan:")
        for index, centroid in enumerate(self.centroids):
            print(f"Route Length (Centroid) {index + 1}: {centroid:.2f} km")
            print(
                f"Members Participating in this Route ({len(self.centroid_member_assignment[index])} participants):"
            )
            # for member in self.centroid_member_assignment[index]:
            #     print(
            #         f"  - Member with range: {member.min_distance} km to {member.max_distance} km"
            #     )
            print()  # New line for readability between centroids


def read_file(path):
    with open(path, "r") as f:
        lines = f.readlines()

    distances = [
        (int(vals[0]), int(vals[1]))
        for line in lines[1:]
        for vals in [line.strip().split()]
    ]
    members = [Member(distance[0], distance[1]) for distance in distances]

    return members


if __name__ == "__main__":
    path = "wandern7.txt"  # File path for input
    members = read_file(path)
    hp = HikePlanner(members)
    hp.run_k_means()
    hp.output_plan()
