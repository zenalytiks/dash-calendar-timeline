import React, {useState} from 'react';
import PropTypes from 'prop-types';
import Timeline, { TimelineHeaders, SidebarHeader, DateHeader } from 'react-calendar-timeline';
import 'react-calendar-timeline/lib/Timeline.css';
import moment from "moment";

/**
 * DashTimeline renders React's Calendar Timeline inside the Dash App.
 */
export default function DashTimeline(props) {
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
    lineHeight,
    itemHeightRatio,
    minZoom,
    maxZoom,
    canMove,
    canChangeGroup,
    canResize,
    useResizeHandle,
    traditionalZoom,
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
    // eslint-disable-next-line no-unused-vars
    clickData
  } = props;

  const [draggedItem, setDraggedItem] = useState(undefined);
  

  const handleItemClick = (itemId, e, time) => {
    const updatedClickData = {
      itemId,
      time
    };

    setProps({
      clickData: updatedClickData
    });
  };

  const itemRenderer = ({ item, itemContext, getItemProps, getResizeProps }) => {
    const { left: leftResizeProps, right: rightResizeProps } = getResizeProps();
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
    return (
      <div {...modifiedItemProps}>
        {itemContext.useResizeHandle ? <div {...leftResizeProps} /> : ''}
        <div style={itemsStyle} className={itemsClass}>
          {customItems
            ? customItemsContent.find(
                (content) => content.props._dashprivate_layout.props.id === item.id.toString()
              )
            : itemContext.title}
        </div>
        {itemContext.useResizeHandle ? <div {...rightResizeProps} /> : ''}
      </div>

    );
    
    
  };

  const groupRenderer = ({ group }) => {
    return (
      <div style={groupsStyle} className={groupsClass}>
        {customGroups
          ? customGroupsContent.find(
              (content) => content.props._dashprivate_layout.props.id === group.id.toString()
            )
          : group.title}
      </div>
    )
  };

  const handleItemMove = (itemId, dragTime, newGroupOrder) => {
    const updatedItems = items.map((item) =>
      item.id === itemId
        ? {
            ...item,
            start_time: dragTime,
            end_time: dragTime + (item.end_time - item.start_time),
            group: groups[newGroupOrder].id,
          }
        : item
    );

    setProps({items: updatedItems});
    setDraggedItem(undefined);

    console.log('Moved', itemId, dragTime, newGroupOrder);
  };

  const handleItemResize = (itemId, time, edge) => {
    const updatedItems = items.map((item) =>
      item.id === itemId
        ? {
            ...item,
            start_time: edge === 'left' ? time : item.start_time,
            end_time: edge === 'left' ? item.end_time : time,
          }
        : item
    );

    setProps({items: updatedItems});
    setDraggedItem(undefined);

    console.log('Resized', itemId, time, edge);
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
      item = items.find(i => i.id === itemId);
    }
    setDraggedItem({ item, group: groups[newGroupOrder], time });
  };

  return (
      <div id={id}>
          <Timeline
            groups={groups}
            items={items}
            defaultTimeStart={defaultTimeStart}
            defaultTimeEnd={defaultTimeEnd}
            visibleTimeStart={visibleTimeStart}
            visibleTimeEnd={visibleTimeEnd}
            buffer={buffer}
            sidebarWidth={sidebarWidth}
            rightSidebarWidth={rightSidebarWidth}
            minResizeWidth={minResizeWidth}
            lineHeight={lineHeight}
            itemHeightRatio={itemHeightRatio}
            minZoom={minZoom}
            maxZoom={maxZoom}
            canMove={canMove}
            canChangeGroup={canChangeGroup}
            canResize={canResize}
            useResizeHandle={useResizeHandle}
            traditionalZoom={traditionalZoom}
            timeSteps={timeSteps}
            onItemClick={handleItemClick}
            // onItemSelect={handleItemClick}
            onItemMove={handleItemMove}
            onItemResize={handleItemResize}
            onItemDrag={handleItemDrag}
            itemRenderer = {itemRenderer}
            groupRenderer = {groupRenderer}

            >
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

DashTimeline.defaultProps = {
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
  clickData: {},
};

DashTimeline.propTypes = {
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
     * Returns the Item ID and time for the item clicked.
     */
    clickData: PropTypes.object,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func
};
