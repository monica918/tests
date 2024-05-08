过滤关键字（完全匹配模式）并查看前 10 行 -w(whole 完全匹配) -C(context 上下文)
grep -w "your_keyword" your_file.log | head -n 10


过滤关键字（完全匹配模式）并查看每个匹配行的前后 10 行
grep -w -C 10 "your_keyword" your_file.log


过滤关键字（完全匹配模式）并查看最后 10 行
grep -w "your_keyword" your_file.log | tail -n 10


