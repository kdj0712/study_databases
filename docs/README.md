##### MongoDB Functions  ####

Compass 내 Console 명령어
사용하기 전에 필요한 컬렉션을 미리 지정하는 use 해당 컬렉션을 선정하고 사용

- insertOne()   :  db.cars_info.insertOne({....})  | collection에 데이터를 입력할 때 넣는 명령어.
- delete : db.posts.deleteMany( {  } ) ; | collection에 있는 record를 삭제하는 명령어
- find_ObjectId : db.fruits.find({}); | 해당 collection에 있는 record의 ObjectID를 찾는 명령어

- db.____.find({ : }); | collection에서 필요한 record를 찾을 때 쓰는 명령어(key와 value를 같이 기재해야 찾을 수 있다.)

- db.posts.find({_id:1,title:1,category:1,likes:1}); |

- db.____.updateMany({}, {$inc:{ likes: 1 }});

db.posts.updateMany({category : "Event"}, { $inc: {event: 1000 } });
db.posts.find({ likes : {$eq : 4}} ,{title:1,category:1,likes:1});
db.posts.find({ likes : {$gt : 4}} ,{title:1,category:1,likes:1});     
db.posts.find({ category : {$in : ["Event","Tech"]}} , {title:1,category:1,likes:1});
db.posts.find({ $and : [ { category : { $in : ["Event","Tech"] }}, { likes : { $gt : 4 } } ] } , {title:1,category:1,likes:1});   $and 조건은 하위 조건에 포함되는 내용들을 
db.posts.updateMany({category : {$eq : "Technology"} },
                    { $set : { likes : 1, body:"update Post" }});
db.fruits_colors.find({fruits_id : { $eq : ObjectId(657bf126e52c79ca7df148a7")} });
db.fruits_colors.find({  }); 변수 + 부등식 + 기준값
compass 연동 python 명령어

- insert_result.inserted_ids 


db.posts.updateMany({category : {$eq : "Technology"} },
                    { $set : {new_id : 45 }}); 이미 있는 record(내가 원하는 조건으로 검색하여 찾아낸)에 새로운 column을 추가하는``