# https://github.com/MarshalX/atproto
from atproto import AtUri,Client
from datetime import datetime
from settings import handle,password,delete_older_than

class bluesky_ephemeros:
 delete = False

 def load(self):
  self.client = Client()
  self.login = self.client.login(handle,password)
  self.profile_feed = self.client.app.bsky.feed.get_author_feed({'actor': handle})
  for feed_view in self.profile_feed.feed:
    post_rkey = AtUri.from_str(feed_view.post.uri).rkey
    difference = datetime.utcnow()-datetime.strptime(feed_view.post.indexed_at.replace('T', ' ').replace('Z', ''), '%Y-%m-%d %H:%M:%S.%f')
    print(f'{feed_view.post.author.handle}: {feed_view.post.record.text}\nDays: {difference.days.real}')
    if (self.delete):
     if(difference.days.real >= delete_older_than):
      if(self.delete_post(post_rkey)):
       print('DELETED\n\n')
     else:
      print('Before expiration date!\n\n')

 def delete_post(self, rkey):
  return self.client.delete_post(rkey)
 
bsephemeros = bluesky_ephemeros()
bsephemeros.delete = True
bsephemeros.load()
