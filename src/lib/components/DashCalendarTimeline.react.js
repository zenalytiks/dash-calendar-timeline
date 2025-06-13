import React, {useState, useEffect} from 'react';
import PropTypes from 'prop-types';
import Timeline, { TimelineMarkers,
  CustomMarker,
  TodayMarker,
  CursorMarker,
  TimelineHeaders,
  SidebarHeader,
  DateHeader } from 'react-calendar-timeline';
import './style.css';
import './Timeline.scss';
import moment from "moment";

/**
 * DashCalendarTimeline renders React's Calendar Timeline inside the Dash App.
 */
export default function DashCalendarTimeline(props) {
    const{
    id,
    setProps,
    groups,
    items, 
    defaultTimeStart,
    defaultTimeEnd,
    visibleTimeStart,
    visibleTimeEnd,
    buffer,
    sidebarWidth,
    rightSidebarWidth,
    minResizeWidth,
    dragSnap,
    lineHeight,
    itemHeightRatio,
    minZoom,
    maxZoom,
    clickTolerance,
    canMove,
    canChangeGroup,
    canResize,
    useResizeHandle,
    traditionalZoom,
    itemTouchSendsClick,
    timeSteps,
    customItems,
    customGroups,
    customItemsContent,
    customGroupsContent,
    selectedItemColor,
    draggingItemColor,
    resizingItemBorder,
    itemsStyle,
    itemsClass,
    groupsStyle,
    groupsClass,
    dragInfoLabel,
    dragInfoLabelStyle,
    sidebarHeaderVariant,
    sidebarHeaderContent,
    timelineHeaderStyle,
    dateHeaderStyle,
    dateHeaderUnit,
    dateHeaderLabelFormat,
    dateHeaderHeight,
    showTodayMarker,
    todayMarkerInterval,
    todayMarkerStyle,
    customMarkers,
    showCursorMarker,
    cursorMarkerStyle,
    // eslint-disable-next-line no-unused-vars
    itemClickData,
    itemDoubleClickData,
    itemContextMenuData,
    itemSelectData,
    canvasClickData,
    canvasDoubleClickData,
    canvasContextMenuData,
    zoomData,
    boundsChangeData
  } = props;

  const [draggedItem, setDraggedItem] = useState(undefined);
  
  const [currentItems, setCurrentItems] = useState(items);
  
  const [hasLocalModifications, setHasLocalModifications] = useState(false);
  
  const [lastReceivedItems, setLastReceivedItems] = useState(items);

  const [localVisibleTimeStart, setLocalVisibleTimeStart] = useState(visibleTimeStart || defaultTimeStart);
  const [localVisibleTimeEnd, setLocalVisibleTimeEnd] = useState(visibleTimeEnd || defaultTimeEnd);

  const [lastVisibleTimeStart, setLastVisibleTimeStart] = useState(visibleTimeStart);
  const [lastVisibleTimeEnd, setLastVisibleTimeEnd] = useState(visibleTimeEnd);

  const itemsHaveChanged = (newItems, oldItems) => {
    if (newItems.length !== oldItems.length) return true;
    
    const newIds = new Set(newItems.map(item => item.id));
    const oldIds = new Set(oldItems.map(item => item.id));
    
    if (newIds.size !== oldIds.size) return true;
    
    for (let id of newIds) {
      if (!oldIds.has(id)) return true;
    }
    
    return false;
  };

  useEffect(() => {
    const itemsChanged = itemsHaveChanged(items, lastReceivedItems);
    
    if (itemsChanged) {
      setCurrentItems(items);
      setHasLocalModifications(false);
      setLastReceivedItems(items);
    } else if (!hasLocalModifications) {
      setCurrentItems(items);
      setLastReceivedItems(items);
    }
  }, [items, hasLocalModifications, lastReceivedItems]);

  useEffect(() => {

    const timeStartChanged = visibleTimeStart !== lastVisibleTimeStart && visibleTimeStart !== localVisibleTimeStart;
    const timeEndChanged = visibleTimeEnd !== lastVisibleTimeEnd && visibleTimeEnd !== localVisibleTimeEnd;
    
    if ((timeStartChanged || timeEndChanged) && visibleTimeStart && visibleTimeEnd) {

      setLocalVisibleTimeStart(visibleTimeStart);
      setLocalVisibleTimeEnd(visibleTimeEnd);
    }
    
    setLastVisibleTimeStart(visibleTimeStart);
    setLastVisibleTimeEnd(visibleTimeEnd);
  }, [visibleTimeStart, visibleTimeEnd, lastVisibleTimeStart, lastVisibleTimeEnd, localVisibleTimeStart, localVisibleTimeEnd]);

  const handleItemClick = (itemId, e, time) => {
    const updatedClickData = {
      itemId,
      time,
      clickX: e.clientX,
      clickY: e.clientY
    };

    setProps({
      itemClickData: updatedClickData
    });
  };

  const handleItemDoubleClick = (itemId, e, time) => {
    const updatedDoubleClickData = {
      itemId,
      time,
      clickX: e.clientX,
      clickY: e.clientY
    };

    setProps({
      itemDoubleClickData: updatedDoubleClickData
    })
  };

  const handleItemContextMenu = (itemId, e, time) => {
    const updatedContextMenu = {
      itemId,
      time,
      clickX: e.clientX,
      clickY: e.clientY
    };

    setProps({
      itemContextMenuData: updatedContextMenu
    })
  };

  const handleItemSelect = (itemId, e, time) => {
    const updatedSelectData = {
      itemId,
      time,
      clickX: e.clientX,
      clickY: e.clientY
    };

    setProps({
      itemSelectData: updatedSelectData
    })
  };

  const handleCanvasClick = (groupId, time, e) => {
    const updatedCanvasClickData = {
      groupId,
      time,
      clickX: e.clientX,
      clickY: e.clientY
    };

    setProps({
      canvasClickData: updatedCanvasClickData
    })
  };

  const handleCanvasDoubleClick = (groupId, time, e) => {
    const updatedCanvasDoubleClickData = {
      groupId,
      time,
      clickX: e.clientX,
      clickY: e.clientY
    };

    setProps({
      canvasDoubleClickData: updatedCanvasDoubleClickData
    })
  };

  const handleCanvasContextMenu = (groupId, time, e) => {
    const updatedCanvasContextMenuData = {
      groupId,
      time,
      clickX: e.clientX,
      clickY: e.clientY
    };

    setProps({
      canvasContextMenuData: updatedCanvasContextMenuData
    })
  };

  const handleZoom = (timelineContext, unit) => {
    const zoomVisibleTimeEnd = timelineContext.visibleTimeEnd
    const zoomVisibleTimeStart = timelineContext.visibleTimeStart
    const zoomTimelineWidth = timelineContext.timelineWidth
    const zoomCanvasTimeStart = timelineContext.canvasTimeStart
    const zoomCanvasTimeEnd = timelineContext.canvasTimeEnd
    const updatedZoomData = {
      zoomTimelineWidth,
      zoomVisibleTimeStart,
      zoomVisibleTimeEnd,
      zoomCanvasTimeStart,
      zoomCanvasTimeEnd,
      unit
    };

    setProps({
      zoomData: updatedZoomData
    })
  };

  const handleBoundsChange = (canvasTimeStart, canvasTimeEnd) => {
    const updatedBoundsChangeData = {
      canvasTimeStart,
      canvasTimeEnd
    };

    setProps({
      boundsChangeData: updatedBoundsChangeData
    })
  };

  const handleTimeChange = (newVisibleTimeStart, newVisibleTimeEnd, updateScrollCanvas) => {
    setLocalVisibleTimeStart(newVisibleTimeStart);
    setLocalVisibleTimeEnd(newVisibleTimeEnd);
    
    updateScrollCanvas(newVisibleTimeStart, newVisibleTimeEnd);
    
  };

  const itemRenderer = ({ item, itemContext, getItemProps, getResizeProps }) => {
    const { left: leftResizeProps, right: rightResizeProps } = getResizeProps();
    console.log(customItemsContent);
    
    const backgroundColor = itemContext.selected 
                              ? (itemContext.dragging 
                                  ? draggingItemColor : selectedItemColor
                                ) 
                              : getItemProps(item.itemProps).style.background;
    const borderResizing = itemContext.resizing ? resizingItemBorder : getItemProps(item.itemProps).style.border;
  
    const modifiedItemProps = {
      ...getItemProps(item.itemProps),
      style: {
        ...getItemProps(item.itemProps).style,
        background: backgroundColor,
        border: borderResizing
      }
    };
  
    // Get the index of current item to access corresponding custom content
    const itemIndex = currentItems.findIndex(i => i.id === item.id);
    const customContent = customItems && customItemsContent[itemIndex] 
      ? customItemsContent[itemIndex] 
      : null;
  
    return (
      <div {...modifiedItemProps}>
        {itemContext.useResizeHandle ? <div {...leftResizeProps} /> : ''}
        <div style={itemsStyle} className={itemsClass}>
          {customItems && customContent
            ? React.cloneElement(customContent, { item, itemContext })
            : itemContext.title}
        </div>
        {itemContext.useResizeHandle ? <div {...rightResizeProps} /> : ''}
      </div>
    );
  };
  
  const groupRenderer = ({ group }) => {
    // Get the index of current group to access corresponding custom content
    const groupIndex = groups.findIndex(g => g.id === group.id);
    const customContent = customGroups && customGroupsContent[groupIndex] 
      ? customGroupsContent[groupIndex] 
      : null;
  
    return (
      <div style={groupsStyle} className={groupsClass}>
        {customGroups && customContent
          ? React.cloneElement(customContent, { group })
          : group.title}
      </div>
    );
  }

  const handleItemMove = (itemId, dragTime, newGroupOrder) => {
    const updatedItems = currentItems.map((item) =>
      item.id === itemId
        ? {
            ...item,
            start_time: dragTime,
            end_time: dragTime + (item.end_time - item.start_time),
            group: groups[newGroupOrder].id,
          }
        : item
    );

    setCurrentItems(updatedItems);
    
    setHasLocalModifications(true);
    
    setProps({items: updatedItems});
    setDraggedItem(undefined);
  };

  const handleItemResize = (itemId, time, edge) => {
    const updatedItems = currentItems.map((item) =>
      item.id === itemId
        ? {
            ...item,
            start_time: edge === 'left' ? time : item.start_time,
            end_time: edge === 'left' ? item.end_time : time,
          }
        : item
    );

    setCurrentItems(updatedItems);
    
    setHasLocalModifications(true);
    
    setProps({items: updatedItems});
    setDraggedItem(undefined);
  };

  const InfoLabel = ({ item, group, time }) => {
    const date = moment(time, "x");
    const label = group ? group.title : "";

    const defaultStyles = {
      display: "inline-block",
      background: "rgba(0, 0, 0, 0.5)",
      color: "white",
      padding: 10,
      fontSize: 20,
      borderRadius: 5,
      zIndex: 85
    }

    const mergedStyles = { ...defaultStyles, ...dragInfoLabelStyle };
  
    return (
      <div
        style={mergedStyles}
      >
        {`${date.format("LLL")}, ${label}`}
      </div>
    );
  }

  const handleItemDrag = ({ eventType, itemId, time, edge, newGroupOrder }) => {
    let item = draggedItem ? draggedItem.item : undefined;
    if (!item) {
      item = currentItems.find(i => i.id === itemId);
    }
    setDraggedItem({ item, group: groups[newGroupOrder], time });
  };

  return (
      <div id={id}>
          <Timeline
            groups={groups}
            items={currentItems}
            defaultTimeStart={defaultTimeStart}
            defaultTimeEnd={defaultTimeEnd}
            visibleTimeStart={localVisibleTimeStart}
            visibleTimeEnd={localVisibleTimeEnd}
            buffer={buffer}
            sidebarWidth={sidebarWidth}
            rightSidebarWidth={rightSidebarWidth}
            minResizeWidth={minResizeWidth}
            dragSnap={dragSnap}
            lineHeight={lineHeight}
            itemHeightRatio={itemHeightRatio}
            minZoom={minZoom}
            maxZoom={maxZoom}
            clickTolerance={clickTolerance}
            canMove={canMove}
            canChangeGroup={canChangeGroup}
            canResize={canResize}
            useResizeHandle={useResizeHandle}
            traditionalZoom={traditionalZoom}
            itemTouchSendsClick={itemTouchSendsClick}
            timeSteps={timeSteps}
            onItemSelect={handleItemSelect}
            onItemClick={handleItemClick}
            onItemDoubleClick={handleItemDoubleClick}
            onItemContextMenu={handleItemContextMenu}
            onCanvasClick={handleCanvasClick}
            onCanvasDoubleClick={handleCanvasDoubleClick}
            onCanvasContextMenu={handleCanvasContextMenu}
            onZoom={handleZoom}
            onItemMove={handleItemMove}
            onItemResize={handleItemResize}
            onItemDrag={handleItemDrag}
            onTimeChange={handleTimeChange}
            onBoundsChange={handleBoundsChange}
            itemRenderer = {itemRenderer}
            groupRenderer = {groupRenderer}

            >
            <TimelineMarkers>
              {showTodayMarker && (
                <TodayMarker
                  interval={todayMarkerInterval}>
                    {({ styles, date }) =>
                      <div style={{ ...styles, ...todayMarkerStyle }} />
                    }
                </TodayMarker>
                )
              }
              {Array.isArray(customMarkers) &&
              customMarkers.map(marker => (
                <CustomMarker key={marker.date} date={marker.date}>
                  {({ styles, date }) => (
                    <div style={{ ...styles, ...marker.style }} />
                  )}
                </CustomMarker>
              ))}
              {showCursorMarker && (
                <CursorMarker>
                    {({ styles, date }) =>
                      <div style={{ ...styles, ...cursorMarkerStyle }} />
                    }
                </CursorMarker>
                )
              }
            </TimelineMarkers>
            <TimelineHeaders
              style={timelineHeaderStyle}>
            <SidebarHeader
              variant={sidebarHeaderVariant}>
              {({ getRootProps }) => {
                return <div {...getRootProps()}>{sidebarHeaderContent}</div>;
              }}
              
            </SidebarHeader>
            <DateHeader
              unit='primaryHeader'/>
            <DateHeader
             style={dateHeaderStyle} 
             unit={dateHeaderUnit}
             labelFormat={dateHeaderLabelFormat}
             height={dateHeaderHeight} />
           </TimelineHeaders>
            
          </Timeline>
          {draggedItem && dragInfoLabel && (
             <InfoLabel
               item={draggedItem.item}
               group={draggedItem.group}
               time={draggedItem.time}
             />
          )} 
      </div>
  );
}

