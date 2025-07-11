# AUTO GENERATED FILE - DO NOT EDIT

import typing  # noqa: F401
from typing_extensions import TypedDict, NotRequired, Literal # noqa: F401
from dash.development.base_component import Component, _explicitize_args

ComponentType = typing.Union[
    str,
    int,
    float,
    Component,
    None,
    typing.Sequence[typing.Union[str, int, float, Component, None]],
]

NumberType = typing.Union[
    typing.SupportsFloat, typing.SupportsInt, typing.SupportsComplex
]


class DashCalendarTimeline(Component):
    """A DashCalendarTimeline component.


Keyword arguments:

- id (string; optional):
    The ID used to identify this component in Dash callbacks.

- boundsChangeData (dict; optional):
    Called when the bounds in the calendar's canvas change. Use it for
    example to load new data to display. (see \"Behind the scenes\"
    below). canvasTimeStart and canvasTimeEnd are unix timestamps in
    milliseconds.

- buffer (number; optional):
    a number (default to 3) which represents the extra timeline
    rendered on right and lift of the visible area which the user will
    scroll through before the time rerenders. Note: setting buffer to
    1 will disable the scrolling on the timeline.

- canChangeGroup (boolean; optional):
    Can items be moved between groups? Can be overridden in the items
    array. Defaults to True.

- canMove (boolean; optional):
    Can items be dragged around? Can be overridden in the items array.
    Defaults to True.

- canResize (string | boolean; optional):
    Can items be resized? Can be overridden in the items array.
    Accepted values: False, \"left\", \"right\", \"both\". Defaults to
    \"right\". If you pass True, it will be treated as \"right\" to
    not break compatibility with versions 0.9 and below.

- canvasClickData (dict; optional):
    Called when an empty spot on the canvas was clicked. Get the group
    ID and the time as arguments. For example open a \"new item\"
    window after this.

- canvasContextMenuData (dict; optional):
    Called when the canvas is clicked by the right button of the
    mouse. Note: If this property is set the default context menu
    doesn't appear.

- canvasDoubleClickData (dict; optional):
    Called when an empty spot on the canvas was double clicked. Get
    the group ID and the time as arguments.

- clickTolerance (number; optional):
    How many pixels we can drag the background for it to be counted as
    a click on the background. Default 3.

- cursorMarkerStyle (dict; optional):
    Use this to render special styles for the cursorMarker.

- customGroups (boolean; optional):
    This will determine whether you'd want to set up custom content
    for groups or not.

- customGroupsContent (a list of or a singular dash component, string or number; optional):
    This will be used to set up custom content of groups in the
    sidebar.

- customItems (boolean; optional):
    This will determine whether you'd want to set up custom content
    for items or not.

- customItemsContent (a list of or a singular dash component, string or number; optional):
    This will be used to set up custom content of items in the main
    timeline.

- customMarkers (list; optional):
    Marker that is placed on the specified date/time. Example usage:
    [     {'date': 1750070400000, 'style':{'backgorund-color':'red'}},
    {'date': 1750675200000, 'style':{'backgorund-color':'green'}},
    {'date': 1751467500000, 'style':{'backgorund-color':'blue'}},  ].

- dateHeaderHeight (number; optional):
    Determines the height of the header in pixels. Default 30.

- dateHeaderLabelFormat (string; optional):
    Controls the how to format the interval label.

- dateHeaderStyle (dict; optional):
    Style applied to the root of the header.

- dateHeaderUnit (string; optional):
    Determines the intervals between columns. Values can be second,
    minute, hour, day, week, month, year or primaryHeader.

- defaultTimeEnd (number; optional):
    This sets the end time for the timeline.

- defaultTimeStart (number; optional):
    This sets the start time for the timeline.

- disableScroll (boolean; optional):
    Disable the scrolling of timeline. Default is False.

- dragInfoLabel (boolean; optional):
    This will render a info label over the timeline while the item is
    being dragged around.

- dragInfoLabelStyle (dict; optional):
    Style applied to the dragInfoLabel.

- dragSnap (number; optional):
    Snapping unit when dragging items. Defaults to 15 * 60 * 1000 or
    15min. When so, the items will snap to 15min intervals when
    dragging.

- draggingItemColor (string; optional):
    Item color while the item is being dragged around.

- groups (list; optional):
    The groups are used to determine the number of groups in a
    Timeline.

- groupsClass (string; optional):
    This will be used to set up custom css classes of content of
    groups in the sidebar.

- groupsStyle (dict; optional):
    This will be used to set up custom css style of content of groups
    in the sidebar.

- itemClickData (dict; optional):
    Called when an item is clicked. Note: the item must be selected
    before it's clicked... except if it's a touch event and
    itemTouchSendsClick is enabled. time is the time that corresponds
    to where you click on the item in the timeline.

- itemContextMenuData (dict; optional):
    Called when the item is clicked by the right button of the mouse.
    time is the time that corresponds to where you context click on
    the item in the timeline. Note: If this property is set the
    default context menu doesn't appear.

- itemDimensions (dict; optional):
    Get the dimensions for the currently rendered items. Warning: Use
    this prop to render custom items on a fixed timeline only. Disable
    scrolling, moving and resizing as it will re-render the timeline
    on every single event for items.

- itemDoubleClickData (dict; optional):
    Called when an item was double clicked. time is the time that
    corresponds to where you double click on the item in the timeline.

- itemHeightRatio (number; optional):
    What percentage of the height of the line is taken by the item?
    Default 0.65.

- itemSelectData (dict; optional):
    This is sent on the first click on an item. time is the time that
    corresponds to where you click/select on the item in the timeline.

- itemTouchSendsClick (boolean; optional):
    Normally tapping (touching) an item selects it. If this is set to
    True, a tap will have the same effect, as selecting with the first
    click and then clicking again to open and send the onItemClick
    event. Defaults to False.

- items (list; optional):
    The items are used to determine the number of items within a
    single group.

- itemsClass (string; optional):
    This will be used to set up custom css classes for content of
    custom items in the main timeline.

- itemsStyle (dict; optional):
    This will be used to set up custom css styles for content of
    custom items in the main timeline.

- lineHeight (number; optional):
    Height of one line in the calendar in pixels. Default 30.

- maxZoom (number; optional):
    Largest time the calendar can zoom to in milliseconds. Default 5 *
    365.24 * 86400 * 1000 (5 years).

- minResizeWidth (number; optional):
    The minimum width, in pixels, of a timeline entry when it's
    possible to resize. If not reached, you must zoom in to resize
    more. Default to 20.

- minZoom (number; optional):
    Smallest time the calendar can zoom to in milliseconds. Default 60
    * 60 * 1000 (1 hour).

- resizingItemBorder (string; optional):
    Item border (CSS border e.g, 2px solid red) while the item is
    being resized.

- rightSidebarWidth (number; optional):
    Width of the right sidebar in pixels. If set to 0, the right
    sidebar is not rendered. Defaults to 0.

- selectedItemColor (string; optional):
    Item color when item is selected.

- showCursorMarker (boolean; optional):
    Marker that is displayed when hovering over the timeline and
    matches where your cursor is.

- showTodayMarker (boolean; optional):
    Marker that is placed on the current date/time.

- sidebarHeaderContent (a list of or a singular dash component, string or number; optional):
    Renders the Content above the sidebar.

- sidebarHeaderVariant (string; optional):
    Determines whether the content goes above the left or right
    sidebar.

- sidebarWidth (number; optional):
    Width of the sidebar in pixels. If set to 0, the sidebar is not
    rendered. Defaults to 150.

- timeSteps (dict; optional):
    With what step to display different units. E.g. 15 for minute
    means only minutes 0, 15, 30 and 45 will be shown.  Default:
    {           second: 1,           minute: 1,           hour: 1,
    day: 1,           month: 1,           year: 1         }.

- timelineHeaderStyle (dict; optional):
    Style applied to the root component of headers.

- todayMarkerInterval (number; optional):
    How often the TodayMarker refreshes. Value represents
    milliseconds. Default is 10000.

- todayMarkerStyle (dict; optional):
    Use this to render special styles for the todayMarker.

- traditionalZoom (boolean; optional):
    Zoom in when scrolling the mouse up/down. Defaults to False.

- useResizeHandle (boolean; optional):
    Append a special .rct-drag-right handle to the elements and only
    resize if dragged from there. Defaults to False.

- visibleTimeEnd (number; optional):
    The exact ending viewport of the calendar.

- visibleTimeStart (number; optional):
    The exact starting viewport of the calendar.

- zoomData (dict; optional):
    Called when the timeline is zoomed, either via mouse/pinch zoom or
    clicking header to change timeline units."""
    _children_props = ['customItemsContent', 'customGroupsContent', 'sidebarHeaderContent']
    _base_nodes = ['customItemsContent', 'customGroupsContent', 'sidebarHeaderContent', 'children']
    _namespace = 'dash_calendar_timeline'
    _type = 'DashCalendarTimeline'


    def __init__(
        self,
        id: typing.Optional[typing.Union[str, dict]] = None,
        groups: typing.Optional[typing.Sequence] = None,
        items: typing.Optional[typing.Sequence] = None,
        defaultTimeStart: typing.Optional[NumberType] = None,
        defaultTimeEnd: typing.Optional[NumberType] = None,
        visibleTimeStart: typing.Optional[NumberType] = None,
        visibleTimeEnd: typing.Optional[NumberType] = None,
        buffer: typing.Optional[NumberType] = None,
        sidebarWidth: typing.Optional[NumberType] = None,
        rightSidebarWidth: typing.Optional[NumberType] = None,
        dragSnap: typing.Optional[NumberType] = None,
        minResizeWidth: typing.Optional[NumberType] = None,
        lineHeight: typing.Optional[NumberType] = None,
        itemHeightRatio: typing.Optional[NumberType] = None,
        minZoom: typing.Optional[NumberType] = None,
        maxZoom: typing.Optional[NumberType] = None,
        clickTolerance: typing.Optional[NumberType] = None,
        canMove: typing.Optional[bool] = None,
        canChangeGroup: typing.Optional[bool] = None,
        canResize: typing.Optional[typing.Union[str, bool]] = None,
        useResizeHandle: typing.Optional[bool] = None,
        traditionalZoom: typing.Optional[bool] = None,
        itemTouchSendsClick: typing.Optional[bool] = None,
        timeSteps: typing.Optional[dict] = None,
        disableScroll: typing.Optional[bool] = None,
        customItems: typing.Optional[bool] = None,
        customGroups: typing.Optional[bool] = None,
        customItemsContent: typing.Optional[ComponentType] = None,
        selectedItemColor: typing.Optional[str] = None,
        draggingItemColor: typing.Optional[str] = None,
        resizingItemBorder: typing.Optional[str] = None,
        itemsStyle: typing.Optional[dict] = None,
        itemsClass: typing.Optional[str] = None,
        customGroupsContent: typing.Optional[ComponentType] = None,
        groupsStyle: typing.Optional[dict] = None,
        groupsClass: typing.Optional[str] = None,
        dragInfoLabel: typing.Optional[bool] = None,
        dragInfoLabelStyle: typing.Optional[dict] = None,
        showTodayMarker: typing.Optional[bool] = None,
        todayMarkerInterval: typing.Optional[NumberType] = None,
        todayMarkerStyle: typing.Optional[dict] = None,
        customMarkers: typing.Optional[typing.Sequence] = None,
        showCursorMarker: typing.Optional[bool] = None,
        cursorMarkerStyle: typing.Optional[dict] = None,
        sidebarHeaderVariant: typing.Optional[str] = None,
        sidebarHeaderContent: typing.Optional[ComponentType] = None,
        timelineHeaderStyle: typing.Optional[dict] = None,
        dateHeaderStyle: typing.Optional[dict] = None,
        dateHeaderUnit: typing.Optional[str] = None,
        dateHeaderLabelFormat: typing.Optional[str] = None,
        dateHeaderHeight: typing.Optional[NumberType] = None,
        itemClickData: typing.Optional[dict] = None,
        itemDoubleClickData: typing.Optional[dict] = None,
        itemContextMenuData: typing.Optional[dict] = None,
        itemSelectData: typing.Optional[dict] = None,
        itemDimensions: typing.Optional[dict] = None,
        canvasClickData: typing.Optional[dict] = None,
        canvasDoubleClickData: typing.Optional[dict] = None,
        canvasContextMenuData: typing.Optional[dict] = None,
        zoomData: typing.Optional[dict] = None,
        boundsChangeData: typing.Optional[dict] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'boundsChangeData', 'buffer', 'canChangeGroup', 'canMove', 'canResize', 'canvasClickData', 'canvasContextMenuData', 'canvasDoubleClickData', 'clickTolerance', 'cursorMarkerStyle', 'customGroups', 'customGroupsContent', 'customItems', 'customItemsContent', 'customMarkers', 'dateHeaderHeight', 'dateHeaderLabelFormat', 'dateHeaderStyle', 'dateHeaderUnit', 'defaultTimeEnd', 'defaultTimeStart', 'disableScroll', 'dragInfoLabel', 'dragInfoLabelStyle', 'dragSnap', 'draggingItemColor', 'groups', 'groupsClass', 'groupsStyle', 'itemClickData', 'itemContextMenuData', 'itemDimensions', 'itemDoubleClickData', 'itemHeightRatio', 'itemSelectData', 'itemTouchSendsClick', 'items', 'itemsClass', 'itemsStyle', 'lineHeight', 'maxZoom', 'minResizeWidth', 'minZoom', 'resizingItemBorder', 'rightSidebarWidth', 'selectedItemColor', 'showCursorMarker', 'showTodayMarker', 'sidebarHeaderContent', 'sidebarHeaderVariant', 'sidebarWidth', 'timeSteps', 'timelineHeaderStyle', 'todayMarkerInterval', 'todayMarkerStyle', 'traditionalZoom', 'useResizeHandle', 'visibleTimeEnd', 'visibleTimeStart', 'zoomData']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'boundsChangeData', 'buffer', 'canChangeGroup', 'canMove', 'canResize', 'canvasClickData', 'canvasContextMenuData', 'canvasDoubleClickData', 'clickTolerance', 'cursorMarkerStyle', 'customGroups', 'customGroupsContent', 'customItems', 'customItemsContent', 'customMarkers', 'dateHeaderHeight', 'dateHeaderLabelFormat', 'dateHeaderStyle', 'dateHeaderUnit', 'defaultTimeEnd', 'defaultTimeStart', 'disableScroll', 'dragInfoLabel', 'dragInfoLabelStyle', 'dragSnap', 'draggingItemColor', 'groups', 'groupsClass', 'groupsStyle', 'itemClickData', 'itemContextMenuData', 'itemDimensions', 'itemDoubleClickData', 'itemHeightRatio', 'itemSelectData', 'itemTouchSendsClick', 'items', 'itemsClass', 'itemsStyle', 'lineHeight', 'maxZoom', 'minResizeWidth', 'minZoom', 'resizingItemBorder', 'rightSidebarWidth', 'selectedItemColor', 'showCursorMarker', 'showTodayMarker', 'sidebarHeaderContent', 'sidebarHeaderVariant', 'sidebarWidth', 'timeSteps', 'timelineHeaderStyle', 'todayMarkerInterval', 'todayMarkerStyle', 'traditionalZoom', 'useResizeHandle', 'visibleTimeEnd', 'visibleTimeStart', 'zoomData']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(DashCalendarTimeline, self).__init__(**args)

setattr(DashCalendarTimeline, "__init__", _explicitize_args(DashCalendarTimeline.__init__))
