"""Client."""
from typing import Optional


class Client:
    """
    Class for clients.

    Every client has:
    a name,
    the name of the bank they are a client of,
    the age of account in days,
    the starting amount of money and
    the current amount of money.
    """

    def __init__(self, name: str, bank: str, account_age: int, starting_amount: int, current_amount: int):
        """
        Client constructor.

        :param name: name of the client
        :param bank: the bank the client belongs to
        :param account_age: age of the account in days
        :param starting_amount: the amount of money the client started with
        :param current_amount: the current amount of money
        """
        self.name = name
        self.bank = bank
        self.account_age = account_age
        self.starting_amount = starting_amount
        self.current_amount = current_amount

    def __repr__(self):
        """
        Client representation.

        :return: clients name
        """
        return self.name

    def earnings_per_day(self):
        """
        Clients earnings per day since the start.

        You can either calculate the value or save it into a new attribute and return the value.
        """
        return float((self.current_amount-self.starting_amount)/self.account_age)


def read_from_file_into_list(filename: str) -> list:
    """
    Read from the file, make client objects and add the clients into a list.

    :param filename: name of file to get info from.
    :return: list of clients.
    """
    clientlist = []
    with open(filename,"r") as file:
        content = file.readlines()
        for line in content:
            info = line.strip().split(",")
            client = Client(info[0],info[1],int(info[2]),int(info[3]),int(info[4]))
            clientlist.append(client)
        return clientlist

def filter_by_bank(filename: str, bank: str) -> list:
    """
    Find the clients of the bank.

    :param filename: name of file to get info from.
    :param bank: to filter by.
    :return: filtered list of people.
    """
    clients_filtered_bybank = []
    with open(filename, "r") as file:
        content = file.readlines()
        for line in content:
            info = line.strip().split(",")
            if info[1] == bank:
                client = Client(info[0],info[1],int(info[2]),int(info[3]), int(info[4]))
                clients_filtered_bybank.append(client)
        return clients_filtered_bybank

def largest_earnings_per_day(filename: str) -> Optional[Client]:
    """
    Find the client that has earned the most money per day.

    If two people have earned the same amount of money per day, then return the one that has earned it in less time.
    If no-one has earned money (everyone has less or equal to wat they started with), then return None.
    :param filename: name of file to get info from.
    :return: client with largest earnings.
    """
    clientlist = read_from_file_into_list(filename)
    # Filter out clients who haven't earned any money
    clients_who_earned_money = [client for client in clientlist if client.current_amount > client.starting_amount]
    # If the list is empty return None
    if not clients_who_earned_money:
        return None
    # Sort clients by earnings per day (descending) and account age (ascending)
    clients_who_earned_money.sort(key=lambda client: (-client.earnings_per_day(), client.account_age))
    # Return the client with the highest earnings per day
    return clients_who_earned_money[0]

def largest_loss_per_day(filename: str) -> Optional[Client]:
    """
    Find the client that has lost the most money per day.

    If two people have lost the same amount of money per day, then return the one that has lost it in less time.
    If everyone has earned money (everyone has more or equal to what they started with), then return None.
    :param filename: name of file to get info from.
    :return: client with largest loss.
    """
    clientlist = read_from_file_into_list(filename)
    # Filter out clients who have lost money
    clients_who_lost_money = [client for client in clientlist if client.current_amount < client.starting_amount]
    # If everyone has earned money
    if not clients_who_lost_money:
        return None
    # Sort clients by earings per day(ascending) and by account age (ascending)
    clients_who_lost_money.sort(key=lambda client: (client.earnings_per_day, client.account_age))
    return clients_who_lost_money[0]
if __name__ == '__main__':
    print(read_from_file_into_list("clients_info.txt"))  # -> [Ann, Mark, Josh, Jonah, Franz]
    print(filter_by_bank("clients_info.txt", "Sprint"))  # -> [Ann, Mark]
    print(largest_earnings_per_day("clients_info.txt"))  # -> Josh
    print(largest_loss_per_day("clients_info.txt"))  # -> Franz
