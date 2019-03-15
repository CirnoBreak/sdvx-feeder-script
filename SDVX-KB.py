from System import Int16

if starting:
   system.setThreadTiming(TimingTypes.HighresSystemTimer)
   system.threadExecutionInterval = 5        # loop delay
   math = 500 # 旋钮灵敏度
   x = 1500
   y = 1500

# Configure your keys to whatever you need here (You probably don't need the BTs/FXs but hey)
# 对应四个按键跟两个FX，由于设置了config.bat暂时不起作用
BTA			= Key.D # BT-A
BTB			= Key.F # BT-B
BTC			= Key.J # BT-C
BTD			= Key.K # BT-D

FXL			= Key.V # FX-L
FXR			= Key.N # FX-R

START		= Key.NumberPadPeriod # Start

VOLL_LEFT   = Key.W # 左旋扭 - 左旋
VOLL_RIGHT  = Key.E # 左旋钮 - 右旋
VOLR_LEFT   = Key.NumberPad9 # 右旋钮 - 左旋
VOLR_RIGHT  = Key.NumberPadPlus # 右旋钮 - 右旋

#------------------------Script nonsense beyond this point.. Modify or improve if desired but this should work in general ((((((::::::------------------------
vJoy[0].setButton(0,int(keyboard.getKeyDown(BTA)))
vJoy[0].setButton(1,int(keyboard.getKeyDown(BTB)))
vJoy[0].setButton(2,int(keyboard.getKeyDown(BTC)))
vJoy[0].setButton(3,int(keyboard.getKeyDown(BTD)))
vJoy[0].setButton(4,int(keyboard.getKeyDown(FXL)))
vJoy[0].setButton(5,int(keyboard.getKeyDown(FXR)))
vJoy[0].setButton(6,int(keyboard.getKeyDown(START)))
if keyboard.getKeyDown(VOLL_RIGHT):
	x += math
	vJoy[0].x = x
if keyboard.getKeyDown(VOLL_LEFT):
	x -= math
	vJoy[0].x = x
if keyboard.getKeyDown(VOLR_RIGHT):
	y += math
	vJoy[0].y = y
if keyboard.getKeyDown(VOLR_LEFT):
	y -= math
	vJoy[0].y = y
