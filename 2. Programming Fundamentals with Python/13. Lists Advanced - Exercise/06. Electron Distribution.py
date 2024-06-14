def electron_distribution(num_electrons):
    filled_shells = []
    shell_number = 1

    while num_electrons > 0:
        max_electrons_in_shell = 2 * shell_number ** 2

        if num_electrons >= max_electrons_in_shell:
            filled_shells.append(max_electrons_in_shell)
            num_electrons -= max_electrons_in_shell
        else:
            filled_shells.append(num_electrons)
            num_electrons = 0

        shell_number += 1

    print(filled_shells)


# Example usage:
num_electrons = int(input())
electron_distribution(num_electrons)