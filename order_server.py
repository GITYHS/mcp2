from flask import Flask, render_template, request
import uuid

app = Flask(__name__)

@app.route('/order')
def order():
    # 주문서 정보 생성
    order_id = str(uuid.uuid4())
    customer_key = str(uuid.uuid4())
    amount = 10000  # 예시 금액
    order_name = "테스트 상품"
    customer_name = "홍길동"
    # 실제로는 DB에 주문 정보 저장 필요

    return render_template(
        'order.html',
        order_id=order_id,
        customer_key=customer_key,
        amount=amount,
        order_name=order_name,
        customer_name=customer_name
    )

if __name__ == '__main__':
    app.run(debug=True)
