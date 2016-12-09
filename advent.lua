conky.config = {

  background = true,
  update_interval = 20,

  cpu_avg_samples = 2,
  net_avg_samples = 2,
  if_up_strictness = 'address',

  double_buffer = true,
  no_buffers = true,
  text_buffer_size = 2048,

  own_window = true,
  own_window_class = 'Conky',
  --own_window_type = 'override',
  --own_window_type = 'desktop',
  own_window_type = 'dock',
  own_window_hints = 'undecorated,sticky,skip_taskbar,skip_pager,below',

  own_window_colour = '#000000',
  own_window_transparent = false,
  own_window_argb_visual = true,
  own_window_argb_value = 192,

  draw_shades = false,
  draw_outline = false,
  draw_borders = false,
  draw_graph_borders = false,

  alignment = 'bottom_right',
  gap_x = 60,
  gap_y = 60,
  minimum_width = 340, minimum_height = 300,
  maximum_width = 360,
  border_inner_margin = 0,
  border_outer_margin = 20,
  xinerama_head = 0,

  override_utf8_locale = true,
  use_xft = true,
  font = 'Ubuntu:size=11',
  xftalpha = 0.8,
  uppercase = false,

  -- Defining colors
  default_color = '#FFFFFF',
  -- Shades of Gray
  color1 = '#DDDDDD',
};

conky.text = [[
${font Monospace:size=10:style=normal}${color2}${exec ~/.conky/conky_advent/advent.py}
]]
