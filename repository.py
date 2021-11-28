from pymongo import MongoClient

class DatabaseConnect:
    url = 'mongodb://localhost:27017'
    client = None
    db = None
    collection = None
    
    def __init__(self, db, collection) -> None:
        self.client = MongoClient(self.url)
        self.db = self.client[db]
        self.collection = self.db[collection]
            
class UserRepository:
    db = None
    collection = None
    
    def __init__(self) -> None:
        self.db = DatabaseConnect('test', 'users')
        self.collection = self.db.collection
        
    def insert_user(self, username, password):
        self.collection.insert_one({ 'username': username, 'password': password })
        return { 'username': username, 'password': password }
    
    def find_user(self, username):
        user = self.collection.find_one({ 'username': username })
        if user:
            return { 'username': user['username'], 'password': user['password'] }
    
    def find_users(self):
        users = []
        
        for user in self.db.collection.find():
            users.append({ 'username': user['username'], 'password': user['password'] })
            
        return users
    
    def update_user(self, username, new_username, password):
        user = self.collection.update_one({ 'username': username }, { '$set': { 'password': password, 'username': new_username }})        
        return { 'username': new_username, 'password': password }
    
    def delete_user(self, username):
        self.collection.delete_one({ 'username': username })
        return True
    
