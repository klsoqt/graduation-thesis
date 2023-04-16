import subprocess
import detect_position
import robotMove
import toArduino

move_counter = 1

while True:
    subprocess.run(
        ['python', 'captureWebcam.py']
    )

    subprocess.run(
        ['python', 'yolov7/detect.py', '--weights', 'yolov7/best_282.pt', '--source', 'data/*', '--device', 'cpu', '--no-trace', '--save-txt']
    )

    path1 = 'runs/detect/exp{}/labels/img_1.txt'.format(move_counter + 1)
    path2 = 'runs/detect/exp{}/labels/img_2.txt'.format(move_counter + 1)

    res = detect_position.detect_move(path1, path2)
    print("==============================")
    print("Nước đi người chơi: ", res[0], '-', res[1])

    #robot_move = robotMove.robotMove["{}".format(move_counter)]

    toArduino.write_read(move_counter)
    # subprocess.run(
    #     ['python', 'toArduino.py']
    # )

    move_counter += 1
