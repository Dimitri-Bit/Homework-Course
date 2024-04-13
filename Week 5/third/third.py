import json
import csv

def read_json_file(file_name):
    with open(file_name, 'r') as file:
        return file.read()
    
    
def search_by_title(json_content, title):
    data = json_content['data']
    articles = data['articles']

    for article in articles:
        if article['title'].lower() == title.lower():
            return article
        
    return None


def is_unique_title(comments, title):
    for comment in comments:
        if comment['title'].lower() == title.lower():
            return False
        
    return True


def add_comment(article, comment):
    if comment['author'] is None:
        comment['author'] = 'anonim'

    if is_unique_title(article['comments'], comment['title']):
        article['comments'].append(comment)


def delete_comment(article, title):
    comments = article['comments']

    for comment in comments:
        if comment['title'].lower() == title.lower():
            comments.remove(comment)

def find_comment(article, title):
    comments = article['comments']

    for comment in comments:
        if comment['title'].lower() == title.lower():
            return comment
        
    return 

def find_comments_from_author(json_content, author):
    data = json_content['data']
    articles = data['articles']
    
    comment_list = []

    for article in articles:
        comments = article['comments']
        for comment in comments:
            comment_author = comment['author']
            if comment_author.lower() == author.lower():
                comment_list.append(comment)

    return comment_list

def find_articles_from_author(json_content, author):
    data = json_content['data']
    articles = data['articles']

    article_list = []

    for article in articles:
        if article['author'].lower() == author.lower():
            article_list.append(article)

    return article_list

def write_article_to_csv(articles):
    fields = ['title', 'author', 'description', 'category', 'views']
    dic_list = []

    for article in articles:
        dic = {'title': article['title'], 'author': article['author'], 'description': article['description'], 'category': article['category'], 'views': article['views']}
        dic_list.append(dic)

    with open('file.csv', 'w') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fields)
        writer.writeheader()
        writer.writerows(dic_list)

def write_article_to_json(articles):
    for article in articles:
        with open("file2.json", "a") as json_file:
            json_file.write(json.dumps(article))


json_content = json.loads(read_json_file('file.json'))

find_article = search_by_title(json_content, 'the evolution of video games')
new_comment_1 = {'title': 'Great Article', 'author': 'Bro', 'description': 'Great review, thanks'}
new_comment_2 = {'title': 'Bad Article', 'author': 'Hater', 'description': 'bad!'}

add_comment(find_article, new_comment_1)
add_comment(find_article, new_comment_2)

print(f"Json after adding comment:\n{json.dumps(json_content, indent=4)}")
delete_comment(find_article, 'Great Article')
print(f"Json after deleting comment:\n{json.dumps(json_content, indent=4)}")

find_comment = find_comment(find_article, 'Bad Article')
print(f"Find comment in article by title:\n{json.dumps(find_comment, indent=4)}")

comments_from_author = find_comments_from_author(json_content, 'PianoLover')
print(f"Comments from specific author:\n {json.dumps(comments_from_author, indent=4)}")

articles_from_author = find_articles_from_author(json_content, 'Samantha Zhou')
print(f"Articles from specific author:\n {json.dumps(articles_from_author, indent=4)}")

sorted_articles_from_author = sorted(articles_from_author, key=lambda d: len(d['comments']))
print(f"Sorted articles by number of comments {json.dumps(sorted_articles_from_author, indent=4)}")


write_article_to_csv(sorted_articles_from_author)
write_article_to_json(sorted_articles_from_author)