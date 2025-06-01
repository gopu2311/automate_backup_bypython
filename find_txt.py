def search_the_keyword(file_path,keyword):
    with open(file_path,'r') as file:
        for line_number , line in enumerate(file,start=1):
            if keyword in line:
                print(f"found the key word on line {line_number}:{line.strip()}")
file_path =
keyword = 
search_the_keyword(file_path,keyword)
