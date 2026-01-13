"""
Script pour tester le monitoring en générant du trafic
"""
import requests
import random
import time
import json
from datetime import datetime

API_URL = "http://localhost:8000"

def generate_random_customer():
    """Génère des données client aléatoires"""
    geographies = ["France", "Germany", "Spain"]
    geography = random.choice(geographies)
    
    return {
        "CreditScore": random.randint(300, 850),
        "Age": random.randint(18, 70),
        "Tenure": random.randint(0, 10),
        "Balance": round(random.uniform(0, 200000), 2),
        "NumOfProducts": random.randint(1, 4),
        "HasCrCard": random.choice([0, 1]),
        "IsActiveMember": random.choice([0, 1]),
        "EstimatedSalary": round(random.uniform(10000, 150000), 2),
        "Geography_Germany": 1 if geography == "Germany" else 0,
        "Geography_Spain": 1 if geography == "Spain" else 0,
        "Gender_Male": random.choice([0, 1])
    }

def test_health():
    """Test du health check"""
    print("\n🏥 Testing health endpoint...")
    try:
        response = requests.get(f"{API_URL}/health", timeout=5)
        if response.status_code == 200:
            print(f"✅ Health check OK: {response.json()}")
            return True
        else:
            print(f"❌ Health check failed: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def test_single_prediction():
    """Test d'une prédiction simple"""
    print("\n🔮 Testing single prediction...")
    customer = generate_random_customer()
    
    try:
        response = requests.post(
            f"{API_URL}/predict",
            json=customer,
            timeout=5
        )
        
        if response.status_code == 200:
            result = response.json()
            print(f"✅ Prediction successful:")
            print(f"   - Churn: {result['prediction']}")
            print(f"   - Probability: {result['churn_probability']:.2%}")
            print(f"   - Risk: {result['risk_level']}")
            return True
        else:
            print(f"❌ Prediction failed: {response.status_code}")
            print(f"   Response: {response.text}")
            return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def test_metrics():
    """Test de l'endpoint métriques"""
    print("\n📊 Testing metrics endpoint...")
    try:
        response = requests.get(f"{API_URL}/metrics", timeout=5)
        if response.status_code == 200:
            lines = response.text.split('\n')
            metrics = [line for line in lines if line and not line.startswith('#')]
            print(f"✅ Metrics endpoint OK ({len(metrics)} metrics)")
            print("\nSample metrics:")
            for metric in metrics[:5]:
                print(f"   {metric}")
            return True
        else:
            print(f"❌ Metrics failed: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def generate_traffic(num_requests=50, delay=0.1):
    """Génère du trafic pour tester le monitoring"""
    print(f"\n🚀 Generating {num_requests} predictions...")
    print(f"   Delay between requests: {delay}s")
    
    success_count = 0
    error_count = 0
    churn_count = 0
    latencies = []
    
    start_time = datetime.now()
    
    for i in range(num_requests):
        customer = generate_random_customer()
        
        try:
            req_start = time.time()
            response = requests.post(
                f"{API_URL}/predict",
                json=customer,
                timeout=5
            )
            latency = time.time() - req_start
            latencies.append(latency)
            
            if response.status_code == 200:
                success_count += 1
                result = response.json()
                if result['prediction'] == 1:
                    churn_count += 1
                
                if (i + 1) % 10 == 0:
                    print(f"   Progress: {i+1}/{num_requests} requests")
            else:
                error_count += 1
                print(f"   ❌ Request {i+1} failed: {response.status_code}")
        
        except Exception as e:
            error_count += 1
            print(f"   ❌ Request {i+1} error: {e}")
        
        time.sleep(delay)
    
    end_time = datetime.now()
    duration = (end_time - start_time).total_seconds()
    
    print("\n📈 Traffic Generation Summary:")
    print(f"   Total requests: {num_requests}")
    print(f"   Successful: {success_count}")
    print(f"   Errors: {error_count}")
    print(f"   Churn predictions: {churn_count} ({churn_count/success_count*100:.1f}%)")
    print(f"   Duration: {duration:.2f}s")
    print(f"   Requests/sec: {num_requests/duration:.2f}")
    
    if latencies:
        print(f"\n⏱️  Latency Stats:")
        print(f"   Min: {min(latencies)*1000:.2f}ms")
        print(f"   Max: {max(latencies)*1000:.2f}ms")
        print(f"   Avg: {sum(latencies)/len(latencies)*1000:.2f}ms")
        print(f"   P95: {sorted(latencies)[int(len(latencies)*0.95)]*1000:.2f}ms")

def check_prometheus():
    """Vérifie si Prometheus est accessible"""
    print("\n🔍 Checking Prometheus...")
    try:
        response = requests.get("http://localhost:9090/-/healthy", timeout=5)
        if response.status_code == 200:
            print("✅ Prometheus is healthy")
            return True
        else:
            print(f"⚠️  Prometheus returned: {response.status_code}")
            return False
    except Exception as e:
        print(f"⚠️  Prometheus not accessible: {e}")
        print("   Make sure Prometheus is running: docker-compose up prometheus")
        return False

def check_grafana():
    """Vérifie si Grafana est accessible"""
    print("\n📊 Checking Grafana...")
    try:
        response = requests.get("http://localhost:3000/api/health", timeout=5)
        if response.status_code == 200:
            print("✅ Grafana is healthy")
            return True
        else:
            print(f"⚠️  Grafana returned: {response.status_code}")
            return False
    except Exception as e:
        print(f"⚠️  Grafana not accessible: {e}")
        print("   Make sure Grafana is running: docker-compose up grafana")
        return False

def main():
    """Fonction principale"""
    print("="*60)
    print("🧪 MONITORING TEST SUITE")
    print("="*60)
    
    # Test 1: API Health
    if not test_health():
        print("\n❌ API is not healthy. Stopping tests.")
        return
    
    # Test 2: Single prediction
    if not test_single_prediction():
        print("\n⚠️  Prediction test failed, but continuing...")
    
    # Test 3: Metrics endpoint
    test_metrics()
    
    # Test 4: Prometheus
    check_prometheus()
    
    # Test 5: Grafana
    check_grafana()
    
    # Test 6: Generate traffic
    print("\n" + "="*60)
    input("Press Enter to generate traffic (or Ctrl+C to skip)...")
    generate_traffic(num_requests=100, delay=0.05)
    
    print("\n" + "="*60)
    print("✅ MONITORING TEST COMPLETE")
    print("="*60)
    print("\n📊 Next steps:")
    print("   1. Check Prometheus: http://localhost:9090")
    print("   2. Check Grafana: http://localhost:3000 (admin/admin)")
    print("   3. View metrics: http://localhost:8000/metrics")
    print("   4. View API docs: http://localhost:8000/docs")
    print("   5. Try Web UI: http://localhost:8000/ui")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  Test interrupted by user")
    except Exception as e:
        print(f"\n❌ Error: {e}")