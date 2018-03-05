text = "X-DSPAM-Confidence:    0.8475"
where = text.find(' ')
print (text[where : ].strip())
