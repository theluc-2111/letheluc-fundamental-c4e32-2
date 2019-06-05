uri = 'mongodb://admin:admin@ds021182.mlab.com:21182/c4e'

import pymongo

client = pymongo.MongoClient(uri)
db = client.c4e
collection = db.ltluc

def insert_poem(title:str,content:str,author:str):
    """
    Chú thích
        title {str} -- [Tiêu đề]
        content {str} -- [Nội dung]
        author {str} -- [Tác giả]
    """
    collection.insert_one({'title':title,'content':content,'author':author})

insert_poem('Bánh trôi nước','Thân em thời trắng phận em tròn. Bảy nổi ba chìm mấy nước non. Rắn nát mặc dầu tay kẻ nặn. Nhưng em vẫn giữ tấm lòng son','Ho Xuan Huong')
insert_poem('Câu Thơ Họa','Mây mù che phủ bóng trùng khơi. Mắt biếc long lanh cảnh tuyệt vời. Sợi nhỏ li ti mơ chẳng tới. Non ngàn biển cạn đá chơi vơi','Sưu tầm')
insert_poem('What do you think about Khanh?','Tốt bụng, Cute vcl','The Luc')

print(list(collection.find()))