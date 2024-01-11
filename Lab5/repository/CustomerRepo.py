from repository.DataRepo import DataRepo
from modelle.kunde import Kunde
import pickle


class CustomerRepo(DataRepo):

    def __init__(self):
        super().__init__("CustomerRepo.txt")
        self.customers = []

    def add_customers(self, customer: Kunde):
        self.customers.append(customer)

    def save(self):
        with open(self.filename, 'wb') as f:
            for customer in self.customers:
                pickle.dump(customer, f)
                f.write(b'\n')

    def load(self):
        self.customers = []
        with open(self.filename, 'rb') as f:
            while True:
                position = f.tell()
                try:
                    customer = pickle.load(f)
                    self.customers.append(customer)
                except EOFError:
                    break
                except pickle.UnpicklingError:
                    f.seek(position)
                    f.readline()

    def load_to_list(self):
        self.customers = []
        with open(self.filename, 'rb') as f:
            while True:
                position = f.tell()
                try:
                    customer = pickle.load(f)
                    self.customers.append(customer)
                except EOFError:
                    break
                except pickle.UnpicklingError:
                    f.seek(position)
                    f.readline()

        return self.customers


    def search_after_partial_name(self, partial_name):
        matching_customers = []
        all_customers = self.load_to_list()

        partial_name = partial_name.lower()

        for customer in all_customers:
            if partial_name in customer.name.lower():
                matching_customers.append(customer)

        return matching_customers


    def search_after_partial_name_filt2(self, partial_name):
        all_customers = self.load_to_list()

        matching_customers = filter(lambda customer: partial_name in customer.name, all_customers)

        matching_customers = list(matching_customers)

        return matching_customers



    def search_after_partial_address(self, partial_address):
        matching_addresses = []
        all_customers = self.load_to_list()

        partial_address = partial_address

        for customer in all_customers:
            if partial_address in customer.adresse:
                matching_addresses.append(customer)

        return matching_addresses



    def search_after_partial_address_with_filter(self, partial_address):
        all_customers = self.load_to_list()

        matching_addresses = filter(lambda customer: partial_address in customer.adresse, all_customers)

        matching_addresses = list(matching_addresses)

        return matching_addresses

    def update_cust_name(self, old_name: str, new_name: str):
        customers = self.load_to_list()

        for customer in customers:
            if customer.name == old_name:
                customer.name = new_name
                break
        self.save()

    def read_file(self):
        f = open(self.filename, 'rb')
        file_content = f.read()
        content = []
        customer_data = file_content.split(b'\n')

        for customer_data in customer_data:
            customer = pickle.loads(customer_data)
            content.append(customer)

        f.close()
        return content

    def write_to_file(self, string):
        f = open(self.filename, 'ab')

        if type(string) == str:
            f.write(string.encode() + b'\n')
        else:
            pickle.dump(string, f)
            f.write(b'\n')

    def convert_to_string(self):
        pass
    def convert_from_string(self, filename, string):
        pass
