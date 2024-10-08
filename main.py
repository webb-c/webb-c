import feedparser, time

URL = "https://webb-c.tistory.com/rss"
RSS_FEED = feedparser.parse(URL)
MAX_POST = 3

markdown_text = """
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-


class Researcher:

    def __init__(self):
        self.name = "Vaughan Sohn"
        self.role = "Researcher"
        self.major = "Computer Science and Engineering"
        self.interest = {
            research=["Quantum Computing", "Optimization Theory", "Reinforcement Learning"],
            others=["Astronomy", "Quantum Physics"]
        }

    def callout(self):
        print("우주의 아름다움도 다양한 지식을 접하며 스스로의 생각이 짜여나갈 때 불현듯 나를 덮쳐오리라.")


me = Researcher()
me.callout()
```
### Hi, there 👋
- 🔭 I'm currently studying quantum computing in KAIST.
- 💡 Tech Blog: https://webb-c.tistory.com/
- 📮 How to reach me: webb41@kaist.ac.kr
- 🚀 [Resume](http://webb-c.github.io/files/CV.pdf) (Last Updated: August 2024)

#### Languages and Tools:
![Python](https://img.shields.io/badge/-Python-black?logo=Python&style=social)&nbsp;&nbsp;
![C](https://img.shields.io/badge/c-%2300599C.svg?style=social&logo=c)&nbsp;&nbsp;
![C++](https://img.shields.io/badge/c++-%2300599C.svg?style=social&logo=c%2B%2B)&nbsp;&nbsp;
![PyTorch](https://img.shields.io/badge/PyTorch-%23EE4C2C.svg?style=social&logo=PyTorch)&nbsp;&nbsp;
![Qiskit](https://img.shields.io/badge/Qiskit-%236929C4.svg?style=social&logo=Qiskit)&nbsp;&nbsp;
![LaTeX](https://img.shields.io/badge/latex-%23008080.svg?style=social&logo=latex)&nbsp;&nbsp;
<a href="https://solved.ac/profile/jwst0210"><img src="http://mazassumnida.wtf/api/mini/generate_badge?boj=jwst0210"/></a>

#### Latest Updated Post:
"""

for idx, feed in enumerate(RSS_FEED['entries']):
    if idx >= MAX_POST:
        break
    else:
        feed_date = feed['published_parsed']
        markdown_text += f"[{time.strftime('%Y/%m/%d', feed_date)} - {feed['title']}]({feed['link']}) <br/>\n"
        
f = open("README.md", mode="w", encoding="utf-8")
f.write(markdown_text)
f.close()
