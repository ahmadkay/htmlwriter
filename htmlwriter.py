# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 06:20:20 2019

@author: Windows10
"""
def startdoc():
    """start the document
    -----
    
    >>print(startdoc())
    <!DOCTYPE html>
        
    """
    ...
    return """<!DOCTYPE html>\n"""

def starthtml(lang="en"):
    """start the html default language is english
    -----
    
    >>print(starthtml())
    <html lang="en">
    
    """
    ...
    return """<html lang="{0}">\n""".format(lang)
def endhtml():
    """at the end of document to close the html tag
    -----

    >>print(endhtml())
    </html>

    """
    ...
    return """</html>\n"""

def websiteTitle(text=""):
    """set the title of the website in the head tag
    -----
    
    >>print(websiteTitle("Example Website Home"))
    <title>Example Website Home</title>

    """
    ...
    return """<title>{0}</title>\n""".format(text)

def style(text=""):
    """if you want to have style in the main doc and have css there
    -----
    >>teststyle = "body{
                color:red
                }"
    >>print(style(teststyle))
    <style>
    body{
    color:red
    }
    </style>

    """
    ...
    return """<style>\n{0}\n</style>\n""".format(text)
def script(text=""):
    """if you want to have script in the main doc and have JS there
    -----
    
    >>testscript= "var tday = new Date;"
    >>print(script(testscript))
    <script>
    var tday = new Date;
    </script>

    """
    ...
    return """<script>\n{0}\n</script>\n""".format(text)

def headlink(rel="",href="",extra=[]):
    """add link in the head
    ----
    
    >>print(headlink("stylesheet","css/stylesheet.css"))
    <link rel="stylesheet" href="css/stylesheet.css" />
    
    """
    ...
    return """<link rel="{0}" href="{1}" {2}/>\n""".format(rel,href," ".join(extra))

def base(href="",target=""):
    """add base link in head
    -----

    >>print(base("localhost:example.com/","_blank"))
    <base href="localhost:example.com/" target="_blank"/>
    
    """
    ...
    return """<base href="{0}" target="{1}"/>\n""".format(href,target)

def meta(extra=[]):
    """make meta tags.
    typical meta tags for a website are:
    charset="UTF-8"
    name="description" content="Free Web tutorials"
    name="keywords" content="HTML, CSS, XML, JavaScript"
    name="author" content="John Doe"
    name="viewport" content="width=device-width, initial-scale=1.0"
    
    -----

    >>print(meta(['charset="UTF-8"']))
    <meta charset="UTF-8"/>
    
    >>print(meta(['name="viewport"', 'content="width=device-width, initial-scale=1.0"']))
    <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
    
    """
    ...
    return """<meta {0}/>\n""".format(" ".join(extra))

def head(items=[]):
    """head tag. you can add all the meta and base and links or scripts and styles as a list
    otherwise it just prints the empty head
    -----
    
    >>print(head())
    <head>
    </head>
    
    
    >>print(head([base("localhost:example.com/","_blank"),
            headlink("stylesheet","css/stylesheet.css"),
            style(teststyle),
            script(testscript)]
            ))
    <head>
    <base href="localhost:example.com/" target="_blank"/>
    <link rel="stylesheet" href="css/stylesheet.css" />
    <style>
    body{
    color:red
    }
    </style>
    <script>
    var tday = new Date;
    </script>
    </head>
    
    """
    ...
    head = """<head>\n"""
    for item in items:
        head += """{0}""".format(item)
    head += """</head>\n"""
    return head


def startbody(extra=[]):
    """starts the body tag. you can add id or class in the extra
    -----
    
    >>print(startbody(['class="sampleclass"']))
    <body class="sampleclass">
        
    """
    ...
    return """<body {0}>\n""".format(" ".join(extra))

def endbody():
    """end the body tag
    -----
    
    >>print(endbody())
    </body>
        
    """
    ...
    return """</body>\n"""


def heading(text="",size=1,extra=[]):
    """make the text surrounded by h tag
    size can be 1 - 6
    you can add id or class in extras
    -----
    
    >>print(heading("hello world"))
    <h1 >hello world</h1>
    
    >>print(heading("hello world",3))
    <h3 >hello world</h3>

    """
    ...
    return """<h{1} {2}>{0}</h{1}>\n""".format(text,size," ".join(extra))

def paragraph(text="",extra=[]):
    """make the text surrounded by p tag
    
    -----
    
    >>print(paragraph("this is the first paragraph and an exmaple."))
    <p >this is the first paragraph and an exmaple.</p>
        
    """
    ...
    return """<p {1}>{0}</p>\n""".format(text," ".join(extra))
    
def span(text="",extra=[]):
    """make the text surrounded by span tag
    
    -----
    
    >>>>print(span("word",['id="idforlater"']))
    <span id="idforlater">word</span>
    
    """
    ...
    return """<span {1}>{0}</span>""".format(text," ".join(extra))

def multi_paragraph(text="",delimiter="\n",extra=[]):
    """seperates paragraphs based on delimiter and then
    make each text surrounded by p tag
    -----

    >>print(multi_paragraph("this is a text;it can be anything;",";"))
    <p >this is a text</p>
    <p >it can be anything</p>
    
    """
    ...
    text = text.split(delimiter)
    paragraphs = ""
    for p in text:
        if p != "":
            paragraphs += """<p {1}>{0}</p>\n""".format(p," ".join(extra))
    return paragraphs

def pre(text="",extra=[]):
    """make the text surrounded by pre tag
    -----
    
    >>print(pre("print this text
            as is and don't 
                  correct their spaces
              just like
                 a
             poem"))
    <pre >
    print this text
    as is and don't 
          correct their spaces
      just like
         a
     poem
    </pre>
    
    """
    ...
    return """<pre {1}>\n{0}\n</pre>\n""".format(text," ".join(extra))

   
def br(count=1):
    """adds multiple line breaks
    -----

    >>print(br(5))
    <br/>
    <br/>
    <br/>
    <br/>
    <br/>
  
    """
    ...
    line_break = ""
    for x in range(count):
        line_break += """<br/>\n"""
    return line_break

def hr(count=1):
    """adds multiple horizental lines
    -----
    
    >>print(hr(2))
    <hr/>
    <hr/>
    
    """
    ...
    h_line = ""
    for x in range(count):
        h_line += """<hr/>\n"""
    return h_line

def link(text="",url="",target="_blank",extra=['title=""']):
    """makes the text a link
    targets: _blank, _self , _parent, _top
    -----
    
    >>print(link("here","https://www.google.com"))
    <a href="https://www.google.com" target="_blank" title="">here</a>
    
    """
    ...
    return """<a href="{1}" target="{2}" {3}>{0}</a>""".format(text,url,target," ".join(extra))


def image(src="",alt="",width="",height="",extra=[]):
    """makes the src an image
    -----
    
    >>print(image("/cat.png","picture of cat","250px","500px"))
    <img src="/cat.png" alt="picture of cat" width="250px" height="500px" />
    
    """
    ...
    return """<img src="{0}" alt="{1}" width="{2}" height="{3}" {4}/>\n""".format(src,alt,width,height," ".join(extra))

def ordered_list(list_type="1",items=[],extra=[]):
    """list_types = 1, A, a, i , I
    -----
    
    >>print(ordered_list("a",["animal","humans","aliens"]))
    <ol type="a" >
    <li>animal</li>
    <li>humans</li>
    <li>aliens</li>
    </ol>    
    
    """
    ...
    olist = """<ol type="{0}" {1}>\n""".format(list_type," ".join(extra))
    for item in items:
        olist += """<li>{0}</li>\n""".format(item)
    olist += """</ol>\n"""
    return olist

def unordered_list(items=[],extra=[]):
    """makes an unordered list
    -----
    
    >>print(unordered_list(["cat","dog","sheep"]))
    <ul >
    <li>cat</li>
    <li>dog</li>
    <li>sheep</li>
    </ul>
    
    """
    ...
    ulist = """<ul {0}>\n""".format(" ".join(extra))
    for item in items:
        ulist += """<li>{0}</li>\n""".format(item)
    ulist += """</ul>\n"""
    return ulist

def bold(text=""):
    """make the text bold"""
    ...
    return """<b>{0}</b>""".format(text)

def strong(text=""):
    """make the text strong"""
    ...
    return """<strong>{0}</strong>""".format(text)
        
def italic(text=""):
    """make the text italic"""
    ...
    return """<i>{0}</i>""".format(text) 

def emphasize(text=""):
    """make the text emphasized"""
    ...
    return """<em>{0}</em>""".format(text) 

def mark(text=""):
    """make the text highlighted"""
    ...
    return """<mark>{0}</mark>""".format(text) 

def small(text=""):
    """make the text small"""
    ...
    return """<small>{0}</small>""".format(text) 

def big(text=""):
    """make the text big"""
    ...
    return """<big>{0}</big>""".format(text) 

def subscript(text=""):
    """make the text subscript"""
    ...
    return """<sub>{0}</sub>""".format(text) 

def superscript(text=""):
    """make the text superscript """
    ...
    return """<sup>{0}</sup>""".format(text) 

def delete(text=""):
    """draw a line over the text"""
    ...
    return """<del>{0}</del>""".format(text)

def insert(text=""):
    """draw a line under the text"""
    ...
    return """<ins>{0}</ins>""".format(text)

def quote(text=""):
    """quote the text"""
    ...
    return """<q>{0}</q>""".format(text)

def block_quote(text="",cite=""):
    """quote the block of text"""
    ...
    return """<blockquote cite="{1}">\n{0}\n</blockquote>\n""".format(text,cite)

def abbr(text="",title=""):
    """abbriviates the text with a title"""
    ...
    return """<abbr title="{1}">{0}</abbr>""".format(text,title)

def address(items=[],extra=[]):
    """writes the address with breaks at the end of each line
    -----
    
    >>print(address(["New york","USA","96584","001232145687"]))
    <address >
    New york<br/>
    USA<br/>
    96584<br/>
    001232145687<br/>
    </address>
    
    """
    ...
    addr = """<address {0}>\n""".format(" ".join(extra))
    for item in items:
        addr += """{0}<br/>\n""".format(item)
    addr += """</address>\n"""
    return addr

def cite(text=""):
    """cite the text"""
    ...
    return """<cite>{0}</cite>""".format(text)
 
    
def comment(text=""):
    """comment the text
    -----
    
    >>print(comment("This is a commentline in the html file"))
    <!-- This is a commentline in the html file -->

    """
    ...
    return """<!-- {0} -->""".format(text)

def table_row(items=[],extra=[]):
    """gets table_head and table_col and make a table row
    
    -----
    
    >>head = table_head("Data")
    >>head2= table_head("Price")
    >>print(table_row([head,head2]))
    <tr >
    <th >Data</th>
    <th >Price</th>
    </tr>
            
    """
    ...
    row = """<tr {0}>\n""".format(" ".join(extra))
    for item in items:
        row += """{0}""".format(item)
    row += """</tr>\n"""
    return row


def table_head(text="",extra=[]):
    """makes a table head"""
    ...
    return """<th {1}>{0}</th>\n""".format(text," ".join(extra))


def table_col(text="",extra=[]):
    """make a table column"""
    ...
    return """<td {1}>{0}</td>\n""".format(text," ".join(extra))

def table(items=[],extra=[]):
    """gets rows and makes a table
    
    -----

    >>head = table_head("Data")
    >>head2= table_head("Price")   
    >>data1 = table_col("rice")
    >>price1 = table_col("30 EUR")
    >>row1= table_row([data1,price1])
    >>row2= table_row([head,head2]) 
    >>print(table([row2,row1]))
    <table >
    <tr >
    <th >Data</th>
    <th >Price</th>
    </tr>
    <tr >
    <td >rice</td>
    <td >30 EUR</td>
    </tr>
    </table> 
     
    """
    ...
    tb = """<table {0}>\n""".format(" ".join(extra))
    for item in items:
        tb += """{0}""".format(item)
    tb += """</table>\n"""
    return tb

def empty_table(rows=3,cols=2,header=True,extra=[]):
    """makes a table with no data
    -----
    
    >>print(empty_table(3,3,True))
    <table >
    <tr>
    <th></th>
    <th></th>
    <th></th>
    </tr>
    <tr>
    <td></td>
    <td></td>
    <td></td>
    </tr>
    <tr>
    <td></td>
    <td></td>
    <td></td>
    </tr>
    <table>
    
    """
    ...
    tbl = """<table {0}>\n""".format(" ".join(extra))
    for row in range(rows):
        tbl+= """<tr>\n"""
        for col in range(cols):
            if header==True and row == 0:
                tbl+= """<th></th>\n"""
            else:
                tbl+= """<td></td>\n"""
        tbl+= """</tr>\n"""
    tbl += """<table>\n"""
    return tbl

def div(items=[],extra=[]):
    """writes the the itmes inside the div
    -----
    
    >>header = heading("this is heading")
    >>par = paragraph("this is paragraph")
    >>mydiv = div([header,par])
    >>print(mydiv)
    <div>
    <h1>this is heading</h1>
    <p>this is paragraph</p>
    </div>
    """
    ...
    div = """<div {0}>\n""".format(" ".join(extra))
    for item in items:
        div += """{0}""".format(item)
    div += """</div>\n"""
    return div

def nav(items=[],delimiter="|",extra=[]):
    """writes the the itmes inside the nav seperated by delimiter
    -----
    
    >>link1 = link("home","/home")
    >>link2 = link("contact","/contact")
    >>link3 = link("about us","/about us")
    >>print(nav([link1,link2,link3]))
    <nav>
    <a href="/home" target="_blank" title="">home</a> |
    <a href="/contact" target="_blank" title="">contact</a> |
    <a href="/about us" target="_blank" title="">about us</a>
    </nav>
    """
    ...
    nav = """<nav {0}>\n""".format(" ".join(extra))
    for i in range(len(items)):
        if i != len(items)-1:
            nav += """{0} {1}\n""".format(items[i],delimiter)
        else:
            nav += """{0}\n""".format(items[i])
    nav += """</nav>\n"""
    return nav


def form_input(input_type="text",name="username",extra=[]):
    """makes an input for a form, you can add extra's as well.
    -----

    >>print(form_input(input_type="password",name="pass",extra=['value=""']))
    <input type="password" name="pass" value=""/>
    
    """
    ...
    return """<input type="{0}" name="{1}" {2}/>\n""".format(input_type,name," ".join(extra))

def label(text="",label_for="",extra=[]):
    """makes a label.
    -----
    
    >>print(label("User Name:","username"))
    <label for="username" >User Name:</label>
    
    """
    ...
    return """<label for="{1}" {2}>{0}</label>\n""".format(text,label_for," ".join(extra))


def form(action="",method="get",extra=[],items=[]):
    """Creates a form and gets form_inputs in a list
    -----
    
    >>print(form("/otherpage.html","POST",items=[form_input("text","username"),form_input("password","password")]))
    <form action="/otherpage.html" method="POST" >
    <input type="text" name="username" />
    <input type="password" name="password" />
    </form>    
    
    """
    ...
    f = """<form action="{0}" method="{1}" {2}>\n""".format(action,method," ".join(extra))
    for item in items:
        f += """{0}""".format(item)
    f += """</form>\n"""
    return f

def button(text="",btn_type="button",extra=[]):
    """makes a button
    -----
    
    >>print(button('click me','submit'))
    <button type="submit" >click me</button>
    
    """
    ...
    return """<button type="{1}" {2}>{0}</button>\n""".format(text,btn_type," ".join(extra))
    
def option(text="",value="",extra=[]):
    """makes an option. """
    ...
    return """<option value="{1}" {2}>{0}</option>\n""".format(text,value," ".join(extra))


def select(extra=[],items=[]):
    """makes a select. you can pass options as a list
    -----
    
    >>print(select(items=[option("BMW","1"),option("BMW RED","2")]))
    <select >
    <option value="1" >BMW</option>
    <option value="2" >BMW RED</option>
    </select>
    
    """
    ...
    f = """<select {0}>\n""".format(" ".join(extra))
    for item in items:
        f += """{0}""".format(item)
    f += """</select>\n"""
    return f

def textarea(rows="5",cols="50",text="",extra=[]):
    """make a text area
    -----
    
    >>print(textarea(10,30,"THis is a sample text"))
    <textarea rows="10" cols="30" >
    THis is a sample text
    </textarea>
    
    """
    ...
    return """<textarea rows="{1}" cols="{2}" {3}>\n{0}\n</textarea>\n""".format(text,rows,cols," ".join(extra))

def video(width="250",height="100",src="",text="",extra=[]):
    """make a html video
    -----
    
    >>print(video("400","600","/video.ogg","Your browser does not support the video tag."))
    <video width="400" height="600" src=/video.ogg controls>
    Your browser does not support the video tag.
    </video>
    
    """
    ...
    return """<video width="{1}" height="{2}" src={3} controls {4}>\n{0}\n</video>\n""".format(text,width,height,src," ".join(extra))

def audio(src="",text="",extra=[]):
    """make a html audio
    -----
    
    >>print(audio("/audio.wav","Your browser does not support the audio element."))
    <audio src=/audio.wav controls >
    Your browser does not support the audio element.
    </audio>
    
    """
    ...
    return """<audio src={1} controls {2}>\n{0}\n</audio>\n""".format(text,src," ".join(extra))




