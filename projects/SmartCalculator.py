class SmartCalculator:
    def __init__(self):
        self.dictionary = {}
    
    def menu(self):
        inputs = input()
        if "=" in inputs:
            if inputs.count("=") > 1:
                print("Invalid assignment")
            else:
                inputs = inputs.replace(" ", "").split(sep="=")
                return self.create_dictionary(inputs)
        elif "*" in inputs or "/" in inputs and not inputs.startswith("/"):
            if inputs.count("(") != inputs.count(")"):
                print("Invalid expression")
            elif any([i.count("*") > 1 for i in inputs.split()]):
                print("Invalid expression")
            elif any([i.count("/") > 1 for i in inputs.split()]):
                print("Invalid expression")
            else:
                sepparent = self.separate_parentheses(inputs.split())
                trans = self.transform(sepparent)
                postfix = self.infix_to_postfix(trans)
                return self.evaluate_postfix(postfix)
        else:
            inputs = inputs.split()
            if len(inputs) == 0:
                return self.menu()
            elif len(inputs) == 1:
                return self.num_o_str(inputs)
            elif len(inputs) > 1:
                trans = self.transform(inputs)
                return self.calculate_with_plus(trans)
    
    def num_o_str(self, num_o_str):
        try:
            print(int(num_o_str[0]))
        except:
            if "".join(num_o_str) == "/help":
                print("The program calculates the sum of numbers")
            elif "".join(num_o_str) == "/exit":
                return 0
            elif "".join(num_o_str)[0] == "/":
                print("Unknown command")
            elif num_o_str[0] in self.dictionary:
                print(self.dictionary[num_o_str[0]])
            else:
                print("Unknown variable")
                
    def transform(self, inputs):
        transformed = []
        for i in inputs:
            if i in self.dictionary:
                transformed.append(self.dictionary[i])
            else:
                transformed.append(i)
        return transformed
            
    def calculate_with_plus(self, inputs):
        inputs = [x for x in inputs if x != "+" * len(x)]
        try:
            print(sum(map(int, inputs)))
        except:
            try:
                return self.calculate_with_minus(inputs)
            except:
                print("Invalid expression2")
    
    def calculate_with_minus(self, inputs):
        for i in range(len(inputs) - 1):
            if inputs[i] == "-" * len(inputs[i]):
                if len(inputs[i]) % 2 == 1:
                    inputs[i + 1] = str(f"-{inputs[i + 1]}")
        inputs = [x for x in inputs if x != "-" * len(x)]        
        print(sum(map(int, inputs)))
        
    def create_dictionary(self, inputs):
        if all([x not in "1234567890" for x in inputs[0]]):
            try:
                if isinstance(int(inputs[1]), int):
                    self.dictionary[inputs[0]] = inputs[1]
            except:
                if any([x in "abcdefghijklmnopqrstuvwxyz" for x in inputs[1]]):
                    if inputs[1] in self.dictionary:
                        self.dictionary[inputs[0]] = self.dictionary[inputs[1]]
                    else:
                        print("Invalid assignment")
        else:
            print("Invalid identifier")
    
    def separate_parentheses(self, expression):
        new_expression = []
        for ch in expression:
            if "(" in ch:
                while "(" in ch:
                    new_expression.append(ch[0])
                    ch = ch[1:]
                new_expression.append(ch)
            elif ")" in ch:
                x = ch.count(")")
                new_expression.append(ch[: len(ch) - x])
                for _ in range(x):
                    new_expression.append(")")
            else:
                new_expression.append(ch)
        return new_expression
    
    def infix_to_postfix(self, expression):
        priority = {'+':1, '-':1, '*':2, '/':2, "^":3} 
        stack = []
        output = []
        for ch in expression:
            if ch not in "+-*/()":  
                output.append(ch)
            elif ch == '(' :  
                stack.append('(')
            elif ch ==')':
                while stack and stack[-1]!= '(':
                    output.append(stack.pop())
                stack.pop()
            else:
                while stack and stack[-1]!='(' and priority[ch]<=priority[stack[-1]]:  
                    output.append(stack.pop()) 
                stack.append(ch)
        while stack:
            output.append(stack.pop())
        return output
    
    def evaluate_postfix(self, postfix): 
        obj = []
        for i in postfix: 
            if i.isdigit(): 
                obj.append(i) 
            else: 
                val1 = int(obj.pop()) 
                val2 = int(obj.pop()) 
                if i == "+":
                    obj.append(str(val2 + val1))
                elif i == "-":
                    obj.append(str(val2 - val1))
                elif i == "*":
                    obj.append(str(val2 * val1))
                elif i == "/":
                    obj.append(str(int(val2 / val1)))
                elif i == "^":
                    obj.append(str(val2 ** val1))
        print(obj.pop()) 
                          
    def main(self):
        while self.menu() != 0:
            continue
        print("Bye!")
        
program = SmartCalculator()
program.main()
