#!/usr/bin/env python3
"""Generate NER performance graph with correct scaling."""

# Data points (epoch 0-4)
data = {
    'Span Match': [0.6196, 0.7266, 0.7289, 0.7289, 0.7289],
    'Grouped Type': [0.6059, 0.6928, 0.6951, 0.6951, 0.6951],
    'Type Match': [0.5980, 0.6625, 0.6489, 0.6542, 0.6560],
    'Strict': [0.5882, 0.6340, 0.6187, 0.6222, 0.6258],
}

# Colors for each line
colors = {
    'Span Match': '#2E7D32',      # Green
    'Grouped Type': '#1976D2',     # Blue
    'Type Match': '#F57C00',       # Orange
    'Strict': '#C62828',           # Red
}

# Graph dimensions
width = 800
height = 480
padding_left = 80
padding_right = 50
padding_top = 60
padding_bottom = 80

plot_width = width - padding_left - padding_right
plot_height = height - padding_top - padding_bottom

# Y-axis range
y_min = 0.58
y_max = 0.74
y_range = y_max - y_min

# X-axis positions for epochs 0-4
epochs = [0, 1, 2, 3, 4]
x_positions = [padding_left + i * (plot_width / 4) for i in range(5)]

def y_to_pixel(value):
    """Convert F1 score to y pixel position."""
    normalized = (value - y_min) / y_range
    return padding_top + plot_height * (1 - normalized)

# Generate SVG
svg_lines = [
    '<?xml version="1.0" encoding="UTF-8"?>',
    f'<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">',
    '  <!-- Background -->',
    f'  <rect width="{width}" height="{height}" fill="#ffffff"/>',
    '',
    '  <!-- Title -->',
    '  <text x="400" y="25" font-family="Arial, sans-serif" font-size="16" font-weight="bold" text-anchor="middle" fill="#333">',
    '    NER Training Performance: F1 Score vs Epochs',
    '  </text>',
    '',
    '  <!-- Grid lines and axes -->',
    '  <g stroke="#e0e0e0" stroke-width="1">',
    f'    <line x1="{padding_left}" y1="{padding_top}" x2="{padding_left}" y2="{padding_top + plot_height}"/>',
    f'    <line x1="{padding_left}" y1="{padding_top + plot_height}" x2="{padding_left + plot_width}" y2="{padding_top + plot_height}"/>',
]

# Horizontal grid lines (every 0.02)
for i in range(9):
    y_val = y_min + i * 0.02
    if y_val <= y_max:
        y_px = y_to_pixel(y_val)
        svg_lines.append(f'    <line x1="{padding_left}" y1="{y_px}" x2="{padding_left + plot_width}" y2="{y_px}" stroke-dasharray="2,2"/>')

svg_lines.append('  </g>')
svg_lines.append('')

# Y-axis labels
svg_lines.append('  <!-- Y-axis labels -->')
svg_lines.append('  <g font-family="Arial, sans-serif" font-size="12" text-anchor="end" fill="#666">')
for i in range(9):
    y_val = y_min + i * 0.02
    if y_val <= y_max:
        y_px = y_to_pixel(y_val)
        svg_lines.append(f'    <text x="{padding_left - 10}" y="{y_px + 4}">{y_val:.2f}</text>')
svg_lines.append('  </g>')
svg_lines.append('')

# X-axis labels
svg_lines.append('  <!-- X-axis labels -->')
svg_lines.append('  <g font-family="Arial, sans-serif" font-size="12" text-anchor="middle" fill="#666">')
for i, epoch in enumerate(epochs):
    x_px = x_positions[i]
    svg_lines.append(f'    <text x="{x_px}" y="{padding_top + plot_height + 20}">{epoch}</text>')
svg_lines.append(f'    <text x="{width/2}" y="{padding_top + plot_height + 45}" font-weight="bold">Training Epochs</text>')
svg_lines.append('  </g>')
svg_lines.append('')

