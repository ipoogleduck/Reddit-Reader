import grpc
import reddit_post_pb2
import reddit_post_pb2_grpc

def get_post(url: str | None = None, id: str | None = None):
    channel = grpc.insecure_channel('localhost:50051')
    stub = reddit_post_pb2_grpc.RedditReaderStub(channel)
    return stub.GetRedditPost(reddit_post_pb2.RedditPostRequest(post_url=url, post_id=id))

def askForUserInput():
    post = None
    if (int(input("Input 0 to get a reddit post by the url and 1 to get it by the post id: ")) == 0):
        url = input("Please paste in the url of the post you would like to retrieve: ")
        print("Loading...")
        post = get_post(url=url)
    else:
        id = input("Please type in the id of the post you would like to retrieve: ")
        print("Loading...")
        post = get_post(id=id)
    print("\n\nGot the post titled: " + post.title)
    print(post.body + "\n\n")

if __name__ == '__main__':
    print("Welcome to the reddit post reader client side tester")
    while(1):
        askForUserInput()
        