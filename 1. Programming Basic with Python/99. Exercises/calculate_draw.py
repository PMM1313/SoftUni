import math


from scipy.optimize import root_scalar


def solve_and_calculate(sum_of_bets, coefficient_draw):
    X_guess = 0.01  # Hardcoded initial guess for bet

    # This is 10 %
    needed_profit = 0.10
    # Define the equation directly inside the function

    def calculate_total_bets(sum_of_bets, bet):
        total_bets_non_rounded = sum_of_bets + bet
        total_bets = math.ceil(total_bets_non_rounded * 100) / 100
        return total_bets

    def calculate_profit(sum_of_bets, bet, needed_profit):
        profit_non_rounded = (sum_of_bets + bet) * needed_profit
        profit = math.ceil(profit_non_rounded * 100) / 100
        return profit

    def equation(potential_bet):
        return potential_bet * coefficient_draw - ((sum_of_bets + potential_bet) + (sum_of_bets + potential_bet) * needed_profit)

    # Solve the equation
    sol = root_scalar(equation, x0=X_guess, method='newton')

    if sol.converged:

        # This is actually finding the needed Bet
        bet = sol.root

        # Calculate bet, profit, and total_bets

        bet_non_rounded = bet

        # Round up to the nearest second decimal place

        bet = math.ceil(bet_non_rounded * 100) / 100

        # Checks if the bet is at least minimum
        bet = minimum_bet_check(bet)

        # Need to check Profit and Total bets if minimum bet is less than 0.25, the equation cant calc them
        profit = calculate_profit(sum_of_bets, bet, needed_profit)
        total_bets = calculate_total_bets(sum_of_bets, bet)

        print("Bet:", bet)
        print("Profit:", profit)
        print("Total Bets:", total_bets)
    else:
        print("Failed to calculate bet.")


def minimum_bet_check(bet):
    if bet < 0.25:
        bet = 0.25
    return bet


# Example usage:
sum_of_bets = 0.25
coefficient_draw = 3.4


solve_and_calculate(sum_of_bets, coefficient_draw)