# Y-axis label
svg_lines.append('  <!-- Y-axis label -->')
y_label_x = 20
y_label_y = height / 2
svg_lines.append(f'  <text x="{y_label_x}" y="{y_label_y}" font-family="Arial, sans-serif" font-size="12" font-weight="bold" text-anchor="middle" transform="rotate(-90 {y_label_x} {y_label_y})" fill="#666">')
svg_lines.append('    F1 Score')
svg_lines.append('  </text>')
svg_lines.append('')

# Plot lines
svg_lines.append('  <!-- Data lines -->')
for name, values in data.items():
    points = ' '.join([f'{x_positions[i]},{y_to_pixel(v):.2f}' for i, v in enumerate(values)])
    color = colors[name]
    stroke_width = 3 if name in ['Span Match', 'Grouped Type'] else 2.5
    dash = ' stroke-dasharray="5,3"' if name == 'Strict' else ''
    svg_lines.append(f'  <polyline points="{points}" fill="none" stroke="{color}" stroke-width="{stroke_width}"{dash}/>')
svg_lines.append('')

# Plot markers
svg_lines.append('  <!-- Data point markers -->')
svg_lines.append('  <g fill="#fff" stroke-width="2">')
for name, values in data.items():
    color = colors[name]
    for i, v in enumerate(values):
        x_px = x_positions[i]
        y_px = y_to_pixel(v)
        svg_lines.append(f'    <circle cx="{x_px}" cy="{y_px:.2f}" r="4" stroke="{color}"/>')
svg_lines.append('  </g>')
svg_lines.append('')

# Legend - vertical stack to prevent overlap
svg_lines.append('  <!-- Legend -->')
svg_lines.append('  <g font-family="Arial, sans-serif" font-size="11">')

legend_items = [
    ('Span Match', 'Span Match (0.7289)'),
    ('Grouped Type', 'Grouped Type (0.6951) ⭐ Most Clinically Relevant'),
    ('Type Match', 'Type Match (0.6560)'),
    ('Strict', 'Strict (0.6340, overfitting pattern)'),
]

legend_x = 90
legend_y_start = 405

for i, (key, label) in enumerate(legend_items):
    legend_y_pos = legend_y_start + (i * 18)

    color = colors[key]
    stroke_width = 3 if key in ['Span Match', 'Grouped Type'] else 2.5
    dash = ' stroke-dasharray="5,3"' if key == 'Strict' else ''

    svg_lines.append(f'  <line x1="{legend_x}" y1="{legend_y_pos}" x2="{legend_x + 35}" y2="{legend_y_pos}" stroke="{color}" stroke-width="{stroke_width}"{dash}/>')

    font_weight = ' font-weight="bold"' if key == 'Grouped Type' else ''
    svg_lines.append(f'  <text x="{legend_x + 40}" y="{legend_y_pos + 4}" fill="#333"{font_weight}>{label}</text>')

svg_lines.append('  </g>')
svg_lines.append('</svg>')

# Write to file
import os
script_dir = os.path.dirname(os.path.abspath(__file__))
svg_path = os.path.join(script_dir, 'ner_performance.svg')
pdf_path = os.path.join(script_dir, 'ner_performance.pdf')

with open(svg_path, 'w') as f:
    f.write('\n'.join(svg_lines))

print(f"✓ Generated {svg_path}")

# Convert to PDF using inkscape
import subprocess
try:
    subprocess.run(['inkscape', svg_path, '--export-filename=' + pdf_path],
                   check=True, capture_output=True)
    print(f"✓ Generated {pdf_path}")
    print(f"  Data ranges: F1 {y_min:.2f} - {y_max:.2f}")
    print(f"  Plot area: {plot_width}x{plot_height} pixels")
except subprocess.CalledProcessError as e:
    print(f"⚠ Failed to convert to PDF: {e}")
    print(f"  You can manually convert: inkscape {svg_path} --export-filename={pdf_path}")
