# (c) @JigarVarma2005

from EmojiCaptcha import Captcha as emoji_captcha
import random
from captcha.image import ImageCaptcha
import uuid

def emoji_() -> dict:
    maker = emoji_captcha().generate()
    emojis_list = ['🃏', '🎤', '🎥', '🎨', '🎩', '🎬', '🎭', '🎮', '🎯', '🎱', '🎲', '🎷', '🎸', '🎹', '🎾', '🏀', '🏆', '🏈', '🏉', '🏐', '🏓', '💠', '💡', '💣', '💨', '💸', '💻', '💾', '💿', '📈', '📉', '📊', '📌', '📍', '📎', '📏', '📐', '📞', '📟', '📠', '📡', '📢', '📣', '📦', '📹', '📺', '📻', '📼', '📽', '🖥', '🖨', '🖲', '🗂', '🗃', '🗄', '🗜', '🗝', '🗡', '🚧', '🚨', '🛒', '🛠', '🛢', '🧀', '🌭', '🌮', '🌯', '🌺', '🌻', '🌼', '🌽', '🌾', '🌿', '🍊', '🍋', '🍌', '🍍', '🍎', '🍏', '🍚', '🍛', '🍜', '🍝', '🍞', '🍟', '🍪', '🍫', '🍬', '🍭', '🍮', '🍯', '🍺', '🍻', '🍼', '🍽', '🍾', '🍿', '🎊', '🎋', '🎍', '🎏', '🎚', '🎛', '🎞', '🐌', '🐍', '🐎', '🐚', '🐛', '🐝', '🐞', '🐟', '🐬', '🐭', '🐮', '🐯', '🐻', '🐼', '🐿', '👛', '👜', '👝', '👞', '👟', '💊', '💋', '💍', '💎', '🔋', '🔌', '🔪', '🔫', '🔬', '🔭', '🔮', '🕯', '🖊', '🖋', '🖌', '🖍', '🥚', '🥛', '🥜', '🥝', '🥞', '🦊', '🦋', '🦌', '🦍', '🦎', '🦏', '🌀', '🌂', '🌑', '🌕', '🌡', '🌤', '⛅️', '🌦', '🌧', '🌨', '🌩', '🌰', '🌱', '🌲', '🌳', '🌴', '🌵', '🌶', '🌷', '🌸', '🌹', '🍀', '🍁', '🍂', '🍃', '🍄', '🍅', '🍆', '🍇', '🍈', '🍉', '🍐', '🍑', '🍒', '🍓', '🍔', '🍕', '🍖', '🍗', '🍘', '🍙', '🍠', '🍡', '🍢', '🍣', '🍤', '🍥', '🍦', '🍧', '🍨', '🍩', '🍰', '🍱', '🍲', '🍴', '🍵', '🍶', '🍷', '🍸', '🍹', '🎀', '🎁', '🎂', '🎃', '🎄', '🎈', '🎉', '🎒', '🎓', '🎙', '🐀', '🐁', '🐂', '🐃', '🐄', '🐅', '🐆', '🐇', '🐕', '🐉', '🐓', '🐖', '🐗', '🐘', '🐙', '🐠', '🐡', '🐢', '🐣', '🐤', '🐥', '🐦', '🐧', '🐨', '🐩', '🐰', '🐱', '🐴', '🐵', '🐶', '🐷', '🐸', '🐹', '👁\u200d🗨', '👑', '👒', '👠', '👡', '👢', '💄', '💈', '🔗', '🔥', '🔦', '🔧', '🔨', '🔩', '🔰', '🔱', '🕰', '🕶', '🕹', '🖇', '🚀', '🤖', '🥀', '🥁', '🥂', '🥃', '🥐', '🥑', '🥒', '🥓', '🥔', '🥕', '🥖', '🥗', '🥘', '🥙', '🦀', '🦁', '🦂', '🦃', '🦄', '🦅', '🦆', '🦇', '🦈', '🦉', '🦐', '🦑', '⭐️', '⏰', '⏲', '⚠️', '⚡️', '⚰️', '⚽️', '⚾️', '⛄️', '⛅️', '⛈', '⛏', '⛓', '⌚️', '☎️', '⚜️', '✏️', '⌨️', '☁️', '☃️', '☄️', '☕️', '☘️', '☠️', '♨️', '⚒', '⚔️', '⚙️', '✈️', '✉️', '✒️']
    r = random.random()
    random.shuffle(emojis_list, lambda: r)
    new_list = emojis_list[:20]
    for i in maker["answer"]:
        if i in new_list:
            new_list.remove(i)
    n_list = new_list[:9]
    for i in maker["answer"]:
        n_list.append(i)
    random.shuffle(n_list, lambda: r)
    maker.update({"list": n_list})
    return maker

def number_() -> dict:
    filename = "./cache/" + uuid.uuid4().hex + '.png'
    image = ImageCaptcha(width = 280, height = 140, font_sizes=[80,83])
    list_ = ["0","1","2","3","5","6","7","8","9"]
    captcha_number = set()
    while len(captcha_number) <= 3:
        captcha_number.add(random.choice(list_))
    final_number = ""
    for num in captcha_number:
        final_number += num
    image.write("   " + final_number, str(filename))
    try:
        data = {"answer":list(captcha_number),"captcha": filename}
    except Exception as t_e:
        print(t_e)
        data = {"is_error": True, "error":t_e}
    return data
