import random
import math

god = 0
crops = 0
married = 0
endgame = 0

narod = 100
kazna = 10000
zerno = 500
land = 100
love = 100

print('Вы медленно открываете глаза и задумчиво смотрите на золотистые лучи утреннего солнца. ')
print('Ваша жизнь до этого момента была лишь тяжелым сном, и вы чувствуете, что сегодня должно случиться нечто важное.')
print('Но перед этим нужно вспомнить, как вас зовут. Введите ваше имя.')
name = input('')
print('Доброе утро, '+name+'!')
print('Сегодня действительно случилось что-то невероятное. Вам прислали письмо! Удивительно! А знаете почему?')
print('Вы всего лишь никому не нужный пьяница и бродяга, промышляющий попрошайничеством. У вас нет ни гроша в кармане.')
print('Погодите... Неужели это извещение о наследстве?')
print('Поздравляю, '+name+'. Теперь вы обладатель крохотного безымянного королевства.')
print('Недавно умерла ваша далекая родственница, которую вы видели только раз в жизни.')
print('Теперь вы наверняка сможете стать великим человеком. Весь мир ждет вас!')
print('Кстати, а как вы назовете вашу землю?')
country = input('')
print('Какое красивое название - '+country+'!')
print('Вы с восхищением оглядываете свои скромные владения. Наступает первый год вашего правления.')
print('В вашем новом государстве сейчас:')
print('Население:', narod, 'человек')
print('Запасы еды:', zerno, 'ед. зерна')
print('Деньги:', kazna, 'золотых')
print('Размер государства:', land)
print('Лояльность народа:', love)
print('К вам неожиданно заходит ваш управитель. Чего же вы ждете?')
print('Нажмите Enter.')
input('')
print('____________________________________________________________________')
print('ПРАВИЛА')
print('-> Население необходимо для ведения военных действий.')
print('-> Зерно необходимо для прокорма населения и торговли. Его можно покупать и выращивать.')
print('-> Казна необходима для торговли, покупки услуг и подарков, подписания мирных договоров, снаряжения солдат.')
print('-> Земля (размер гос-ва) необходима для посева зерна.')
print('-> Чтобы увеличить количество людей, давайте им больше еды, чем нужно.')
print('-> Вы можете жениться только один раз.')
print('<-><-><->')
print('-> Если количество людей опустится ниже 30, вы проиграете.')
print('-> Если размер гос-ва опустится ниже 30, вы проиграете.')
print('-> Если расположение (лояльность) народа опустится ниже 20, вы проиграете.')
print('-> Цель игры - как можно дольше управлять страной.')
print('____________________________________________________________________')
print('Время превратить этот мизерный кусочек земли в огромную империю! Нажмите Enter.')
input('')
print('')
print('HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH')
print('<<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>>')
print('HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH')
print('')

