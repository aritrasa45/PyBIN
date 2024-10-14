import argparse
import os
import sys

"""
enter -h with the filename in terminal to know
more about this tool.
"""

parser = argparse.ArgumentParser(description='BinFetcheR How to use ------->>>')

parser.add_argument('filename', type=str, help='the url to fetch binary from ', default=None)

parser.add_argument('--debug', type=bool, help= 'to True or False verbose mode',  default =False)



parser.add_argument('--save', type=str, help= 'to save the output binary to any file as a text form',  default = None )

parser.add_argument('--save_type', type=str, help= 'the option to save binaries in the to [rb , ab , [w] ',  default = None )


args = parser.parse_args()



binaries = []
def binary_function():


    global binaries

    try:

        with open (args.filename,"rb") as f:
            contents = f.read()
            binaries.append(contents)


    except Exception as file_excp:
        print(file_excp)
        sys.exit(0)

    if not args.debug is None and args.debug is True:
        print(binaries[0])


    if not args.save is None:

        if not args.save_type is None:

            try:

                with open (args.save,str(args.save_type)) as save:
                    save.write(binaries[0])


            except Exception as e:
                print(e)
                sys.exit(0)

        else:
            print("No save_type applied")
            sys.exit(0)
                                                                                        

if __name__ == '__main__':
    binary_function()   
