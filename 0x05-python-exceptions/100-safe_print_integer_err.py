#!/usr/bin/python3

def safe_print_integer_err(value):
    import sys

    ret = False
    try:
        print("{:d}".format(value))
    except ValueError as e:
        print(e, file=sys.stderr)
    except TypeError as e:
        print(e, file=sys.stderr)
    else:
        ret = True
    finally:
        return ret
