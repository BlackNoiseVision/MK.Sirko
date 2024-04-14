# У цьому файлі міститься скрипт гри.

# Оголошення персонажів, які використовуються в цій грі. Колірний аргумент розфарбовує
# ім’я персонажа.

define s = Character("Сірко", color="#84645b")
define m = Character("Чоловік", color="#be833e")
define w = Character("Вовк", color="#e1e1e1")

image sirko = "sirko.png"
image man = "owner.png"
image wolf = "wolf.png"
image wom = "woman.png"

label start:
    play music "house.mp3" loop fadein 1.5 fadeout 1.5

    scene bg house with pixellate
    show man:
        subpixel True pos (0.48, 0.53) xzoom 0.1 yzoom 0.1 
    with Dissolve(1.5)

    "В одного чоловіка був собака Сірко – тяжко старий."
    
    #show sirko:
    #    pos (0.28, 0.77) xzoom 0.2 yzoom 0.2 

    window auto hide
    show sirko:
        subpixel True ypos 0.61 
        xzoom 0.2 yzoom 0.2 
        xpos -0.18 
        linear 1.31 xpos 0.2 
    with Pause(1.41)
    show sirko:
        pos (0.2, 0.61) 
    window auto show




    "Хазяїн бачить, що з нього нічого не буде, що він до хазяйства нездатний, і прогнав його від себе."


    window auto hide
    show man:
        subpixel True 
        pos (0.48, 0.53) xzoom 0.09999999999999998 yzoom 0.09999999999999998 
        linear 0.50 pos (0.36, 0.42) xzoom 0.2 yzoom 0.2 
    with Pause(0.60)
    show man:
        pos (0.36, 0.42) xzoom 0.2 yzoom 0.2 
    
    show man:
        subpixel True 
        zrotate 0.0 
        linear 0.6 zrotate 40.0 
    with Pause(0.25)
    show man:
        zrotate 40.0 

    show sirko:
        subpixel True 
        pos (0.2, 0.61) matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
        linear 0.10 pos (-0.18, 0.34) matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 171.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
    with Pause(0.20)
    show sirko:
        pos (-0.18, 0.34) matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 171.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 

    show man:
        subpixel True 
        zrotate 40.0 
        linear 0.15 zrotate 0.0 
    with Pause(0.25)
    show man:
        zrotate 0.0 
    
    pause 1.0
    hide man with Dissolve(1.0)



    show bg field with PushMove(2.0, "pushright")

    play music "field.mp3" loop fadein 1.5 fadeout 1.5

    show sirko:
        subpixel True 
        pos (1.03, 0.23) zrotate 189.0 
        linear 0.20 pos (0.05, 0.66) zrotate 1269.0 
    with Pause(0.30)
    show sirko:
        pos (0.05, 0.66) zrotate 1269.0 
    with vpunch

    pause 2.0
    
    "Цей Сірко никає по полю."

    window auto hide
    show sirko:
        subpixel True 
        pos (0.05, 0.66) 
        linear 1.20 pos (0.82, 0.56) 
    with Pause(1.30)
    show sirko:
        pos (0.82, 0.56) 
    
    show sirko:
        subpixel True 
        pos (0.82, 0.56) matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 171.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
        linear 0.20 pos (0.82, 0.56) matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, -180.0, 189.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
    with Pause(0.30)
    show sirko:
        pos (0.82, 0.56) matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, -180.0, 189.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
    
    show sirko:
        subpixel True 
        pos (0.82, 0.56) 
        linear 0.46 pos (0.68, 0.54) 
    with Pause(0.56)
    show sirko:
        pos (0.68, 0.54) 

    pause 0.3
    window auto show

    "Коли це приходить до нього вовк."
    
    #show wolf:
    #    subpixel True pos (-0.15, 0.72) xzoom 0.3 yzoom 0.3 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, -180.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
    
    show wolf:
        subpixel True pos (-0.32, 0.56) xzoom 0.3 yzoom 0.3 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, -180.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
    
    window auto hide
    show wolf:
        subpixel True 
        pos (-0.32, 0.56) 
        linear 0.70 pos (0.12, 0.62) 
    with Pause(0.7)
    show wolf:
        pos (0.12, 0.62) 

    pause 0.5    
    window auto show




    "Та й питає."
    w "Чого ти тут ходиш?"
    "Сірко йому:"
    s "Що ж, брате, прогнав мене хазяїн, а я і ходжу тут."
    "Тоді вовк йому каже:"
    w "А зробити так, щоб тебе хазяїн ізнов прийняв до себе?"
    "Сірко відповідає:"
    s "Зроби, голубчику; я вже таки чимсь тобі віддячу."
    "Вовк каже:"
    w "Ну, гляди: як вийде твій хазяїн із жінкою жать і вона дитину положить під копою."
    w "То ти будеш близько ходить коло того поля."
    w "Щоб я знав, де те поле."
    w"То я візьму дитину, а ти будеш забирати у мене ту дитину."
    w"Тоді неначе я тебе і злякаюсь та й пущу дитину."
    
    window auto hide
    show wolf:
        subpixel True 
        pos (0.12, 0.62) 
        linear 0.40 pos (-0.33, 0.43) 
    with Pause(0.50)
    show wolf:
        pos (-0.33, 0.43) 

    show sirko:
        subpixel True 
        pos (0.68, 0.54) 
        linear 0.40 pos (1.12, 0.53) 
    with Pause(0.50)
    show sirko:
        pos (1.12, 0.53) 
    window auto show
    hide wolf
    hide sirko 

    show bg field2 with wiperight
    
    show sirko:
        subpixel True pos (0.2, 0.36) xzoom 0.05 yzoom 0.05 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, -180.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
    with Dissolve(0.5)

    "У жнива той чоловік і жінка вийшли у поле жать. "
    
    #show man:
    #    subpixel True pos (1.05, 0.37) xzoom 0.08 yzoom 0.08 
        
    window auto hide
    show man:
        subpixel True 
        pos (1.05, 0.37) 
        xzoom 0.08 yzoom 0.08 
        linear 0.40 pos (0.74, 0.33) 
    with Pause(1.00)
    show man:
        pos (0.74, 0.33) 
    
    
    #show woman:
    #    subpixel True pos (1.05, 0.49) xzoom 0.1 yzoom 0.1 
    
    
    window auto hide
    show woman:
        subpixel True 
        pos (1.05, 0.49) 
        xzoom 0.1 yzoom 0.1 
        linear 0.40 pos (0.48, 0.29) 
    with Pause(0.40)
    show woman:
        pos (0.48, 0.29) 
    window auto show

    image kid = "kid.png"

    
    
    show kid:
        subpixel True pos (0.45, 0.45) xzoom 0.07 yzoom 0.07  
    with dissolve

    "Жінка положила свою маленьку дитину під копою, а сама і жне коло чоловіка."
    
    window auto hide
    show woman:
        subpixel True 
        pos (0.44, 0.29) 
        linear 0.60 pos (0.8, 0.4) 
    with Pause(0.70)
    show woman:
        pos (0.8, 0.4) 
    
    show wolf:
        subpixel True pos (-0.1, 0.52) xzoom 0.1 yzoom 0.1 yrotate -180.0 
    
    window auto hide
    show wolf:
        subpixel True 
        pos (-0.1, 0.52) 
        linear 1.16 pos (0.42, 0.42) 
    with Pause(1.26)
    show wolf:
        pos (0.42, 0.42) 

    hide kid
    
    show wolf:
        subpixel True 
        matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
        linear 0.10 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, -180.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
    with Pause(0.20)
    show wolf:
        matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, -180.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
    
    show wolf:
        subpixel True 
        pos (0.42, 0.42) 
        linear 0.25 pos (-0.1, 0.57) 
    with Pause(0.35)
    show wolf:
        pos (-0.1, 0.57) 
    window auto show







    "Коли це вовк біжить житом, та за ту дитину – і несе її полем."

    
    window auto hide
    show sirko:
        subpixel True 
        pos (0.2, 0.36) xzoom 0.050000000000000044 yzoom 0.050000000000000044 
        linear 1.00 pos (0.05, 0.41) xzoom 0.2 yzoom 0.2 
    with Pause(1.10)
    show sirko:
        pos (0.05, 0.41) xzoom 0.2 yzoom 0.2 
    
    show sirko:
        subpixel True 
        pos (0.05, 0.41) 
        linear 0.13 pos (-0.3, 0.43) 
    with Pause(0.23)
    show sirko:
        pos (-0.3, 0.43) 
    window auto show




    "Сірко за тим вовком. Доганяє його. А чоловік кричить:"
    play audio "gidg-ga.mp3"
    m "Гидж-га, Сірко!"
    
    show man:
        subpixel True 
        zrotate 0.0 
        linear 0.6 zrotate 360.0 
    with Pause(0.6)
    show man:
        zrotate 360.0 

    pause 0.5
    show sirko:
        subpixel True xzoom 0.1 yzoom 0.1 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
        pos (-0.3, 0.43) 
        linear 1.00 pos (0.53, 0.43) 
    with Pause(1.10)
    show sirko:
        pos (0.53, 0.43) 
    window auto show



    image bread = "bread.png"
    image salo = "salo.png"

    "Сірко якось догнав того вовка і забрав дитину: приніс до того чоловіка та й оддав йому."
    show kid:
        subpixel True pos (0.71, 0.51) xzoom 0.07 yzoom 0.07  
    with Dissolve (1.5)
    pause 0.5
    show bread:
        pos (0.75, 0.42) xzoom 0.3 yzoom 0.3 
    with dissolve
    show salo:
        subpixel True pos (0.78, 0.43) xzoom 0.05 yzoom 0.05 
    with dissolve

    "Тоді той чоловік вийняв із торби хліб і кусок сала та й каже:"
    m "На, Сірко їж, – за те, що не дав вовкові дитини з'їсти!"



    show bread:
        subpixel True 
        pos (0.75, 0.42) 
        linear 0.20 pos (0.54, 0.47) 
    with Pause(0.30)
    show bread:
        pos (0.54, 0.47) 
    hide bread with dissolve
    
    show salo:
        subpixel True 
        pos (0.78, 0.43) 
        linear 0.20 pos (0.54, 0.46) 
    with Pause(0.30)
    show salo:
        pos (0.54, 0.46) 
    hide salo with dissolve


    hide kid with dissolve
    
    window auto hide
    show sirko:
        subpixel True 
        pos (0.48, 0.43) 
        linear 1.88 pos (1.04, 0.38) 
    show man:
        subpixel True 
        pos (0.74, 0.33) 
        linear 1.88 pos (1.09, 0.32) 
    show woman:
        subpixel True 
        pos (0.8, 0.4) 
        linear 1.88 pos (1.15, 0.38) 
    with Pause(1.98)
    show sirko:
        pos (1.04, 0.38) 
    show man:
        pos (1.09, 0.32) 
    show woman:
        pos (1.15, 0.38) 
    window auto show

    hide man
    hide sirko
    hide woman
    hide wolf
    show bg housen with Dissolve(1.5)
    "Ото увечері ідуть із поля, беруть і Сірка. Прийшли додому, чоловік і каже:"
    m "Жінко, вари лишень гречані галушки та сито їх із салом затовчи."
    "Тільки що вони ізварилися, він садовить Сірка за стіл та й сам сів коло його і каже:"
    m "А сип, жінко, галушки, та будемо вечеряти."
    "Жінка і насипала. Він Сіркові набрав у полумисок; так уже йому годить, щоб він не був голодний, щоб він часом гарячим не опікся!"
    "Ото Сірко і думає:"
    s "«Треба подякувати вовкові, що він мені таку вигоду зробив»"
    show bg house with Dissolve(1.5)
    "А той чоловік, діждавши м'ясниць, віддає свою дочку заміж."
    show bg field with PushMove(2.0, "pushright")

    show wolf:
        subpixel True pos (0.11, 0.44) xzoom 0.3 yzoom 0.3 yrotate -180.0 
    with dissolve

    
    show sirko:
        subpixel True pos (0.66, 0.36) xzoom 0.25 yzoom 0.25 yrotate -180.0 
    with dissolve
    "Сірко пішов у поле, знайшов там вовка та й каже йому:"
    s "Прийди у неділю увечері до городу мого хазяїна, а я тебе зазву у хату та віддячу тобі за те, що ти мені добро зробив."
    
    
    window auto hide
    show wolf:
        subpixel True 
        zrotate 0.0 
        linear 0.30 zrotate 360.0 
    with Pause(0.40)
    show wolf:
        zrotate 360.0 
    


    hide wolf with dissolve
    hide sirko with dissolve
    show bg housen with Dissolve(1.5)
    "Ото вовк, діждавши неділі, прийшов на те місце, куди йому Сірко сказав."
    window auto hide
    show wolf:
        subpixel True pos (-0.21, 0.79) xzoom 0.2 yzoom 0.2 yrotate 180.0 

    show wolf:
        subpixel True 
        pos (-0.21, 0.79) 
        linear 0.70 pos (0.16, 0.69) 
    with Pause(0.80)
    show wolf:
        pos (0.16, 0.69) 
    window auto show

    "А в той самий день у того чоловіка було весілля."
    "Сірко вийшов до його та й увів у хату і посадовив його під столом."
    hide wolf with dissolve

    "Ото Сірко на столі узяв пляшку горілки, м'яса доволі і поніс під стіл. А люди хотіли ту собаку бити. Чоловік каже:"
    m "Не бийте Сірка: він мені добро зробив, то я і йому добро буду робити, поки його й віку."
    "Сірко, що найсмачніше на столі лежить, бере та подає вовкові. Обгодував і упоїв так, що вовк не витерпів та й каже:"
    w "Буду співати!"
    "Сірко каже:"
    s "Не співай, бо тут тобі буде лихо! Краще я ще тобі подам пляшку горілки, та тільки мовчи."
    "Вовк, як випив ту пляшку горілки, та й каже:"
    w "Отепер уже буду співати!"
    "Та як завиє під столом... Тоді деякі люди повтікали з хати, а деякі хотіли бити вовка. А Сірко і ліг на вовкові, наче хоче задушити."
    "Хазяїн каже:"
    m "Не бийте вовка, бо ви мені Сірка уб'єте! Він і сам йому раду дасть – ось не займайте!"
        
    show wolf:
        subpixel True pos (850, 653) 
        xzoom 0.15 yzoom 0.15 
    with dissolve
    
    window auto hide
    show wolf:
        subpixel True 
        pos (850, 653) 
        linear 0.25 pos (-401, 933) 
    with Pause(0.35)
    show wolf:
        pos (-401, 933) 

    
    show sirko:
        subpixel True pos (0.45, 0.56) xzoom 0.13 yzoom 0.13 yrotate 180.0 
    with dissolve
    
    window auto hide
    show sirko:
        subpixel True 
        pos (0.45, 0.56) 
        linear 0.25 pos (-0.17, 0.8) 
    with Pause(0.35)
    show sirko:
        pos (-0.17, 0.8) 
    window auto show


    show bg fieldn with PushMove(2.0, "pushright")
    image o = "00316-1384942589.png"
    window auto hide
    show o:
        subpixel True pos (0.77, 0.17) xzoom 0.08 yzoom 0.08 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(0.83)*BrightnessMatrix(-0.13)*HueMatrix(-540.0) blend None 
    with dissolve
    show wolf:
        subpixel True pos (1990, 608) 
        xzoom 0.15 yzoom 0.15 

    
    show wolf:
        subpixel True 
        pos (1990, 608) xzoom 0.15 yzoom 0.15 
        linear 0.82 pos (1226, 600) xzoom 0.3 yzoom 0.3 
    with Pause(0.92)
    show wolf:
        pos (1226, 600) xzoom 0.3 yzoom 0.3 

    show sirko:
        subpixel True pos (1.07, 0.58) xzoom 0.13 yzoom 0.13 yrotate 180.0 
    
    show sirko:
        subpixel True 
        pos (1.07, 0.58) 
        linear 0.81 pos (0.88, 0.45) 
    with Pause(0.91)
    show sirko:
        pos (0.88, 0.45) 
    window auto show

    "Ото Сірко вивів вовка аж на поле та й каже:"
    s"Ти мені добро зробив, а я тобі!"
    "Та й розпрощались."
    stop music
    play audio "spooky.mp3"
    s "А хто це там стоїть?"
    

    return
