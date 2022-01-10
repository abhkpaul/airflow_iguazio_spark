
def SendEmail(school,standard,name,city):
    print(school)
    print(standard)
    print(name)
    print(city)

def main():
    # op_kwargs = {'key1': 'value1', 'key2': 'value2'},
    # SendEmail(op_kwargs)

    data = {'school': 'DAV', 'standard': '7', 'name': 'abc', 'city': 'delhi'}
    SendEmail(**data)

if __name__ == '__main__' : main()