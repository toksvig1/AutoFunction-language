import sys
class Inter:
    def ev(self, s):
        self.varsNoSF = {}
        lines = [x for x in s.split("\n") if x.strip() != ""]
        pc = 0
        while pc < len(lines):
            line = lines[pc]
            match line.split(maxsplit=1)[0]:
                case 'if':
                    if self.ev_expr(line.split(maxsplit=1)[1])==1: 
                        pc =pc+1 
                        print("a")
                    else:
                        while lines[pc].split(maxsplit=1)[0] != "end": pc = pc + 1
                        pc = pc + 1
                case 'end': 
                    pc = pc + 1
                case _:
                    (name,_,expr) = line.split(maxsplit=2)
                    self.varsNoSF[name] = self.ev_expr(expr)
                    #print(name+" | "+expr)
                    pc = pc + 1
        print(self.varsNoSF)
    def ev_expr(self, s):
        toks = s.split()
        #print(toks)
        stack = []
        #print(toks)
        for tok in toks:
            #print(tok)
            if tok.isdigit(): stack.append(int(tok))
            elif tok in self.varsNoSF: stack.append(self.varsNoSF[tok])
            else:
                rhs = stack.pop()
                lhs = stack.pop()
                #print(lhs)
                #print(rhs)
                if tok == "+": stack.append(lhs + rhs)
                elif tok == "-": stack.append(lhs-rhs)
                elif tok == "*": stack.append(lhs*rhs)
                elif tok == "==": 
                    if lhs in self.varsNoSF: lhs = self.varsNoSF[lhs]
                    if rhs in self.varsNoSF: rhs = self.varsNoSF[rhs]
                    if lhs == rhs:
                        stack.append(1)
                    else:
                        stack.append(0)
        return stack[0]
Inter().ev(open(sys.argv[1]).read())
