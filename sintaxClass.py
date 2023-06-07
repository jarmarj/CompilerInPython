class Sintax:
    def __init__(self, productions, terminals, non_terminals, parsing_table, start_symbol, input):
        self.productions = productions
        self.terminals = terminals
        self.non_terminals = non_terminals
        self.parse_table = parsing_table
        self.start_symbol = start_symbol
        self.lista_tokens = input

    def create_dictionary(self):
        dictionary = {}
        for index, value in enumerate(self.lista_tokens):
            dictionary[index] = value
        return dictionary

    def get_column(self, token):
        try:
            columna = self.terminals.index(token)
            return columna
        except ValueError:
            if (token.startswith('%') == True):  # identificador
                return 0
            elif ((token.startswith("'") == True) or (token.startswith("'"))):  # texto
                return 31
            else:
                try:
                    int(token)
                    return 37
                except ValueError:
                    try:
                        float(token)
                        return 37
                    except ValueError:
                        print(f'there is no {token} in terminals')
                        return -1

    def get_row(self, symbol_stack):
        try:
            row = self.non_terminals.index(symbol_stack)
            return row
        except ValueError:
            print(f'there is no {symbol_stack} in non-terminals')

    def i_buffer(self):
        input_buffer = []
        input_buffer.append('$')

        for token in reversed(self.lista_tokens):
            # print(token)
            input_buffer.append(token)
        # print(input_buffer)
        return input_buffer

    def parse(self):
        ip_buffer = self.i_buffer()
        print(f'i/p buffer {ip_buffer}')

        stack = []
        stack.append(self.start_symbol[0])
        stack.append(self.start_symbol[1])
        print(f'stack {stack}')

        while (len(stack) != 0):
            print('\n\n---------------------------------------------------------------------------')
            # determine the terminal and non-terminal
            stack_item = stack[-1]
            token = ip_buffer[-1]

            if stack[-1] == 'nulo':
                stack.pop()
                print(f'stack after pop nulo {stack}')
                print(f'i/p buffer after pop nulo {ip_buffer}')
                continue
            if ip_buffer[-1] == stack[-1]:
                stack.pop()
                ip_buffer.pop()
                print(f'stack after match {stack}')
                print(f'i/p buffer after match {ip_buffer}')
                continue

            # searches for the stack item in non-terminal list
            row = self.get_row(stack_item)
            print(f'row of {stack_item}: {row}')

            # searches for the token in the terminal list
            col = self.get_column(token)
            print(f'col of {token}: {col}')

            # given the row and col, searches for the production in the matrix
            prod_number = int(self.parse_table[row][col])
            print(f'production for {token} - {stack_item}')
            print(prod_number)

            # from the productions dictionary, gets the value fot that key
            prod_list = self.productions[(prod_number)]

            print(f'prod list {prod_list}')
            # if there is a production list, then pop and substitute in stack
            if prod_list:
                stack.pop()
                for item in reversed(prod_list):
                    if item == 'texto':
                        for i in reversed(ip_buffer):
                                if str(i).startswith("'"):
                                    stack.append(i)
                                    break
                        continue
                    if 'identificador' == item:
                        if token == '(' or token == 'longitud' or token == 'esentero' or token == 'esdecimal' or token == 'entero' or token == 'decimal' or token == 'sumar' or token == 'minimo' or token == 'maximo':
                            for i in reversed(ip_buffer):
                                if str(i).__contains__('%'):
                                    stack.append(i)
                                    break
                            continue
                        stack.append(token)
                        continue

                    stack.append(item)

                print(f'stack after appending prod {stack}')
                print(f'i/p buffer after appendig to prod {ip_buffer}')

        print('\n\nLIST OF TOKENS ACCEPTED')
