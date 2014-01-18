from etsy import Etsy
import json

api = Etsy('a7tgx4sgryg3lyu0enutd5qu')
listing = api.findAllFeaturedListings(offset=10, limit=1)[0]

if listing:
  print 'Featured listing: "%s" (%s)' % (listing['title'], listing['url'])
else:
  print 'Unable to retrieve featured listing.'
