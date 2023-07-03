# CACI NS Blog
This is the Blog for CACI NS, which uses the following components to build the HTML Site content within the `docs` directory upon a successful `git push`:

1. Static Site Generator `site_generator.py`
2. GitHub Actions `CI - GitHub Actions` (to trigger `site_generator.py` and perform the `git commit...` into the `docs` directory)

Note that GitHub has limitations around the folder name used for public hosting, hence use of the `docs` directory rather than one named "public" or similar.

## Deployment
`site_generator.py` is the Static Site Generator and will be triggered via GitHub Actions on successful trigger of a `git push` from local source changes.

## Blog Content
Two types of content (pages) are possible on the Blog:

1. Blog Posts
2. Blog Pages

Both are specified in [Markdown format](https://www.markdownguide.org/cheat-sheet/), which can render HTML, Images, Bullet Points, Bold Text and so on. The Static Site Generator (SSG) generates these by checking for corresponding `.md` Markdown-formatted text files in the following directories in the Git Repo root:

* posts/
* pages/

### Posts
Each Post should have a unique alphanumeric-only filename ending in `.md`, in format similar to `year-month-day-title.md`, such as:

* `2023-03-07-choosing-between-devops-versus-itil.md`

Within the Markdown file, the frontmatter section (the lines in between `---` delimiters) should contain the following `key`:`value` attributes:

* `title`
  * A human-English, properly-capitalised title for the Blog Post
* `slug`
  * Alphanumeric-only (letters, numbers and hyphens only) summary of the title - this becomes the URL for the Blog Post
* `date`
  * In format `year-month-day hours:minutes` with leading 0's left intact (i.e. March is `03` and not `3`)
* `category`
  * All-lowercase, single category the Blog Post falls under, examples are `devops`, `networking`, `itsm`, `telco`
* `icon`
  * Name of the [Font Awesome 4.7 icon](https://fontawesome.com/v4/icons/) to use as the frontpage Summary Image for the Blog Post

Example frontmatter might look like the below:

```YAML
---
title: Choosing between DevOps versus ITIL
slug: choosing-between-devops-versus-itil
date: 2023-03-07 13:41
category: itsm
icon: question
---
```
Headings within the Blog Post Markdown should start at Level 2 (`##`) as a top-level heading.

Headings can be lower-level than this (such as Level 3 `###` or Level 4 `####`), but can **NOT** be higher-level than this (i.e. do *NOT* use Level 1 `#` headings). 

### Pages

Each Page should have a unique alphanumeric-only filename ending in `.md`, in format similar to `title.md`, such as:

* `about.md`

Do **NOT** use `categories` as a Page Name, as this is a special page rendered elsewhere.

Within the Markdown file, the frontmatter section (the lines in between `---` delimiters) should contain the following `key`:`value` attributes:

* `title`
  * A human-English, properly-capitalised title for the Blog Page
* `permalink`
  * Alphanumeric-only (letters, numbers and hyphens only) summary of the title, starting and ending with a forward slash `/` - this becomes the URL for the Blog Page

Example frontmatter might look like the below:

```YAML
---
title: About
permalink: /about/
---
```
Headings within the Blog Page Markdown should start at Level 2 (`##`) as a top-level heading.

Headings can be lower-level than this (such as Level 3 `###` or Level 4 `####`), but can **NOT** be higher-level than this (i.e. do *NOT* use Level 1 `#` headings). 

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
