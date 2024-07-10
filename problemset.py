
class CodeForcesHelp:

    def F71A_help_1(self, word: str) -> str:
        n = len(word) - 2
        return "{}{}{}".format(word[0], n, word[-1])


class CodeForces(CodeForcesHelp):

    def F71A(self):

        # Input
        nums = self.F71A_input()

        # Processing
        nums = self.F71A_processing(nums)

        # Output
        self.F71A_output(nums)

    def F71A_input(self):
        n = int(input())
        rel = []
        for i in range(n):
            rel.append(input())
        return rel
    
    def F71A_processing(self, nums: list[str]) -> list[str]:
        rel = []
        for word in nums:
            if len(word) > 10:
                rel.append(self.F71A_help_1(word))
            else:
                rel.append(word)
        return rel
    
    def F71A_output(self, nums):
        for word in nums:
            print(word)
   
    def F116A_input(self):
        n = int(input())
        rel = []
        for i in range(n):
            a, b = map(int, input().split())
            rel.append((a, b))
        return rel
    
    def F116A_processing(self, nums):
        zamax = 0
        temp = 0
        for zatuple in nums:
            temp += zatuple[1]
            temp -= zatuple[0]
            zamax = max(zamax, temp)
        return zamax

    def F116A(self):

        # Input
        nums = self.F116A_input()

        # Processing
        ans = self.F116A_processing(nums)

        # Output
        print(ans)

    def F231A(self):

        # Input
        nums = self.F231A_input()

        # Processing
        n = self.F231A_processing(nums)

        # Output
        self.F231A_output(n)

    def F231A_input(self):
        n = int(input())
        rel = []
        for i in range(n):
            rel.append(list(map(int, input().split())))
        return rel
    
    def F231A_processing(self, nums):
        sana = 0
        for num in nums:
            if sum(num) >= 2:
                sana += 1
        return sana
    
    def F231A_output(self, n):
        print(n)

    def F1970G1_input(self):
        t = int(input())
        for test in range(t):
            n, m, c = map(int, input().split())

        pass

    def F1970G1(self):

        # Input
        # Processing
        # Output
        pass

    def F617A_input(self):
        return int(input())
    
    def F617A_processing(self, x: int) -> int:
        if (x <= 5):
            return 1
        elif (x % 5 == 0):
            return x // 5
        else:
            return x // 5 + 1
        
    def F617A_output(self, ans):
        print(ans)

    def F617A(self):

        # Input
        x = self.F617A_input()

        # Processing
        ans = self.F617A_processing(x)

        # Output
        self.F617A_output(ans)


def main():
    solution = CodeForces()
    solution.F231A()


if __name__ == "__main__":
    main()
