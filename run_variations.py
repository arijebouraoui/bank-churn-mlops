# run_variations.py
from zenml_pipeline import training_pipeline

print("\n" + "="*50)
print("🚀 Run 1: Baseline (100 trees, depth 10)")
print("="*50)
training_pipeline(n_estimators=100, max_depth=10)

print("\n" + "="*50)
print("🚀 Run 2: More Trees (200 trees, depth 15)")
print("="*50)
training_pipeline(n_estimators=200, max_depth=15)

print("\n" + "="*50)
print("🚀 Run 3: Simpler Model (50 trees, depth 5)")
print("="*50)
training_pipeline(n_estimators=50, max_depth=5)

print("\n" + "="*50)
print("✅ All 3 runs completed!")
print("="*50)