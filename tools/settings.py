s3bucket ='s3://thunderbird-telemetry1/results/'
region = 'us-east-1'
release_version = "78."

keyedscalars = [
    {'key': 'tb.account.count', 'combine':['facebook']},
    {'key': 'tb.account.successful_email_account_setup'},
    {'key': 'tb.account.failed_email_account_setup'},
    {'key': 'tb.filelink.uploaded_size'},
    {'key': 'tb.mails.read_secure'},
    {'key': 'tb.websearch.usage', 'combine':['google', 'wikipedia', 'amazon']},
    {'key': 'tb.addressbook.addressbook_count'},
   # {'key': 'tb.addressbook.contact_count'},
    {'key': 'tb.calendar.calendar_count'},
    {'key': 'tb.calendar.read_only_calendar_count'},
]

scalars = [
    {'key': 'tb.compose.format_html'},
    {'key': 'tb.compose.format_plain_text'},
    {'key': 'tb.filelink.ignored'},
    {'key': 'tb.mails.sent'},
    {'key': 'tb.mails.read'},
]
