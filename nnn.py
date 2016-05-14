from SimpleImage import read_image

DOC_TEMPLATE = """
<!DOCTYPE html>
<html>
    <head>
        <title>A tabular Floyd</title>
        <meta charset="UTF-8">
    </head>
    <body>
       <h1>I'm in your table!</h1> 
       %s
    </body>
</html>
"""

def make_table_data(intensity):
    return '<td style="background-color:rgb(%s, %s, %s)' \
           ';width:5px;height:5px"></td>' % \
           (intensity, intensity, intensity)

def make_table_row(data):
    row_data = []
    for item in data:
        row_data.append(make_table_data(item))
    return '<tr>' + ''.join(row_data) + '</tr>'

def make_table(rows):
    rows_html = []
    for row_data in rows:
        rows_html.append(make_table_row(row_data))
    return '<table style="padding:0px;border:0px;' \
           'border-spacing:0px">' + '\n'.join(rows_html) + '</table>'

def main():
    image = read_image("floyd.png")
    table = make_table(image)
    html_doc = DOC_TEMPLATE % table
    out_file = open("floyd.html", "w")
    out_file.write(html_doc)
    out_file.close()

main()