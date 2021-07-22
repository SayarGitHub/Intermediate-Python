# *args is like a list and **kwargs is like a dictionary
blog_1 = "Hello! welcome to my blog."
blog_2 = "You are awesome."
blog_3 = "Aww look at my bear."

site_title = "My blog"


def blog_posts(site_title, *args, **kwargs):
    print(site_title)
    for post in args:
        print(post)
    for id, value in kwargs.items():
        print(f"kwargs: {id}, {value}")


blog_posts(
    site_title,
    blog_1,
    blog_2,
    blog_3,
    blog_1="Hello! welcome to my blog.",
    blog_2="You are awesome.",
    blog_3="Aww look at my bear.",
)


def graph_operation(x, y):
    print(f"function that graphs {x} and {y}")


x1 = [1, 2, 3]
y1 = [4, 5, 6]
graph_operation(x1, y1)

graph_me = [x1, y1]
graph_operation(*graph_me)
