#!/usr/bin/python
from configparser import ConfigParser

full_path = "/Users/sisayfilate/Documents/sfilate/workspace/python-for-data-analyst/week-3/day-8-pandas-continued/database.ini"
# print("full path: ", full_path)


def config(filename=full_path, section="postgresql"):
    # create a parser
    parser = ConfigParser()

    # read config file
    # section = "postgresql"
    parser.read(filename)
    db = {}
    if parser.has_section(section):
        # if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception(
            "Section {0} is not found in the {1} file.".format(section, filename)
        )
    # print(db)

    return db


# invoc the config function
# config()
