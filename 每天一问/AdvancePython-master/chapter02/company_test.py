class Company(object):

    def __init__(self, name_list):
        self.name_list = name_list

    def __getitem__(self, item):
        return self.name_list[item]

    # def __len__(self):
    #     return 1


company = Company(["renl", "anj", "lvfei"])
print(type(company))
company1 = company[:2]
print(type(company1))
print(len(company1))

print(company[::-1])

