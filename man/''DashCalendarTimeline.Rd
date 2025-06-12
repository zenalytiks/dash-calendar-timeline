% Auto-generated: do not edit by hand
\name{''DashCalendarTimeline}

\alias{''DashCalendarTimeline}

\title{DashCalendarTimeline component}

\description{
DashCalendarTimeline renders React's Calendar Timeline inside the Dash App.
}

\usage{
''DashCalendarTimeline(id=NULL, boundsChangeData=NULL, buffer=NULL,
canChangeGroup=NULL, canMove=NULL, canResize=NULL,
canvasClickData=NULL, canvasContextMenuData=NULL,
canvasDoubleClickData=NULL, clickTolerance=NULL,
cursorMarkerStyle=NULL, customGroups=NULL,
customGroupsContent=NULL, customItems=NULL,
customItemsContent=NULL, customMarkers=NULL,
dateHeaderHeight=NULL, dateHeaderLabelFormat=NULL,
dateHeaderStyle=NULL, dateHeaderUnit=NULL,
defaultTimeEnd=NULL, defaultTimeStart=NULL,
dragInfoLabel=NULL, dragInfoLabelStyle=NULL, dragSnap=NULL,
draggingItemColor=NULL, groups=NULL, groupsClass=NULL,
groupsStyle=NULL, itemClickData=NULL,
itemContextMenuData=NULL, itemDoubleClickData=NULL,
itemHeightRatio=NULL, itemSelectData=NULL,
itemTouchSendsClick=NULL, items=NULL, itemsClass=NULL,
itemsStyle=NULL, lineHeight=NULL, maxZoom=NULL,
minResizeWidth=NULL, minZoom=NULL, resizingItemBorder=NULL,
rightSidebarWidth=NULL, selectedItemColor=NULL,
showCursorMarker=NULL, showTodayMarker=NULL,
sidebarHeaderContent=NULL, sidebarHeaderVariant=NULL,
sidebarWidth=NULL, timeSteps=NULL, timelineHeaderStyle=NULL,
todayMarkerInterval=NULL, todayMarkerStyle=NULL,
traditionalZoom=NULL, useResizeHandle=NULL,
visibleTimeEnd=NULL, visibleTimeStart=NULL, zoomData=NULL)
}

