def minimum(list):
    if list:
        return min(list)
    else:
        return None


def greet(firstname, lastname=''):
    print(f"Hello {firstname} {lastname}")