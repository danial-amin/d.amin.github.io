import plotly.graph_objects as go
import plotly.express as px
from textwrap import fill

# Investment Distribution Pie Chart
fig1 = go.Figure(data=[go.Pie(
    labels=['North America', 'Europe', 'East Asia', 'Rest of Asia', 'Africa', 'Latin America'],
    values=[45, 25, 20, 7, 2, 1],
    hole=.3
)])
fig1.update_traces(textposition='inside', textinfo='percent+label')
fig1.update_layout(title_text="Global AI Investment Distribution")
fig1.write_html('assets/plotly/ai-investment-distribution.html')

# Value Distribution Bar Chart
import pandas as pd
df = pd.DataFrame({
    'Model': ['Current', 'Current', 'Current', 'Proposed', 'Proposed', 'Proposed'],
    'Region': ['Silicon Valley', 'Global South', 'Europe', 'Silicon Valley', 'Global South', 'Europe'],
    'Value': [70, 10, 20, 40, 35, 25]
})
fig2 = px.bar(df, x='Model', y='Value', color='Region', 
              title='Current vs. Proposed AI Value Distribution',
              labels={'Value': 'Percentage of Value (%)'})
fig2.write_html('assets/plotly/ai-value-distribution.html')

def wrap_text(text, width=12):
    """Wrap text to fit within specified width"""
    lines = text.split('\n')
    wrapped_lines = []
    for line in lines:
        if len(line) > width:
            wrapped_lines.extend(fill(line, width=width).split('\n'))
        else:
            wrapped_lines.append(line)
    return '<br>'.join(wrapped_lines)

# Create the AI Workforce Flow Diagram
fig = go.Figure()

# Define positions for nodes with increased vertical spacing between layers
nodes = {
    'Data Annotation Workers (Kenya, Philippines)': (1, 5),
    'Content Moderators (Global South)': (3, 5),
    'ML Engineers (Pakistan, India)': (5, 5),
    'AI Training Pipeline': (3, 2.8),
    'AI Products': (3, 0.5),
    'Profits Flow to Silicon Valley': (3, -2)
}

# Enhanced color palette with gradients
colors = {
    'Data Annotation Workers (Kenya, Philippines)': '#FFD700',  # Gold
    'Content Moderators (Global South)': '#FF6B35',            # Orange-red
    'ML Engineers (Pakistan, India)': '#4ECDC4',               # Teal
    'AI Training Pipeline': '#45B7D1',                         # Sky blue
    'AI Products': '#9B59B6',                                  # Purple
    'Profits Flow to Silicon Valley': '#E74C3C'                # Red
}

# Enhanced styling for different node types
node_styles = {
    'Data Annotation Workers (Kenya, Philippines)': {'size': 120, 'symbol': 'circle'},
    'Content Moderators (Global South)': {'size': 120, 'symbol': 'circle'},
    'ML Engineers (Pakistan, India)': {'size': 120, 'symbol': 'circle'},
    'AI Training Pipeline': {'size': 140, 'symbol': 'diamond'},
    'AI Products': {'size': 130, 'symbol': 'square'},
    'Profits Flow to Silicon Valley': {'size': 110, 'symbol': 'triangle-up'}
}

# Add nodes with enhanced styling
for node, (x, y) in nodes.items():
    wrapped_text = wrap_text(node, width=14)
    style = node_styles[node]
    
    fig.add_trace(go.Scatter(
        x=[x], y=[y],
        mode='markers+text',
        marker=dict(
            size=style['size'], 
            color=colors[node],
            symbol=style['symbol'],
            line=dict(width=3, color='white'),
            opacity=0.9
        ),
        text=wrapped_text,
        textposition='middle center',
        textfont=dict(
            size=11, 
            color='white' if node == 'Profits Flow to Silicon Valley' else 'black',
            family='Arial Black'
        ),
        showlegend=False,
        hoverinfo='text',
        hovertext=f"<b>{node}</b><br>Click for details",
        name=node
    ))

# Add connecting arrows with enhanced styling
arrows = [
    ('Data Annotation Workers (Kenya, Philippines)', 'AI Training Pipeline'),
    ('Content Moderators (Global South)', 'AI Training Pipeline'),
    ('ML Engineers (Pakistan, India)', 'AI Training Pipeline'),
    ('AI Training Pipeline', 'AI Products'),
    ('AI Products', 'Profits Flow to Silicon Valley')
]

for start, end in arrows:
    x0, y0 = nodes[start]
    x1, y1 = nodes[end]
    
    # Calculate offset to avoid overlapping with node borders
    dx = x1 - x0
    dy = y1 - y0
    length = (dx**2 + dy**2)**0.5
    
    # Offset arrows to start/end at node edges
    offset = 0.15
    x0_offset = x0 + (dx / length) * offset
    y0_offset = y0 + (dy / length) * offset
    x1_offset = x1 - (dx / length) * offset
    y1_offset = y1 - (dy / length) * offset
    
    # Add enhanced arrow
    fig.add_annotation(
        x=x1_offset, y=y1_offset,
        ax=x0_offset, ay=y0_offset,
        xref='x', yref='y',
        axref='x', ayref='y',
        arrowhead=3,
        arrowsize=2,
        arrowwidth=3,
        arrowcolor='#2C3E50',
        opacity=0.8
    )

