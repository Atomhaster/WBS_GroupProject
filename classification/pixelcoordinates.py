import cv2 as cv

def find_coord(event, x,y,flags,params):
    if event==cv.EVENT_FLAG_LBUTTON:
        # showing the coordinates on the image using the left mouse click
        print(x,",",y)
        font = cv.FONT_HERSHEY_PLAIN
        cv.putText(img,str(x) + ","+ str(y), (x,y),font,1,(255,0,0))
        cv.imshow("image",img)

# display the image
# if __name__=="__main__":
img = cv.imread("G://WBS - Data Science mit Python//WBS_GroupProject//example_paintings//Alfred_Sisley_63.jpg")
cv.imshow("image",img)
cv.setMouseCallback("image",find_coord)
cv.imshow("image",img)
cv.waitKey(0)
cv.destroyAllWindows()