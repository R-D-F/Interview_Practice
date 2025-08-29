# Q1. List comprehensions and filtering
# Given a list of file sizes (in KB):
# 👉 Write a function that returns all files larger than 15,000 KB.


def get_files_over_kb(kb: int, files: list) -> list:
    """returns file sizes (kb) greater than kb"""
    output = []
    for i in files:
        if i > kb:
            output.append(i)
    return output


file_sizes = [1050, 15800, 800, 25000, 13400, 500]

print(get_files_over_kb(15000, file_sizes))
