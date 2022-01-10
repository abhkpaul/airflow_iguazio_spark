
from mlrun import get_or_create_ctx

if __name__ == '__main__':
    context = get_or_create_ctx("iguazio")
    sparkPackage = context.get_param("spark_package")
    sparkModule = context.get_param("spark_module")
    sparkFunction = context.get_param("spark_function")
    sparkFunctionParam = context.get_param("spark_function_param")
    print('IMPORTING {} FROM {}'.format(sparkModule,sparkPackage))
    exec('from {} import {}'.format(sparkPackage,sparkModule))
    print('EXECUTING FUNCTION : {}'.format(sparkFunction))
    eval('{}.{}()'.format(sparkModule,sparkFunction,sparkFunctionParam))


