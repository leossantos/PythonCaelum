def teste_args_kwargs(arg1, arg2, arg3):
    print("arg1: ", arg1)
    print("arg2: ", arg2)
    print("arg3: ", arg3)


kwargs = {'arg3': 3, 'arg2': 'dois', 'arg1': 'um', 'arg4': 7}
teste_args_kwargs(**kwargs)