# Add background shapes for visual enhancement with increased padding
fig.add_shape(
    type="rect",
    x0=0.2, y0=4.2, x1=5.8, y1=5.8,
    fillcolor="rgba(52, 152, 219, 0.1)",
    line=dict(color="rgba(52, 152, 219, 0.3)", width=2, dash="dot")
)

fig.add_annotation(
    x=3, y=6.1,
    text="<b>Global Workforce Layer</b>",
    showarrow=False,
    font=dict(size=14, color="#2C3E50"),
    bgcolor="rgba(255, 255, 255, 0.8)",
    bordercolor="#2C3E50",
    borderwidth=1
)

# Add value flow indicator
fig.add_shape(
    type="rect",
    x0=2.5, y0=-0.8, x1=3.5, y1=1.3,
    fillcolor="rgba(231, 76, 60, 0.1)",
    line=dict(color="rgba(231, 76, 60, 0.3)", width=2, dash="dot")
)

fig.add_annotation(
    x=4, y=0.5,
    text="<b>Value<br>Extraction</b>",
    showarrow=True,
    arrowhead=2,
    arrowsize=1,
    arrowcolor="#E74C3C",
    font=dict(size=12, color="#E74C3C"),
    ax=3.5, ay=0.2
)

# Enhanced layout with professional styling
fig.update_layout(
    title=dict(
        text='<b>Global AI Workforce and Value Flow</b><br><sub>The Hidden Infrastructure of AI Development</sub>',
        x=0.5,
        font=dict(size=20, color='#2C3E50', family='Arial')
    ),
    showlegend=False,
    xaxis=dict(
        showgrid=False, 
        showticklabels=False, 
        zeroline=False,
        range=[-0.5, 6.5]
    ),
    yaxis=dict(
        showgrid=False, 
        showticklabels=False, 
        zeroline=False,
        range=[-1.5, 5.5]
    ),
    plot_bgcolor='#F8F9FA',
    paper_bgcolor='white',
    width=900,
    height=600,
    margin=dict(l=60, r=60, t=120, b=60),
    font=dict(family='Arial', size=12, color='#2C3E50')
)

# Add subtle grid pattern
fig.add_shape(
    type="rect",
    x0=-0.5, y0=-1.5, x1=6.5, y1=5.5,
    fillcolor="rgba(0, 0, 0, 0)",
    line=dict(color="rgba(0, 0, 0, 0.05)", width=1)
)

# Save the enhanced figure
fig.write_html('assets/plotly/ai-workforce-flow-enhanced.html', config={
    'displayModeBar': True,
    'displaylogo': False,
    'modeBarButtonsToRemove': ['pan2d', 'lasso2d']
})

# 1. Generalist vs Specialist Performance
fig1 = go.Figure()
domains = ['Legal', 'Medical', 'Finance', 'Engineering', 'Marketing']
generalist = [60, 55, 65, 58, 70]
specialist = [90, 92, 88, 95, 85]

fig1.add_trace(go.Bar(name='Generalist AI', x=domains, y=generalist))
fig1.add_trace(go.Bar(name='Specialist AI Persona', x=domains, y=specialist))
fig1.update_layout(title='Performance Comparison: Generalist vs Specialist AI')
fig1.write_html('assets/plotly/generalist-vs-specialist.html')

# 2. Implementation Phases Timeline
fig3 = go.Figure()
phases = ['Domain Analysis', 'Persona Development', 'Orchestration Layer', 'UI Design', 'Deployment']
timeline = [30, 60, 90, 120, 150]
fig3.add_trace(go.Scatter(x=timeline, y=phases, mode='markers+lines', 
                         marker=dict(size=12), line=dict(width=3)))
fig3.update_layout(title='Implementation Roadmap Timeline (Days)', 
                   xaxis_title='Days', yaxis_title='Phase')
fig3.write_html('assets/plotly/implementation-phases.html')

# Create the Persona Architecture Model
fig = go.Figure()

# Define positions for different components
user_layer = {'y': 5, 'color': '#e3f2fd'}
orchestration_layer = {'y': 4, 'color': '#bbdefb'}
persona_layer = {'y': 2.5, 'color': '#90caf9'}
foundation_layer = {'y': 1, 'color': '#64b5f6'}

