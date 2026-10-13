import json
import urllib.request
import urllib.error
import sys

def test_backend(url="http://localhost:8080/"):
    print(f"Dang kiem tra ket noi toi: {url}")
    try:
        req = urllib.request.Request(url, headers={"Accept": "application/json"})
        with urllib.request.urlopen(req, timeout=5) as response:
            status_code = response.getcode()
            body = response.read().decode('utf-8')
            data = json.loads(body)
            print(f"HTTP Status: {status_code}")
            print(f"Response Body: {data}")
            if status_code == 200 and data.get("status") == "success":
                print("Ket qua: PASS")
                return True
            else:
                print("Ket qua: FAIL (Du lieu tra ve khong dung)")
                return False
    except urllib.error.URLError as e:
        print(f"Loi ket noi: {e}")
        return False

if __name__ == "__main__":
    target_url = sys.argv[1] if len(sys.argv) > 1 else "http://localhost:8080/"
    success = test_backend(target_url)
    sys.exit(0 if success else 1)