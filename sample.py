import htmlwriter as hw

g = open("sample.html","w")


g.write(hw.startdoc())
g.write(hw.starthtml())
meta1 = hw.meta(['charset="UTF-8"'])
meta2 = hw.meta(['name="viewport"', 'content="width=device-width, initial-scale=1.0"'])
meta3 = hw.meta(['http-equiv="X-UA-Compatible"','content="ie=edge"'])
meta4 = hw.meta(['name="description"','content="Sample website with htmlwriter python library"'])
meta5 = hw.meta(['name="keywords"','content="sample,example,python"'])
meta6 =hw.meta(['name="author" content="Amir Kamizi"'])
website_title = hw.websiteTitle("Sample Website")
g.write(hw.head([meta1,meta2,meta3,meta4,meta5,meta6,website_title]))
g.write(hw.startbody())

g.write(hw.heading("Heading 1"))
g.write(hw.paragraph("A simple description paragraph that can go on and on"))

g.write(hw.hr())
g.write(hw.paragraph("text with a "+hw.bold("bold word")+" and one "+hw.italic("italic word")))
g.write(hw.paragraph("3 break lines with just "+hw.insert("ONE LINE OF CODE")))
g.write(hw.br(3))

g.write(hw.link("a simple link to my website","amirkamizi.com",target="_blank"))
g.write(hw.br())
g.write(hw.link("link to this python library","https://github.com/amirkamizi/htmlwriter",target="_self"))
items = []
items.append("empty table")
items.append("form inputs and forms")
items.append("table cols,table rows and table heads")
items.append("unordered and ordered lists")
items.append("image and videos")
items.append("multi paragraph with any delimiter")
items.append("and many other things you should try")
g.write(hw.heading("What can you do",4))
g.write(hw.unordered_list(items))
g.write(hw.endbody())
g.write(hw.endhtml())


g.close()