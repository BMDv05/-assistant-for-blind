import pyttsx3
import threading

class VoiceAssistant:
    def __init__(self):
        """تهيئة محرك النطق الصوتي"""
        self.engine = pyttsx3.init()
        # محاولة العثور على صوت عربي في الجهاز
        voices = self.engine.getProperty('voices')
        for voice in voices:
            if "arabic" in voice.name.lower():
                self.engine.setProperty('voice', voice.id)
                break

    def speak(self, text):
        """نطق النص المدخل بدون تعطيل الكاميرا"""
        if not text:
            return
            
        # تشغيل الصوت في خيط (Thread) منفصل لضمان استمرار عمل الكاميرا
        threading.Thread(target=self._run, args=(text,), daemon=True).start()

    def _run(self, text):
        """الدالة الداخلية لتشغيل المحرك"""
        try:
            self.engine.say(text)
            self.engine.runAndWait()
        except Exception as e:
            print(f"Voice Error: {e}")

# دالة مساعدة لضمان التوافق مع أي استدعاء قديم (اختياري)
def speak_text(text):
    v = VoiceAssistant()
    v.speak(text)