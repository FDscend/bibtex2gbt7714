# 总体概况

BibTeX 是一套用于管理文献、产生文献目录的格式，通常与 LaTeX 一起使用。初始作者是 Oren Patashnik 与 Leslie Lamport，初始版本于 1985 年发布，稳定版于 2010 年发布。

BibTeX 被广泛使用，知网、万方、Elsevier 等数据库都支持下载

# 文件格式

BibTeX 文件名一般是以 bib 结尾，格式可以概括为：一个@开始，接一个参考的文献类型（如期刊、出版书籍等），用括号包住主体内容，包含作者、标题、时间、地址等内容。

具体来看几个例子

- 根据作者之一的 Oren Patashnik 于 1988 年的使用文档，BibTeX 的格式如下：

```r
@INPROCEEDINGS(no-gnats,
crossref = "gg-proceedings",
author = "Rocky Gneisser",
title = "No Gnats Are Taken for Granite",
pages = "133-139")
```

这里的 INPROCEEDINGS 表示这篇文献是会议论文集中的一篇，其它类型的见这个图，你可以截屏保存。

这里类型不区分大小写，你可以见到全大写、首字母大写、全小写。

值得注意的是，内容由圆括号包住，值用双引号包住

- 根据维基的例子，BibTeX 的格式如下：

```r
@Book{abramowitz+stegun,
 author    = "Milton {Abramowitz} and Irene A. {Stegun}",
 title     = "Handbook of Mathematical Functions with Formulas, Graphs, and Mathematical Tables",
 publisher = "Dover",
 year      =  1964,
 address   = "New York City",
 edition   = "ninth Dover printing, tenth GPO printing"
}
```

值得注意的是，这里是由花括号包住，同时出现了没被双引号包住的值（year）

- 我们随便从万方上找一篇期刊，下载其 BibTeX ，内容如下：

```py
 @article{干春晖 2011 中国产业结构变迁对经济增长和波动的影响,
author={干春晖 and 郑若谷 and 余典范},
title={中国产业结构变迁对经济增长和波动的影响},
organization={上海财经大学 and 上海财经大学},
journal={经济研究},
year={2011},
volume={46},
number={5},
pages={4-16,31},
month={1},
}
```

可以注意到，下载得到的是 txt 文件，而不是 bib 文件。不过都是纯文本，一样可以用文本编辑器打开。

主体内容的所有键值对，都用花括号（而不是双引号）包住值，同时多名作者依旧是用 and 连接

- 我们再从知网上随便找一篇期刊，下载 BibTeX 文件，内容如下：

```py
@article{JSYJ201208003,
 author = {孙志军,薛磊,许阳明 & 王正},
 title = {深度学习研究综述},
 journal = {计算机应用研究},
 volume = {29},
 number = 2806-2810,
 year = {2012},
 issn = {1001-3695},
 doi ={}
 }
```

注意到主体内容也是不用双引号包住值，而是使用花括号，以及 number 的值没有使用任何符号包住。

除此之外，多名作者之间使用的不是 and ，而是使用了逗号与 and 符号

- 还有像 Oxford Academic 这种，同时用双引号和花括号的：

```py
@article{10.1093/rfs/3.3.431,
    author = {Lo, Andrew W. and MacKinlay, A. Craig},
    title = "{Data-Snooping Biases in Tests of Financial Asset Pricing Models}",
    journal = {The Review of Financial Studies},
    volume = {3},
    number = {3},
    pages = {431-467},
    year = {2015},
    month = {04},
    abstract = "{Tests of financial asset pricing models may yield misleading inferences when properties of the data are used to construct the test statistics. In particular, such tests are often based on returns to portfolios of common stock, where portfolios are constructed by sorting on some empirically motivated characteristic of the securities such as market value of equity. Analytical calculations, Monte Carlo simulations, and two empirical examples show that the effects of this type of data snooping can be substantial.}",
    issn = {0893-9454},
    doi = {10.1093/rfs/3.3.431},
    url = {https://doi.org/10.1093/rfs/3.3.431},
    eprint = {https://academic.oup.com/rfs/article-pdf/3/3/431/24416126/030431.pdf},
}
```

# 标准不一致

- 总结以上内容，我们大概可以知道，BibTeX 是一种字典格式，但没有一个完全统一标准，不同渠道的文件可能存在表现不一致的情况。比如下面这个例子：

这篇论文在知网、万方都有收录，我们观察其 BibTeX 内容，可以发现 2806-2810 应当是页码，万方使用 pages 表示，而知网使用 number 表示 。万方用 number 表示第 8 期，而知网缺少了这一信息。

而根据 Oren Patashnik 的使用文档，应当用 pages 表示页码。

另外，万方使用 and 连接多名作者，知网使用逗号和 and 符号连接多名作者。知网的做法不是通用做法，可能不会被一些程序准确识别。

总的来说，万方提供的这份 BibTeX 文件相比知网的更加完善、符合一般规范。

- 但是，万方提供的 BibTeX 也存在一定问题，比如这个例子：

```py
@mastersthesis{朱建军 2005 层次分析法的若干问题研究及应用,
author={朱建军},
title={层次分析法的若干问题研究及应用},
school={东北大学},
year={2005},
type={博士论文},
month={},
}
```

这其实是篇博士论文，按照规范类型应当标记为 phdthesis ，而不是硕士论文的 mastersthesis 。不过说按照我国 GB7714-2015 标准，都统一为学位论文 D 了，实际使用中倒也看不出来问题

# 摘要换行

我又从 Elsevier 上随便找了篇论文下载 BibTeX 文件。这份文件内容更加完善，甚至还有链接、关键字、摘要，这三个都不在 Oren Patashnik 的使用文档中提及，应该算是 Elsevier 自己增加的内容。

观察格式能发现，所有值都用花括号包住，这点和万方一样，但是它的摘要换行了，不再遵循一个键值对一行的惯例，算是一个特点吧。（如果想写脚本解析就不能简单地按行读取键值对了）