# Define components with positions
components = {
    # User Layer
    'User Interface': (2, user_layer['y'], user_layer['color']),
    
    # Orchestration Layer
    'Query Router': (1, orchestration_layer['y'], orchestration_layer['color']),
    'Context Manager': (2, orchestration_layer['y'], orchestration_layer['color']),
    'Response Aggregator': (3, orchestration_layer['y'], orchestration_layer['color']),
    
    # Persona Layer
    'Legal AI\nPersona': (0.5, persona_layer['y'], persona_layer['color']),
    'Medical AI\nPersona': (1.5, persona_layer['y'], persona_layer['color']),
    'Financial AI\nPersona': (2.5, persona_layer['y'], persona_layer['color']),
    'Technical AI\nPersona': (3.5, persona_layer['y'], persona_layer['color']),
    
    # Foundation Layer
    'Foundation Models': (1, foundation_layer['y'], foundation_layer['color']),
    'Knowledge Bases': (2, foundation_layer['y'], foundation_layer['color']),
    'Tool APIs': (3, foundation_layer['y'], foundation_layer['color'])
}

# Add layer backgrounds
for layer_name, layer_info in [
    ('User Interface Layer', user_layer),
    ('Orchestration Layer', orchestration_layer), 
    ('Specialized Persona Layer', persona_layer),
    ('Foundation Layer', foundation_layer)
]:
    fig.add_shape(
        type="rect",
        x0=-0.2, y0=layer_info['y']-0.3,
        x1=4.2, y1=layer_info['y']+0.3,
        fillcolor=layer_info['color'],
        opacity=0.3,
        line=dict(width=0)
    )

# Add components
for component, (x, y, color) in components.items():
    fig.add_trace(go.Scatter(
        x=[x], y=[y],
        mode='markers+text',
        marker=dict(
            size=60 if 'Persona' in component else 50,
            color=color,
            line=dict(width=2, color='darkblue'),
            symbol='square' if 'Persona' in component else 'circle'
        ),
        text=component,
        textposition='middle center',
        textfont=dict(size=9, color='black', family='Arial'),
        showlegend=False,
        hoverinfo='text',
        hovertext=component
    ))

# Add connections/arrows
connections = [
    # User to Orchestration
    ('User Interface', 'Query Router'),
    ('User Interface', 'Context Manager'),
    ('User Interface', 'Response Aggregator'),
    
    # Orchestration to Personas
    ('Query Router', 'Legal AI\nPersona'),
    ('Query Router', 'Medical AI\nPersona'),
    ('Query Router', 'Financial AI\nPersona'),
    ('Query Router', 'Technical AI\nPersona'),
    
    # Personas to Foundation
    ('Legal AI\nPersona', 'Foundation Models'),
    ('Medical AI\nPersona', 'Foundation Models'),
    ('Financial AI\nPersona', 'Knowledge Bases'),
    ('Technical AI\nPersona', 'Tool APIs'),
]

for start, end in connections:
    x0, y0, _ = components[start]
    x1, y1, _ = components[end]
    
    # Add arrow
    fig.add_annotation(
        x=x1, y=y1,
        ax=x0, ay=y0,
        xref='x', yref='y',
        axref='x', ayref='y',
        arrowhead=2,
        arrowsize=1,
        arrowwidth=1.5,
        arrowcolor='#1976d2',
        opacity=0.7
    )

# Add layer labels
layer_labels = [
    ('User Interface Layer', 4.5, user_layer['y']),
    ('Orchestration Layer', 4.5, orchestration_layer['y']),
    ('Specialized Persona Layer', 4.5, persona_layer['y']),
    ('Foundation Layer', 4.5, foundation_layer['y'])
]

for label, x, y in layer_labels:
    fig.add_annotation(
        x=x, y=y,
        text=label,
        showarrow=False,
        font=dict(size=12, color='#1976d2', family='Arial Black'),
        textangle=-90
    )

# Update layout
fig.update_layout(
    title={
        'text': 'Persona-Driven AI Architecture Model',
        'x': 0.5,
        'font': {'size': 16, 'family': 'Arial Black'}
    },
    showlegend=False,
    xaxis=dict(
        showgrid=False, 
        showticklabels=False, 
        zeroline=False,
        range=[-0.5, 5]
    ),
    yaxis=dict(
        showgrid=False, 
        showticklabels=False, 
        zeroline=False,
        range=[0.5, 5.5]
    ),
    plot_bgcolor='white',
    paper_bgcolor='white',
    width=800,
    height=600,
    margin=dict(l=50, r=100, t=80, b=50)
)

# Add description boxes
descriptions = [
    "Users interact through a unified interface",
    "Smart routing and context management",
    "Domain-specific AI experts",
    "Shared computational resources"
]

for i, desc in enumerate(descriptions):
    fig.add_annotation(
        x=-0.3, y=5-i*1.25,
        text=desc,
        showarrow=False,
        font=dict(size=10, color='#424242'),
        align='left',
        bgcolor='rgba(255,255,255,0.8)',
        bordercolor='#bdbdbd',
        borderwidth=1
    )

# Save the figure
fig.write_html('assets/plotly/persona-architecture.html')
