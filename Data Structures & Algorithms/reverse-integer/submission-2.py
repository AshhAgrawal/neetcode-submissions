class Solution:
    def reverse(self, x: int) -> int:
        # Define 32-bit signed integer limits (problem constraint)
        MAX = 2147483647      #  2^31 - 1
        MIN = -2147483648     # -2^31
        
        res = 0  # This will store the reversed number
        
        # Continue until all digits of x are processed
        while x:
            # Extract the last digit of x
            # Using fmod instead of % to correctly handle negative numbers
            digit = int(math.fmod(x, 10))
            
            # Remove the last digit from x
            # int(x/10) truncates toward 0 (important for negative numbers)
            x = int(x / 10)

            # BEFORE updating res, check if it will overflow
            # Case 1: If res is already greater than MAX//10,
            # multiplying by 10 will definitely overflow
            # Case 2: If res == MAX//10, we must ensure digit does not exceed last digit of MAX
            if (res > MAX // 10 or (res == MAX // 10 and digit >= MAX % 10)):
                return 0  # overflow → return 0 as per problem
            
            # Similar overflow check for negative side
            # Case 1: If res is already less than MIN//10 → overflow
            # Case 2: If res == MIN//10, digit must not go below last digit of MIN
            if (res < MIN // 10 or (res == MIN // 10 and digit <= MIN % 10)):
                return 0  # overflow → return 0
            
            # Safe to append digit
            # Shift current result left (multiply by 10) and add new digit
            res = (res * 10) + digit
        
        # Final reversed number within bounds
        return res