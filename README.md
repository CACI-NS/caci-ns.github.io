# CACI NS Blog
This is the Blog for CACI NS, which uses the following components to build the HTML Site content within the `docs` directory upon a successful `git push`:

1. Static Site Generator `site_generator.py`
2. GitHub Actions `CI - GitHub Actions` (to trigger `site_generator.py` and perform the `git commit...` into the `docs` directory)

Note that GitHub has limitations around the folder name used for public hosting, hence use of the `docs` directory rather than one named "public" or similar.

## Deployment
`site_generator.py` is the Static Site Generator and will be triggered via GitHub Actions on successful trigger of a `git push` from local source changes.

## Template Files
These are present within the Git Repo `templates` directory and are Jinja2 Templates which are used by the Static Site Generator (SSG) script `site_generator.py`:

* templates/ - Folder of Jinja2 templates
  * base.html - This is the base Header/Footer/HTML template used by all generated HTML pages
  * categories.html - This is the Categories page listing all known Blog Post categories and associated Posts
  * home.html - This becomes the Homepage for the site when generated through the SSG
  * post.html - This becomes each Blog Post page when generated through the SSG
  * page.html - This becomes each Blog Page page when generated through the SSG
  * sitemap.xml - This becomes the Site XML Sitemap

## HTML Assets
These are present within the Git Repo `docs` directory and should be modified locally and git commit/pushed as needed:

* img/ - Folder of static site images and assets
  * background.jpg - This is used for the "hero" Header on each website page
* apple-touch-icon.png - This is the Apple Touch icon for the website
* favicon.ico - This is the Browser Favourite icon for the website
* favicon-16x16.png - This is a small PNG version of the Browser Favourite icon for the website
* favicon-32x32.png - This is a large PNG version of the Browser Favourite icon for the website
* site.css - This defines the CSS Style Sheet to colour and theme the website

Other folders are generated based on the SSG generating the required folders for the Blog Pages and Blog Posts.

## Support
Contact these people for help:

* [info@caci.co.uk](mailto:info@caci.co.uk)
