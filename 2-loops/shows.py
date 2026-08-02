shows= [
    "hello ",
    " hello my lovely",
    "world IS amazing  "
]

def main():
    cleaned = [title.strip().title() for title in shows]
    print(', '.join(cleaned))


main()