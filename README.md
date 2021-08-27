# AyoPakaiMasker
AyoPakaiMasker is mask detection using Python and OpenCV, and it is using the algorithm of Haarcascade to detect nose and mouth. It uses a mechanism that if OpenCV detects nose and mouth, it will return True. Opencv will write the text "Kamu pakai masker" and change the rectangle of the face to green. If OpenCV only detects nose OR mouth, it will write text "Pakai Masker Yang Benar Dong" and shift the rectangle of face to yellow if openCV does not see both nose and mouth. It will return False. It will write the text "Kamu tidak pakai masker" and change the face's rectangle to red.
# WARNING
1. It has very low accuracy in low light.
2. It only detect single face in one time.
3. It run very slow, because the code is not optimized (only 3-25 FPS).
