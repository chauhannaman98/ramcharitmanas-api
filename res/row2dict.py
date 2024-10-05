def row2dict(row):
    d = {}
    for column in row.__table__.columns:
        d[column.name] = str(getattr(row, column.name))

    translation_list = []
    for translation in row.translations:
        t_dict = {}
        t_dict["language"] = translation.__dict__["language"]
        t_dict["id"] = translation.__dict__["id"]
        t_dict["translation"] = translation.__dict__["translation"]
        translation_list.append(t_dict)

    d["translations"] = translation_list

    return d