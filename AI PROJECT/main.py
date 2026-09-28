import cv2
import json
import time
from vision_detector import VisionDetector         
from ocr_module import get_text_from_frame         
from voice_engine import VoiceAssistant            # لجلب محرك الصوت فقط
from description_manager import generate_description # لجلب الوصف من ملفه الخاص

def main():
    vision = VisionDetector()
    voice = VoiceAssistant()
    count = 0

    print("The system working now .... press q to end")

    try:
        while True:
            frame = vision.read_frame()
            if frame is None: break
            count += 1

            # معالجة الصور والنصوص
            detections = vision.detect(frame)
            texts = get_text_from_frame(frame) if count % 30 == 0 else []

            # دمج البيانات للموقع والصوت
            description, alerts = generate_description(detections, texts)

            # تحديث ملف الويب
            with open('data_log.json', 'w', encoding='utf-8') as f:
                json.dump({"description": description, "alerts": alerts}, f, ensure_ascii=False)

            # التشغيل الصوتي
            if alerts:
                voice.speak(alerts[0])
            elif count % 100 == 0 and description:
                voice.speak(description)

            # عرض الكاميرا
            cv2.imshow("Smart Project", vision.visualize(frame, detections))
            if cv2.waitKey(1) & 0xFF == ord('q'): break
    finally:
        vision.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()