from speaking_clubs.models import Chat, Stream, Group, Level


def main():
    levels = ["A1", "A2", "B1"]
    times = ["18", "19", "20"]
    weeks = ["Вторник - Четверг", "Вторник - Пятница"]

    ch_num = 0
    gr_num = 0

    reser = Stream.objects.filter(name="Занято").first()
    cur_stream = Stream.objects.filter(name="21 поток").first()

    if not all((reser, cur_stream)):
        print(f"{reser=} {cur_stream=}")
        return

    for chat in Chat.objects.all():
        chat.stream = reser
        chat.save()

    for level in levels:
        for time in times:
            for week in weeks:
                if level == "A1" and time == "18" and week == "Вторник - Четверг":
                    gr = Group.objects.filter(
                        level__name=level, weekdays=week, time=time
                    ).first()
                    if not gr:
                        print(f"not gr {level} {time} {week}")
                        return
                    gr_num += 1
                    urls = [
                        "https://t.me/+pxCN_-Mlyj0wOWMy",
                        "https://t.me/+7tooEEHH-_dmNDQy",
                        "https://t.me/+YNnOXQRFGhc3YjQy",
                    ]
                    for url in urls:
                        ch = Chat.objects.filter(chat=url).first()
                        if not ch:
                            print(f"not ch '{level}' '{time}' '{week}' '{url}'")
                        if ch:
                            ch.stream = None
                            ch.group = gr
                            ch.save()
                            ch_num += 1

                if level == "A1" and time == "18" and week == "Вторник - Пятница":
                    gr = Group.objects.filter(
                        level__name=level, weekdays=week, time=time
                    ).first()
                    if not gr:
                        print(f"not gr {level} {time} {week}")
                        return
                    gr_num += 1
                    urls = [
                        "https://t.me/+V3hyl727fvxjYTMy",
                        "https://t.me/+Wtdc7WcAVrM1YjNi",
                        "https://t.me/+iJ8mRKlaA_o3OTRi",
                    ]
                    for url in urls:
                        ch = Chat.objects.filter(chat=url).first()
                        if not ch:
                            print(f"not ch '{level}' '{time}' '{week}' '{url}'")
                        if ch:
                            ch.stream = None
                            ch.group = gr
                            ch.save()
                            ch_num += 1

                if level == "A1" and time == "19" and week == "Вторник - Четверг":
                    gr = Group.objects.filter(
                        level__name=level, weekdays=week, time=time
                    ).first()
                    if not gr:
                        print(f"not gr {level} {time} {week}")
                        return
                    gr_num += 1
                    urls = [
                        "https://t.me/+beb50e_PTpNjYjZi",
                        "https://t.me/+DmzlCcJ7jZRmYjUy",
                        "https://t.me/+araxYPNxnP4yZDMy",
                    ]
                    for url in urls:
                        ch = Chat.objects.filter(chat=url).first()
                        if not ch:
                            print(f"not ch '{level}' '{time}' '{week}' '{url}'")
                        if ch:
                            ch.stream = None
                            ch.group = gr
                            ch.save()
                            ch_num += 1
                if level == "A1" and time == "19" and week == "Вторник - Пятница":
                    gr = Group.objects.filter(
                        level__name=level, weekdays=week, time=time
                    ).first()
                    if not gr:
                        print(f"not gr {level} {time} {week}")
                        return
                    gr_num += 1
                    urls = [
                        "https://t.me/+twVdCJeq7Vk2YjRi",
                        "https://t.me/+J45yW2I_pSw2Njhi",
                        "https://t.me/+vpYF6usMJck3ZTI6",
                    ]
                    for url in urls:
                        ch = Chat.objects.filter(chat=url).first()
                        if not ch:
                            print(f"not ch '{level}' '{time}' '{week}' '{url}'")
                        if ch:
                            ch.stream = None
                            ch.group = gr
                            ch.save()
                            ch_num += 1
                if level == "A1" and time == "20" and week == "Вторник - Четверг":
                    gr = Group.objects.filter(
                        level__name=level, weekdays=week, time=time
                    ).first()
                    if not gr:
                        print(f"not gr {level} {time} {week}")
                        return
                    gr_num += 1
                    urls = [
                        "https://t.me/+buexGPPbtd05NjRi",
                        "https://t.me/+4UPEltoTJEg2YWZi",
                        "https://t.me/+bAkEtQx5gIg0MTUy",
                    ]
                    for url in urls:
                        ch = Chat.objects.filter(chat=url).first()
                        if not ch:
                            print(f"not ch '{level}' '{time}' '{week}' '{url}'")
                        if ch:
                            ch.stream = None
                            ch.group = gr
                            ch.save()
                            ch_num += 1

                if level == "A1" and time == "20" and week == "Вторник - Пятница":
                    gr = Group.objects.filter(
                        level__name=level, weekdays=week, time=time
                    ).first()
                    if not gr:
                        print(f"not gr {level} {time} {week}")
                        return
                    gr_num += 1
                    urls = [
                        "https://t.me/+dJjhjuOFssQ2MmMy",
                        "https://t.me/+8ERMFQwDQl04Zjli",
                        "https://t.me/+DfuwoA_Kpcw1ZTFi",
                    ]
                    for url in urls:
                        ch = Chat.objects.filter(chat=url).first()
                        if not ch:
                            print(f"not ch '{level}' '{time}' '{week}' '{url}'")
                        if ch:
                            ch.stream = None
                            ch.group = gr
                            ch.save()
                            ch_num += 1

                if level == "A2" and time == "18" and week == "Вторник - Четверг":
                    gr = Group.objects.filter(
                        level__name=level, weekdays=week, time=time
                    ).first()
                    if not gr:
                        print(f"not gr {level} {time} {week}")
                        return
                    gr_num += 1
                    urls = [
                        "https://t.me/+h2RBCStzPd1jZTJi",
                        "https://t.me/+lvgpvq-tmbE4ZDUy",
                        "https://t.me/+S-7EUB8jmSY2MmYy",
                    ]
                    for url in urls:
                        ch = Chat.objects.filter(chat=url).first()
                        if not ch:
                            print(f"not ch '{level}' '{time}' '{week}' '{url}'")
                        if ch:
                            ch.stream = None
                            ch.group = gr
                            ch.save()
                            ch_num += 1

                if level == "A2" and time == "18" and week == "Вторник - Пятница":
                    gr = Group.objects.filter(
                        level__name=level, weekdays=week, time=time
                    ).first()
                    if not gr:
                        print(f"not gr {level} {time} {week}")
                        return
                    gr_num += 1
                    urls = [
                        "https://t.me/+sLIE2tdeomVlODli",
                        "https://t.me/+1CPJAjeffcRkYzEy",
                        "https://t.me/+DP9fjc3xDtJhZTM6",
                    ]
                    for url in urls:
                        ch = Chat.objects.filter(chat=url).first()
                        if not ch:
                            print(f"not ch '{level}' '{time}' '{week}' '{url}'")
                        if ch:
                            ch.stream = None
                            ch.group = gr
                            ch.save()
                            ch_num += 1

                if level == "A2" and time == "19" and week == "Вторник - Четверг":
                    gr = Group.objects.filter(
                        level__name=level, weekdays=week, time=time
                    ).first()
                    if not gr:
                        print(f"not gr {level} {time} {week}")
                        return
                    gr_num += 1
                    urls = [
                        "https://t.me/+VjoH6wH3_CxjZGRi",
                        "https://t.me/+Ak_H2qD_1UI4ODYy",
                        "https://t.me/+7m_zxHtF8UgxYjYy",
                    ]
                    for url in urls:
                        ch = Chat.objects.filter(chat=url).first()
                        if not ch:
                            print(f"not ch '{level}' '{time}' '{week}' '{url}'")
                        if ch:
                            ch.stream = None
                            ch.group = gr
                            ch.save()
                            ch_num += 1
                if level == "A2" and time == "19" and week == "Вторник - Пятница":
                    gr = Group.objects.filter(
                        level__name=level, weekdays=week, time=time
                    ).first()
                    if not gr:
                        print(f"not gr {level} {time} {week}")
                        return
                    gr_num += 1
                    urls = [
                        "https://t.me/+0Y4sXPoOwr40Yzcy",
                        "https://t.me/+USdyqxnU9IlhYzgy",
                        "https://t.me/+WuoicPRiSY0zNDNi ",
                    ]
                    for url in urls:
                        ch = Chat.objects.filter(chat=url).first()
                        if not ch:
                            print(f"not ch '{level}' '{time}' '{week}' '{url}'")
                        if ch:
                            ch.stream = None
                            ch.group = gr
                            ch.save()
                            ch_num += 1

                if level == "A2" and time == "20" and week == "Вторник - Четверг":
                    gr = Group.objects.filter(
                        level__name=level, weekdays=week, time=time
                    ).first()
                    if not gr:
                        print(f"not gr {level} {time} {week}")
                        return
                    gr_num += 1
                    urls = [
                        "https://t.me/+5s9dW4NUmdliMmQ6",
                        "https://t.me/+8TNlfe5HGTI2MzAy",
                        "https://t.me/+FOws-ybkRoRiOTgy",
                    ]
                    for url in urls:
                        ch = Chat.objects.filter(chat=url).first()
                        if not ch:
                            print(f"not ch '{level}' '{time}' '{week}' '{url}'")
                        if ch:
                            ch.stream = None
                            ch.group = gr
                            ch.save()
                            ch_num += 1

                if level == "A2" and time == "20" and week == "Вторник - Пятница":
                    gr = Group.objects.filter(
                        level__name=level, weekdays=week, time=time
                    ).first()
                    if not gr:
                        print(f"not gr {level} {time} {week}")
                        return
                    gr_num += 1
                    urls = [
                        "https://t.me/+KQ8drg-M0RUyN2Qy",
                        "https://t.me/+Gpq5_69flpdjMDBi",
                        "https://t.me/+fC8KI7MTt6wyYjMy",
                    ]
                    for url in urls:
                        ch = Chat.objects.filter(chat=url).first()
                        if not ch:
                            print(f"not ch '{level}' '{time}' '{week}' '{url}'")
                        if ch:
                            ch.stream = None
                            ch.group = gr
                            ch.save()
                            ch_num += 1
                if level == "B1" and time == "18" and week == "Вторник - Четверг":
                    gr = Group.objects.filter(
                        level__name=level, weekdays=week, time=time
                    ).first()
                    if not gr:
                        print(f"not gr {level} {time} {week}")
                        return
                    gr_num += 1
                    urls = [
                        "https://t.me/+_tHqpsvwGedhYzFi",
                        "https://t.me/+cB0TFI5v3Os2YjMy",
                    ]
                    for url in urls:
                        ch = Chat.objects.filter(chat=url).first()
                        if not ch:
                            print(f"not ch '{level}' '{time}' '{week}' '{url}'")
                        if ch:
                            ch.stream = None
                            ch.group = gr
                            ch.save()
                            ch_num += 1
                if level == "B1" and time == "18" and week == "Вторник - Пятница":
                    gr = Group.objects.filter(
                        level__name=level, weekdays=week, time=time
                    ).first()
                    if not gr:
                        print(f"not gr {level} {time} {week}")
                        return
                    gr_num += 1
                    urls = [
                        "https://t.me/+sB1pb4ZTtRdjN2Ey",
                        "https://t.me/+GyuC7L5Ax71iNmMy",
                    ]
                    for url in urls:
                        ch = Chat.objects.filter(chat=url).first()
                        if not ch:
                            print(f"not ch '{level}' '{time}' '{week}' '{url}'")
                        if ch:
                            ch.stream = None
                            ch.group = gr
                            ch.save()
                            ch_num += 1
                if level == "B1" and time == "19" and week == "Вторник - Четверг":
                    gr = Group.objects.filter(
                        level__name=level, weekdays=week, time=time
                    ).first()
                    if not gr:
                        print(f"not gr {level} {time} {week}")
                        return
                    gr_num += 1
                    urls = [
                        "https://t.me/+meSo3Y9HFZ1iYTcy",
                        "https://t.me/+_IQzWirqEmFmZTg6",
                    ]
                    for url in urls:
                        ch = Chat.objects.filter(chat=url).first()
                        if not ch:
                            print(f"not ch '{level}' '{time}' '{week}' '{url}'")
                        if ch:
                            ch.stream = None
                            ch.group = gr
                            ch.save()
                            ch_num += 1
                if level == "B1" and time == "19" and week == "Вторник - Пятница":
                    gr = Group.objects.filter(
                        level__name=level, weekdays=week, time=time
                    ).first()
                    if not gr:
                        print(f"not gr {level} {time} {week}")
                        return
                    gr_num += 1
                    urls = [
                        "https://t.me/+BI4kGYd-9tNjMGEy",
                        "https://t.me/+jFad35g9cdA2NzQ6",
                    ]
                    for url in urls:
                        ch = Chat.objects.filter(chat=url).first()
                        if not ch:
                            print(f"not ch '{level}' '{time}' '{week}' '{url}'")
                        if ch:
                            ch.stream = None
                            ch.group = gr
                            ch.save()
                            ch_num += 1
                if level == "B1" and time == "20" and week == "Вторник - Четверг":
                    gr = Group.objects.filter(
                        level__name=level, weekdays=week, time=time
                    ).first()
                    if not gr:
                        print(f"not gr {level} {time} {week}")
                        return
                    gr_num += 1
                    urls = [
                        "https://t.me/+TDWWXzRQhOo1NmJi",
                        "https://t.me/+Dt-X0HQYvz02ZTAy",
                    ]
                    for url in urls:
                        ch = Chat.objects.filter(chat=url).first()
                        if not ch:
                            print(f"not ch '{level}' '{time}' '{week}' '{url}'")
                        if ch:
                            ch.stream = None
                            ch.group = gr
                            ch.save()
                            ch_num += 1
                if level == "B1" and time == "20" and week == "Вторник - Пятница":
                    gr = Group.objects.filter(
                        level__name=level, weekdays=week, time=time
                    ).first()
                    if not gr:
                        print(f"not gr {level} {time} {week}")
                        return
                    gr_num += 1
                    urls = [
                        "https://t.me/+EzVXTuMs2iZkZWUy",
                        "https://t.me/+B5dcHp2vlfgxMjRi",
                    ]
                    for url in urls:
                        ch = Chat.objects.filter(chat=url).first()
                        if not ch:
                            print(f"not ch '{level}' '{time}' '{week}' '{url}'")
                        if ch:
                            ch.stream = None
                            ch.group = gr
                            ch.save()
                            ch_num += 1
    print(f"{ch_num=} {gr_num=}")


main()
