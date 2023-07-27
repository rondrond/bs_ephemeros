# https://github.com/MarshalX/atproto
from atproto import AtUri,Client
from datetime import datetime
from credentials import username,password,older_than

class bluesky_ephemeros:
 def load(self):
  self.client = Client()
  self.login = self.client.login(username,password)
  self.profile_feed = self.client.bsky.feed.get_author_feed({'actor': username})
  for feed_view in self.profile_feed.feed:
    post_rkey = AtUri.from_str(feed_view.post.uri).rkey
    now = datetime.utcnow()
    difference = datetime.utcnow()-datetime.strptime(feed_view.post.indexedAt.replace('T', ' ').replace('Z', ''), '%Y-%m-%d %H:%M:%S.%f')
    print(f'{feed_view.post.author.handle}: {feed_view.post.record.text}')
    print('Dias:')
    print(f'{difference.days.real}')

    if(difference.days.real >= older_than):
     if(self.delete_post(post_rkey)):
      print('Deleted\n\n')
    else:
     print('Before expiration date!\n\n')

 def delete_post(self, rkey):
  return self.client.delete_post(rkey)

bsephemeros = bluesky_ephemeros();
bsephemeros.load()

