# Include the Dropbox SDK
import dropbox

####################################

# DO NOT TOUCH THESE EVER!!!!
app_key = '7kqv2t692l369j9'
app_secret = '5tvt2wdqti3m7op'

####################################

flow = dropbox.client.DropboxOAuth2FlowNoRedirect(app_key, app_secret)

authorize_url = flow.start()
print '1. Go to: ' + authorize_url
print '2. Click "Allow" (you might have to log in first)'
print '3. Copy the authorization code.'
code = raw_input("Enter the authorization code here: ").strip()
