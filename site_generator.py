# Author: CACI NS Team
# Date: 15-Sep-2023
# Description: CACI NS Blog Static Site Generator
from jinja2 import Environment, FileSystemLoader
from markdown2 import markdown
import os
import re
import datetime

# Settings
SITE_URL = 'https://caci-ns.github.io' # Root website URL
SEO_NAME = 'CACI Network Services Blog' # SEO Site Name
SEO_DESCRIPTION = 'Expert consultants in your Networking, Cloud, IT Infrastructure, DevOps and Automation challenges - adept in a wide spectrum of end-to-end services from Consulting, Deployment through to Delivery Assurance' # SEO Site Description text
SEO_CARD_IMAGE = 'https://caci-ns.github.io/card.png' # SEO OpenGraph/LD Card Image URL
OUTPUT_DIRECTORY = 'docs/' # Generated HTML file folder (www root for Azure Web App)
TEMPLATES_DIRECTORY = 'templates/' # Jinja2 HTML Templates directory


# Functions
# Generate HTML pagefile from Jinja2 template
def html_page_create(output_dir, jinja2_templates_dir, jinja2_template_file, jinja2_replacements, page_type='WebSite', page_description=SEO_DESCRIPTION, page_route='/', page_name='index.html'):
    '''Saves processed HTML file in output_dir as index.html within /page_route directory (so becomes http://website.com/page_route/)
    Returns: Saves HTML file to disk for Jinja2-processed dict jinja2_replacements replaced for HTML values
    '''
    try:
        # Initialise variables
        seo = {'url': SITE_URL, 'title': SEO_NAME, 'page_title': SEO_NAME, 'name': SEO_NAME, 'type': page_type, 'description': page_description, 'image': SEO_CARD_IMAGE}
        # Process page-specific SEO tags
        if(page_route != '/'):
            # Process non-homepage SEO
            seo['url'] = SITE_URL + page_route
            if(page_type == 'Article'):
                # Process Blog-specific SEO
                seo['page_title'] = jinja2_replacements['post']['title'] + ' - ' + seo['title']
                seo['title'] = jinja2_replacements['post']['title']
                seo['image'] = jinja2_replacements['post']['hero_image']
                seo['description'] = re.findall('([a-zA-Z0-9\-\(\),;:\'\s\./]{1,})', jinja2_replacements['post']['summary'], re.MULTILINE)[0][:200]
            else:
                # Process website pages (non-homepage)-specific SEO
                seo['page_title'] = seo['title'] + ' - ' + page_route.split('/')[1].replace('-',' ').title()
                seo['title'] = seo['title'] + ' ' + page_route.split('/')[1].replace('-',' ').title()

        # Load jinja2_template_file as Jinja2 template
        template_env = Environment(loader=FileSystemLoader(jinja2_templates_dir), trim_blocks=True, lstrip_blocks=True)
        template_file = template_env.get_template(jinja2_template_file)
        # Render Jinja2 HTML file
        template_html = template_file.render({**jinja2_replacements, 'seo': seo, 'year': datetime.datetime.now().strftime('%Y')})

        # (Homepage-only) Randomly inject salesbox.html interstitial after a random blog post summary card
        if(page_route == '/'):
            # Open salesbox.html for replacement as string
            with open(TEMPLATES_DIRECTORY + 'salesbox.html', 'r') as f:
                salesbox_html = f.read()
            # Find last occurence in between heading 2 and paragraph in latter part of post
            template_html = ('</article>\n' + salesbox_html + '\n<article class="card">').join(template_html.split('</article>\n    <article class="card">', 1))

        # (Blog Post-only) Randomly inject salesbox.html interstitial after a random paragraph
        if(page_type == 'Article'):
            # Open salesbox.html for replacement as string
            with open(TEMPLATES_DIRECTORY + 'salesbox.html', 'r') as f:
                salesbox_html = f.read()
            # Find last occurence in between heading 2 and paragraph in latter part of post
            template_html = ('</p>\n' + salesbox_html + '\n<h2>').join(template_html.rsplit('</p>\n\n<h2>', 1))

        # Recursively create subdirectories (and sub-subdirectories... etc) for SEO-optimised page_route (slug) variables
        file_dirs_count = page_route.count('/')
        if(file_dirs_count > 1):
            # Check if sub-subdirectory exists, create if not
            if not os.path.exists(OUTPUT_DIRECTORY + page_route):
                # Create subdirectory and sub-subdirectories if new (SEO slug)
                os.makedirs(OUTPUT_DIRECTORY + page_route, exist_ok=True)

        # Write rendered HTML file to disk at page_route location in output_dir
        with open(output_dir + page_route + '/' + page_name, 'w', encoding='utf-8') as file:
            file.write(template_html)
        
        # Return success
        return True
    except Exception as e:
        # Print error to screen
        print('WARN - HTML Page Create Error - ' + str(e)[:500])

        # Return failure
        return False


