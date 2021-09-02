from pyzbar import pyzbar
import cv2
import msvcrt as m

frame = ""


def wait():
    m.getch()


def draw_barcode(decoded, image):
    n_points = len(decoded.polygon)
    for i in range(n_points):
        image = cv2.line(image, decoded.polygon[i], decoded.polygon[(i+1) % n_points], color=(0, 255, 0), thickness=5)

    # image = cv2.rectangle(image, (decoded.rect.left, decoded.rect.top),
    #                       (decoded.rect.left + decoded.rect.width, decoded.rect.top + decoded.rect.height),
    #                       color=(0, 255, 0),
    #                       thickness=5)
    return image


def decode(image):
    # decodes all barcodes from an image
    decoded_objects = pyzbar.decode(image)
    for obj in decoded_objects:
        # draw the barcode
        image = draw_barcode(obj, image)
        print("detected barcode:", obj)
        # print barcode type & data
        print("Type:", obj.type)
        print("Data:", obj.data)
        print()
        cv2.imshow("frame", frame)
        cv2.waitKey(2000)
    return image


if __name__ == "__main__":
    # define a video capture object
    vid = cv2.VideoCapture(0)

    while (True):
        # Capture the video frame
        # by frame
        ret, frame = vid.read()
        # Display the resulting frame
        b = decode(frame)
        # cv2.imshow("frame", b)
        # cv2.waitKey(1000)
        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # After the loop release the cap object
    vid.release()
    # Destroy all the windows
    cv2.destroyAllWindows()
