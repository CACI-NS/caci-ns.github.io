# Author: CACI NS Team
# Date: 25-May-2023
# Description: CACI NS Blog Static Site Generator
import os
import re
import datetime
from jinja2 import Environment, FileSystemLoader
from markdown2 import markdown

# Define constants
OUTPUT_DIRECTORY = 'docs/' # Remote Git Repo folder name that contains Blog HTML files
TEMPLATES_DIRECTORY = 'templates/' # Jinja2 HTML Templates directory

# Main program
year = datetime.datetime.now().strftime("%Y")
print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ' JOB START - CACI NS Blog Static Site Generator\n')

# Process blog posts from Posts folder
POSTS = {}
posts_tmp = []
# Select Posts (Folder) within local repo and reverse-sort (newest Post at the top of the Homepage)
try:
 for post_md_filename in os.listdir('posts'):
  with open('posts/' + post_md_filename, 'r') as f:
   posts_tmp[post_md_filename] = markdown(f.read(), extras=['metadata', 'tables'])
 POSTS = dict(reversed(posts_tmp.items()))
 ##DEBUG
 print(POSTS)
 ##DEBUG
except Exception as e:
 # Failed to attach to specified Posts (Folder) within repo
 print(' Enumerating Posts... Failed [' + str(e).split('.')[0] + ']')

# Process blog pages from Pages folder
PAGES = {}
# Select Pages (Folder) within local repo
try:
 for page_md_filename in os.listdir('pages'):
  with open('pages/' + page_md_filename, 'r') as f:
   PAGES[page_md_filename] = markdown(f.read(), extras=['metadata', 'tables'])
except Exception as e:
 # Failed to attach to specified Pages (Folder) within repo
 print(' Enumerating Pages... Failed [' + str(e).split('.')[0] + ']')

# Process default SEO tags
SEO = {
 'url': 'https://caci-ns.github.io',
 'name': 'CACI Network Services Blog',
 'title': 'CACI Network Services Blog',
 'description': 'Expert consultants in your Networking, Cloud, IT Infrastructure, DevOps and Automation challenges - adept in a wide spectrum of end-to-end services from Consulting, Deployment through to Delivery Assurance',
 'type': 'WebSite'
}

# Load Jinja2 HTML templates in
try:
 production = Environment(loader=FileSystemLoader(TEMPLATES_DIRECTORY), trim_blocks=True, lstrip_blocks=True)
 home_template = production.get_template('home.html')
 post_template = production.get_template('post.html')
 page_template = production.get_template('page.html')
 categories_template = production.get_template('categories.html')
 sitemap_template = production.get_template('sitemap.xml')
 # Successful Jinja2 Template load, output to log
 print('Loading Jinja2 Blog Site Templates... Done')
except Exception as e:
 # Failed Jinja2 Template load, output to log
 print('Loading Jinja2 Blog Site Templates... Failed [' + str(e)[:60] + ']')

# Render Blog posts to dictionary
render_posts = []
render_categories = []
print('\nRendering each Blog Post to HTML...')
for post in POSTS:
 post_metadata = POSTS[post].metadata
 post_first_paragraph = re.findall('<p>(.*)</p>', POSTS[post], re.MULTILINE)
 post_data = {
  'content': POSTS[post],
  'title': post_metadata['title'],
  'summary': post_first_paragraph[0] if (len(post_first_paragraph) > 0) else POSTS[post][:400],
  'slug': post_metadata['slug'],
  'date': datetime.datetime.strptime(post_metadata['date'], "%Y-%m-%d %H:%M").strftime("%b %d, %Y"),
  'date_raw': post_metadata['date'],
  'year': post_metadata['date'][0:4],
  'month': post_metadata['date'][5:7],
  'day': post_metadata['date'][8:10],
  'category': post_metadata['category'],
  'icon': post_metadata['icon']
 }
 # Add current post to render_posts list
 render_posts.append(post_data)
 print(' Rendered Blog Post - ' + post_metadata['title'])
 # Add current category to render_categories list (if not already present)
 if not post_data['category'] in render_categories:
  render_categories.append(post_data['category'])
  print('  Rendered Blog Category - ' + post_metadata['category'])

 # Output individual Blog Post page HTML files
 render_seo = SEO
 render_seo['url'] = 'https://caci-ns.github.io' + '/' + post_data['category'] + '/' + post_data['year'] + '/' + post_data['month'] + '/' + post_data['day'] + '/' + post_data['slug'] + '.html'
 render_seo['title'] = post_data['title']
 render_seo['description'] = re.findall('([a-zA-Z0-9\-\(\),\'\s\.]{1,})', post_first_paragraph[0], re.MULTILINE)[0][:200]
 render_seo['type'] = 'Article'
 post_html = post_template.render(post=post_data, seo=render_seo, year=year, page_title=post_data['title'] + ' - CACI/CD Network Services Blog')
 try:
  # Create new category/year/month/day/ (SEO URL) folders Posts entries as subfolders
  post_page_directory = OUTPUT_DIRECTORY + '/' + post_data['category'] + '/' + post_data['year'] + '/' + post_data['month'] + '/' + post_data['day']
  # Create category SEO directory
  if not os.path.exists(OUTPUT_DIRECTORY + '/' + post_data['category']):
   os.mkdir(OUTPUT_DIRECTORY + '/' + post_data['category'])
  # Create category/year SEO directory
  if not os.path.exists(OUTPUT_DIRECTORY + '/' + post_data['category'] + '/' + post_data['year']):
   os.mkdir(OUTPUT_DIRECTORY + '/' + post_data['category'] + '/' + post_data['year'])
  # Create category/year/month SEO directory
  if not os.path.exists(OUTPUT_DIRECTORY + '/' + post_data['category'] + '/' + post_data['year'] + '/' + post_data['month']):
   os.mkdir(OUTPUT_DIRECTORY + '/' + post_data['category'] + '/' + post_data['year'] + '/' + post_data['month'])
  # Create category/year/month/day SEO directory
  if not os.path.exists(OUTPUT_DIRECTORY + '/' + post_data['category'] + '/' + post_data['year'] + '/' + post_data['month'] + '/' + post_data['day']):
   os.mkdir(OUTPUT_DIRECTORY + '/' + post_data['category'] + '/' + post_data['year'] + '/' + post_data['month'] + '/' + post_data['day'])
  # Write Blog Post HTML page to the new category/year/month/day/ SEO directory
  with open(post_page_directory + '/' + post_data['slug'] + '.html', 'w', encoding='utf-8') as file:
   file.write(post_html)
  # Successfully rendered Blog Post pages, output to log
  print('  Rendering Blog Post HTML page... Done')
 except Exception as e:
  # Failed to render Blog Post pages, output to log
  print('  Rendering Blog Post HTML page... Failed [' + str(e)[:100] + ']')

