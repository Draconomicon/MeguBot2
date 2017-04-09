def remove_duplicates(values):
    output = []
    seen = set()
    for value in values:
        # If value has not been encountered yet,
        # ... add it to both list and set.
        if value not in seen:
            output.append(value)
            seen.add(value)
    return output


def send_email():
    import main
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText

    FROM = "imegubot@gmail.com"
    TO = "piotr.hrankowski@gmail.com"
    msg = MIMEMultipart()
    msg['From'] = FROM
    msg['To'] = TO
    msg['Subject'] = "MeguBot"
    msg.attach(MIMEText(main.mail_body, 'html'))

    text = msg.as_string()

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(FROM, "zcb10adg")
        server.sendmail(FROM, TO, text)
        server.quit()
    except:
        print('Mail not sent')


def UpdateMailBody(body):
    import main
    main.mail_body += body


