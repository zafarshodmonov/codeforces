
class C944:

    def C_1(self, nums):
        # nums --> [2, 9, 10, 6]
        A = nums[0]  # A --> 2
        B = nums[1]  # B --> 9
        C = nums[2]  # C --> 10
        D = nums[3]  # D --> 6
        zamin = int(min(A, B))  # zamin --> 2
        zamax = int(max(A, B))  # zamax --> 9
        Y = list(range(zamax + 1, 13)) + list(range(1, zamin)) # Y --> [10, 11, 12, 1]
        X = list(range(zamin + 1, zamax))  # X --> [3, 4, 5, 6, 7, 8]
        if (C in X) and (D in X) or (C in Y) and (D in Y):
            return False
        return True
        

    def C(self):

        # Input
        def inp():
            n = int(input())
            nums = []
            for i in range(n):
                nums.append(list(map(int, input().split())))
            return nums
        
        nums = inp()

        # Processing
        ans = ""
        for i in nums:
            if self.C_1(i):
                ans += "YES" + "\n"
            else:
                ans += "NO" + "\n"
        ans = ans[:-1]

        # Output
        print(ans)


class Contest_27_06_2024:

    @staticmethod
    def A():

        # Input
        def input_A():

            N = int(input())
            rel = []
            for i in range(N):
                x, y = map(int, input().split())
                rel.append((x, y))
            return rel
        
        nums = input_A()

        # Processing
        def help_A(x, y):
            men = -x if x > 0 else x
            tanga = y - abs(x) + 1
            return True if men <= tanga else False
        
        def processing(nums):
            rel = []
            for x, y in nums:
                if help_A(x, y):
                    rel.append("YES")
                else:
                    rel.append("NO")
            return rel

        # Output
        for i in processing(nums):
            print(i)

    def B():
        pass

    def C():
        pass

    def D():
        pass

    def E():
        pass

    def F():
        pass


class Contest_30_06_2024:
    pass


def main():
    contest_27_06_2024 = Contest_27_06_2024()
    contest_27_06_2024.A()


if __name__ == "__main__":
    main()
