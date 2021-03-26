import utils
import sys

def main():
   
    command = sys.argv[1]
    if command == 'build':
        utils.all_html()
    elif command == 'new':
        utils.create_new_page()
    
if __name__ == '__main__':
    main()