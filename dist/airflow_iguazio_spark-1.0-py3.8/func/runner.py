# import sys
# sys.path.insert(0, '/v3io/projects/sparksimulation/spark_igz-1.0-py3.8.egg')
from modules import jobA
def runJobaA():
    jobA.main()


# import jobA

# if __name__ == '__main__':
#     print("This runs before the spark context!")
#
#     jobA.main()
#
#     print("This runs after the job call")