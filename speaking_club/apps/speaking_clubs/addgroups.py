from speaking_clubs.models import Chat, Stream, Group, Level, Teacher


def main():
    levels = ["A1", "A2", "B1"]
    times = ["18", "19", "20"]
    weeks = ["Среда - Суббота", "Среда - Пятница"]

    ch_num = 0
    gr_num = 0

    reser = Stream.objects.filter(name="Занято").first()
    cur_stream = Stream.objects.filter(name="24 поток").first()

    if not all((reser, cur_stream)):
        print(f"{reser=} {cur_stream=}")
        return

    for chat in Chat.objects.all():
        chat.stream = reser
        chat.save()

    for level in levels:
        for time in times:
            for week in weeks:
                if level == "A1" and time == "18" and week == "Среда - Суббота":
                    gr = Group.objects.filter(
                        level__name=level, weekdays=week, time=time
                    ).first()
                    if not gr:
                        print(f"not gr {level} {time} {week}")
                        return
                    gr_num += 1
                    urls = [
                        "https://t.me/+QOm9XKMXCtk0ZmJi",
                        "https://t.me/+vmpQpSDvgbE3ZGJi",
                    ]
                    for url in urls:
                        ch = Chat.objects.filter(chat=url).first()
                        if not ch:
                            print(f"not ch '{level}' '{time}' '{week}' '{url}'")
                            th = Teacher.objects.first()
                            ch = Chat.objects.create(chat=url, teacher=th, group=gr, stream=None)
                        if ch:
                            ch.stream = None
                            ch.group = gr
                            ch.save()
                            ch_num += 1

                if level == "A1" and time == "18" and week == "Среда - Пятница":
                    gr = Group.objects.filter(
                        level__name=level, weekdays=week, time=time
                    ).first()
                    if not gr:
                        print(f"not gr {level} {time} {week}")
                        return
                    gr_num += 1
                    urls = [
                        "https://t.me/+qj2xuDJxwLQ5Njhi",
                    ]
                    for url in urls:
                        ch = Chat.objects.filter(chat=url).first()
                        if not ch:
                            print(f"not ch '{level}' '{time}' '{week}' '{url}'")
                            th = Teacher.objects.first()
                            ch = Chat.objects.create(chat=url, teacher=th, group=gr, stream=None)
                        if ch:
                            ch.stream = None
                            ch.group = gr
                            ch.save()
                            ch_num += 1

                if level == "A1" and time == "19" and week == "Среда - Суббота":
                    gr = Group.objects.filter(
                        level__name=level, weekdays=week, time=time
                    ).first()
                    if not gr:
                        print(f"not gr {level} {time} {week}")
                        return
                    gr_num += 1
                    urls = [
                        "https://t.me/+Y9IvBI6Hg6wxYmRi",
                        "https://t.me/+GZKDg1qfh0EwNDY6",
                    ]
                    for url in urls:
                        ch = Chat.objects.filter(chat=url).first()
                        if not ch:
                            print(f"not ch '{level}' '{time}' '{week}' '{url}'")
                            th = Teacher.objects.first()
                            ch = Chat.objects.create(chat=url, teacher=th, group=gr, stream=None)
                        if ch:
                            ch.stream = None
                            ch.group = gr
                            ch.save()
                            ch_num += 1
                if level == "A1" and time == "19" and week == "Среда - Пятница":
                    gr = Group.objects.filter(
                        level__name=level, weekdays=week, time=time
                    ).first()
                    if not gr:
                        print(f"not gr {level} {time} {week}")
                        return
                    gr_num += 1
                    urls = [
                        "https://t.me/+twVdCJeq7Vk2YjRi",
                        "https://t.me/+UqiqwPN_srs4N2Fi",
                        "https://t.me/+qj2xuDJxwLQ5Njhi",
                    ]
                    for url in urls:
                        ch = Chat.objects.filter(chat=url).first()
                        if not ch:
                            print(f"not ch '{level}' '{time}' '{week}' '{url}'")
                            th = Teacher.objects.first()
                            ch = Chat.objects.create(chat=url, teacher=th, group=gr, stream=None)
                        if ch:
                            ch.stream = None
                            ch.group = gr
                            ch.save()
                            ch_num += 1
                if level == "A1" and time == "20" and week == "Среда - Суббота":
                    gr = Group.objects.filter(
                        level__name=level, weekdays=week, time=time
                    ).first()
                    if not gr:
                        print(f"not gr {level} {time} {week}")
                        return
                    gr_num += 1
                    urls = [
                        "https://t.me/+4UPEltoTJEg2YWZi",
                        "https://t.me/+bAkEtQx5gIg0MTUy",
                        "https://t.me/+jeHsl3GcdBAxNmYy",
                        "https://t.me/+rzCUEHqAQ_9lYTUy",
                    ]
                    for url in urls:
                        ch = Chat.objects.filter(chat=url).first()
                        if not ch:
                            print(f"not ch '{level}' '{time}' '{week}' '{url}'")
                            th = Teacher.objects.first()
                            ch = Chat.objects.create(chat=url, teacher=th, group=gr, stream=None)
                        if ch:
                            ch.stream = None
                            ch.group = gr
                            ch.save()
                            ch_num += 1

                if level == "A1" and time == "20" and week == "Среда - Пятница":
                    gr = Group.objects.filter(
                        level__name=level, weekdays=week, time=time
                    ).first()
                    if not gr:
                        print(f"not gr {level} {time} {week}")
                        return
                    gr_num += 1
                    urls = [
                        "https://t.me/+8ERMFQwDQl04Zjli",
                        "https://t.me/+fojSMuMXD3EwYmEy",
                        "https://t.me/+2ouz6kNTucVkODJi",
                    ]
                    for url in urls:
                        ch = Chat.objects.filter(chat=url).first()
                        if not ch:
                            print(f"not ch '{level}' '{time}' '{week}' '{url}'")
                            th = Teacher.objects.first()
                            ch = Chat.objects.create(chat=url, teacher=th, group=gr, stream=None)
                        if ch:
                            ch.stream = None
                            ch.group = gr
                            ch.save()
                            ch_num += 1

                if level == "A2" and time == "18" and week == "Среда - Суббота":
                    gr = Group.objects.filter(
                        level__name=level, weekdays=week, time=time
                    ).first()
                    if not gr:
                        print(f"not gr {level} {time} {week}")
                        return
                    gr_num += 1
                    urls = [
                        "https://t.me/+R1ZQI9pSWSoyYmNi",
                        "https://t.me/+aodt3iWsxzNlZTli",
                    ]
                    for url in urls:
                        ch = Chat.objects.filter(chat=url).first()
                        if not ch:
                            print(f"not ch '{level}' '{time}' '{week}' '{url}'")
                            th = Teacher.objects.first()
                            ch = Chat.objects.create(chat=url, teacher=th, group=gr, stream=None)
                        if ch:
                            ch.stream = None
                            ch.group = gr
                            ch.save()
                            ch_num += 1

                if level == "A2" and time == "18" and week == "Среда - Пятница":
                    gr = Group.objects.filter(
                        level__name=level, weekdays=week, time=time
                    ).first()
                    if not gr:
                        print(f"not gr {level} {time} {week}")
                        return
                    gr_num += 1
                    urls = [
                        "https://t.me/+1CPJAjeffcRkYzEy",
                        "https://t.me/+DP9fjc3xDtJhZTM6",
                        "https://t.me/+y2kdAOIfDqBjM2Iy",
                        "https://t.me/+ydghmw9ftaU4MDAy",
                    ]
                    for url in urls:
                        ch = Chat.objects.filter(chat=url).first()
                        if not ch:
                            print(f"not ch '{level}' '{time}' '{week}' '{url}'")
                            th = Teacher.objects.first()
                            ch = Chat.objects.create(chat=url, teacher=th, group=gr, stream=None)
                        if ch:
                            ch.stream = None
                            ch.group = gr
                            ch.save()
                            ch_num += 1

                if level == "A2" and time == "19" and week == "Среда - Суббота":
                    gr = Group.objects.filter(
                        level__name=level, weekdays=week, time=time
                    ).first()
                    if not gr:
                        print(f"not gr {level} {time} {week}")
                        return
                    gr_num += 1
                    urls = [
                        "https://t.me/+Ak_H2qD_1UI4ODYy",
                        "https://t.me/+7m_zxHtF8UgxYjYy",
                        "https://t.me/+e6DBIYm7tgI2YTky",
                        "https://t.me/+iF0UOJyefrM0NjQ6",
                    ]
                    for url in urls:
                        ch = Chat.objects.filter(chat=url).first()
                        if not ch:
                            print(f"not ch '{level}' '{time}' '{week}' '{url}'")
                            th = Teacher.objects.first()
                            ch = Chat.objects.create(chat=url, teacher=th, group=gr, stream=None)
                        if ch:
                            ch.stream = None
                            ch.group = gr
                            ch.save()
                            ch_num += 1
                if level == "A2" and time == "19" and week == "Среда - Пятница":
                    gr = Group.objects.filter(
                        level__name=level, weekdays=week, time=time
                    ).first()
                    if not gr:
                        print(f"not gr {level} {time} {week}")
                        return
                    gr_num += 1
                    urls = [
                        "https://t.me/+0Y4sXPoOwr40Yzcy",
                        "https://t.me/+WuoicPRiSY0zNDNi",
                        "https://t.me/+cV5nsUQ_2ytiNGEy",
                        "https://t.me/+_Q0pjizCm20yYzA6",
                    ]
                    for url in urls:
                        ch = Chat.objects.filter(chat=url).first()
                        if not ch:
                            print(f"not ch '{level}' '{time}' '{week}' '{url}'")
                            th = Teacher.objects.first()
                            ch = Chat.objects.create(chat=url, teacher=th, group=gr, stream=None)
                        if ch:
                            ch.stream = None
                            ch.group = gr
                            ch.save()
                            ch_num += 1

                if level == "A2" and time == "20" and week == "Среда - Суббота":
                    gr = Group.objects.filter(
                        level__name=level, weekdays=week, time=time
                    ).first()
                    if not gr:
                        print(f"not gr {level} {time} {week}")
                        return
                    gr_num += 1
                    urls = [
                        "https://t.me/+yWGx1LKZeBxlNjFi",
                        "https://t.me/+Lb0xGIWHAVxkOGZi",
                    ]
                    for url in urls:
                        ch = Chat.objects.filter(chat=url).first()
                        if not ch:
                            print(f"not ch '{level}' '{time}' '{week}' '{url}'")
                            th = Teacher.objects.first()
                            ch = Chat.objects.create(chat=url, teacher=th, group=gr, stream=None)
                        if ch:
                            ch.stream = None
                            ch.group = gr
                            ch.save()
                            ch_num += 1

                if level == "A2" and time == "20" and week == "Среда - Пятница":
                    gr = Group.objects.filter(
                        level__name=level, weekdays=week, time=time
                    ).first()
                    if not gr:
                        print(f"not gr {level} {time} {week}")
                        return
                    gr_num += 1
                    urls = [
                        "https://t.me/+KQ8drg-M0RUyN2Qy",
                        "https://t.me/+fC8KI7MTt6wyYjMy",
                        "https://t.me/+yWGx1LKZeBxlNjFi",
                        "https://t.me/+ryLCa-gUFFRmYzQ6",
                    ]
                    for url in urls:
                        ch = Chat.objects.filter(chat=url).first()
                        if not ch:
                            print(f"not ch '{level}' '{time}' '{week}' '{url}'")
                            th = Teacher.objects.first()
                            ch = Chat.objects.create(chat=url, teacher=th, group=gr, stream=None)
                        if ch:
                            ch.stream = None
                            ch.group = gr
                            ch.save()
                            ch_num += 1
                if level == "B1" and time == "18" and week == "Среда - Суббота":
                    gr = Group.objects.filter(
                        level__name=level, weekdays=week, time=time
                    ).first()
                    if not gr:
                        print(f"not gr {level} {time} {week}")
                        return
                    gr_num += 1
                    urls = [
                        "https://t.me/+cB0TFI5v3Os2YjMy",
                    ]
                    for url in urls:
                        ch = Chat.objects.filter(chat=url).first()
                        if not ch:
                            print(f"not ch '{level}' '{time}' '{week}' '{url}'")
                            th = Teacher.objects.first()
                            ch = Chat.objects.create(chat=url, teacher=th, group=gr, stream=None)
                        if ch:
                            ch.stream = None
                            ch.group = gr
                            ch.save()
                            ch_num += 1
                if level == "B1" and time == "18" and week == "Среда - Пятница":
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
                            th = Teacher.objects.first()
                            ch = Chat.objects.create(chat=url, teacher=th, group=gr, stream=None)
                        if ch:
                            ch.stream = None
                            ch.group = gr
                            ch.save()
                            ch_num += 1
                if level == "B1" and time == "19" and week == "Среда - Суббота":
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
                            th = Teacher.objects.first()
                            ch = Chat.objects.create(chat=url, teacher=th, group=gr, stream=None)
                        if ch:
                            ch.stream = None
                            ch.group = gr
                            ch.save()
                            ch_num += 1
                if level == "B1" and time == "19" and week == "Среда - Пятница":
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
                            th = Teacher.objects.first()
                            ch = Chat.objects.create(chat=url, teacher=th, group=gr, stream=None)
                        if ch:
                            ch.stream = None
                            ch.group = gr
                            ch.save()
                            ch_num += 1
                if level == "B1" and time == "20" and week == "Среда - Суббота":
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
                            th = Teacher.objects.first()
                            ch = Chat.objects.create(chat=url, teacher=th, group=gr, stream=None)
                        if ch:
                            ch.stream = None
                            ch.group = gr
                            ch.save()
                            ch_num += 1
                if level == "B1" and time == "20" and week == "Среда - Пятница":
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
                            th = Teacher.objects.first()
                            ch = Chat.objects.create(chat=url, teacher=th, group=gr, stream=None)
                        if ch:
                            ch.stream = None
                            ch.group = gr
                            ch.save()
                            ch_num += 1
    print(f"{ch_num=} {gr_num=}")


main()
