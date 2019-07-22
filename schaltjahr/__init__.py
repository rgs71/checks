import check50
import random


@check50.check()
def exists():
    """Check for files"""
    check50.exists("leapyear.py")
    check50.exisis("main.py")


@check50.check(exists)
def nicht_schaltjahr():
    """Überprüfe einige nicht Schaltjahre"""
    for tc in range(10):
        a = 400 * random.randint(0, 10)
        b = 100 * random.randint(1, 4)
        c = 4 * random.randint(1, 25)
        d = random.randint(1, 4)
        check50.run("python3 main.py").stdin(f"{a}").stdout(
            f"Das Jahr {a} ist ein Schaltjahr.", regex=False
        ).exit(0)
        check50.run("python3 main.py").stdin(f"{a+b}").stdout(
            f"Das Jahr {a+b} ist kein Schaltjahr.", regex=False
        ).exit(0)
        check50.run("python3 main.py").stdin(f"{a+b+c}").stdout(
            f"Das Jahr {a+b+c} ist ein Schaltjahr.", regex=False
        ).exit(0)
        check50.run("python3 main.py").stdin(f"{a+b+c+d}").stdout(
            f"Das Jahr {a+b+c+d} ist kein Schaltjahr.", regex=False
        ).exit(0)