while love >= 20 and narod >= 30 and land >= 30:

    def rescheck():
        print('Ресурсы государства ' + country + ':')
        print('Население:', narod, 'человек')
        print('Запасы еды:', zerno, 'ед. зерна')
        print('Деньги:', kazna, ' золотых')
        print('Размер государства:', land)
        print('Лояльность народа:', love)
        print('Год продолжается. Нажмите Enter.')
        input('')
        print('')
        print('<<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>>')
        print('')

    def disaster_event():
        global narod
        global zerno
        global crops
        dis_name = random.choice(['нашествие грызунов', 'нашествие саранчи', 'землетрясение',
                                  'сход лавины с гор', 'извержение вулкана', 'эпидемия чумы',
                                  'наводнение', 'засуха'])
        dis_cost = random.choice([0.2, 0.3, 0.4, 0.5])
        print('О ужас! Произошла катастрофа - '+dis_name+'!')
        if dis_name == 'нашествие грызунов':
            zerno -= int(zerno * float(dis_cost))
            print('Ваши запасы зерна пострадали. Теперь у вас только', zerno, 'ед. зерна.')
        elif dis_name == 'нашествие саранчи' or dis_name == 'засуха':
            crops = 0
            print('Вашим посевы были уничтожены. Они не принесут зерна в следующем году.')
        else:
            narod -= int(narod * float(dis_cost))
            print('Погибло множество ваших людей. От вашего народа осталось только', narod, 'чел.')
        print('')
        print('<<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>>')
        print('')

    def ask_event():
        global kazna
        global love
        ask_ans = ''
        if god <= 4:
            ask_cost = random.randint(1000, 4000)
        else:
            ask_cost = random.randint(3000, 7000)
        ask_name = random.choice(['Крестьяне', 'Рабочие', 'Торговцы', 'Священнослужители'])
        if ask_name == 'Крестьяне':
            ask_want = random.choice(['удобрения', 'новое оборудование', 'качественные семена для посева'])
            ask_do = 'купить'
        if ask_name == 'Рабочие':
            ask_want = random.choice(['новое оборудование', 'качественные станки', 'дорогостоящие инструменты'])
            ask_do = 'купить'
        if ask_name == 'Торговцы':
            ask_want = random.choice(['торгового каравана', 'торговых путей'])
            ask_do = 'заплатить наемникам для охраны'
        if ask_name == 'Священнослужители':
            ask_want = random.choice(['внеплановое богослужение', 'важный религиозный праздник'])
            ask_do = 'провести'
        print(ask_name+' вашего королевства просят у вас', ask_cost, 'золотых для того, чтобы '+ask_do+' '+ask_want+'.')
        print('Дать деньги?')
        while ask_ans != 'да' and ask_ans != 'нет':
            print('Введите "да" или "нет" (без кавычек).')
            ask_ans = input('')
        if ask_ans == 'да' and kazna >= ask_cost:
            kazna -= ask_cost
            love += 4
            print('Вы согласились заплатить деньги, чтобы '+ask_do+' '+ask_want+'. '+ask_name+' благодарны вам.')
            print('Теперь у вас', kazna, 'золотых и', love, 'народной лояльности.')
        elif ask_ans == 'нет':
            love -= 15
            print('Вы отказались заплатить деньги, чтобы '+ask_do+' '+ask_want+'. '+ask_name+' возмущены.')
            print('Расположение народа ухудшилось. Теперь у вас', love, 'народной лояльности.')
        else:
            love -= 10
            print('Вам не хватает денег, чтобы '+ask_do+' '+ask_want+'. '+ask_name+' недовольны.')
            print('Расположение народа ухудшилось. Теперь у вас', love, 'народной лояльности.')
        print('')
        print('<<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>>')
        print('')

    def aggro_event():
        army = 0
        global kazna
        global land
        global love
        global narod
        global god
        aggro_ans = ''
        army_cost = 40
        army_rec = ''
        peace_goldcost = random.randint(int(god/3)*1000, int(god/3)*2000)
        peace_landcost = int(land*0.1)
        print('Пришли тревожные вести с окраинных деревень. На вас напало соседнее королевство.')
        print('Вы можете объявить набор в армию, чтобы дать врагу отпор. (не рекомендуется на ранних стадиях игры)')
        print('Чтобы снарядить одного солдата, вам нужен 1 человек из народа и', army_cost, 'золотых.')
        if kazna >= narod * army_cost:
            print('Сейчас вы можете снарядить максимум', narod, 'солдат за', narod*army_cost, 'золотых.')
        else:
            print('Сейчас вы можете снарядить максимум', math.floor(kazna/army_cost), 'солдат за',
                  math.floor(kazna/army_cost)*army_cost, 'золотых.')
        print('Чем больше солдат у вас будет, тем выше шанс победы.')
        print('Чтобы избежать конфликта, вы можете подписать мирный договор.')
        print('Для этого вам нужно', peace_goldcost, 'золотых. Также вам придется отдать', peace_landcost, 'ед. земли.')
        print('Вы также можете попробовать подписать договор, не имея нужного количества средств.')
        while aggro_ans != 'война' and aggro_ans != 'мир':
            print('Введите "война", чтобы начать военные действия, или "мир", чтобы подписать мирный договор.')
            aggro_ans = input('')
        if aggro_ans == 'война':
            print('Сколько солдат из народа набрать?')
            while army_rec.isdigit() is False or int(army_rec) < 0 or int(army_rec) > narod \
                    or int(army_rec)*army_cost > kazna:
                if kazna >= narod*army_cost:
                    print('Введите число от 0 до', narod)
                else:
                    print('Введите число от 0 до', math.floor(kazna/army_cost))
                army_rec = input('')
            army_rec = int(army_rec)
            kazna -= army_rec*army_cost
            narod -= army_rec
            print('Вы завербовали', army_rec, 'солдат. Теперь у вас', kazna, 'золотых.')
            print('После войны оставшиеся солдаты вернутся к мирной жизни.')
            print('Чтобы начать военные действия, нажмите Enter.')
            input('')
            print('>< >< >< >< >< >< >< >< >< >< >< >< >< >< >< ><')
            win_chance = random.randint(army - 30, army + 30)
            if win_chance >= 150:
                land += random.randint(10, 50)
                army = army - int(0.2 * army)
                love += 20
                narod += army
                print('Ваша армия нанесла сокрушительное поражение врагу. Празднуйте свою победу!')
                print('Вы захватили часть земель противника. Теперь у вас', land, 'ед. земли.')
                print('К сожалению, некоторые солдаты не вернулись с поля боя. У вас осталось', narod, 'человек.')
                print('Благодаря победе боевой дух ваших людей увеличился. Теперь у вас', love, 'народной лояльности.')
            elif win_chance >= 120:
                army = army - int(0.2 * army)
                narod += army
                print('Ваши войска долго и упорно сражались, но, как и войска противника, не добились успеха.')
                print('Вы с противником сошлись на том, что ваши силы равны и воевать дальше не имеет смысла.')
                print('К сожалению, некоторые солдаты не вернулись с поля боя. У вас осталось', narod, 'человек.')
            else:
                army = army - int(0.3 * army)
                narod += army
                kazna_loss = int(0.3 * kazna)
                kazna -= kazna_loss
                land_loss = int(0.3 * land)
                land -= land_loss
                love -= 30
                print('Ваша армия потерпела поражение на поле боя.')
                print('Чтобы не потерять свое королевство, вам пришлось подписать мирный довор на невыгодных условиях.')
                print('Вы потеряли', land_loss, 'ед. земли и', kazna_loss, 'золотых.')
                print('Теперь у вас', land, 'ед. земли и', kazna, 'золотых.')
                print('К сожалению, некоторые солдаты не вернулись с поля боя. У вас осталось', narod, 'человек.')
                print('Ваш народ в отчаянии. Теперь у вас', love, 'народной лояльности.')
        if aggro_ans == 'мир' and kazna >= peace_goldcost:
            print('Вы подписали мирный договор.')
            print('Вы заплатили', peace_goldcost, 'золотых. Также вам пришлось отдать', peace_landcost, 'ед. земли.')
            kazna -= peace_goldcost
            land -= peace_landcost
            print('Теперь у вас', land, 'ед. земли и', kazna, 'золотых.')
        elif aggro_ans == 'мир':
            print('К сожалению, вам не хватило денег, чтобы подписать мирный договор.')
            kazna = 0
            land -= peace_landcost
            love -= 30
            print('Вы потеряли все свои деньги и часть территории. Теперь у вас', land, 'ед. земли.')
            print('Враг победным маршем прошел по вашей стране, показывая свое превосходство.')
            print('Ваш народ морально подавлен. Теперь у вас', love, 'народной лояльности.')
        print('')
        print('<<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>>')
        print('')

    def wifechar_event():
        global love
        global married
        global country
        love += 5
        print('Ваша жена '+married+' провела ряд благотворительных акций в пользу простого народа.')
        print('Люди королевства '+country+' любят ее, и, соответственно, вас.')
        print('Теперь у вас', love, 'народной лояльности.')
        print('')
        print('<<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>>')
        print('')

    def wifelove_event():
        global narod
        global country
        global zerno
        global married
        wifelove_gained = random.randint(10, 30)
        wifelove_cost = random.randint(50, 100)
        wifelove_ans = 0
        print('Ваша жена '+married+' просит вас приютить в стране '+country+' беженцев из умирающего государства.')
        print('"Дорогой '+name+', этим бедным людям нужна наша помощь! Дай им немного еды, и они будут жить здесь."')
        print(married+' просит вас дать беженцам', wifelove_cost, 'ед. зерна. У вас есть', zerno, 'ед. зерна.')
        while wifelove_ans != 'да' and wifelove_ans != 'нет':
            print('Введите "да", чтобы поделиться едой, и "нет", чтобы отказаться от беженцев.')
            wifelove_ans = input('')
        if wifelove_ans == 'да' and wifelove_cost <= zerno:
            zerno -= wifelove_cost
            narod += wifelove_gained
            print('Вы соогласились принять беженцев. Теперь у вас', narod, 'людей и', zerno, 'ед. зерна.')
        elif wifelove_ans == 'нет':
            print('Вы отказались принять беженцев. '+married+' расстроена.')
        else:
            print('К сожалению, вы не смогли помочь беженцам, так как у вас не было достаточно еды.')
        print('')
        print('<<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>>')
        print('')

    god = god + 1

    if god != 1:
        print('')
        print('HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH')
        print('<<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>>')
        print('HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH')
        print('')
        print('Наступает', god, 'год вашего правления в государстве '+country+'. Ваши ресурсы:')
        print('Население:', narod, 'человек')
        if crops != '' and god != 1:
            zerno += crops * 2
            print('Прошлогодние посевы принесли вам', crops * 2, 'пшеницы.')
        crops = 0
        print('Запасы еды:', zerno, 'ед. зерна')
        print('Деньги:', kazna, ' золотых')
        print('Размер государства:', land)
        print('Лояльность народа:', love)
        print('Нажмите Enter.')
        input('')
        print('')
        print('<<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>>')
        print('')

    wifechar_chance = random.randint(1, 5)
    if wifechar_chance == 1 and married != 0:
        wifechar_event()

    wifelove_chance = random.randint(1, 4)
    if wifelove_chance == 1 and married != 0:
        wifelove_event()

    kingdom_name = random.choice(['Ольсвейр', 'Морровинг', 'Серотопье', 'Миродил', 'Ватмора'])
    price = random.randint(5, 15)
    print('Ваш сосед из королевства', kingdom_name, 'хочет купить у вас зерно по', price, 'зол. за единицу.')
    print('У вас есть', zerno, ' ед. зерна. Сколько вы хотите ему продать?')
    sell = input('')
    if sell == '':
        print('Вы решили ничего не продавать.')
    else:
        while sell.isdigit() is False or int(sell) < 0 or int(sell) > zerno:
            print('Вам нужно ввести число от 0 до', zerno)
            sell = input('')
        sell = int(sell)
        zerno -= sell
        kazna += sell * price
        print('Вы продали', sell, 'ед. зерна. Теперь у вас', zerno, 'ед. зерна и', kazna, 'золотых.')
    print('')
    print('<<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>>')
    print('')

    kingdom_name = random.choice(['Арена', 'Баггерфолл', 'Хаммерхелл', 'Акабир', 'Йокуда'])
    price = random.randint(5, 15)
    flower = random.choice(['рожь', 'пшеница', 'овес', 'ячмень', 'рис', 'просо', 'гречиха'])
    print('У королевства', kingdom_name, 'есть', flower, 'на продажу по цене', price, 'зол. за ед. зерна.')
    print('У вас есть', kazna, 'золотых и', zerno, ' ед. зерна. Сколько вы хотите купить?')
    buy = input('')
    if buy == '':
        print('Вы решили ничего не покупать.')
    else:
        while buy.isdigit() is False or int(buy) < 0 or int(buy) > math.floor(kazna/price):
            print('Введите число от 0 до', math.floor(kazna/price))
            buy = input('')
        buy = int(buy)
        zerno += buy
        kazna -= buy * price
        print('Вы купили', buy, 'ед. зерна. Теперь у вас', zerno, 'ед. зерна и', kazna, 'золотых.')
    print('')
    print('<<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>>')
    print('')

    wifechar_chance = random.randint(1, 5)
    if wifechar_chance == 1 and married != 0:
        wifechar_event()

    print('Ваши крестьяне собираются сеять зерно.')
    print('У вас есть', land, 'ед. земли и', zerno, 'зерна. Сколько зерна посеять (на 1 ед. земли - 1 ед. зерна)?')
    crops = input('')
    if crops == '':
        print('Вы решили не сеять зерно в этом году.')
    else:
        while crops.isdigit() is False or int(crops) > zerno or int(crops) > land or int(crops) < 0:
            print('Вам нужно ввести подходящее число. У вас только', zerno, 'ед. зерна и ', land, 'ед. земли.')
            crops = input('')
        crops = int(crops)
        zerno -= crops
        print('Вы посеяли', crops, 'ед. зерна. Пшеница созреет в следующем году.')
    print('')
    print('<<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>>')
    print('')

    disaster_chance = random.randint(1, 5)
    if disaster_chance == 1:
        disaster_event()
        rescheck()

    if land < 30 or narod < 30 or love < 20:
        break

    print('Поскольку все запасы еды у вас, ваш долг - кормить свой народ. 1-му человеку нужна 1 ед. зерна в год.')
    print('На данный момент у вас', zerno, 'ед. зерна и', narod, 'голодных людей.')
    print('Сколько зерна вы хотите раздать?')
    feed = input('')
    if feed == '':
        feed = 0
        love -= 60
        narod = int(narod / 2)
        print('Вы отказались кормить народ, из-за чего часть людей восстала, а часть погибла от голода.')
        print('Теперь у вас', zerno, 'ед. зерна,', narod, 'людей и', love, 'народной лояльности.')
    else:
        while feed.isdigit() is False or int(feed) < 0 or int(feed) > zerno:
            print('Введите число от 0 до', zerno)
            feed = input('')
        feed = int(feed)
        if feed == 0:
            love -= 60
            narod = int(narod / 2)
            print('Вы отказались кормить народ, из-за чего часть людей восстала, а часть погибла от голода.')
            print('Теперь у вас', zerno, 'ед. зерна,', narod, 'людей и', love, 'народной лояльности.')
        else:
            tempnarod = narod
            zerno -= feed
            love += int(((feed - narod) / narod) * 3)
            narod += int((feed - narod) / 4)
            if tempnarod == narod:
                print('Вы полностью накормили население. Ваши люди могут продолжать жить и работать.')
                print('Теперь у вас', zerno, 'ед. зерна,', narod, 'людей и', love, 'народной лояльности.')
            elif tempnarod > narod:
                print('Вы дали людям слишком мало еды. Из-за этого часть людей погибло от голода. Народ взволнован.')
                print('Теперь у вас', zerno, 'ед. зерна,', narod, 'людей и', love, 'народной лояльности.')
            elif tempnarod < narod:
                print('Вы дали людям много еды. Они сыты и довольны. Благодаря этому население увеличилось.')
                print('Теперь у вас', zerno, 'ед. зерна,', narod, 'людей и', love, 'народной лояльности.')
    print('')
    print('<<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>>')
    print('')

    if land < 30 or narod < 30 or love < 20:
        break

    rescheck()

    ask_chance = random.randint(1, 4)
    if ask_chance == 1:
        ask_event()
        rescheck()

    if land < 30 or narod < 30 or love < 20:
        break

    marryeve = random.randint(1, 2)
    if marryeve == 1:
        if married == 0:
            wedding = 0
            marryevent = random.randint(1, 10)
            if marryevent == 1:
                wife_name = 'Лидия'
                wife_desc1 = 'Это девушка примерно вашего возраста. Вы находите с ней множество общих тем для разговоров. '
                wife_desc2 = 'Вас привлекает ее сдержанность, она гораздо разумнее многих своих ровесниц.'
                wife_price = 2500
            if marryevent == 2:
                wife_name = 'Астрид'
                wife_desc1 = 'Впервые вы познакомились с ней еще будучи бедняком. Она была очень рада видеть вас. '
                wife_desc2 = 'Девушка рассказывает вам о ее нелегкой жизни и о том, что она совсем недавно потеряла мужа.'
                wife_price = 2500
            if marryevent == 3:
                wife_name = 'Иордис'
                wife_desc1 = 'Она дочь обедневшего феодала, вынужденного искать ей жениха, который бы смог содержать ее. '
                wife_desc2 = 'Девушка не обладает выдающимися качествами, однако она скромна и прилежна.'
                wife_price = 3000
            if marryevent == 4:
                wife_name = 'Жанна'
                wife_desc1 = 'Младшая дочь знаменитого военноначальника, она известна своей твердостью и честностью. '
                wife_desc2 = 'Девушка обожает военное дело и все, что с ним связано.'
                wife_price = 4000
            if marryevent == 5:
                wife_name = 'Эвелинн'
                wife_desc1 = 'Это одна из многих дочерей соседствующего с вами графа. Она живет мыслью о скором замужестве. '
                wife_desc2 = 'Несмотря на свою легкомысленность, Эвелинн не может не очаровывать своей ангельской внешностью.'
                wife_price = 5000
            if marryevent == 6:
                wife_name = 'Орианна'
                wife_desc1 = 'Орианна молодая и красивая женщина, пережившая уже трех своих мужей. '
                wife_desc2 = 'Несмотря на три коротких брака, она успела родить двух здоровых дочерей.'
                wife_price = 6000
            if marryevent == 7:
                wife_name = 'Мэри'
                wife_desc1 = 'Мэри обожает кошек, церковь и своего отца - крупного феодала. Она мечтает найти себе принца. '
                wife_desc2 = 'Проблемы с лишним весом не мешают Мэри искать принца, разъезжая по соседним королевствам.'
                wife_price = 7000
            if marryevent == 8:
                wife_name = 'Екатерина'
                wife_desc1 = 'Екатерина - одна из многочисленных незаконнорожденных дочерей великого князя. '
                wife_desc2 = 'У Екатерины острый подбородок, острая талия и еще более острый язык.'
                wife_price = 8000
            if marryevent == 9:
                wife_name = 'Азара'
                wife_desc1 = 'Молодая, прекрасная и образованная, принцесса Ольсвейра известна своей недоступностью. '
                wife_desc2 = 'Многие хотели взять ее в жены, но она ни разу не давала согласия.'
                wife_price = 12000
            if marryevent == 10:
                wife_name = 'Мавен'
                wife_desc1 = 'Мавен взрослая и самодостаточная принцесса королевства Рифген. Она необычайно умна для женщины. '
                wife_desc2 = 'Барды всех королевств превозносят ее красоту и харизму в своих песнях.'
                wife_price = 15000
            print('Вы все больше задумываетесь о том, насколько вы одиноки. Подобные мысли заставляют вас грустить.')
            print('К счастью, волей судьбы вы встречаете даму по имени '+wife_name+'.')
            print(wife_desc1)
            print(wife_desc2)
            print('Сделаете ли вы ей предложение?')
            while wedding != 'да' and wedding != 'нет':
                print('Введите "да" или "нет" (без кавычек).')
                wedding = input('')
            if wedding == 'да' and kazna >= wife_price:
                kazna -= wife_price
                married = wife_name
                print(wife_name+' согласилась выйти за вас. Теперь она живет с вами в '+country+'.')
                print('Вам пришлось потратить', wife_price, 'для свадьбы, зато вы больше не чувствуете себя одиноким.')
                print('Начинается ваша новая жизнь в браке с женщиной по имени '+wife_name+'.')
            elif wedding == 'нет':
                print('Вы решили не делать предложение даме по имени '+wife_name+'.')
            else:
                print('К сожалению, '+wife_name+' отказала вам, сказав, что вы с ней пока не можете быть вместе.')
                print('Не отчаивайтесь, вы сможете попытать удачу в другой раз.')
                print('СОВЕТ: копите деньги. Женщины любят их больше, чем кто-либо другой.')
            print('')
            print(
                '<<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>>')
            print('')
            rescheck()

    wifechar_chance = random.randint(1, 5)
    if wifechar_chance == 1 and married != 0:
        wifechar_event()

    aggro_chance = random.randint(1, 5)
    if aggro_chance == 1 and god >= 3:
        aggro_event()
        rescheck()

    if land < 30 or narod < 30 or love < 20:
        break

    ask_chance = random.randint(1, 4)
    if ask_chance == 1:
        ask_event()
        rescheck()

    if land < 30 or narod < 30 or love < 20:
        break

    scanswer = 0
    scland = 0
    sccrops = 0
    sckazna = 0
    sclove = 0
    scienceevent = random.randint(1, 5)
    scluck = random.randint(1, 3)
    if scienceevent == 1:
        scinventor = 'географ'
        scprice = random.randint(7500, 10000)
        scland = random.randint(20, 40)
        sctext = 'он будет исследовать для вас новые земли.'
        sctemp = 'Территория государства '+country+' увеличилась.'
    if scienceevent == 2:
        scinventor = 'моряк'
        scprice = random.randint(15000, 20000)
        scland = random.randint(50, 100)
        sctext = 'он будет исследовать моря и океаны под вашим флагом.'
        sctemp = 'Территория государства '+country+' значительно увеличилась.'
    if scienceevent == 3 and crops != 0 and crops != '':
        scinventor = 'агроном'
        scprice = random.randint(1000, 5000)
        sccrops = random.randint(75, 150)
        sctext = 'он сможет разработать эффективные удобрения для ваших посевов.'
        sctemp = 'Ваши посевы принесут больше зерна в следующем году.'
    elif scienceevent == 3:
        scinventor = 'алхимик'
        scprice = random.randint(1000, 5000)
        sckazna = scprice * 2
        sctext = 'он обещает удвоить отданное вами золото с помощью магического камня.'
        sctemp = 'Ваши запасы золота увеличились.'
    if scienceevent == 4:
        scinventor = 'алхимик'
        scprice = random.randint(1000, 5000)
        sckazna = scprice * 2
        sctext = 'он обещает удвоить отданное вами золото с помощью магического камня.'
        sctemp = 'Ваши запасы золота увеличились.'
    if scienceevent == 5:
        scinventor = 'бард'
        scprice = random.randint(3000, 7000)
        sclove = random.randint(10, 50)
        sctext = 'ваше имя будет превозноситься в его песнях.'
        sctemp = 'Ваша слава увеличилась. Народ стал любить вас больше.'
    print('Сегодня к вам пришел '+scinventor+'. За скромную плату в', scprice, ''+sctext)
    print('У вас сейчас', kazna, 'золотых. Заплатить деньги?')
    while scanswer != 'да' and scanswer != 'нет':
        print('Введите "да" или "нет" (без кавычек).')
        scanswer = input('')
    if scanswer == 'да' and scprice <= kazna:
        kazna -= scprice
        if scluck == 1 or scluck == 2:
            land += scland
            crops += sccrops
            kazna += sckazna
            love += sclove
            print('Исследование прошло успешно! '+sctemp)
        if scluck == 3:
            print('Ваш доверенный '+scinventor+' так и не вернулся. И ваши деньги тоже.')
    elif scanswer == 'да' and scprice > kazna:
        print('К сожалению, у вас недостаточно золота для '+scinventor+'а.')
    elif scanswer == 'нет':
        print('Вы отказались от услуг '+scinventor+'а.')
    print('')
    print('<<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>>')
    print('')

    rescheck()

    wifechar_chance = random.randint(1, 5)
    if wifechar_chance == 1 and married != 0:
        wifechar_event()

    aggro_chance = random.randint(1, 5)
    if aggro_chance == 1 and god >= 3:
        aggro_event()
        rescheck()

    if land < 30 or narod < 30 or love < 20:
        break

    disaster_chance = random.randint(1, 5)
    if disaster_chance == 1:
        disaster_event()
        rescheck()

    wifelove_chance = random.randint(1, 4)
    if wifelove_chance == 1 and married != 0:
        wifelove_event()

    if land < 30 or narod < 30 or love < 20:
        break

