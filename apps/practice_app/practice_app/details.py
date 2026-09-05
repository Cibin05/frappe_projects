from practice_app.practice.doctype.details.details import details


class CustomDetails(details):

    def validate(self):
        super().validate()
        print(">>> OVERRIDDEN CLASS")