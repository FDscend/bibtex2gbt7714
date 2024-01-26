import bib2GBT
import sys
import os


if __name__ == "__main__":
    bibFileDic = sys.argv[1]
    save2file = sys.argv[2]

    lines = []
    files = []

    for filepath,dirnames,filenames in os.walk(bibFileDic):
        for filename in filenames:
            file_path = os.path.join(filepath,filename)
            
            files.append("\n原始文件名：" + file_path + '\n')
            _count = 1
            for l in bib2GBT.mainProscess(file_path):
                lines.append(l)     
                files.append(f'[{_count}] ' + l + '\n')
                _count += 1

            # lines.append(bib2GBT.mainProscess(file_path))
            # files.append("原始文件名：" + file_path + '\n')
            # files.append(bib2GBT.mainProscess(file_path) + '\r\n')


    if save2file == "true":
        with open("output_GBT7714.txt", "w", encoding='utf-8') as f:
            for l in files:
                f.write(l)
    else: 
        count = 1
        for l in lines:
            print(f'[{count}]', l)
            count += 1
    