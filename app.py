from flask import Flask, request, jsonify
import pywhatkit
import time

app = Flask(__name__)

@app.route('/send-whatsapp', methods=['POST'])
def send_whatsapp_message():
    data = request.json
    phone_number = data.get('phone_number')
    message = data.get('message')

    # التحقق من وجود رقم الهاتف والرسالة في الطلب
    if not phone_number or not message:
        return jsonify({"error": "Phone number and message are required."}), 400

    try:
        # إرسال الرسالة باستخدام pywhatkit
        pywhatkit.sendwhatmsg_instantly(phone_number, message)
        
        # الانتظار لضمان إرسال الرسالة قبل الرد
        # هذا التأخير ضروري لأن pywhatkit يعتمد على فتح المتصفح
        time.sleep(15) 

        # إغلاق كل نوافذ المتصفح
        pywhatkit.close_tab(wait_time=2)
        
        return jsonify({"status": "Message sent successfully!"}), 200
    except Exception as e:
        # إذا حدث أي خطأ، قم بإرسال رسالة الخطأ
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # تشغيل الخادم على المنفذ 10000
    app.run(host='0.0.0.0', port=10000)