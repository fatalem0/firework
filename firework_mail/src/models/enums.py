import enum

class userTypeEnum(enum.Enum):
    client = "Клиент"
    employer = "Сотрудник"
    def __str__(self):
        if self is not None:
            return self.value
        else:
            return self

class statusEnum(enum.Enum):
    new = "NEW"
    failed_val = "VALIDATION FAILED"
    success_val = "VALIDATION SUSSESS"
    active = "ACTIVE"
    blocked = "BLOCKED"
    archive = "ARCHIVE"
    def __str__(self):
        if self is not None:
            return self.value
        else:
            return self


class sexEnum(enum.Enum):
    male = "Мужской"
    female = "Женский"
    def __str__(self):
        if self is not None:
            return self.value
        else:
            return self


class clientTypeEnum(enum.Enum):
    patient = "Пациент"
    staff = "Мед.Персонал"
    relatives = "Родственники"
    def __str__(self):
        if self is not None:
            return self.value
        else:
            return self


class stagesEnum(enum.Enum):
    justDiagnosed = "Только поставлен диагноз"
    cure = "Лечение"
    therapy = "Поддерживающая терапия"
    remission = "Ремиссия"
    palliativeCare = "Паллеотивное лечение"
    staff = "Я мед.персонал"
    def __str__(self):
        if self is not None:
            return self.value
        else:
            return self


class experienceTypeEnum(enum.Enum):
    positive = "Положительный"
    neutral = "Нейтральный"
    negative = "Отрицательный"
    def __str__(self):
        if self is not None:
            return self.value
        else:
            return self
        

class statusConsultationEnum(enum.Enum):
    first = "Первичная"
    second = "Вторичная"
    def __str__(self):
        if self is not None:
            return self.value
        else:
            return self
        

class copeWithSleepDisturbancesEnum(enum.Enum):
    bySelf = "Cправляется с нарушением сна самостоятельно"
    withMedicine = "Справляется с нарушением сна с помощью медикаментов"
    cantСope = "Не справляется с нарушением сна"
    def __str__(self):
        return self.name
        

class appetiteDisordersEnum(enum.Enum):
    increased = "Повышен"
    decreased = "Снижен"
    def __str__(self):
        return self.name
        

class validationStatusEnum(enum.Enum):
    blueprint = "Черновик"
    validated = "Провалидировано"
    def __str__(self):
        if self is not None:
            return self.value
        else:
            return self


class stressLevelEnum(enum.Enum):
    green = "Зеленый"
    yellow = "Желтый"
    red = "Красный"
    def __str__(self):
        if self is not None:
            return self.value
        else:
            return self

    
class questionTypeEnum(enum.Enum):
    radio = "Radio Button"
    checkbox = "Checkbox"
    select = "Selector"
    text = "Text"
    def __str__(self):
        if self is not None:
            return self.value
        else:
            return self


class chanelTypeEnum(enum.Enum):
    telegramm = "Телеграмм"
    mail = "Почта"
    def __str__(self):
        if self is not None:
            return self.value
        else:
            return self
        
class sendingStatusEnum(enum.Enum):
    send = "Успех"
    not_send = "Неуспех"
    def __str__(self):
        if self is not None:
            return self.value
        else:
            return self
