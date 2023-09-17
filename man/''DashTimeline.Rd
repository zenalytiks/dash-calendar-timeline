% Auto-generated: do not edit by hand
\name{''DashTimeline}

\alias{''DashTimeline}

\title{DashTimeline component}

\description{
DashTimeline renders React's Calendar Timeline inside the Dash App.
}

\usage{
''DashTimeline(id=NULL, buffer=NULL, canChangeGroup=NULL, canMove=NULL,
canResize=NULL, clickData=NULL, customGroups=NULL,
customGroupsContent=NULL, customItems=NULL,
customItemsContent=NULL, dateHeaderHeight=NULL,
dateHeaderLabelFormat=NULL, dateHeaderStyle=NULL,
dateHeaderUnit=NULL, defaultTimeEnd=NULL,
defaultTimeStart=NULL, dragInfoLabel=NULL,
dragInfoLabelStyle=NULL, draggingItemColor=NULL,
groups=NULL, groupsClass=NULL, groupsStyle=NULL,
itemHeightRatio=NULL, items=NULL, itemsClass=NULL,
itemsStyle=NULL, lineHeight=NULL, maxZoom=NULL,
minResizeWidth=NULL, minZoom=NULL, resizingItemBorder=NULL,
rightSidebarWidth=NULL, selectedItemColor=NULL,
sidebarHeaderContent=NULL, sidebarHeaderVariant=NULL,
sidebarWidth=NULL, timeSteps=NULL, timelineHeaderStyle=NULL,
traditionalZoom=NULL, useResizeHandle=NULL,
visibleTimeEnd=NULL, visibleTimeStart=NULL)
}

\arguments{
\item{id}{Character. The ID used to identify this component in Dash callbacks.}

\item{buffer}{Numeric. a number (default to 3) which represents the extra timeline rendered on right and lift of the visible area which the user will scroll through before the time rerenders. Note: setting buffer to 1 will disable the scrolling on the timeline.}

\item{canChangeGroup}{Logical. Can items be moved between groups? Can be overridden in the items array. Defaults to true}

\item{canMove}{Logical. Can items be dragged around? Can be overridden in the items array. Defaults to true}

\item{canResize}{Character | logical. Can items be resized? Can be overridden in the items array. Accepted values: false, "left", "right", "both". Defaults to "right". If you pass true, it will be treated as "right" to not break compatibility with versions 0.9 and below.}

\item{clickData}{Named list. Returns the Item ID and time for the item clicked.}

\item{customGroups}{Logical. This will determine whether you'd want to set up custom content for groups or not.}

\item{customGroupsContent}{A list of or a singular dash component, string or number. This will be used to set up custom content of groups in the sidebar.}

\item{customItems}{Logical. This will determine whether you'd want to set up custom content for items or not.}

\item{customItemsContent}{A list of or a singular dash component, string or number. This will be used to set up custom content of items in the main timeline.}

\item{dateHeaderHeight}{Numeric. Determines the height of the header in pixels. Default 30.}

\item{dateHeaderLabelFormat}{Character. Controls the how to format the interval label}

\item{dateHeaderStyle}{Named list. Style applied to the root of the header.}

\item{dateHeaderUnit}{Character. Determines the intervals between columns. Values can be second, minute, hour, day, week, month, year or primaryHeader.}

\item{defaultTimeEnd}{Numeric. This sets the end time for the timeline.}

\item{defaultTimeStart}{Numeric. This sets the start time for the timeline.}

\item{dragInfoLabel}{Logical. This will render a info label over the timeline while the item is being dragged around.}

\item{dragInfoLabelStyle}{Named list. Style applied to the dragInfoLabel.}

\item{draggingItemColor}{Character. Item color while the item is being dragged around.}

\item{groups}{Unnamed list. The groups are used to determine the number of groups in a Timeline.}

\item{groupsClass}{Character. This will be used to set up custom css classes of content of groups in the sidebar.}

\item{groupsStyle}{Named list. This will be used to set up custom css style of content of groups in the sidebar.}

\item{itemHeightRatio}{Numeric. What percentage of the height of the line is taken by the item? Default 0.65}

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

\item{traditionalZoom}{Logical. Zoom in when scrolling the mouse up/down. Defaults to false.}

\item{useResizeHandle}{Logical. Append a special .rct-drag-right handle to the elements and only resize if dragged from there. Defaults to false.}

\item{visibleTimeEnd}{Numeric. The exact ending viewport of the calendar.}

\item{visibleTimeStart}{Numeric. The exact starting viewport of the calendar.}
}

\value{named list of JSON elements corresponding to React.js properties and their values}

