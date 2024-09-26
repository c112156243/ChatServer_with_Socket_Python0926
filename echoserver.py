def calculate_bmi(weight, height):
    return weight / (height ** 2)

def get_health_status(bmi):
    if bmi < 18.5:
        return "體重過輕"
    elif 18.5 <= bmi < 24.9:
        return "正常範圍"
    elif 25 <= bmi < 29.9:
        return "體重過重"
    else:
        return "肥胖"

def main():
    try:
        weight = float(input("請輸入體重(公斤): "))
        height = float(input("請輸入身高(公尺): "))
        bmi = calculate_bmi(weight, height)
        status = get_health_status(bmi)
        print(f"您的BMI值為: {bmi:.2f}")
        print(f"健康狀況: {status}")
    except ValueError:
        print("請輸入有效的數字。")

if __name__ == "__main__":
    main()