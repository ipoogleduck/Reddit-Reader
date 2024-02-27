# Reddit Reader
Create a Reddit app here https://old.reddit.com/prefs/apps/ and create a .env file in the root of the repo with CLIENT_ID and CLIENT_SECRET from the app you just made.
## How to programmatically REQUEST data
To request data, you'll need to implement the RedditReader stub through grcp. You'll then call the GetRedditPost function with one of two parameters. `post_url` will return the title and body of the respective post while `post_id` will return the same based on the post's ID. If both parameters are provided, it will default to the post url.
Python Example:
```
import grpc
import reddit_post_pb2
import reddit_post_pb2_grpc

def get_post(url: str | None = None, id: str | None = None):
    channel = grpc.insecure_channel('localhost:50051')
    stub = reddit_post_pb2_grpc.RedditReaderStub(channel)
    return stub.GetRedditPost(reddit_post_pb2.RedditPostRequest(post_url=url, post_id=id))

get_post(url="http://reddit.com/example")

```

## How to programmatically RECEIVE data
To receive data, you just get the return object after calling the rpc function. Using the example above, you'll get an object with `title` and `body` corresponding to the queried post.

![ULM Diagram](https://github.com/ipoogleduck/Reddit-Reader/blob/main/ULM_Diagram.png)
