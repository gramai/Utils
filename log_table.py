"""
log_table(line_length, text, table_name, *args):
Functionality: Logs given parameters as a table.

Parameters: 
    - line_length = the size (in characters) of each line of the table
    - text = Text to be printed before the table, as a description
    - table_name = Name of the table that is showed on the first row
    - *args = arguments passed as a tuple of tupples
        e.g.: table_args = (("Company: ", "S.C. Iasi Fier"),
                            ("Subcompany: ", "S.C. Iasi Fier Manufacturi"),
                            ("Amount: ", str(6.55))
                            )
        OBS. all parameters MUST BE strings

Example output for log_table(55,"Passing to the next company",
                             "Billing Details", *table_args)
                             
    2018-07-26 13:57:42,418: INFO: Passing to next company...
    --------------------Billing Details--------------------
    Company:                                 S.C. Iasi Fier 
    Subcompany:                  S.C. Iasi Fier Manufacturi 
    Amount:                                            6.55 
    -------------------------------------------------------

"""


def log_table(line_length,
              text,
              table_name,
              *args,
              export_format='log'):
    table_string = "'" + text + "' + '\\n' + "
    table_string += "'{:-^" + str(line_length) + "}'.format('" + table_name + "') +'"
    for i in range(0, len(args)):
        table_string += "{" + str(3 * i) + ":<0}" + \
                        " {" + str(3 * i + 1) + ": >{" + str(3 * i + 2) + "}} "
    table_string += "'.format("
    for i in range(0, len(args) - 1):
            table_string += "'\\n" + args[i][0] + "', '" + args[i][1] + "', " + str(line_length - len(args[i][0]) - 1) + ", "
    # For last argument of the list
    if len(args) > 1:
        i += 1
    else:
        i = 0
    table_string += "'\\n" + args[i][0] + "', '" + args[i][1] + "', " + str(line_length - len(args[i][0]) - 1) + ") + "
    table_string += "'\\n' + "
    table_string += "'{:-^" + str(line_length) + "}'.format('')" + " + '\\n'"
    if export_format == 'string':
        return table_string
    elif export_format == 'both':
        logger.info(eval(table_string))
        return eval(table_string)
    else:
        logger.info(eval(table_string))
