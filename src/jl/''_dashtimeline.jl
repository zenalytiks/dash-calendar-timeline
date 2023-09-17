# AUTO GENERATED FILE - DO NOT EDIT

export ''_dashtimeline

"""
    ''_dashtimeline(;kwargs...)

A DashTimeline component.
DashTimeline renders React's Calendar Timeline inside the Dash App.
Keyword arguments:
- `id` (String; optional): The ID used to identify this component in Dash callbacks.
- `buffer` (Real; optional): a number (default to 3) which represents the extra timeline rendered on right and lift of the visible area which the user will scroll through before the time rerenders. Note: setting buffer to 1 will disable the scrolling on the timeline.
- `canChangeGroup` (Bool; optional): Can items be moved between groups? Can be overridden in the items array. Defaults to true
- `canMove` (Bool; optional): Can items be dragged around? Can be overridden in the items array. Defaults to true
- `canResize` (String | Bool; optional): Can items be resized? Can be overridden in the items array. Accepted values: false, "left", "right", "both". Defaults to "right". If you pass true, it will be treated as "right" to not break compatibility with versions 0.9 and below.
- `clickData` (Dict; optional): Returns the Item ID and time for the item clicked.
- `customGroups` (Bool; optional): This will determine whether you'd want to set up custom content for groups or not.
- `customGroupsContent` (a list of or a singular dash component, string or number; optional): This will be used to set up custom content of groups in the sidebar.
- `customItems` (Bool; optional): This will determine whether you'd want to set up custom content for items or not.
- `customItemsContent` (a list of or a singular dash component, string or number; optional): This will be used to set up custom content of items in the main timeline.
- `dateHeaderHeight` (Real; optional): Determines the height of the header in pixels. Default 30.
- `dateHeaderLabelFormat` (String; optional): Controls the how to format the interval label
- `dateHeaderStyle` (Dict; optional): Style applied to the root of the header.
- `dateHeaderUnit` (String; optional): Determines the intervals between columns. Values can be second, minute, hour, day, week, month, year or primaryHeader.
- `defaultTimeEnd` (Real; optional): This sets the end time for the timeline.
- `defaultTimeStart` (Real; optional): This sets the start time for the timeline.
- `dragInfoLabel` (Bool; optional): This will render a info label over the timeline while the item is being dragged around.
- `dragInfoLabelStyle` (Dict; optional): Style applied to the dragInfoLabel.
- `draggingItemColor` (String; optional): Item color while the item is being dragged around.
- `groups` (Array; optional): The groups are used to determine the number of groups in a Timeline.
- `groupsClass` (String; optional): This will be used to set up custom css classes of content of groups in the sidebar.
- `groupsStyle` (Dict; optional): This will be used to set up custom css style of content of groups in the sidebar.
- `itemHeightRatio` (Real; optional): What percentage of the height of the line is taken by the item? Default 0.65
- `items` (Array; optional): The items are used to determine the number of items within a single group.
- `itemsClass` (String; optional): This will be used to set up custom css classes for content of custom items in the main timeline.
- `itemsStyle` (Dict; optional): This will be used to set up custom css styles for content of custom items in the main timeline.
- `lineHeight` (Real; optional): Height of one line in the calendar in pixels. Default 30
- `maxZoom` (Real; optional): Largest time the calendar can zoom to in milliseconds. Default 5 * 365.24 * 86400 * 1000 (5 years)
- `minResizeWidth` (Real; optional): The minimum width, in pixels, of a timeline entry when it's possible to resize. If not reached, you must zoom in to resize more. Default to 20.
- `minZoom` (Real; optional): Smallest time the calendar can zoom to in milliseconds. Default 60 * 60 * 1000 (1 hour)
- `resizingItemBorder` (String; optional): Item border (CSS border e.g, 2px solid red) while the item is being resized.
- `rightSidebarWidth` (Real; optional): Width of the right sidebar in pixels. If set to 0, the right sidebar is not rendered. Defaults to 0.
- `selectedItemColor` (String; optional): Item color when item is selected.
- `sidebarHeaderContent` (a list of or a singular dash component, string or number; optional): Renders the Content above the sidebar.
- `sidebarHeaderVariant` (String; optional): Determines whether the content goes above the left or right sidebar.
- `sidebarWidth` (Real; optional): Width of the sidebar in pixels. If set to 0, the sidebar is not rendered. Defaults to 150.
- `timeSteps` (Dict; optional): With what step to display different units. E.g. 15 for minute means only minutes 0, 15, 30 and 45 will be shown.
Default:
       {
         second: 1,
         minute: 1,
         hour: 1,
         day: 1,
         month: 1,
         year: 1
       }
- `timelineHeaderStyle` (Dict; optional): Style applied to the root component of headers.
- `traditionalZoom` (Bool; optional): Zoom in when scrolling the mouse up/down. Defaults to false.
- `useResizeHandle` (Bool; optional): Append a special .rct-drag-right handle to the elements and only resize if dragged from there. Defaults to false.
- `visibleTimeEnd` (Real; optional): The exact ending viewport of the calendar.
- `visibleTimeStart` (Real; optional): The exact starting viewport of the calendar.
"""
function ''_dashtimeline(; kwargs...)
        available_props = Symbol[:id, :buffer, :canChangeGroup, :canMove, :canResize, :clickData, :customGroups, :customGroupsContent, :customItems, :customItemsContent, :dateHeaderHeight, :dateHeaderLabelFormat, :dateHeaderStyle, :dateHeaderUnit, :defaultTimeEnd, :defaultTimeStart, :dragInfoLabel, :dragInfoLabelStyle, :draggingItemColor, :groups, :groupsClass, :groupsStyle, :itemHeightRatio, :items, :itemsClass, :itemsStyle, :lineHeight, :maxZoom, :minResizeWidth, :minZoom, :resizingItemBorder, :rightSidebarWidth, :selectedItemColor, :sidebarHeaderContent, :sidebarHeaderVariant, :sidebarWidth, :timeSteps, :timelineHeaderStyle, :traditionalZoom, :useResizeHandle, :visibleTimeEnd, :visibleTimeStart]
        wild_props = Symbol[]
        return Component("''_dashtimeline", "DashTimeline", "dash_calendar_timeline", available_props, wild_props; kwargs...)
end

