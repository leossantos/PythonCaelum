class Conta:
    pass

    #Em outro arquivo:
    from conta import Conta

    conta = Conta()
    print(type(conta))
    #<class '__main__.Conta'>