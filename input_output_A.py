

def A(name: str, n: int, fin, fout) -> list[tuple]:
    path_input = "testcase/testcase_{}/input/".format(name)
    path_output = "testcase/testcase_{}/output/".format(name)
    input_list = []
    output_list = []
    for i in range(1, n + 1):
        with open("{}input_{}.txt".format(path_input, i), "r") as infile:
            input_list.append(fin(list(map(lambda s: s.removesuffix("\n"), infile.readlines()))))
        with open("{}output_{}.txt".format(path_output, i), "r") as outfile:
            output_list.append(fout(list(map(lambda s: s.removesuffix("\n"), outfile.readlines()))))
    rel = []
    for i in range(n):
        x = input_list[i]
        y = output_list[i]
        a = type(x) is tuple
        b = type(y) is tuple
        if a and b:
            rel.append(x + y)
        elif not a and b:
            rel.append((x, * y))
        elif a and not b:
            rel.append((* x, y))
        else:
            rel.append((x, y))
    return rel
        
        
class InputFunction:

    def F71A(self, inputs: list[str]):
        rel = []
        for i, e in enumerate(inputs):
            if i == 0:
                continue
            rel.append(e)
        return rel

    
    def F116A(self, s):
        rel = []
        for i, e in enumerate(s):
            if i == 0:
                continue
            a, b = map(int, e.split())
            rel.append((a, b))
        return rel
    
    def F231A(self, inputs: list[str]):
        rel = []
        for i, e in enumerate(inputs):
            if i == 0:
                continue
            rel.append(list(map(int, inputs[i].split())))
        return rel


class OutputFunction:

    def F71A(self, outputs: list[str]) -> list[str]:
        return outputs


    def F116A(self, outputs) -> int:
        return int(outputs[0])
    
    def F231A(self, outputs: list[str]) -> int:
        return int(outputs[0])
        
        