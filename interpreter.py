import sys

"""
        while pc < len(lines):
            line = lines[pc]
            match line.split(maxsplit=1)[0]:
                case 'while':
                    print("wh")
                    orgline = pc
                    while self.ev_expr(line.split(maxsplit=1)[1])==1:
                        pc =pc+1 
                        if lines[pc].split(maxsplit=1)[0] == "end":
                            pc = orgline
                    while lines[pc].split(maxsplit=1)[0] != "end": pc = pc + 1
                    pc = pc + 1
                case 'if':
                    if self.ev_expr(line.split(maxsplit=1)[1])==1: 
                        pc =pc+1 
                    else:
                        while lines[pc].split(maxsplit=1)[0] != "end": pc = pc + 1
                        pc = pc + 1
                case 'print':
                    print(self.varsNoSF[line.split(maxsplit=1)[1]])
                    pc = pc + 1
                case 'end': 
                    pc = pc + 1
                case _:
                    (name,_,expr) = line.split(maxsplit=2)
                    self.varsNoSF[name] = self.ev_expr(expr)
                    pc = pc + 1
        """






class Inter:
    def ev(self, s):
        self.varsNoSF = {}
        lines = [x for x in s.split("\n") if x.strip() != ""]
        pc = 0
        self.recurvline_func(lines,pc,0,False,False)
        print(self.varsNoSF)
    def ev_expr(self, s):
        toks = s.split()
        #print(toks)
        stack = []
        #print(toks)
        for tok in toks:
            #print(tok)
            #stack = stack.copy() stack.append(int(tok)) stack.append(self.varsNoSF[tok])
            if tok.isdigit(): stack = stack + [int(tok)]
            elif tok in self.varsNoSF: stack = stack + [self.varsNoSF[tok]]
            else:
                rhs = stack.pop()
                lhs = stack.pop()
                #print(lhs)
                #print(rhs)
                if tok == "+": stack = stack + [lhs + rhs]
                elif tok == "-": stack = stack + [lhs-rhs]
                elif tok == "*": stack = stack + [lhs*rhs]
                elif tok == "==": 
                    if lhs in self.varsNoSF: lhs = self.varsNoSF[lhs]
                    if rhs in self.varsNoSF: rhs = self.varsNoSF[rhs]
                    if lhs == rhs:
                        stack = stack + [1]
                    else:
                        stack = stack + [0]
                elif tok == "<":
                    if lhs in self.varsNoSF: lhs = self.varsNoSF[lhs]
                    if rhs in self.varsNoSF: rhs = self.varsNoSF[rhs]
                    if lhs < rhs:
                        stack = stack + [1]
                    else:
                        stack = stack + [0]
        return stack[0]
    
    def recurvline_func(self,lines,pc,loop,orgpos,exprorg):
        line = lines[pc]
        match line.split(maxsplit=1)[0]:
            case 'if':
                if self.ev_expr(line.split(maxsplit=1)[1])==1: 
                    pc =pc+1 
                else:
                    while lines[pc].split(maxsplit=1)[0] != "end": pc = pc + 1
                    pc = pc + 1
            case 'end': 
                if loop:
                    if self.ev_expr(exprorg)==1:
                        pc = int(orgpos)
                    else:
                        pc = pc + 1
                else:
                    pc = pc + 1
            case 'while':
                print("a")
                if self.ev_expr(line.split(maxsplit=1)[1])==1: 
                    self.recurvline_func(lines,pc,pc,True,line.split(maxsplit=1)[1])
            case _:
                (name,_,expr) = line.split(maxsplit=2)
                self.varsNoSF[name] = self.ev_expr(expr)
                #print(name+" | "+expr)
                pc = pc + 1
        if pc < len(lines):
            self.recurvline_func(lines,pc,0,False,False)

    """
    def recurv_func(self, lines, pc, orgpos):
        print("run")
        if pc == 2:
            self.recurv_func(lines,pc)
    """
Inter().ev(open(sys.argv[1]).read())
