ADB（Android Debug Bridge）是 Android 开发工具中的一部分，用于与连接的 Android 设备进行通信和调试。以下是一些常用的 ADB 命令：

adb devices：查看连接到计算机的 Android 设备列表。

adb shell：进入设备的命令行 shell。

adb install <path_to_apk>：安装一个应用程序。

adb uninstall <package_name>：卸载一个应用程序。

adb pull <remote_file_path> <local_file_path>：从设备复制文件到计算机。

adb push <local_file_path> <remote_file_path>：从计算机复制文件到设备。

adb logcat：查看设备的日志输出。

adb reboot：重启设备。

adb screenrecord <file_name.mp4>：录制设备屏幕。

adb shell am start -n <package_name>/<activity_name>：启动一个应用程序的特定 Activity。

adb shell am force-stop <package_name>：强制停止一个应用程序。

adb shell input keyevent <key_code>：模拟按键事件。
adb shell pm list packages -3   查看 Android 设备上已安装的第三方应用包列表



