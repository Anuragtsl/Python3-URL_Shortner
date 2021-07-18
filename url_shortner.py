import bitly_api
BITLY_ACCESS_TOKEN ="YOUR ACCESS TOKEN HERE"
access = bitly_api.Connection(access_token = BITLY_ACCESS_TOKEN)
full_link = input('Enter URL to be shortened: ')
short_url = access.shorten(full_link)
print('Short URL = ', short_url['url'])