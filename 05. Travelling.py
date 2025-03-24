def travel_planner():
    while True:
        # Read destination input
        destination = input()

        # Check if it's time to end
        if destination.lower() == "end":
            break

        # Read the required budget for this destination
        try:
            budget = float(input())
        except ValueError:
            print("Invalid budget. Please enter a number.")
            continue

        # Start saving for this destination
        savings = 0.0
        while savings < budget:
            # Read the next amount saved
            try:
                amount = input()
                if amount.lower() == "end":
                    return
                savings += float(amount)
            except ValueError:
                print("Invalid amount. Please enter a number.")
                continue

        # When enough is saved
        print(f"Going to {destination}!")


# Run the program
travel_planner()
