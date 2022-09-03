import os

    def datasets_per_tag(tag):
        df = pandas.read_excel(os.getcwd()+'/file/tags-datasets.xlsx')
    my_list = df[lambda x: ~pandas.isnull(x[tag])][tag]
    pattern = re.compile(r'\s+')
    s = my_list.to_string(index=False).replace('\n',',')
    return(print(pattern.sub(' ', s)))



