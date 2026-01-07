import sys

def check_result(marks):
    if marks >= 75:
        return "Distinction"
    elif marks >= 40:
        return "Pass"
    else:
        return "Fail"


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide marks")
        sys.exit(1)

    marks = int(sys.argv[1])
    result = check_result(marks)
    print(result)
