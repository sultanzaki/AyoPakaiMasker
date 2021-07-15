# AyoPakaiMasker
AyoPakaiMasker is mask detection using Python and OpenCV, it is using the algorithm of Haarcascade to detect nose and mouth.
it use mechanism that if openCV detect nose AND mouth it will return True, then openCV will write text "Kamu pakai masker" and change the rectangle of face to green, if openCV
only detect nose OR mouth it will write text "Pakai Masker Yang Benar Dong" and change the rectangle of face to yellow, if openCV does not detect both, nose and mouth. It will return False. it will write text "Kamu tidak pakai masker" and and change the rectangle of face to red.
# WARNING
1. It has very low accuracy in low light.
2. It only detect single face in one time.
3. It run very slow, because the code is not optimized (only 3-25 FPS).
