import feedparser
from datetime import datetime, timedelta

# 从RSS获取最新5篇博客
def get_blog_posts(rss_url):
    feed = feedparser.parse(rss_url)
    posts = []
    for entry in feed.entries[:5]:
        pub_date = datetime(*entry.published_parsed[:6])
        posts.append({
            'title': entry.title,
            'url': entry.link,
            'date': pub_date.strftime('%Y-%m-%d')
        })
    return posts

# 生成Markdown内容
def generate_markdown(posts):
    md = "## 📝 **最新博客文章**\n\n"
    for post in posts:
        md += f"- [{post['title']}]({post['url']}) - {post['date']}\n"
    return md

if __name__ == "__main__":
    rss_url = "YOUR_BLOG_RSS_FEED_URL"  # 替换为你的RSS地址
    posts = get_blog_posts(rss_url)
    with open("README.md", "r+") as f:
        content = f.read()
        updated_content = content.replace("{{ BLOG_POSTS_LIST }}", generate_markdown(posts))
        f.seek(0)
        f.write(updated_content)
        f.truncate()