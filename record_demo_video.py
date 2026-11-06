"""
record_demo_video.py
--------------------
Automated High-Definition Demo Video Generator for CoffeeYield AI.
Records an end-to-end interactive demonstration walkthrough of the
Streamlit dashboard and compiles it into a smooth 1080p Full HD MP4 video.
"""

import os
import time
import io
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def create_title_card(title, subtitle, tag="", width=1920, height=1080):
    img = Image.new('RGB', (width, height), color='#0A101D')
    draw = ImageDraw.Draw(img)
    
    # Gradient accent borders
    draw.rectangle([0, 0, width, 14], fill='#10B981')
    draw.rectangle([0, height-14, width, height], fill='#3B82F6')
    
    # Glass container box
    draw.rounded_rectangle([180, 200, width-180, height-200], radius=30, fill='#111C2E', outline='#1E293B', width=3)
    
    # Tag badge
    draw.rounded_rectangle([width//2 - 240, 260, width//2 + 240, 310], radius=15, fill='#064E3B', outline='#059669', width=2)
    draw.text((width//2, 285), "🌿 EXPLAINABLE AI • MAJOR PROJECT DEMONSTRATION", fill='#34D399', anchor='mm')
    
    # Title
    draw.text((width//2, 385), title, fill='#FFFFFF', anchor='mm')
    
    # Subtitle
    draw.text((width//2, 455), subtitle, fill='#E2E8F0', anchor='mm')
    
    # Metrics line
    draw.text((width//2, 540), "Gradient Boosting R² = 0.9530  •  TreeSHAP Local Attribution  •  Liebig Bio-Stress Engine", fill='#60A5FA', anchor='mm')
    
    # Authorship & GitHub link
    draw.text((width//2, 650), "Developed by: Prajwal (prajwalhg-design)", fill='#94A3B8', anchor='mm')
    draw.text((width//2, 700), "Repository: github.com/prajwalhg-design/coffee-yield-prediction", fill='#38BDF8', anchor='mm')
    draw.text((width//2, 750), "Includes 8-Page IEEE Research Paper & Streamlit Web Intelligence App", fill='#64748B', anchor='mm')
    
    return cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)

def create_outro_card(width=1920, height=1080):
    img = Image.new('RGB', (width, height), color='#0A101D')
    draw = ImageDraw.Draw(img)
    
    # Borders
    draw.rectangle([0, 0, width, 14], fill='#10B981')
    draw.rectangle([0, height-14, width, height], fill='#3B82F6')
    
    draw.rounded_rectangle([180, 160, width-180, height-160], radius=30, fill='#111C2E', outline='#1E293B', width=3)
    
    draw.text((width//2, 240), "☕ CoffeeYield AI • Project Resources", fill='#FFFFFF', anchor='mm')
    draw.text((width//2, 290), "Scan the QR code below or visit GitHub to inspect source code and research paper", fill='#94A3B8', anchor='mm')
    
    # Try embedding the generated QR code
    qr_path = r'C:\Users\prajw\.gemini\antigravity\scratch\coffee_yield_project\qr_code.png'
    if os.path.exists(qr_path):
        qr_img = Image.open(qr_path).convert('RGB')
        qr_img = qr_img.resize((320, 320), Image.Resampling.LANCZOS)
        img.paste(qr_img, ((width - 320)//2, 340))
        
    draw.text((width//2, 720), "https://github.com/prajwalhg-design/coffee-yield-prediction", fill='#34D399', anchor='mm')
    draw.text((width//2, 770), "Author: Prajwal | Open Source & IEEE Publication Ready", fill='#64748B', anchor='mm')
    
    return cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)

def main():
    print("Initializing high-definition browser recorder...")
    options = Options()
    options.add_argument('--headless=new')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    options.add_argument('--window-size=1920,1080')
    
    driver = webdriver.Chrome(options=options)
    driver.get('http://localhost:8501')
    print("Waiting for Streamlit web app to initialize...")
    time.sleep(7)
    
    width, height = 1920, 1080
    fps = 20
    output_path = r'C:\Users\prajw\.gemini\antigravity\scratch\coffee_yield_project\demo_video.mp4'
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))
    
    def capture_frame():
        png_bytes = driver.get_screenshot_as_png()
        pil_img = Image.open(io.BytesIO(png_bytes)).convert('RGB')
        if pil_img.size != (width, height):
            pil_img = pil_img.resize((width, height), Image.Resampling.LANCZOS)
        return cv2.cvtColor(np.array(pil_img), cv2.COLOR_RGB2BGR)
        
    def hold_view(duration_sec):
        num_frames = int(duration_sec * fps)
        frame = capture_frame()
        for _ in range(num_frames):
            out.write(frame)
            
    def smooth_scroll(start_y, end_y, steps=20, step_pause=0.03):
        for y in np.linspace(start_y, end_y, steps):
            driver.execute_script(f"window.scrollTo({{top: {int(y)}, behavior: 'instant'}});")
            time.sleep(step_pause)
            out.write(capture_frame())

    # 1. INTRO TITLE CARD (3.5 seconds)
    print("1. Writing Title Sequence...")
    intro_frame = create_title_card(
        "COFFEE YIELD PREDICTION & LOSS DIAGNOSTIC SYSTEM",
        "A Multi-Modal Explainable AI Decision Support System for Precision Agriculture"
    )
    for _ in range(int(3.5 * fps)):
        out.write(intro_frame)
        
    # 2. HERO & KPI METRICS
    print("2. Capturing Hero & KPI Dashboard...")
    driver.execute_script("window.scrollTo({top: 0, behavior: 'instant'});")
    time.sleep(1)
    hold_view(3.0) # Show Hero Banner and 4 KPI cards
    
    # Scroll to diagnosis banner
    smooth_scroll(0, 480, steps=25)
    hold_view(2.5) # Show Primary Bottleneck Alert
    
    # 3. TAB 1: FACTOR-WISE YIELD LOSS BREAKDOWN
    print("3. Navigating to Tab 1: Yield Loss Breakdown...")
    try:
        t1 = driver.find_element(By.XPATH, "//p[contains(text(), 'Yield Loss')]")
        driver.execute_script("arguments[0].click();", t1)
        time.sleep(1.5)
    except Exception as e:
        print("Tab 1 click error:", e)
        
    driver.execute_script("window.scrollTo({top: 480, behavior: 'instant'});")
    hold_view(3.0) # View Plotly Waterfall Chart & Radial Gauge
    smooth_scroll(480, 800, steps=20)
    hold_view(2.5) # View Loss Factor Diagnostic Ledger Table
    
    # 4. TAB 2: EXPLAINABLE AI (SHAP)
    print("4. Navigating to Tab 2: Explainable AI (SHAP)...")
    try:
        t2 = driver.find_element(By.XPATH, "//p[contains(text(), 'Explainable AI')]")
        driver.execute_script("arguments[0].click();", t2)
        time.sleep(1.5)
    except Exception as e:
        print("Tab 2 click error:", e)
        
    driver.execute_script("window.scrollTo({top: 480, behavior: 'instant'});")
    hold_view(3.5) # View Local SHAP Attribution Bar Chart & Global Importance
    
    # 5. TAB 3: PRECISION AGRONOMIC ADVISORY (Rx)
    print("5. Navigating to Tab 3: Agronomic Advisory (Rx)...")
    try:
        t3 = driver.find_element(By.XPATH, "//p[contains(text(), 'Advisory')]")
        driver.execute_script("arguments[0].click();", t3)
        time.sleep(1.5)
    except Exception as e:
        print("Tab 3 click error:", e)
        
    driver.execute_script("window.scrollTo({top: 480, behavior: 'instant'});")
    hold_view(2.5) # View high priority lime/dolomite prescription card
    smooth_scroll(480, 850, steps=25)
    hold_view(3.0) # View fertilizer and irrigation dosages
    
    # 6. TAB 4: INTERACTIVE 'WHAT-IF' SIMULATOR
    print("6. Navigating to Tab 4: What-If Simulator...")
    try:
        t4 = driver.find_element(By.XPATH, "//p[contains(text(), 'What-If')]")
        driver.execute_script("arguments[0].click();", t4)
        time.sleep(1.5)
    except Exception as e:
        print("Tab 4 click error:", e)
        
    driver.execute_script("window.scrollTo({top: 480, behavior: 'instant'});")
    hold_view(3.5) # View Sliders & Live Projected Recovery Chart
    
    # 7. TAB 5: MODEL EVALUATION & BENCHMARK
    print("7. Navigating to Tab 5: Model Evaluation...")
    try:
        t5 = driver.find_element(By.XPATH, "//p[contains(text(), 'Evaluation')]")
        driver.execute_script("arguments[0].click();", t5)
        time.sleep(1.5)
    except Exception as e:
        print("Tab 5 click error:", e)
        
    driver.execute_script("window.scrollTo({top: 480, behavior: 'instant'});")
    hold_view(3.0) # View comparative evaluation table & viva arguments
    
    # 8. RETURN TO TOP
    print("8. Returning to Top Overview...")
    smooth_scroll(480, 0, steps=30)
    hold_view(2.0)
    
    # 9. OUTRO CARD (3.5 seconds)
    print("9. Writing Outro Sequence with QR Code...")
    outro_frame = create_outro_card()
    for _ in range(int(3.5 * fps)):
        out.write(outro_frame)
        
    out.release()
    driver.quit()
    
    # Also copy to brain artifact directory
    brain_video_path = r'C:\Users\prajw\.gemini\antigravity\brain\8ddc1524-2d7e-4612-a363-58bd93735cf3\demo_video.mp4'
    import shutil
    shutil.copy2(output_path, brain_video_path)
    print(f"Video saved to both:\n{output_path}\n{brain_video_path}")
    print(f"File size: {os.path.getsize(output_path) / (1024*1024):.2f} MB")

if __name__ == "__main__":
    main()
