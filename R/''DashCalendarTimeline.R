# AUTO GENERATED FILE - DO NOT EDIT

#' @export
''DashCalendarTimeline <- function(id=NULL, buffer=NULL, canChangeGroup=NULL, canMove=NULL, canResize=NULL, clickData=NULL, customGroups=NULL, customGroupsContent=NULL, customItems=NULL, customItemsContent=NULL, dateHeaderHeight=NULL, dateHeaderLabelFormat=NULL, dateHeaderStyle=NULL, dateHeaderUnit=NULL, defaultTimeEnd=NULL, defaultTimeStart=NULL, dragInfoLabel=NULL, dragInfoLabelStyle=NULL, draggingItemColor=NULL, groups=NULL, groupsClass=NULL, groupsStyle=NULL, itemHeightRatio=NULL, items=NULL, itemsClass=NULL, itemsStyle=NULL, lineHeight=NULL, maxZoom=NULL, minResizeWidth=NULL, minZoom=NULL, resizingItemBorder=NULL, rightSidebarWidth=NULL, selectedItemColor=NULL, sidebarHeaderContent=NULL, sidebarHeaderVariant=NULL, sidebarWidth=NULL, timeSteps=NULL, timelineHeaderStyle=NULL, traditionalZoom=NULL, useResizeHandle=NULL, visibleTimeEnd=NULL, visibleTimeStart=NULL) {
    
    props <- list(id=id, buffer=buffer, canChangeGroup=canChangeGroup, canMove=canMove, canResize=canResize, clickData=clickData, customGroups=customGroups, customGroupsContent=customGroupsContent, customItems=customItems, customItemsContent=customItemsContent, dateHeaderHeight=dateHeaderHeight, dateHeaderLabelFormat=dateHeaderLabelFormat, dateHeaderStyle=dateHeaderStyle, dateHeaderUnit=dateHeaderUnit, defaultTimeEnd=defaultTimeEnd, defaultTimeStart=defaultTimeStart, dragInfoLabel=dragInfoLabel, dragInfoLabelStyle=dragInfoLabelStyle, draggingItemColor=draggingItemColor, groups=groups, groupsClass=groupsClass, groupsStyle=groupsStyle, itemHeightRatio=itemHeightRatio, items=items, itemsClass=itemsClass, itemsStyle=itemsStyle, lineHeight=lineHeight, maxZoom=maxZoom, minResizeWidth=minResizeWidth, minZoom=minZoom, resizingItemBorder=resizingItemBorder, rightSidebarWidth=rightSidebarWidth, selectedItemColor=selectedItemColor, sidebarHeaderContent=sidebarHeaderContent, sidebarHeaderVariant=sidebarHeaderVariant, sidebarWidth=sidebarWidth, timeSteps=timeSteps, timelineHeaderStyle=timelineHeaderStyle, traditionalZoom=traditionalZoom, useResizeHandle=useResizeHandle, visibleTimeEnd=visibleTimeEnd, visibleTimeStart=visibleTimeStart)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'DashCalendarTimeline',
        namespace = 'dash_calendar_timeline',
        propNames = c('id', 'buffer', 'canChangeGroup', 'canMove', 'canResize', 'clickData', 'customGroups', 'customGroupsContent', 'customItems', 'customItemsContent', 'dateHeaderHeight', 'dateHeaderLabelFormat', 'dateHeaderStyle', 'dateHeaderUnit', 'defaultTimeEnd', 'defaultTimeStart', 'dragInfoLabel', 'dragInfoLabelStyle', 'draggingItemColor', 'groups', 'groupsClass', 'groupsStyle', 'itemHeightRatio', 'items', 'itemsClass', 'itemsStyle', 'lineHeight', 'maxZoom', 'minResizeWidth', 'minZoom', 'resizingItemBorder', 'rightSidebarWidth', 'selectedItemColor', 'sidebarHeaderContent', 'sidebarHeaderVariant', 'sidebarWidth', 'timeSteps', 'timelineHeaderStyle', 'traditionalZoom', 'useResizeHandle', 'visibleTimeEnd', 'visibleTimeStart'),
        package = 'dashCalendarTimeline'
        )

    structure(component, class = c('dash_component', 'list'))
}
