source ~/Google\ Drive/secret.sh

message=$1
echo $message
# http $SLACK_EMACS_WEBHOOK_BASE_URL text="$message"
# The --ignore-stdin is needed when calling from emacs
http --ignore-stdin $SLACK_EMACS_WEBHOOK_BASE_URL text="$message"