DashCalendarTimeline.defaultProps = {
  groups: [{}],
  items: [{}],
  customGroupsContent: [],
  customItemsContent: [],
  customGroups: false,
  customItems: false,
  draggingItemColor: "red",
  selectedItemColor: "#1a6fb3",
  resizingItemBorder: "2px solid red",
  dragInfoLabel: false,
  showTodayMarker: false,
  todayMarkerInterval: 10000,
  showCursorMarker: false
};

DashCalendarTimeline.propTypes = {
    /**
     * The ID used to identify this component in Dash callbacks.
     */
    id: PropTypes.string,

    /**
     * The groups are used to determine the number of groups in a Timeline.
     */
    groups: PropTypes.array,

    /**
     * The items are used to determine the number of items within a single group.
     */
    items: PropTypes.array,

    /**
     * This sets the start time for the timeline.
     */
    defaultTimeStart: PropTypes.number,

    /**
     * This sets the end time for the timeline.
     */
    defaultTimeEnd: PropTypes.number,

    /**
     * The exact starting viewport of the calendar.
     */
    visibleTimeStart: PropTypes.number,

    /**
     * The exact ending viewport of the calendar.
     */
    visibleTimeEnd: PropTypes.number,

    /**
     * a number (default to 3) which represents the extra timeline rendered on right and lift of the visible area which the user will scroll through before the time rerenders. Note: setting buffer to 1 will disable the scrolling on the timeline.
     */
    buffer: PropTypes.number,
    
    /**
     * Width of the sidebar in pixels. If set to 0, the sidebar is not rendered. Defaults to 150.
     */
    sidebarWidth: PropTypes.number,

    /**
     * Width of the right sidebar in pixels. If set to 0, the right sidebar is not rendered. Defaults to 0.
     */
    rightSidebarWidth: PropTypes.number,

    /**
     * Snapping unit when dragging items. Defaults to 15 * 60 * 1000 or 15min. When so, the items will snap to 15min intervals when dragging.
     */
    dragSnap: PropTypes.number,

    /**
     * The minimum width, in pixels, of a timeline entry when it's possible to resize. If not reached, you must zoom in to resize more. Default to 20.
     */
    minResizeWidth: PropTypes.number,

    /**
     * Height of one line in the calendar in pixels. Default 30
     */
    lineHeight: PropTypes.number,

    /**
     * What percentage of the height of the line is taken by the item? Default 0.65
     */
    itemHeightRatio: PropTypes.number,

    /**
     * Smallest time the calendar can zoom to in milliseconds. Default 60 * 60 * 1000 (1 hour)
     */
    minZoom: PropTypes.number,

    /**
     * Largest time the calendar can zoom to in milliseconds. Default 5 * 365.24 * 86400 * 1000 (5 years)
     */
    maxZoom: PropTypes.number,

    /**
     * How many pixels we can drag the background for it to be counted as a click on the background. Default 3.
     */
    clickTolerance: PropTypes.number,

    /**
     * Can items be dragged around? Can be overridden in the items array. Defaults to true
     */
    canMove: PropTypes.bool,

    /**
     * Can items be moved between groups? Can be overridden in the items array. Defaults to true
     */
    canChangeGroup: PropTypes.bool,

    /**
     * Can items be resized? Can be overridden in the items array. Accepted values: false, "left", "right", "both". Defaults to "right". If you pass true, it will be treated as "right" to not break compatibility with versions 0.9 and below.
     */
    canResize: PropTypes.oneOfType([
      PropTypes.string,
      PropTypes.bool
    ]),

    /**
     * Append a special .rct-drag-right handle to the elements and only resize if dragged from there. Defaults to false.
     */
    useResizeHandle: PropTypes.bool,

    /**
     * Zoom in when scrolling the mouse up/down. Defaults to false.
     */
    traditionalZoom: PropTypes.bool,

    /**
     * Normally tapping (touching) an item selects it. If this is set to true, a tap will have the same effect, as selecting with the first click and then clicking again to open and send the onItemClick event. Defaults to false.
     */
    itemTouchSendsClick: PropTypes.bool,

    /**
     * With what step to display different units. E.g. 15 for minute means only minutes 0, 15, 30 and 45 will be shown.
     * Default:
       {
         second: 1,
         minute: 1,
         hour: 1,
         day: 1,
         month: 1,
         year: 1
       }
     */
    timeSteps: PropTypes.object,

    /**
     * This will determine whether you'd want to set up custom content for items or not. 
     */
    customItems: PropTypes.bool,

    /**
     * This will determine whether you'd want to set up custom content for groups or not. 
     */
    customGroups: PropTypes.bool,

    /**
     * This will be used to set up custom content of items in the main timeline. 
     */
    customItemsContent: PropTypes.node,

    /**
     * Item color when item is selected. 
     */
    selectedItemColor: PropTypes.string,

    /**
     * Item color while the item is being dragged around.
     */
    draggingItemColor: PropTypes.string,

    /**
     * Item border (CSS border e.g, 2px solid red) while the item is being resized.
     */
    resizingItemBorder: PropTypes.string,

    /**
     * This will be used to set up custom css styles for content of custom items in the main timeline. 
     */
    itemsStyle: PropTypes.object,

    /**
     * This will be used to set up custom css classes for content of custom items in the main timeline. 
     */
    itemsClass: PropTypes.string,

    /**
     * This will be used to set up custom content of groups in the sidebar. 
     */
    customGroupsContent: PropTypes.node,

    /**
     * This will be used to set up custom css style of content of groups in the sidebar. 
     */
    groupsStyle: PropTypes.object,

    /**
     * This will be used to set up custom css classes of content of groups in the sidebar. 
     */
    groupsClass: PropTypes.string,

    /**
     * This will render a info label over the timeline while the item is being dragged around.
     */
    dragInfoLabel: PropTypes.bool,

    /**
     * Style applied to the dragInfoLabel.
     */
    dragInfoLabelStyle: PropTypes.object,

    /**
     * Marker that is placed on the current date/time.
     */
    showTodayMarker: PropTypes.bool,

    /**
     * How often the TodayMarker refreshes. Value represents milliseconds. Default is 10000.
     */
    todayMarkerInterval: PropTypes.number,

    /**
     * Use this to render special styles for the todayMarker.
     */
    todayMarkerStyle: PropTypes.object,

    /**
     * Marker that is placed on the specified date/time. Example usage:
     * [
     *    {'date': 1750070400000, 'style':{'backgorund-color':'red'}},
     *    {'date': 1750675200000, 'style':{'backgorund-color':'green'}},
     *    {'date': 1751467500000, 'style':{'backgorund-color':'blue'}},
     * ]
     */
    customMarkers: PropTypes.array,

    /**
     * Marker that is displayed when hovering over the timeline and matches where your cursor is.
     */
    showCursorMarker: PropTypes.bool,

    /**
     * Use this to render special styles for the cursorMarker.
     */
    cursorMarkerStyle: PropTypes.object,

    /**
     * Determines whether the content goes above the left or right sidebar.
     */
    sidebarHeaderVariant: PropTypes.string,

    /**
     * Renders the Content above the sidebar.
     */
    sidebarHeaderContent: PropTypes.node,

    /**
     * Style applied to the root component of headers.
     */
    timelineHeaderStyle: PropTypes.object,

    /**
     * Style applied to the root of the header.
     */
    dateHeaderStyle: PropTypes.object,

    /**
     * Determines the intervals between columns. Values can be second, minute, hour, day, week, month, year or primaryHeader.
     */
    dateHeaderUnit: PropTypes.string,

    /**
     * Controls the how to format the interval label
     */
    dateHeaderLabelFormat: PropTypes.string,

    /**
     * Determines the height of the header in pixels. Default 30.
     */
    dateHeaderHeight: PropTypes.number,

    /**
     * Called when an item is clicked. Note: the item must be selected before it's clicked... except if it's a touch event and itemTouchSendsClick is enabled. time is the time that corresponds to where you click on the item in the timeline.
     */
    itemClickData: PropTypes.object,

    /**
     * Called when an item was double clicked. time is the time that corresponds to where you double click on the item in the timeline.
     */
    itemDoubleClickData: PropTypes.object,

    /**
     * Called when the item is clicked by the right button of the mouse. time is the time that corresponds to where you context click on the item in the timeline. Note: If this property is set the default context menu doesn't appear.
     */
    itemContextMenuData: PropTypes.object,

    /**
     * This is sent on the first click on an item. time is the time that corresponds to where you click/select on the item in the timeline.
     */
    itemSelectData: PropTypes.object,

    /**
     * Called when an empty spot on the canvas was clicked. Get the group ID and the time as arguments. For example open a "new item" window after this.
     */
    canvasClickData: PropTypes.object,

    /**
     * Called when an empty spot on the canvas was double clicked. Get the group ID and the time as arguments.
     */
    canvasDoubleClickData: PropTypes.object,

    /**
     * Called when the canvas is clicked by the right button of the mouse. Note: If this property is set the default context menu doesn't appear.
     */
    canvasContextMenuData:PropTypes.object,

    /**
     * Called when the timeline is zoomed, either via mouse/pinch zoom or clicking header to change timeline units.
     */
    zoomData: PropTypes.object,

    /**
     * Called when the bounds in the calendar's canvas change. Use it for example to load new data to display. (see "Behind the scenes" below). canvasTimeStart and canvasTimeEnd are unix timestamps in milliseconds.
     */
    boundsChangeData: PropTypes.object,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func
};