import drawsvg as draw

def generate_custom_scoreboard(team1_name, team1_logo_url, team1_text_color, team2_name, team2_logo_url, team2_text_color,
                              venue, score_line, 
                              team1_name_bg_color, team1_logo_bg_color,
                              team2_name_bg_color, team2_logo_bg_color,
                              venue_bg_color, venue_text_color, score_bg_color, score_text_color):
    
    width = 400
    height = 60
    
    d = draw.Drawing(width, height)
    
    # Team 1 name background
    d.append(draw.Rectangle(0, 0, 200, 30, fill=team1_name_bg_color))
    
    # Team 2 name background (extended to cover VS text)
    d.append(draw.Rectangle(200, 0, 200, 30, fill=team2_name_bg_color))
    
    # Venue background section  
    d.append(draw.Rectangle(0, 30, width, 15, fill=venue_bg_color))
    
    # Score background section
    d.append(draw.Rectangle(0, 45, width, 15, fill=score_bg_color))
    
    # Team 1 logo background
    d.append(draw.Rectangle(0, 0, 40, 60, fill=team1_logo_bg_color))
    
    # Team 1 logo image
    if team1_logo_url:
        team1_logo = draw.Image(0, 0, 40, 60, path=team1_logo_url)
        d.append(team1_logo)
    
    # Team 2 logo background
    d.append(draw.Rectangle(360, 0, 40, 60, fill=team2_logo_bg_color))
    
    # Team 2 logo image
    if team2_logo_url:
        team2_logo = draw.Image(360, 0, 40, 60, path=team2_logo_url)
        d.append(team2_logo)
    
    # Team 1 name
    d.append(draw.Text(team1_name, 12, 50, 20, 
                      font_family='Arial', 
                      fill=team1_text_color))
    
    # Team 2 name with VS prefix
    team2_text = f"VS {team2_name}"
    d.append(draw.Text(team2_text, 12, 220, 20, 
                      font_family='Arial', 
                      fill=team2_text_color))
    
    # Venue information (center aligned)
    d.append(draw.Text(venue, 9, 200, 40, text_anchor='middle',
                      font_family='Arial', 
                      fill=venue_text_color))
    
    # Score/betting line (center aligned)
    d.append(draw.Text(score_line, 9, 200, 53, text_anchor='middle',
                      font_family='Arial', 
                      fill=score_text_color))
    
    return d

# Example usage
# if __name__ == "__main__":
#     print("Generating custom scoreboard...")
    
#     try:
#         # Generate custom scoreboard with separate background colors
#         custom_drawing = generate_custom_scoreboard(
#             team1_name="LAKERS",
#             team1_logo_url="https://a.espncdn.com/i/teamlogos/ncaa/500/2006.png",
#             team2_name="WARRIORS",
#             team2_logo_url="https://a.espncdn.com/i/teamlogos/ncaa/500/2598.png",
#             venue="AT CRYPTO.COM ARENA",
#             score_line="LAL -3.5 O/U 215",
#             team1_name_bg_color="#552583",
#             team1_text_color= "#000",
#             team1_logo_bg_color="#FFD700",
#             team2_name_bg_color="#006BB6",
#             team2_text_color= "#000", 
#             team2_logo_bg_color="#FFC72C",
#             venue_bg_color="#4B0000",
#             venue_text_color= "#000",
#             score_bg_color="#2B0000",
#             score_text_color="#000"
#         )
        
#         custom_drawing.save_svg("custom_scoreboard.svg")
#         print("Custom scoreboard saved to custom_scoreboard.svg")
        
#     except ImportError:
#         print("drawsvg not available. Install with: pip install drawsvg")