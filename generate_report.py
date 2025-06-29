
import pandas as pd
import matplotlib.pyplot as plt
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from datetime import datetime

# Load data from CSV
df = pd.read_csv("sales_data.csv", parse_dates=["Date"])

# Aggregate sales by product
sales_summary = df.groupby('Product')['Sales'].sum().reset_index()

# Generate a bar chart
plt.figure(figsize=(6, 4))
plt.bar(sales_summary['Product'], sales_summary['Sales'], color='skyblue')
plt.title('Total Sales by Product')
plt.xlabel('Product')
plt.ylabel('Total Sales')
chart_path = 'sales_chart.png'
plt.tight_layout()
plt.savefig(chart_path)
plt.close()

# Create PDF report
report_path = f"Sales_Report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
c = canvas.Canvas(report_path, pagesize=A4)
width, height = A4

# Report Title
c.setFont("Helvetica-Bold", 18)
c.drawCentredString(width / 2, height - 50, "Automated Sales Report")

# Report Generation Date
c.setFont("Helvetica", 12)
c.drawString(50, height - 80, f"Generated On: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

# Insert chart
c.drawImage(chart_path, 100, height - 350, width=400, preserveAspectRatio=True)

# Insert table
c.setFont("Helvetica-Bold", 12)
c.drawString(50, height - 380, "Sales Summary:")
y = height - 400
c.setFont("Helvetica", 10)
for idx, row in sales_summary.iterrows():
    c.drawString(60, y, f"{row['Product']}: ₹{row['Sales']}")
    y -= 15

# Footer
c.setFont("Helvetica-Oblique", 10)
c.drawString(50, 30, "Generated using Python | Automated Reporting System")

c.save()

print(f"Report generated successfully: {report_path}")
