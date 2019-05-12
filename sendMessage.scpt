on run {targetPhoneNumber, targetMessageToSend}
    repeat 1 times
        tell application "Messages"
            set targetService to 1st service whose service type = iMessage
            set targetBuddy to buddy targetPhoneNumber of targetService
            set targetMessage to targetMessageToSend
            send targetMessage to targetBuddy
        end tell
    end repeat    
end run