# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class DashTimeline(Component):
    """A DashTimeline component.
DashTimeline renders React's Calendar Timeline inside the Dash App.

Keyword arguments:

- id (string; optional):
    The ID used to identify this component in Dash callbacks.

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

- clickData (dict; optional):
    Returns the Item ID and time for the item clicked.

- customGroups (boolean; default False):
    This will determine whether you'd want to set up custom content
    for groups or not.

- customGroupsContent (a list of or a singular dash component, string or number; optional):
    This will be used to set up custom content of groups in the
    sidebar.

- customItems (boolean; default False):
    This will determine whether you'd want to set up custom content
    for items or not.

- customItemsContent (a list of or a singular dash component, string or number; optional):
    This will be used to set up custom content of items in the main
    timeline.

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

- dragInfoLabel (boolean; default False):
    This will render a info label over the timeline while the item is
    being dragged around.

- dragInfoLabelStyle (dict; optional):
    Style applied to the dragInfoLabel.

- draggingItemColor (string; default "red"):
    Item color while the item is being dragged around.

- groups (list; default [{}]):
    The groups are used to determine the number of groups in a
    Timeline.

- groupsClass (string; optional):
    This will be used to set up custom css classes of content of
    groups in the sidebar.

- groupsStyle (dict; optional):
    This will be used to set up custom css style of content of groups
    in the sidebar.

- itemHeightRatio (number; optional):
    What percentage of the height of the line is taken by the item?
    Default 0.65.

- items (list; default [{}]):
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

- resizingItemBorder (string; default "2px solid red"):
    Item border (CSS border e.g, 2px solid red) while the item is
    being resized.

- rightSidebarWidth (number; optional):
    Width of the right sidebar in pixels. If set to 0, the right
    sidebar is not rendered. Defaults to 0.

- selectedItemColor (string; default "#1a6fb3"):
    Item color when item is selected.

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

- traditionalZoom (boolean; optional):
    Zoom in when scrolling the mouse up/down. Defaults to False.

- useResizeHandle (boolean; optional):
    Append a special .rct-drag-right handle to the elements and only
    resize if dragged from there. Defaults to False.

- visibleTimeEnd (number; optional):
    The exact ending viewport of the calendar.

- visibleTimeStart (number; optional):
    The exact starting viewport of the calendar."""
    _children_props = ['customItemsContent', 'customGroupsContent', 'sidebarHeaderContent']
    _base_nodes = ['customItemsContent', 'customGroupsContent', 'sidebarHeaderContent', 'children']
    _namespace = 'dash_calendar_timeline'
    _type = 'DashTimeline'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, groups=Component.UNDEFINED, items=Component.UNDEFINED, defaultTimeStart=Component.UNDEFINED, defaultTimeEnd=Component.UNDEFINED, visibleTimeStart=Component.UNDEFINED, visibleTimeEnd=Component.UNDEFINED, buffer=Component.UNDEFINED, sidebarWidth=Component.UNDEFINED, rightSidebarWidth=Component.UNDEFINED, minResizeWidth=Component.UNDEFINED, lineHeight=Component.UNDEFINED, itemHeightRatio=Component.UNDEFINED, minZoom=Component.UNDEFINED, maxZoom=Component.UNDEFINED, canMove=Component.UNDEFINED, canChangeGroup=Component.UNDEFINED, canResize=Component.UNDEFINED, useResizeHandle=Component.UNDEFINED, traditionalZoom=Component.UNDEFINED, timeSteps=Component.UNDEFINED, customItems=Component.UNDEFINED, customGroups=Component.UNDEFINED, customItemsContent=Component.UNDEFINED, selectedItemColor=Component.UNDEFINED, draggingItemColor=Component.UNDEFINED, resizingItemBorder=Component.UNDEFINED, itemsStyle=Component.UNDEFINED, itemsClass=Component.UNDEFINED, customGroupsContent=Component.UNDEFINED, groupsStyle=Component.UNDEFINED, groupsClass=Component.UNDEFINED, dragInfoLabel=Component.UNDEFINED, dragInfoLabelStyle=Component.UNDEFINED, sidebarHeaderVariant=Component.UNDEFINED, sidebarHeaderContent=Component.UNDEFINED, timelineHeaderStyle=Component.UNDEFINED, dateHeaderStyle=Component.UNDEFINED, dateHeaderUnit=Component.UNDEFINED, dateHeaderLabelFormat=Component.UNDEFINED, dateHeaderHeight=Component.UNDEFINED, clickData=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'buffer', 'canChangeGroup', 'canMove', 'canResize', 'clickData', 'customGroups', 'customGroupsContent', 'customItems', 'customItemsContent', 'dateHeaderHeight', 'dateHeaderLabelFormat', 'dateHeaderStyle', 'dateHeaderUnit', 'defaultTimeEnd', 'defaultTimeStart', 'dragInfoLabel', 'dragInfoLabelStyle', 'draggingItemColor', 'groups', 'groupsClass', 'groupsStyle', 'itemHeightRatio', 'items', 'itemsClass', 'itemsStyle', 'lineHeight', 'maxZoom', 'minResizeWidth', 'minZoom', 'resizingItemBorder', 'rightSidebarWidth', 'selectedItemColor', 'sidebarHeaderContent', 'sidebarHeaderVariant', 'sidebarWidth', 'timeSteps', 'timelineHeaderStyle', 'traditionalZoom', 'useResizeHandle', 'visibleTimeEnd', 'visibleTimeStart']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'buffer', 'canChangeGroup', 'canMove', 'canResize', 'clickData', 'customGroups', 'customGroupsContent', 'customItems', 'customItemsContent', 'dateHeaderHeight', 'dateHeaderLabelFormat', 'dateHeaderStyle', 'dateHeaderUnit', 'defaultTimeEnd', 'defaultTimeStart', 'dragInfoLabel', 'dragInfoLabelStyle', 'draggingItemColor', 'groups', 'groupsClass', 'groupsStyle', 'itemHeightRatio', 'items', 'itemsClass', 'itemsStyle', 'lineHeight', 'maxZoom', 'minResizeWidth', 'minZoom', 'resizingItemBorder', 'rightSidebarWidth', 'selectedItemColor', 'sidebarHeaderContent', 'sidebarHeaderVariant', 'sidebarWidth', 'timeSteps', 'timelineHeaderStyle', 'traditionalZoom', 'useResizeHandle', 'visibleTimeEnd', 'visibleTimeStart']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(DashTimeline, self).__init__(**args)