\arguments{
\item{id}{Character. The ID used to identify this component in Dash callbacks.}

\item{boundsChangeData}{Named list. Called when the bounds in the calendar's canvas change. Use it for example to load new data to display. (see "Behind the scenes" below). canvasTimeStart and canvasTimeEnd are unix timestamps in milliseconds.}

\item{buffer}{Numeric. a number (default to 3) which represents the extra timeline rendered on right and lift of the visible area which the user will scroll through before the time rerenders. Note: setting buffer to 1 will disable the scrolling on the timeline.}

\item{canChangeGroup}{Logical. Can items be moved between groups? Can be overridden in the items array. Defaults to true}

\item{canMove}{Logical. Can items be dragged around? Can be overridden in the items array. Defaults to true}

\item{canResize}{Character | logical. Can items be resized? Can be overridden in the items array. Accepted values: false, "left", "right", "both". Defaults to "right". If you pass true, it will be treated as "right" to not break compatibility with versions 0.9 and below.}

\item{canvasClickData}{Named list. Called when an empty spot on the canvas was clicked. Get the group ID and the time as arguments. For example open a "new item" window after this.}

\item{canvasContextMenuData}{Named list. Called when the canvas is clicked by the right button of the mouse. Note: If this property is set the default context menu doesn't appear.}

\item{canvasDoubleClickData}{Named list. Called when an empty spot on the canvas was double clicked. Get the group ID and the time as arguments.}

\item{clickTolerance}{Numeric. How many pixels we can drag the background for it to be counted as a click on the background. Default 3.}

\item{cursorMarkerStyle}{Named list. Use this to render special styles for the cursorMarker.}

\item{customGroups}{Logical. This will determine whether you'd want to set up custom content for groups or not.}

\item{customGroupsContent}{A list of or a singular dash component, string or number. This will be used to set up custom content of groups in the sidebar.}

\item{customItems}{Logical. This will determine whether you'd want to set up custom content for items or not.}

\item{customItemsContent}{A list of or a singular dash component, string or number. This will be used to set up custom content of items in the main timeline.}

\item{customMarkers}{Unnamed list. Marker that is placed on the specified date/time. Example usage.
[
   {'date': today, 'style':{'backgorund-color':'red'}},
   {'date': tomorrow, 'style':{'backgorund-color':'green'}},
   {'date': nextFriday, 'style':{'backgorund-color':'blue'}},
]}

\item{dateHeaderHeight}{Numeric. Determines the height of the header in pixels. Default 30.}

\item{dateHeaderLabelFormat}{Character. Controls the how to format the interval label}

\item{dateHeaderStyle}{Named list. Style applied to the root of the header.}

\item{dateHeaderUnit}{Character. Determines the intervals between columns. Values can be second, minute, hour, day, week, month, year or primaryHeader.}

\item{defaultTimeEnd}{Numeric. This sets the end time for the timeline.}

\item{defaultTimeStart}{Numeric. This sets the start time for the timeline.}

\item{dragInfoLabel}{Logical. This will render a info label over the timeline while the item is being dragged around.}

\item{dragInfoLabelStyle}{Named list. Style applied to the dragInfoLabel.}

\item{dragSnap}{Numeric. Snapping unit when dragging items. Defaults to 15 * 60 * 1000 or 15min. When so, the items will snap to 15min intervals when dragging.}

\item{draggingItemColor}{Character. Item color while the item is being dragged around.}

\item{groups}{Unnamed list. The groups are used to determine the number of groups in a Timeline.}

\item{groupsClass}{Character. This will be used to set up custom css classes of content of groups in the sidebar.}

\item{groupsStyle}{Named list. This will be used to set up custom css style of content of groups in the sidebar.}

\item{itemClickData}{Named list. Called when an item is clicked. Note: the item must be selected before it's clicked... except if it's a touch event and itemTouchSendsClick is enabled. time is the time that corresponds to where you click on the item in the timeline.}

\item{itemContextMenuData}{Named list. Called when the item is clicked by the right button of the mouse. time is the time that corresponds to where you context click on the item in the timeline. Note: If this property is set the default context menu doesn't appear.}

\item{itemDoubleClickData}{Named list. Called when an item was double clicked. time is the time that corresponds to where you double click on the item in the timeline.}

\item{itemHeightRatio}{Numeric. What percentage of the height of the line is taken by the item? Default 0.65}

\item{itemSelectData}{Named list. This is sent on the first click on an item. time is the time that corresponds to where you click/select on the item in the timeline.}

\item{itemTouchSendsClick}{Logical. Normally tapping (touching) an item selects it. If this is set to true, a tap will have the same effect, as selecting with the first click and then clicking again to open and send the onItemClick event. Defaults to false.}

\item{items}{Unnamed list. The items are used to determine the number of items within a single group.}

\item{itemsClass}{Character. This will be used to set up custom css classes for content of custom items in the main timeline.}

\item{itemsStyle}{Named list. This will be used to set up custom css styles for content of custom items in the main timeline.}

\item{lineHeight}{Numeric. Height of one line in the calendar in pixels. Default 30}

\item{maxZoom}{Numeric. Largest time the calendar can zoom to in milliseconds. Default 5 * 365.24 * 86400 * 1000 (5 years)}

\item{minResizeWidth}{Numeric. The minimum width, in pixels, of a timeline entry when it's possible to resize. If not reached, you must zoom in to resize more. Default to 20.}

\item{minZoom}{Numeric. Smallest time the calendar can zoom to in milliseconds. Default 60 * 60 * 1000 (1 hour)}

\item{resizingItemBorder}{Character. Item border (CSS border e.g, 2px solid red) while the item is being resized.}

\item{rightSidebarWidth}{Numeric. Width of the right sidebar in pixels. If set to 0, the right sidebar is not rendered. Defaults to 0.}

\item{selectedItemColor}{Character. Item color when item is selected.}

\item{showCursorMarker}{Logical. Marker that is displayed when hovering over the timeline and matches where your cursor is.}

\item{showTodayMarker}{Logical. Marker that is placed on the current date/time.}

\item{sidebarHeaderContent}{A list of or a singular dash component, string or number. Renders the Content above the sidebar.}

\item{sidebarHeaderVariant}{Character. Determines whether the content goes above the left or right sidebar.}

\item{sidebarWidth}{Numeric. Width of the sidebar in pixels. If set to 0, the sidebar is not rendered. Defaults to 150.}

\item{timeSteps}{Named list. With what step to display different units. E.g. 15 for minute means only minutes 0, 15, 30 and 45 will be shown.
Default:
       {
         second: 1,
         minute: 1,
         hour: 1,
         day: 1,
         month: 1,
         year: 1
       }}

\item{timelineHeaderStyle}{Named list. Style applied to the root component of headers.}

\item{todayMarkerInterval}{Numeric. How often the TodayMarker refreshes. Value represents milliseconds. Default is 10000.}

\item{todayMarkerStyle}{Named list. Use this to render special styles for the todayMarker.}

\item{traditionalZoom}{Logical. Zoom in when scrolling the mouse up/down. Defaults to false.}

\item{useResizeHandle}{Logical. Append a special .rct-drag-right handle to the elements and only resize if dragged from there. Defaults to false.}

\item{visibleTimeEnd}{Numeric. The exact ending viewport of the calendar.}

\item{visibleTimeStart}{Numeric. The exact starting viewport of the calendar.}

\item{zoomData}{Named list. Called when the timeline is zoomed, either via mouse/pinch zoom or clicking header to change timeline units.}
}

\value{named list of JSON elements corresponding to React.js properties and their values}

