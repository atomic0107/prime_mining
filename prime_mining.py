import wx

print("hello")
rec_side = 25       #四角の辺の大きさ
bd_width = 1000     #フレームの横幅
bd_height = 1000    #フレームの縦幅
clr = "black"       #1から始まる螺旋の色
prime_cnt = 50

#Pnumcolor = "white" #素数の色
Pnumcolor = "black"  #素数の色
tnumcolor = "red"    #3の倍数
#Unumcolor = "black" #素数以外の数の色
Unumcolor = "white"  #素数以外の数の色
#P2color="blue"
#prm_cnt = 1#発見した素数をカウントする変数
#lp_cnt = 0

####################################################################
#Function Description
#Arg1:　素数か判定する数　これまで出現してきた素数で割って余りが出ないかチェック
#Arg2:　これまでに発見された素数の数
#Arg3:　素数のリスト　関数外から参照可能
#Arg3:　素数のリスト　関数外から参照可能
#Return: 素数判定FLAG
####################################################################
def prime_func(num ,prm_lp, prm ):

    cnt = 0
    ret = "FALSE"
    #num = num + 1

    for j in range(0,prm_lp):
        rem = num % prm[j]

        if rem == 0:
            cnt = 1#FALSE
            break

        if ( num/3 ) < prm[j]:#数は数自身/2以上の数で割り切れる事はないためskip
            break

    if cnt == 0:
            prm_lp = prm_lp + 1#新しい素数をカウント、次の素数発見のための割り算回数が１増える
            prm.append(num)#新しい素数をリストに追加
            ret = "TRUE"#TRUE
    return ret

def zigzag(dc,num,flag,x,y,lp_cnt,prm_cnt,prime):

    E_OK = "TRUE"
    xside = rec_side
    yside = rec_side

    for i in range(0,lp_cnt):
        ret = prime_func(
                num,#素数か判定する数
                prm_cnt,#素数の発生した数
                prime#素数のリスト
            )
        if flag == 1:
            x = x + xside * pow(-1,lp_cnt)#向きを変更
        else :
            y = y + yside * pow(-1,lp_cnt)#向きを変更

        dc.SetBrush(wx.Brush(Unumcolor))#普通の数の色の設定
        if E_OK == ret:#素数発見
            prm_cnt = prm_cnt + 1
            dc.SetBrush(wx.Brush(Pnumcolor))
        if num % 3 == 0:
            dc.SetBrush(wx.Brush("red"))
        if num % 5 == 0:
            dc.SetBrush(wx.Brush("yellow"))
        if num % 7 == 0:
            dc.SetBrush(wx.Brush("blue"))
        if num % 11 == 0:
            dc.SetBrush(wx.Brush("green"))
        if num % 13 == 0:
            dc.SetBrush(wx.Brush("orange"))
        dc.DrawRectangle(x, y, rec_side, rec_side)
        #print("%d,%d,%d,%d,ret=%s"%(num,x,y,j,ret))
        num = num + 2


def ret_wxclr(cnt,clr):
    if cnt > 1024:#?→Blue
        #clr = 0x0000ff + 0x010000
        clr = clr + 0x010000
    elif cnt > 768:#?→Blue
        clr = clr - 0x000100
    elif cnt > 512:#Green→?
        clr = clr + 0x000001
    elif cnt > 256:#yellow→Green
        clr = clr - 0x010000
    elif cnt <= 256:#red→yellow
        clr = clr + 0x000100
    return clr

def convert_clr(clr):
    clr_txt = format(clr,'x')
    obj_clr = '#'+clr_txt
    print(obj_clr)
    return obj_clr