print('')
print('____________________________________________________________________________________________________')
print('<<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>>')
print('****************************************************************************************************')
print('')

if god % 10 == 1:
    godend = 'год'
elif god % 10 == 2 or god % 10 == 3 or god % 10 == 4:
    godend = 'года'
else:
    godend = 'лет'
print(name+' правил', god, ''+godend+'. Но ни один король не правит вечно...')

if endgame == 0:
    if love < 20:
        print('Вы так сильно испортили отношения с собственным народом, что даже женщины и дети приняли участие'
              'в восстании против вас.')
        print('Ваша голова теперь украшает забор вокруг замка королевства '+country+'.')
    elif narod < 30:
        print('В королевстве '+country+' остались единицы людей. Вы больше не можете сопротивляться нашествиям'
                                       'из других стран.')
        if married == 0:
            print('Ваши люди сами сбежали к соседнему королю. Вы последний человек в своем королевстве.')
        else:
            print('Ваши люди сами сбежали к соседнему королю. Даже ваша жена '+married+' оставила вас.'
                  'Вы последний человек в своем королевстве.')
    elif land < 30:
        print('У вас остались жалкие гектары земли. Никто больше не воспринимает'+country+'как суверенное государство.')
        print('Вам пришлось стать полностью зависимым от соседнего короля.')

print('')
print('****************************************************************************************************')
print('<<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>>')
print('____________________________________________________________________________________________________')
print('')

print('СПАСИБО ЗА ИГРУ, '+name+'!')
