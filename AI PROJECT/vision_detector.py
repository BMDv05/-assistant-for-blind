import cv2
from ultralytics import YOLO

class VisionDetector:
    def __init__(self):
        print("Module: Loading YOLOv8 Model...")
        self.model = YOLO('yolov8n.pt') 
        self.cap = cv2.VideoCapture(0)

    def read_frame(self):
        ret, frame = self.cap.read()
        return frame if ret else None

    def detect(self, frame):
        results = self.model(frame, verbose=False)
        detections = []
        
        for r in results[0].boxes:
            cls_id = int(r.cls[0])
            label = self.model.names[cls_id] # الاسم بالإنكليزي 
            
            box = r.xyxy[0].cpu().numpy()
            x1, y1, x2, y2 = int(box[0]), int(box[1]), int(box[2]), int(box[3])
            
            height = y2 - y1
            
            # تحديد المسافة (عربي للصوت + إنكليزي للشاشة)
            if height > 300:
                distance_ar = "قريب"
                distance_en = "Close"
                color = (0, 0, 255) # أحمر
            elif height > 150:
                distance_ar = "متوسط"
                distance_en = "Medium"
                color = (0, 255, 255) # أصفر
            else:
                distance_ar = "بعيد"
                distance_en = "Far"
                color = (0, 255, 0) # أخضر
                
            detections.append({
                "type": label,
                "distance": distance_ar,     # هذا يذهب للصوت(
                "display_text": distance_en, # هذا يذهب للشاشة فقط
                "box": [x1, y1, x2, y2],
                "color": color
            })
            
        return detections

    def visualize(self, frame, detections):
        for det in detections:
            x1, y1, x2, y2 = det['box']
            color = det['color']
            
            # نستخدم النص الإنكليزي هنا ليظهر بشكل صحيح
            label = f"{det['type']} - {det['display_text']}"
            
            cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
            
            # خلفية للنص
            (w, h), _ = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.6, 2)
            cv2.rectangle(frame, (x1, y1 - 20), (x1 + w, y1), color, -1)
            
            # الكتابة
            cv2.putText(frame, label, (x1, y1 - 5), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
                        
        return frame

    def release(self):
        self.cap.release()