from factory import ParserFactory

def main():
    file_format = input("Write file format (json/xml/csv): ")

    data = input("Paste data for report: ")

    parser = ParserFactory.get_parser(file_format)
    result = parser.parse(data)

    print("Result: ")
    print(result)


if __name__ == "__main__":
    main()