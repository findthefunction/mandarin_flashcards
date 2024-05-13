import random
import time
from dictionaries.updated_data import data


# # Define the dictionary of Mandarin characters/phrases, their frequencies, pinyin pronunciations, and examples of usage
# flash_cards = {
#     '你好': {'frequency': 10, 'pinyin': 'nǐ hǎo', 'example': '你好，李先生。', 'translation': 'Hello, Mr. Li.'},  # 'Hello'
#     '谢谢': {'frequency': 9, 'pinyin': 'xièxie', 'example': '谢谢你的帮助。', 'translation': 'Thank you for your help.'},   # 'Thank you'
#     '是': {'frequency': 8, 'pinyin': 'shì', 'example': '这是我的书。', 'translation': 'This is my book.'}, # 'Is'   
#     '不': {'frequency': 7, 'pinyin': 'bù', 'example': '我不是老师。', 'translation': 'I am not a teacher.'},  # 'No'
#     '好': {'frequency': 6, 'pinyin': 'hǎo', 'example': '这个东西很好。', 'translation': 'This thing is very good.'},  # 'Good'
#     '吗': {'frequency': 5, 'pinyin': 'ma', 'example': '你好吗？', 'translation': 'How are you?'},  # 'Question particle'
#     '我': {'frequency': 4, 'pinyin': 'wǒ', 'example': '我是学生。', 'translation:': 'I am a student.'},  # 'I'
#     '很': {'frequency': 3, 'pinyin': 'hěn', 'example': '我很好。', 'translation': 'I am very good.'},  # 'Very'
#     '也': {'frequency': 2, 'pinyin': 'yě', 'example': '我也是。', 'translation': 'Me too.'},  # 'Also'  
#     '和': {'frequency': 1, 'pinyin': 'hé', 'example': '我和你。', 'translation': 'You and me.'}, # 'And'
#     '再见': {'frequency': 1, 'pinyin': 'zàijiàn', 'example': '再见，李先生。', 'translation': 'Goodbye, Mr. Li.'},  # 'Goodbye'
#     '对不起': {'frequency': 1, 'pinyin': 'duìbuqǐ', 'example': '对不起，我迟到了。', 'translation': 'Sorry, I am late.'},  # 'Sorry'
#     '没关系': {'frequency': 1, 'pinyin': 'méiguānxi', 'example': '没关系，我不生气。', 'translation': 'It is okay, I am not angry.'},  # 'It is okay'
#     '请': {'frequency': 1, 'pinyin': 'qǐng', 'example': '请坐。', 'translation': 'Please sit down.'},  # 'Please'
#     '对': {'frequency': 1, 'pinyin': 'duì', 'example': '对不起。', 'translation': 'I am sorry.'},  # 'Correct'
#     '不客气': {'frequency': 1, 'pinyin': 'bùkèqì', 'example': '不客气，我很高兴帮助你。', 'translation': 'You are welcome, I am happy to help you.'},  # 'You are welcome'
#     '是的': {'frequency': 1, 'pinyin': 'shìde', 'example': '是的，我明白了。', 'translation': 'Yes, I understand.'},  # 'Yes'
#     '不是': {'frequency': 1, 'pinyin': 'bùshì', 'example': '不是，我不同意。', 'translation': 'No, I do not agree.'},  # 'No'
#     '可以': {'frequency': 1, 'pinyin': 'kěyǐ', 'example': '可以，我同意。', 'translation': 'Okay, I agree.'},  # 'Okay'
#     '他': {'frequency': 1, 'pinyin': 'tā', 'example': '他是我的朋友。', 'translation': 'He is my friend.'}, # 'He'
#     '她': {'frequency': 1, 'pinyin': 'tā', 'example': '她是我的妹妹。', 'translation': 'She is my sister.'}, # 'She'
#     '它': {'frequency': 1, 'pinyin': 'tā', 'example': '它是我的狗。', 'translation': 'It is my dog.'}, # 'It'
#     '这': {'frequency': 1, 'pinyin': 'zhè', 'example': '这是我的书。', 'translation': 'This is my book.'}, # 'This'
#     '那': {'frequency': 1, 'pinyin': 'nà', 'example': '那是我的车。', 'translation': 'That is my car.'}, # 'That'
#     '哪': {'frequency': 1, 'pinyin': 'nǎ', 'example': '哪是我的笔？', 'translation': 'Which is my pen?'}, # 'Which'
#     '人': {'frequency': 1, 'pinyin': 'rén', 'example': '他是一个好人。', 'translation': 'He is a good person.'}, # 'Person'
#     '年': {'frequency': 1, 'pinyin': 'nián', 'example': '我今年二十岁。', 'translation': 'I am twenty years old this year.'}, # 'Year'
#     '大': {'frequency': 1, 'pinyin': 'dà', 'example': '这是一个大苹果。', 'translation': 'This is a big apple.'}, # 'Big'
#     '小': {'frequency': 1, 'pinyin': 'xiǎo', 'example': '这是一个小苹果。', 'translation': 'This is a small apple.'}, # 'Small'
#     '多': {'frequency': 1, 'pinyin': 'duō', 'example': '我有很多书。', 'translation': 'I have many books.'}, # 'Many'
#     '少': {'frequency': 1, 'pinyin': 'shǎo', 'example': '我只有少数朋友。', 'translation': 'I only have a few friends.'}, # 'Few'
#     '现在': {'frequency': 1, 'pinyin': 'xiànzài', 'example': '现在是下午三点。', 'translation': 'It is three o\'clock in the afternoon now.'}, # 'Now'
#     '时间': {'frequency': 1, 'pinyin': 'shíjiān', 'example': '我没有时间。', 'translation': 'I don\'t have time.'}, # 'Time'
#     '点': {'frequency': 1, 'pinyin': 'diǎn', 'example': '现在是三点。', 'translation': 'It is three o\'clock now.'}, # 'O\'clock'
#     '去': {'frequency': 1, 'pinyin': 'qù', 'example': '我去学校。', 'translation': 'I go to school.'}, # 'Go'
#     '来': {'frequency': 1, 'pinyin': 'lái', 'example': '他来我家。', 'translation': 'He comes to my house.'}, # 'Come'
#     '上': {'frequency': 1, 'pinyin': 'shàng', 'example': '我上楼。', 'translation': 'I go upstairs.'}, # 'Up'
#     '下': {'frequency': 1, 'pinyin': 'xià', 'example': '我下楼。', 'translation': 'I go downstairs.'}, # 'Down'
#     '里': {'frequency': 1, 'pinyin': 'lǐ', 'example': '我在家里。', 'translation': 'I am at home.'}, # 'Inside'
#     '吃': {'frequency': 5, 'pinyin': 'chī', 'example': '我吃饭。', 'translation': 'I eat.'}, # 'Eat'
#     '喝': {'frequency': 4, 'pinyin': 'hē', 'example': '我喝水。', 'translation': 'I drink water.'}, # 'Drink'
#     '玩': {'frequency': 3, 'pinyin': 'wán', 'example': '我玩游戏。', 'translation': 'I play games.'}, # 'Play'
#     '看': {'frequency': 5, 'pinyin': 'kàn', 'example': '我看书。', 'translation': 'I read a book.'}, # 'Read'
#     '书': {'frequency': 4, 'pinyin': 'shū', 'example': '这是一本书。', 'translation': 'This is a book.'}, # 'Book'
#     '电视': {'frequency': 3, 'pinyin': 'diànshì', 'example': '我看电视。', 'translation': 'I watch TV.'}, # 'TV'
#     '电脑': {'frequency': 4, 'pinyin': 'diànnǎo', 'example': '我用电脑。', 'translation': 'I use a computer.'}, # 'Computer'
#     '手机': {'frequency': 5, 'pinyin': 'shǒujī', 'example': '我有一部手机。', 'translation': 'I have a mobile phone.'}, # 'Mobile phone'
#     '学习': {'frequency': 5, 'pinyin': 'xuéxí', 'example': '我在学习。', 'translation': 'I am studying.'},
#     '工作': {'frequency': 5, 'pinyin': 'gōngzuò', 'example': '我在工作。', 'translation': 'I am working.'},
#     '爱': {'frequency': 4, 'pinyin': 'ài', 'example': '我爱你。', 'translation': 'I love you.'},
#     '喜欢': {'frequency': 5, 'pinyin': 'xǐhuān', 'example': '我喜欢吃苹果。', 'translation': 'I like to eat apples.'},
#     '天气': {'frequency': 3, 'pinyin': 'tiānqì', 'example': '今天天气很好。', 'translation': 'The weather is very good today.'},
#     '热': {'frequency': 3, 'pinyin': 'rè', 'example': '今天很热。', 'translation': 'It is hot today.'},
#     '冷': {'frequency': 3, 'pinyin': 'lěng', 'example': '今天很冷。', 'translation': 'It is cold today.'},
#     '好': {'frequency': 5, 'pinyin': 'hǎo', 'example': '这个苹果很好吃。', 'translation': 'This apple is very tasty.'},
#     '坏': {'frequency': 3, 'pinyin': 'huài', 'example': '这个苹果坏了。', 'translation': 'This apple is bad.'},
#     '快': {'frequency': 4, 'pinyin': 'kuài', 'example': '他跑得很快。', 'translation': 'He runs very fast.'},
#     '慢': {'frequency': 3, 'pinyin': 'màn', 'example': '他跑得很慢。', 'translation': 'He runs very slow.'},
#     '高': {'frequency': 3, 'pinyin': 'gāo', 'example': '这座山很高。', 'translation': 'This mountain is very high.'},
#     '低': {'frequency': 2, 'pinyin': 'dī', 'example': '这座山很低。', 'translation': 'This mountain is very low.'},
#     '长': {'frequency': 3, 'pinyin': 'cháng', 'example': '这条河很长。', 'translation': 'This river is very long.'},
#     '短': {'frequency': 2, 'pinyin': 'duǎn', 'example': '这条河很短。', 'translation': 'This river is very short.'},
#     '老': {'frequency': 3, 'pinyin': 'lǎo', 'example': '他很老。', 'translation': 'He is very old.'},
#     '年轻': {'frequency': 3, 'pinyin': 'niánqīng', 'example': '他很年轻。', 'translation': 'He is very young.'},
#     '美丽': {'frequency': 3, 'pinyin': 'měilì', 'example': '她很美丽。', 'translation': 'She is very beautiful.'},
#     '丑': {'frequency': 2, 'pinyin': 'chǒu', 'example': '他很丑。', 'translation': 'He is very ugly.'},
#     '早': {'frequency': 4, 'pinyin': 'zǎo', 'example': '早上好。', 'translation': 'Good morning.'},
#     '晚': {'frequency': 4, 'pinyin': 'wǎn', 'example': '晚上好。', 'translation': 'Good evening.'},
#     '开': {'frequency': 4, 'pinyin': 'kāi', 'example': '开门。', 'translation': 'Open the door.'},
#     '关': {'frequency': 4, 'pinyin': 'guān', 'example': '关窗。', 'translation': 'Close the window.'},
#     '进': {'frequency': 4, 'pinyin': 'jìn', 'example': '进来。', 'translation': 'Come in.'},
    
# }

# Flatten the list of dictionaries to a single dictionary
flash_cards = {list(item.keys())[0]: list(item.values())[0] for item in data}

# Generate a list of characters based on their frequency
characters = [char for char, details in flash_cards.items() for _ in range(details['frequency'])]

# Initialize the counter
counter = 0

while True:
    # Randomly select a character/phrase
    flash_card = random.choice(characters)

    # Extract details from the dictionary
    card_details = flash_cards[flash_card]

    # Increment the counter
    counter += 1

    # Display the character/phrase, pinyin, example, translation, example translation, and usage notes
    print("=" * 50)
    print(f"Flashcard #{counter}")
    print(f"Character/Phrase  : {flash_card}")
    print(f"Pinyin            : {card_details['pinyin']}")
    print(f"Translation       : {card_details['translation']}")
    print(f"Example           : {card_details['example']}")
    print(f"Example Translation: {card_details['example_translation']}")
    print(f"Usage Notes       : {card_details['usage_notes']}")
    print("=" * 50 + "\n")

    # Wait for the user to press a key to continue
    input("Press enter to continue...")
    