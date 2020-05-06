

class Match:
    def __init__(self, page, state, matched_text, date, document_link, document_id):
        self.page = page
        self.state = state
        self.date = date
        self.matched_text = matched_text
        self.document_id = document_id
        self.document_link = document_link

    def __str__(self):
        return 'state:<{state}>\ndate:<{date}>,\npage:<{page}>,\ndocument_id:<{document_id}>,\ndocument_link:<{document_link}>,\nsentence:<{sentence}>' \
            .format(state=self.state, date=self.date, page=self.page, document_id=self.document_id, document_link=self.document_link, sentence=self.matched_text)


