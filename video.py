import cv2

# Nombre del archivo de video
video_file = 'video/cargando.mp4'

# Abre el video
cap = cv2.VideoCapture(video_file)

# Verifica si el video se abrió correctamente
if not cap.isOpened():
    print("Error al abrir el video.")
    exit()

# Bucle para leer frames del video
while True:
    # Lee un frame del video
    ret, frame = cap.read()

    # Si no se puede leer más frames, sal del bucle
    if not ret:
        break

    # Muestra el frame en una ventana
    cv2.imshow('Video', frame)

    # Espera 25 milisegundos (puedes ajustar este valor según tu necesidad)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# Libera los recursos
cap.release()

# Cierra todas las ventanas
cv2.destroyAllWindows()