####################################################################
#Function Description:螺旋状に四角を並べるプログラム
#Arg1:
#Arg2:螺旋描画開始位置　X
#Arg3:螺旋描画開始位置　Y
#Arg4:四角の一辺の大きさ
#Arg5:四角の色
#Return:　なし
####################################################################
def DrawRecLine(dc,x,y,rec_side,clr):
    prime = [2]#素数に２を追加
    prime_clr = ["#FF0000"]
    #prime_clr = [0xff0000]
    temp_clr = 0xff0000
    prm_cnt = 1#発見した素数をカウントする変数
    lp_cnt = 0
    num = 3#３から素数探索
    E_OK = "TRUE"
    xside = rec_side
    yside = rec_side

    dc.SetBrush(wx.Brush(clr))
    dc.DrawRectangle(x, y, rec_side, rec_side)
    for i in range(0,prime_cnt):
        #side_cnt=0
        #zigzag(dc,num,1,x,y,lp_cnt,prm_cnt,prime)
        #zigzag(dc,num,0,x,y,lp_cnt,prm_cnt,prime)
        #"""
        for j in range(0,lp_cnt):

            ret = prime_func(
                    num,#素数か判定する数
                    prm_cnt,#素数の発生した数
                    prime#素数のリスト
                )
            x = x + xside * pow(-1,lp_cnt)#向きを変更

            dc.SetBrush(wx.Brush(Unumcolor))#普通の数の色の設定
            if E_OK == ret:#素数発見
                prm_cnt = prm_cnt + 1
                #temp_clr = ret_wxclr(prm_cnt,temp_clr)#新素数色を算出
                #prime_clr.append(convert_clr(temp_clr))
                #prime_clr[prm_cnt] = convert_clr(prime_clr)
                #prime_clr.append(temp_clr)
                #新素数色の配列登録
                dc.SetBrush(wx.Brush(Pnumcolor))#新素数の色
            """
            for i in range (0,prm_cnt):
                if num % prime[i] == 0:
                    dc.SetBrush(wx.Brush(prime_clr[i]))
            """
            """
            if num % 3 == 0:
                dc.SetBrush(wx.Brush("red"))
            if num % 5 == 0:
                dc.SetBrush(wx.Brush("yellow"))
            if num % 7 == 0:
                dc.SetBrush(wx.Brush("blue"))
            if num % 11 == 0:
                dc.SetBrush(wx.Brush("green"))
            if num % 13 == 0:
                dc.SetBrush(wx.Brush("orange"))
            """
            dc.DrawRectangle(x, y, rec_side, rec_side)
            #print("%d,%d,%d,%d,ret=%s"%(num,x,y,j,ret))

            num = num + 1

        for k in range(0,lp_cnt):

            ret = prime_func(
                    num,#素数か判定する数
                    prm_cnt,#素数の発生した数
                    prime#素数のリスト
                )
            #if side_cnt == 1:
            y = y + yside * pow(-1,lp_cnt)#向きを変更
            dc.SetBrush(wx.Brush(Unumcolor))#普通の数の色の設定
            if E_OK == ret:#素数発見
                prm_cnt = prm_cnt + 1
                dc.SetBrush(wx.Brush(Pnumcolor))
            """
            if num % 3 == 0:
                dc.SetBrush(wx.Brush("red"))
            if num % 5 == 0:
                dc.SetBrush(wx.Brush("yellow"))
            if num % 7 == 0:
                dc.SetBrush(wx.Brush("blue"))
            if num % 11 == 0:
                dc.SetBrush(wx.Brush("green"))
            if num % 13 == 0:
                dc.SetBrush(wx.Brush("orange"))
            """
            dc.DrawRectangle(x, y, rec_side, rec_side)
            #print("%d,%d,%d,%d,ret=%s"%(num,x,y,k,ret))
            num = num + 1
        #"""
        #if j == lp_cnt -1:
        lp_cnt = lp_cnt + 1

        #print("lp_cnt=%d"%i)
    #dc.SetBrush(wx.Brush(P2color))
    #dc.DrawRectangle(bd_width/2 - rec_side, bd_height/2, rec_side, rec_side)
    d = len(prime)
    print("last_num = %d, num of prime = %d,%d"%(num,d,prime[d-1]))
    print(prime)

def OnPaint(event):

    obj = event.GetEventObject()#イベントを発生したオブジェクトを取得する関数
    dc = wx.BufferedPaintDC(obj)#指定したオブジェクトを描画キャンパスに設定するクラス
    dc.Clear()

    dc.SetPen(wx.TRANSPARENT_PEN)
    dc.SetBrush(wx.Brush(clr))
    DrawRecLine(dc,bd_height/2,bd_width/2,rec_side,clr)
    #DrawRecLine(dc, 0,0,rec_side,clr)
    #dc.SetPen(wx.TRANSPARENT_PEN)

def OnEraseBackground(event):
    pass#NOP 処理がないとエラーになるためNOP記述

def Main():
    frame = wx.Frame(None,title="Uram")#ウィンドウ作成クラス
    frame.SetClientSize(bd_width,bd_height)
    panel=wx.Panel(frame)
    panel.SetBackgroundColour('white')

    panel.Bind(wx.EVT_PAINT,OnPaint)#描画イベント発行
    panel.Bind(wx.EVT_ERASE_BACKGROUND,OnEraseBackground)

    frame.Center()
    frame.Show()

if __name__=="__main__":

    app = wx.App()
    Main()
    app.MainLoop()
