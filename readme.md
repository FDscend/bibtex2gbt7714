# 简介

本项目使用 Python 将 BibTeX 文件转换为 GB/T7714-2015 格式，支持可视操作、单一命令行、批量命令行

# 使用

## 方式一：使用 `bib2GBT.ipynb` 进行可视操作

只需将第二个代码块的 `bibFile` 的值改成 bib 文件地址，然后点击全部运行，即可在最后一个代码块下面看到输出结果

## 方式二：使用 `bib2GBT.py` 进行命令行操作

在终端输入 `python bib2GBT.py 单一文件路径`，如 `python bib2GBT.py 'test/2-3.bib'` ，即可在终端打印结果

## 方式三：使用 `bib2GBT_2.py` 进行命令行批量操作

将所有 BibTeX 文件放到同一个文件夹中（该文件夹中不能含 BibTeX 以外格式的文件，否则报错），在终端输入 ` python bib2GBT.py 文件夹路径 参数`

- 如 `python bib2GBT_2.py 'test' 'true'` ，即可将 test 文件夹中所有文件当作 BibTeX 转换，并将结果保存到 output_GBT7714.txt
- 如 `python bib2GBT_2.py 'test' 0` ，即可将 test 文件夹中所有文件当作 BibTeX 转换，并在终端打印结果

# 注意事项

1. 代码使用了 `match ... case` ，需要 Python 3.10+ 才能运行
2. 本项目是 [GitHub - FDscend/fdscend_word_addin: 在 Word 中一键实现代码排版，附一些实用小功能](https://github.com/FDscend/fdscend_word_addin) 的子项目，BibTeX 的转换已经作为实验性功能加入。如果你使用 Word，可以通过这个插件一键实现 BibTeX 的转换。
3. 各家的 BibTeX 格式不完全一致，实际使用中可能会遇到转换错误。反馈 bug 时请附带 BibTeX 文件及出处（比如来自知网、万方）
