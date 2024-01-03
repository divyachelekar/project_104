import cv2
img = cv2.imread("project104pro/solar-system.jpg")
cv2.putText(img ,
            "Sun",
            (20,300),
            cv2.FONT_HERSHEY_COMPLEX_SMALL,
            0.8,
            (255,255,255)
            )
cv2.putText(img ,
            "Mercury",
            (120,180),
            cv2.FONT_HERSHEY_COMPLEX_SMALL,
            0.5,
            (255,255,255)
            )
cv2.putText(img ,
            "Venus",
            (195,270),
            cv2.FONT_HERSHEY_COMPLEX_SMALL,
            0.5,
            (255,255,255)
            )
cv2.putText(img ,
            "Earth",
            (295,270),
            cv2.FONT_HERSHEY_COMPLEX_SMALL,
            0.5,
            (255,255,255)
            )
cv2.putText(img ,
            "Mars",
            (395,270),
            cv2.FONT_HERSHEY_COMPLEX_SMALL,
            0.5,
            (255,255,255)
            )
cv2.putText(img ,
            "Jupiter",
            (425,150),
            cv2.FONT_HERSHEY_COMPLEX_SMALL,
            0.5,
            (255,255,255)
            )
cv2.putText(img ,
            "Saturn",
            (700,120),
            cv2.FONT_HERSHEY_COMPLEX_SMALL,
            0.5,
            (255,255,255)
            )
cv2.putText(img ,
            "Uranus",
            (950,140),
            cv2.FONT_HERSHEY_COMPLEX_SMALL,
            0.5,
            (255,255,255)
            )
cv2.putText(img ,
            "Neptune",
            (1100,140),
            cv2.FONT_HERSHEY_COMPLEX_SMALL,
            0.5,
            (255,255,255)
            )
cv2.imwrite("Solar_systemwithname.jpg",img)
cv2.imshow("output" , img)
cv2.waitKey(0)
