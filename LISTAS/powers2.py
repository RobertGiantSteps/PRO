# **************
# POTENCIAS DE 2
# **************

BASE = 2
def run(num_powers: int) -> list:
    powers2 = [BASE**i for i in range(num_powers+1)]
   
 

    return powers2


if __name__ == '__main__':
    run(0)