import grpc
import praw
import reddit_post_pb2
import reddit_post_pb2_grpc
from concurrent import futures
import os
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
USER_AGENT = "script:com.example.kevinspostreader:v1.0 (by u/ipoogleduck)"

class RedditPostServicer(reddit_post_pb2_grpc.RedditReaderServicer):
    def GetRedditPost(self, request, context):
        reddit = praw.Reddit(client_id=CLIENT_ID,
                                client_secret=CLIENT_SECRET,
                                user_agent=USER_AGENT)
        if request.HasField("post_url"):
            submission = reddit.submission(url=request.post_url)
        else:
            print(request.post_id)
            submission = reddit.submission(id=request.post_id)
        print("Sending back reddit post: " + submission.title)
        # print(submission.selftext)
        return reddit_post_pb2.RedditPostResponse(title=submission.title, body=submission.selftext)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10)) # Can remove thread pool to do execution one at a time on the main thread
    reddit_post_pb2_grpc.add_RedditReaderServicer_to_server(RedditPostServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server started")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
