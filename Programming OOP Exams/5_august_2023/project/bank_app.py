from project.clients.adult import Adult
from project.clients.student import Student
from project.loans.mortgage_loan import MortgageLoan
from project.loans.student_loan import StudentLoan


class BankApp:
    VALID_LOANS = {"StudentLoan": StudentLoan,
                   "MortgageLoan": MortgageLoan}

    VALID_CLIENTS = {"Student": Student,
                     "Adult": Adult}

    VALID_CLIENT_LOANS = {"Student": "StudentLoan",
                          "Adult": "MortgageLoan"}

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.loans = []
        self.clients = []

    def add_loan(self, loan_type: str):

        if loan_type not in self.VALID_LOANS:
            raise Exception("Invalid loan type!")

        loan = self.VALID_LOANS[loan_type]()
        self.loans.append(loan)
        return f"{loan_type} was successfully added."

    def add_client(self, client_type: str, client_name: str, client_id: str, income: float):

        if client_type not in self.VALID_CLIENTS:
            raise Exception("Invalid client type!")

        if len(self.clients) >= self.capacity:
            return "Not enough bank capacity."

        client = self.VALID_CLIENTS[client_type](client_name, client_id, income)
        self.clients.append(client)
        return f"{client_type} was successfully added."

    def grant_loan(self, loan_type: str, client_id: str):

        client = next(filter(lambda c: c.client_id == client_id, self.clients))
        loan = [l for l in self.loans if l.__class__.__name__ == loan_type][0]

        if (client.__class__.__name__ == "Student" and loan.__class__.__name__ == "StudentLoan") or \
                (client.__class__.__name__ == "Adult" and loan.__class__.__name__ == "MortgageLoan"):

            self.loans.remove(loan)
            client.loans.append(loan)
            return f"Successfully granted {loan_type} to {client.name} with ID {client_id}."

        else:
            raise Exception("Inappropriate loan type!")

    def remove_client(self, client_id: str):

        try:
            client = next(filter(lambda c: c.client_id == client_id, self.clients))
        except StopIteration:
            raise Exception("No such client!")

        if client.loans:
            raise Exception("The client has loans! Removal is impossible!")

        self.clients.remove(client)
        return f"Successfully removed {client.name} with ID {client_id}."

    def increase_loan_interest(self, loan_type: str):

        changed_loans = 0

        granted_loans = []

        for client in self.clients:
            for loan in client.loans:
                granted_loans.append(loan)

        for loan in self.loans:
            if loan.__class__.__name__ == loan_type and loan not in granted_loans:
                loan.increase_interest_rate()
                changed_loans += 1

        return f"Successfully changed {changed_loans} loans."

    def increase_clients_interest(self, min_rate: float):

        changed_clients = 0

        for client in self.clients:
            if client.interest < min_rate:
                client.increase_clients_interest()
                changed_clients += 1

        return f"Number of clients affected: {changed_clients}."

    def get_statistics(self):

        granted_loans = []
        non_granted_loans = []

        for client in self.clients:
            for loan in client.loans:
                granted_loans.append(loan)

        for loan in self.loans:
            if loan not in non_granted_loans:
                non_granted_loans.append(loan)

        average_client_interest = 0
        all_clients_interest = sum([c.interest for c in self.clients])
        number_of_clients = len(self.clients)

        if number_of_clients > 0:
            average_client_interest = all_clients_interest / number_of_clients
        else:
            average_client_interest = 0

        info = f'Active Clients: {len(self.clients)}\n'
        info += f'Total Income: {sum([c.income for c in self.clients]):.2f}\n'
        info += f'Granted Loans: {len(granted_loans)}, Total Sum: {sum([l.amount for l in granted_loans]):.2f}\n'
        info += f'Available Loans: {len(non_granted_loans)}, Total Sum: {sum([l.amount for l in non_granted_loans]):.2f}\n'
        info += f'Average Client Interest Rate: {average_client_interest:.2f}'

        return info

bank = BankApp(3)

print(bank.add_loan('StudentLoan'))
print(bank.add_loan('MortgageLoan'))
print(bank.add_loan('StudentLoan'))
print(bank.add_loan('MortgageLoan'))


print(bank.add_client('Student', 'Peter Simmons', '1234567891', 500))
print(bank.add_client('Adult', 'Samantha Peters', '1234567000', 1000))
print(bank.add_client('Student', 'Simon Mann', '1234567999', 700))
print(bank.add_client('Student', 'Tammy Smith', '1234567555', 700))

print(bank.grant_loan('StudentLoan', '1234567891'))
print(bank.grant_loan('MortgageLoan', '1234567000'))
print(bank.grant_loan('MortgageLoan', '1234567000'))

print(bank.remove_client('1234567999'))

print(bank.increase_loan_interest('StudentLoan'))
print(bank.increase_loan_interest('MortgageLoan'))

print(bank.increase_clients_interest(1.2))
print(bank.increase_clients_interest(3.5))

print(bank.get_statistics())