# Main
if __name__ == '__main__':
    # Initialise variables
    blog_posts = {}
    blog_posts_data = []
    blog_categories = set()
    sitemap_permalinks = []
    # Output to log
    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ' JOB START - CACI NS Blog Static Site Generator\n')

    # Blog - Process each blog post page (reverse sort: newest first, oldest last)
    print('Rendering each Blog Post to HTML...')
    posts_files = os.listdir('posts')
    posts_files.sort(reverse=True)
    for post_md_filename in posts_files:
        with open('posts/' + post_md_filename, 'r', encoding='utf-8') as f:
            blog_posts[post_md_filename] = markdown(f.read(), extras=['metadata', 'tables', 'fenced-code-blocks'])
            blog_post_first_paragraph = re.sub('<a.*?>|</a>', '', re.findall('<p>(.*)</p>',  blog_posts[post_md_filename], re.MULTILINE)[0])
            blog_post_images = re.findall('<img src="(.*)" alt=', blog_posts[post_md_filename], re.MULTILINE)
            blog_post_data = {
                'content': blog_posts[post_md_filename],
                'title': blog_posts[post_md_filename].metadata['title'],
                'summary': blog_post_first_paragraph if (len(blog_post_first_paragraph) > 0) else blog_posts[post_md_filename][:400],
                'slug': blog_posts[post_md_filename].metadata['slug'],
                'category': blog_posts[post_md_filename].metadata['category'],
                'permalink': '/' + blog_posts[post_md_filename].metadata['category'] + '/' + blog_posts[post_md_filename].metadata['slug'] + '/',
                'date': datetime.datetime.strptime(blog_posts[post_md_filename].metadata['date'], "%Y-%m-%d %H:%M").strftime("%b %d, %Y"),
                'icon': blog_posts[post_md_filename].metadata['icon'],
                'hero_image': SITE_URL + blog_post_images[0] if (len(blog_post_images) > 0) else SEO_CARD_IMAGE
            }
            # Append to blog_posts metadata for later processing
            blog_posts_data.append(blog_post_data)
            # Append to sitemap permalinks for later processing
            sitemap_permalinks.append(blog_post_data['permalink'])
            # (If unique) append to categories for later processing
            blog_categories.add(blog_post_data['category'])
            # Output to log
            print(' Rendered Blog Post - ' + blog_post_data['title'])
            html_page_create(OUTPUT_DIRECTORY, TEMPLATES_DIRECTORY, 'post.html', {'post': blog_post_data}, 'Article', SEO_DESCRIPTION, blog_post_data['permalink'])

    # Blog - Process categories page
    html_page_create(OUTPUT_DIRECTORY, TEMPLATES_DIRECTORY, 'categories.html', {'categories': blog_categories, 'posts': blog_posts_data}, 'WebSite', 'CACI brings you news, views and insights in our blog on the world of Network Infrastructure, Cloud, DevOps and Network Automation', '/categories/')
    # Append to sitemap permalinks for later processing
    sitemap_permalinks.append('/categories/')
    print('\nRendering Blogs Categories page to HTML... Done')

    # Home - Process summary blog posts page
    html_page_create(OUTPUT_DIRECTORY, TEMPLATES_DIRECTORY, 'home.html', {'posts': blog_posts_data}, 'WebSite', 'CACI brings you news, views and insights in our blog on the world of Network Infrastructure, Cloud, DevOps and Network Automation', '/')
    print('\nRendering Blogs Homepage to HTML... Done')

    # Sitemap - Process overall XML sitemap for all pages and posts
    html_page_create(OUTPUT_DIRECTORY, TEMPLATES_DIRECTORY, 'sitemap.xml', {'site_url': SITE_URL, 'permalinks': sitemap_permalinks}, 'WebSite', SEO_DESCRIPTION, '/', 'sitemap.xml')
    print('\nRendering Sitemap to XML... Done')

    # Output to log
    print('\n' + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ' JOB END - CACI NS Blog Static Site Generator')