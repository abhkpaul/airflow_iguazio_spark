
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


# def igz_func_jobb():
#     jobB.main()

import sys
# sys.path.insert(0, '/v3io/projects/sparksimulation/spark_igz-1.0-py3.8.egg')

# exec('from {} import {}'.format(module[0], module[2]))
# exec('{}(**kwargs)'.format(module[2]))
# import jobA

# if __name__ == '__main__':
#     print("This runs before the spark context!")
#
#     jobA.main()
#
#     print("This runs after the job call")


# igz_func_jobb()
# globals()[sys.argv[1]](sys.argv[2])