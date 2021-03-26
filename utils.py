import glob
from jinja2 import Template

def build_html():

    pages = []
    template_html = []

    html_pages = glob.glob("./content/*.html")

    if './content/index.html' in html_pages and './content/about.html' in html_pages:
    
        for index, page in enumerate(html_pages, 0):
          
            page_name = page[10:-5]
        
            pages.append({
                'input_file' : page,
                'title' : page_name,
                'output_file' : f'./docs/{page_name}.html',
                })

        for page in pages:
            template_html.append({
                'title' : page['title'],
                })
    
    return (pages, template_html)

def build_page(pages, template_html):
    
    template = Template(open('./templates/base.html').read())
    for index, page in enumerate(pages):
       
        with open(page['input_file']) as html:
            content = html.read()

        result = template.render({
            'title' : page['title'],
            'template_html' : template_html,
            'content' : content,
        })

        with open(page['output_file'], 'w+') as html:
            html.write(result)

  
def all_html():
    (pages, template_html) = build_html()
    build_page(pages, template_html)
  
def create_new_page():
    with open('./content/new.html', 'w+') as html:
            html.write('''
                <h1>New Content!</h1>
                <p>New content</p>
            ''')
