import uuid
import datetime as dt

class Synopsis:
    """
        An overview of everything under the synopsis, contains all ventures, projects, components, and information
    """
    def __init__(self):
        UUID: uuid.uuid4 = None
        self._data = dict(
            Name = None,
            Version = "0.0.1",
            Metadata = dict(
                CreationDate = None,
                ModifiedDate = None,
            ),
            Configuration = dict(
                Format = dict(
                    Datetime = "",
                    Date = "",
                    Time = "",
                    YearMonth = "",
                    MonthDay = "",
                    ShortDatetime = "",
                    ShortDate = "",
                ),
                WeekFirstDay = 0, # Sunday
                DecimalDelimiter = ".",
                NumberGrouping = 3,
                ThousandDelimiter = ",",
            ),
            Groups = dict(
                Admin = [],
                Moderator = [],
                User = [],
                Viewer = [],
            )
        )
        self.Users = dict(

        )
    pass