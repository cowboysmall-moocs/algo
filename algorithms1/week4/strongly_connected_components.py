


def main(argv):
    file = open(argv[0])
    node_list = [element.strip('\t\r\n').split('\t') for element in file.readlines()]
    file.close()


if __name__ == "__main__":
    main(sys.argv[1:])
