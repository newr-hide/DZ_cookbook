
def the_reader(original_file):
    tmp_sourse = []
    for file in original_file:
        with open(file,"r", encoding="utf-8") as source:
            text_in_source = source.readlines()
            length_text = len(text_in_source)
            tmp_sourse.append([length_text,file,text_in_source])
    sort_text = sorted(tmp_sourse)

    for list_text in sort_text:
         with open("result.txt", "a", encoding="utf-8") as file:
             print(list_text[1],list_text[0],list_text[2],file=file, sep="\n")


the_reader(["1.txt","2.txt","3.txt"])
