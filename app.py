import gradio as gr
import pandas as pd
import joblib

# Load data
try:
    df = pd.read_csv('labeled_nutrition_data.csv')
    # Use the high-accuracy supervised category
    if 'supervised_category' in df.columns:
        df['category'] = df['supervised_category']
except FileNotFoundError:
    # Fallback/Init if file not found (though it should exist now)
    df = pd.DataFrame(columns=['name', 'calories', 'proteins', 'fat', 'carbohydrate', 'category'])

def calculate_daily_calories(weight, goal):
    base = weight * 25
    multipliers = {
        'Diet': 0.8,
        'Maintain': 1.0,
        'Bulking': 1.2,
        'Muscle Gain': 1.15
    }
    return base * multipliers.get(goal, 1.0)

def recommend_foods(weight, goal, n_recommendations):
    weight = float(weight)
    n = int(n_recommendations)
    daily_cal = calculate_daily_calories(weight, goal)
    
    # Filter logic based on the new columns: calories, proteins, carbohydrate
    if goal == 'Diet':
        # Low calorie, decent protein
        filtered = df[(df['calories'] <= 200) & (df['proteins'] >= 3)]
        filtered = filtered.sort_values('calories', ascending=True)
    elif goal == 'Bulking':
        # High calorie, high protein
        filtered = df[(df['calories'] >= 150) & (df['proteins'] >= 5)]
        filtered = filtered.sort_values('proteins', ascending=False)
    elif goal == 'Muscle Gain':
        # Focused on protein
        filtered = df[df['proteins'] >= 10]
        filtered = filtered.sort_values('proteins', ascending=False)
    else:  # Maintain
        # Moderate calories
        filtered = df[(df['calories'] >= 50) & (df['calories'] <= 400)]
        filtered = filtered.sort_values('proteins', ascending=False) # Sort by something reasonable
    
    # Select columns to display
    # Check if 'image' column exists to potentially use it, but for now just text
    display_cols = ['name', 'calories', 'proteins', 'fat', 'carbohydrate', 'category']
    
    # Handle case where filter returns empty
    if filtered.empty:
        # Fallback to just category based filtering if strict rules fail
        if goal == 'Diet':
            filtered = df[df['category'] == 'Low Calorie']
        elif goal in ['Bulking', 'Muscle Gain']:
            filtered = df[df['category'] == 'High Protein']
        else:
            filtered = df[df['category'] == 'Balanced']
            
    result = filtered.head(n)[display_cols]
    
    # Rename columns for friendly display
    result.columns = ['Makanan', 'Kalori', 'Protein (g)', 'Lemak (g)', 'Karbo (g)', 'Kategori']
    
    summary = f"""
    Berat Badan: {weight} kg
    Tujuan: {goal}
    Target Kalori Harian: {daily_cal:.0f} kcal
    Kalori per Makan (est. 3x makan): {daily_cal/3:.0f} kcal
    """
    
    return summary, result

# Create Gradio interface
with gr.Blocks(title="Food Recommendation System", theme=gr.themes.Soft()) as demo:
    gr.Markdown("# Sistem Rekomendasi Makanan")
    gr.Markdown("Dapatkan rekomendasi makanan berdasarkan berat badan dan tujuan Anda")
    
    with gr.Row():
        weight_input = gr.Number(label="Berat Badan (kg)", value=65, minimum=30, maximum=200)
        goal_input = gr.Dropdown(
            label="Tujuan",
            choices=["Diet", "Maintain", "Bulking", "Muscle Gain"],
            value="Maintain"
        )
        n_input = gr.Slider(label="Jumlah Rekomendasi", minimum=5, maximum=20, value=10, step=1)
    
    submit_btn = gr.Button("Dapatkan Rekomendasi", variant="primary")
    
    summary_output = gr.Textbox(label="Ringkasan Kebutuhan")
    table_output = gr.Dataframe(label="Rekomendasi Makanan", wrap=True)
    
    submit_btn.click(
        fn=recommend_foods,
        inputs=[weight_input, goal_input, n_input],
        outputs=[summary_output, table_output]
    )

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)
