# Youtube-Data-Transfer
We use selenium to automate the process of visitng links and manipulating web elements inorder to populate your history and subscriptions from your old account to your new account. This code works only in chrome browser.

For this to work you should install undetected_chromedriver by executing this command
pip3 install undetected_chromedriver

# Gather Youtube Data
You can gather your data by visitng https://takeout.google.com/

Select Youtube and Youtube Music

Select subscriptions and history

Select HTML format

And download the data


# Watch History
Give appropriate paths to driver and wathcHistory file and exceute watchHistory.py file to transfer your watch history from your old account to your new account.

This script automatically visits video links you have visited through your previous account in LRV. You can manually select the number of most recent videos and the time you want to stay in each link.

# Subscriptions
Give appropriate paths to driver and subscriptions csv file and execute subscriptions.py file to subscribe to all channels ou were subcribing in your previous account.

This script automatically visits all channels and subscribes to them. You can select subscription preference manually.
