from datetime import datetime, timedelta
from dash_calendar_timeline import DashCalendarTimeline
from dash import Dash, html

now = datetime.now()

# Helper to convert datetime to UNIX timestamp in milliseconds
to_unix_ms = lambda dt: int(dt.timestamp() * 1000)

groups = [
    { "id": 1, "title": "group 1" },
    { "id": 2, "title": "group 2" }
]

items = [
    {
        "id": 1,
        "group": 1,
        "title": "item 1",
        "start_time": to_unix_ms(now),
        "end_time": to_unix_ms(now + timedelta(hours=1))
    },
    {
        "id": 2,
        "group": 2,
        "title": "item 2",
        "start_time": to_unix_ms(now - timedelta(minutes=30)),
        "end_time": to_unix_ms(now + timedelta(minutes=30))
    },
    {
        "id": 3,
        "group": 1,
        "title": "item 3",
        "start_time": to_unix_ms(now + timedelta(hours=2)),
        "end_time": to_unix_ms(now + timedelta(hours=3))
    }
]


app = Dash(
            __name__,
            meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1.0"}]
        )

app.layout = html.Div(
    [
        DashCalendarTimeline(
            groups=groups,
            items=items,
            defaultTimeStart=to_unix_ms(now),
            defaultTimeEnd=to_unix_ms(now + timedelta(hours=5))
        )
    ]
)


if __name__ == '__main__':
    app.run(debug=True)