# Render Pages to dictionary
render_pages = []
print('\nRendering each Blog Page to HTML...')
for page in PAGES:
 page_metadata = PAGES[page].metadata
 page_first_paragraph = re.findall('<p>(.*)</p>', PAGES[page], re.MULTILINE)
 page_data = {
  'content': PAGES[page],
  'title': page_metadata['title'],
  'permalink': page_metadata['permalink']
 }
 # Add current page to render_pages list
 render_pages.append(page_data)
 print(' Rendered Blog Page - ' + page_metadata['title'])

 # Output individual Blog Page HTML files
 render_seo = SEO
 render_seo['url'] = 'https://caci-ns.github.io' + page_data['permalink']
 render_seo['title'] = page_data['title'] + ' - CACI Network Services Blog'
 render_seo['description'] = re.findall('([a-zA-Z0-9\-\(\),\'\s\.]{1,})', page_first_paragraph[0], re.MULTILINE)[0][:200]
 render_seo['type'] = 'WebSite'
 page_html = page_template.render(page=page_data, year=year, seo=render_seo, page_title=page_data['title'] + ' - CACI/CD Network Services Blog')
 try:
  # Create new <page_name>/ (SEO URL) folder
  page_page_directory = OUTPUT_DIRECTORY + page_data['permalink']
  # Create <page_name> SEO directory
  if not os.path.exists(page_page_directory):
   os.mkdir(page_page_directory)
  # Write Blog Post HTML page to the new category/year/month/day/ SEO directory
  with open(page_page_directory + '/index.html', 'w', encoding='utf-8') as file:
   file.write(page_html)
  # Successfully rendered Blog Pages, output to log
  print('  Rendering Blog Page HTML pages... Done')
 except Exception as e:
  # Failed to render Blog Pages, output to log
  print('  Rendering Blog Page HTML pages... Failed [' + str(e)[:100] + ']')

# Output Blog home page HTML file
render_seo = SEO
render_seo['url'] = 'https://caci-ns.github.io'
render_seo['title'] = 'CACI Network Services Blog'
render_seo['type'] = 'WebSite'
render_seo['description'] = 'Expert consultants in your Networking, Cloud, IT Infrastructure, DevOps and Automation challenges - adept in a wide spectrum of end-to-end services from Consulting, Deployment through to Delivery Assurance'
home_html = home_template.render(posts=render_posts, seo=render_seo, year=year, page_title='CACI Network Services Blog')
try:
 with open(OUTPUT_DIRECTORY + 'index.html', 'w', encoding='utf-8') as file:
  file.write(home_html)
 # Successfully rendered Blog Home page, output to log
 print('\nRendering Blog Home HTML page... Done')
except Exception as e:
 # Failed to render Blog Home page, output to log
 print('\nRendering Blog Home HTML page... Failed [' + str(e)[:60] + ']')

# Output Blog Categories page HTML file
render_seo = SEO
render_seo['url'] = 'https://caci-ns.github.io/categories/'
render_seo['title'] = 'Categories - CACI Network Services Blog'
render_seo['type'] = 'WebSite'
categories_html = categories_template.render(posts=render_posts, categories=render_categories, seo=render_seo, year=year, page_title='Categories - CACI Network Services Blog')
try:
 # Create new categories/ (SEO URL) folder
 categories_page_directory = OUTPUT_DIRECTORY + 'categories'
 # Create categories SEO directory
 if not os.path.exists(categories_page_directory):
  os.mkdir(categories_page_directory)
 with open(categories_page_directory + '/index.html', 'w', encoding='utf-8') as file:
  file.write(categories_html)
 # Successfully rendered Blog Categories page, output to log
 print('\nRendering Blog Categories HTML page... Done')
except Exception as e:
 # Failed to render Blog Categories page, output to log
 print('\nRendering Blog Categories HTML page... Failed [' + str(e)[:60] + ']')

# Output Blog Sitemap XML file
sitemap_xml = sitemap_template.render(posts=render_posts, pages=render_pages)
try:
 with open(OUTPUT_DIRECTORY + 'sitemap.xml', 'w') as file:
  file.write(sitemap_xml)
 # Successfully rendered Blog Sitemap, output to log
 print('\nRendering Blog XML Sitemap... Done')
except Exception as e:
 # Failed to render Blog Sitemap, output to log
 print('\nRendering Blog XML Sitemap... Failed [' + str(e)[:60] + ']')

# Output log message
print('\n' + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ' JOB END - CACI NS Blog Static Site Generator')
