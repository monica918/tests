adb shell monkey -p com.example.app 1000      将在指定的应用程序上随机执行1000个事件，包括触摸、滑动、按键等操作

adb shell：进入设备的命令行 shell。

adb shell monkey -p com.example.app --pct-touch 50    测试将随机执行各种事件，其中50%的事件将是触摸事件，其余的事件将是其他类型的事件（如滑动、按键等）pct 是百分比的意思

adb shell monkey -p com.example.app --pct-motion 80    测试将随机执行各种事件，其中80%的事件将是触摸事件